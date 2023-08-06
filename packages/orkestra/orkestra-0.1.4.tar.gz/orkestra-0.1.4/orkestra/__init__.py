from pathlib import Path
from typing import *

OptionalFn = Optional[Union[Callable, List[Callable]]]

@runtime_checkable
class Composable(Protocol):
    downstream: list

class Compose:
    def __init__(self, func: OptionalFn=None, context=False, **metadata):
        self.downstream = []
        self.func = func
        self.metadata = metadata
        self.context = context

        if func and not isinstance(func, list):

            module = func.__module__.split('.')

            self.entry = str(Path(*module).parent)
            self.index = Path(*module).name + ".py"
            self.handler = func.__name__
    
    def __call__(self, event_or_func, context=None):
        
        if isinstance(self.func, list):
            raise TypeError("can't call a list of functions")
        
        if self.func is not None:
            event = event_or_func
            if self.context:
                return self.func(event, context)
            else:
                return self.func(event)
        else:
            func = event_or_func
            return self.__class__(func)

    def __repr__(self) -> str:

        if isinstance(self.func, list):
            func = repr(self.func)
        else:
            func = self.func.__name__ if self.func is not None else None
        
        return (
            "Task("
            f"func={func}, "
            f"metadata={self.metadata}, "
            f"len_downstream={len(self.downstream)}"
            ")"
        )

    def __rshift__(self, right: Union[Composable, List[Composable]]):
        right = Compose(func=right) if isinstance(right, list) else right
        self.downstream.append(right)
        return right

compose: Composable = Compose
