from typing import Type, Any, Callable, TypeVar
from fastapi import Request, Depends as D
import functools

T = TypeVar('T')


def IOCService(_type: Type[T]) -> Any:  # noqa: N802
    def resolver(t: Type[T], request: Request) -> Callable[[], T]:
        return request.app.state.ioc_container.resolve(t)

    return D(functools.partial(resolver, _type))