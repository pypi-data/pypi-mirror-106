from typing import AnyStr, Iterator, List, Union

def glob0(dirname: AnyStr, pattern: AnyStr) -> List[AnyStr]: ...
def glob1(dirname: AnyStr, pattern: AnyStr) -> List[AnyStr]: ...
def glob(pathname: AnyStr, *, recursive: bool = ...) -> List[AnyStr]: ...
def iglob(pathname: AnyStr, *, recursive: bool = ...) -> Iterator[AnyStr]: ...
def escape(pathname: AnyStr) -> AnyStr: ...
def has_magic(s: Union[str, bytes]) -> bool: ...  # undocumented
