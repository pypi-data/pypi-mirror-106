import inspect
from typing import Callable, Dict, List, Set

from ..typing import T_Dispatcher
from .decorator import Decorator


class ExecTarget:
    callable: Callable
    inline_dispatchers: List[T_Dispatcher]
    headless_decorators: List[Decorator]
    enable_internal_access: bool = False

    param_paths: Dict[str, List[List[T_Dispatcher]]]
    maybe_failure: Set[str]

    def __init__(
        self,
        callable: Callable,
        inline_dispatchers: List[T_Dispatcher] = None,
        headless_decorators: List[Decorator] = None,
        enable_internal_access: bool = False,
    ):
        self.callable = callable
        self.inline_dispatchers = inline_dispatchers or []
        self.headless_decorators = headless_decorators or []
        self.enable_internal_access = enable_internal_access

        self.param_paths = {}
        self.maybe_failure = set(inspect.signature(self.callable).parameters.keys())
