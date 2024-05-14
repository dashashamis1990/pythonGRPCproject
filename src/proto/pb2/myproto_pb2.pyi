from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Request(_message.Message):
    __slots__ = ["message", "number_of_times"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    NUMBER_OF_TIMES_FIELD_NUMBER: _ClassVar[int]
    message: str
    number_of_times: int
    def __init__(self, message: _Optional[str] = ..., number_of_times: _Optional[int] = ...) -> None: ...

class Response(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: bool
    def __init__(self, status: bool = ...) -> None: ...
