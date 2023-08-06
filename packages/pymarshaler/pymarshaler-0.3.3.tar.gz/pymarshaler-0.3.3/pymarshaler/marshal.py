import datetime
import inspect
import typing
from enum import Enum

import orjson

from pymarshaler.arg_delegates import ArgBuilderDelegate, ListArgBuilderDelegate, \
    SetArgBuilderDelegate, TupleArgBuilderDelegate, DictArgBuilderDelegate, BuiltinArgBuilderDelegate, \
    UserDefinedArgBuilderDelegate, DateTimeArgBuilderDelegate, EnumArgBuilderDelegate
from pymarshaler.errors import MissingFieldsError, InvalidDelegateError, PymarshalError
from pymarshaler.utils import is_builtin, is_user_defined


class _RegisteredDelegates:

    def __init__(self):
        self.registered_delegates = {}

    def register(self, cls, delegate: ArgBuilderDelegate):
        self.registered_delegates[cls] = delegate

    def get_for(self, cls):
        try:
            for delegate_cls, delegate in self.registered_delegates.items():
                if cls == delegate_cls or issubclass(cls, delegate_cls):
                    return delegate
            return None
        except TypeError:
            return None


class _ArgBuilderFactory:

    def __init__(self, func, ignore_unknown_fields: bool, walk_unknown_fields: bool):
        self._registered_delegates = _RegisteredDelegates()
        self._default_arg_builder_delegates = {
            typing.List._name: lambda x: ListArgBuilderDelegate(x, func),
            typing.Set._name: lambda x: SetArgBuilderDelegate(x, func),
            typing.Tuple._name: lambda x: TupleArgBuilderDelegate(x, func),
            typing.Dict._name: lambda x: DictArgBuilderDelegate(x, func),
            "PythonBuiltin": lambda x: BuiltinArgBuilderDelegate(x),
            "UserDefined": lambda x: UserDefinedArgBuilderDelegate(
                x,
                func,
                ignore_unknown_fields,
                walk_unknown_fields
            ),
            "DateTime": lambda: DateTimeArgBuilderDelegate()
        }

    def register(self, cls, delegate_cls):
        self._registered_delegates.register(cls, delegate_cls(cls))

    def get_delegate(self, cls) -> ArgBuilderDelegate:
        is_class = inspect.isclass(cls)

        if not is_class:
            if '_name' in cls.__dict__:
                return self._safe_get(cls._name)(cls)
        else:
            cls_maybe = self._registered_delegates.get_for(cls)
            if cls_maybe:
                return cls_maybe
            elif issubclass(cls, Enum):
                return EnumArgBuilderDelegate(cls)
            elif is_user_defined(cls):
                return self._default_arg_builder_delegates['UserDefined'](cls)
            elif issubclass(cls, datetime.datetime):
                return self._default_arg_builder_delegates['DateTime']()
            elif is_builtin(cls):
                return self._default_arg_builder_delegates['PythonBuiltin'](cls)

        raise InvalidDelegateError(f'No delegate for class {cls}')

    def _safe_get(self, name):
        if name not in self._default_arg_builder_delegates:
            raise InvalidDelegateError(f'Unsupported class type {name}')
        return self._default_arg_builder_delegates[name]


def _default(o):
    try:
        return o.__dict__
    except AttributeError:
        return repr(o)


class Marshal:

    def __init__(self, ignore_unknown_fields: bool = False, walk_unknown_fields: bool = False):
        if walk_unknown_fields and ignore_unknown_fields is False:
            raise PymarshalError('If walk_unknown_fields is True, ignore_unknown_fields must also be True')

        self._arg_builder_factory = _ArgBuilderFactory(
            self._apply_typing,
            ignore_unknown_fields,
            walk_unknown_fields
        )

    @staticmethod
    def marshal(obj) -> bytes:
        """
        Convert a class instance to JSON formatted bytes
        :param obj: The object to convert
        :return: bytes JSON representation of the class instance
        Example:
        >>> class Test:
            >>> def __init__(self, name: str):
                >>> self.name = name
        >>> test_instance = Test('foo', indent=0)
        >>> data = Marshal.marshal(test_instance)
        >>> print(data)
        '{name: foo}'
        """
        return orjson.dumps(obj, default=_default)

    def unmarshal_str(self, cls, data: str):
        """
        Reconstruct an instance of type `cls` from a JSON formatted string
        :param cls: The class type. Must be a user defined type
        :param data: The string JSON data
        :return: An instance of the class `cls`

        Example:

        >>> class Test:

            >>> def __init__(self, name: str):
                >>> self.name = name

        >>> marshal = Marshal()
        >>> data = "{'name': 'foo'}"
        >>> test_instance = marshal.unmarshal_str(Test,data)
        >>> print(test_instance.name)
        'foo'
        """
        return self.unmarshal(cls, orjson.loads(data))

    def unmarshal(self, cls, data: dict):
        """
        Reconstruct an instance of type `cls` from a JSON formatted string
        :param cls: The class type. Must be a user defined type
        :param data: The string JSON data
        :return: An instance of the class `cls`

        Example:

        >>> class Test:

            >>> def __init__(self, name: str):
                >>> self.name = name


        >>> marshal = Marshal()
        >>> data = "{'name': 'foo'}"
        >>> test_instance = marshal.unmarshal_str(Test,data)
        >>> print(test_instance.name)
        'foo'
        """
        try:
            return self._unmarshal(cls, data)
        except ValueError:
            raise ValueError(f'Failed to pymarshaler {data} to class {cls.__name__}')

    def register_delegate(self, cls, delegate_cls):
        self._arg_builder_factory.register(cls, delegate_cls)

    def _unmarshal(self, cls, data: dict):
        init_params = inspect.signature(cls.__init__).parameters
        args = self._arg_builder_factory.get_delegate(cls).resolve(data)
        if is_user_defined(type(args)):
            result = args
        else:
            missing = _get_unsatisfied_args(args, init_params)
            if len(missing) > 0:
                unfilled = [key for key, param in missing.items() if param.default is inspect.Parameter.empty]
                if len(unfilled) > 0:
                    raise MissingFieldsError(f'Missing required field(s): {", ".join(unfilled)}')
            result = cls(**args)
        if 'validate' in dir(cls):
            result.validate()
        return result

    def _apply_typing(self, param_type, value: typing.Any) -> typing.Any:
        delegate = self._arg_builder_factory.get_delegate(param_type)
        result = delegate.resolve(value)
        if is_user_defined(param_type):
            return param_type(**result)
        return result


def _get_unsatisfied_args(current_args: dict, all_params: dict):
    return {k: v for (k, v) in all_params.items() if k not in current_args and _is_valid_missing(k)}


def _is_valid_missing(k: str) -> bool:
    return k != 'self' and k != 'args' and k != 'kwargs'
