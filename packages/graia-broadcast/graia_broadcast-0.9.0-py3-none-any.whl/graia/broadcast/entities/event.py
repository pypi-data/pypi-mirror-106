from typing import Any, Protocol, Tuple, TypeVar, Union
import inspect

import typing

if typing.TYPE_CHECKING:
    from .dispatcher import BaseDispatcher

T = TypeVar("T")


def issubclass_safely(
    cls, class_or_tuple: Union[type, Tuple[Union[type, Tuple], ...]]
) -> bool:
    return inspect.isclass(cls) and issubclass(cls, class_or_tuple)


class Dispatchable(Protocol[T]):
    def __instancecheck__(self, instance: Any) -> bool:
        if issubclass_safely(getattr(instance, "Dispatcher", None), BaseDispatcher):
            return True
        return super().__instancecheck__(instance)

    Dispatcher: "BaseDispatcher"


BaseEvent = Dispatchable

from .dispatcher import BaseDispatcher
