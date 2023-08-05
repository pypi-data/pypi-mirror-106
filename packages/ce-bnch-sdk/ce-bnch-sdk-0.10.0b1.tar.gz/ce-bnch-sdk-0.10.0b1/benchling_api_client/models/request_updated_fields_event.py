from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.request import Request
from ..models.request_updated_fields_event_event_type import RequestUpdatedFieldsEventEventType
from ..types import UNSET, Unset

T = TypeVar("T", bound="RequestUpdatedFieldsEvent")


@attr.s(auto_attribs=True)
class RequestUpdatedFieldsEvent:
    """  """

    event_type: Union[Unset, RequestUpdatedFieldsEventEventType] = UNSET
    request: Union[Unset, Request] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        event_type: Union[Unset, int] = UNSET
        if not isinstance(self.event_type, Unset):
            event_type = self.event_type.value

        request: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.request, Unset):
            request = self.request.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if event_type is not UNSET:
            field_dict["eventType"] = event_type
        if request is not UNSET:
            field_dict["request"] = request

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        event_type = None
        _event_type = d.pop("eventType", UNSET)
        if _event_type is not None and _event_type is not UNSET:
            event_type = RequestUpdatedFieldsEventEventType(_event_type)

        request: Union[Unset, Request] = UNSET
        _request = d.pop("request", UNSET)
        if not isinstance(_request, Unset):
            request = Request.from_dict(_request)

        request_updated_fields_event = cls(
            event_type=event_type,
            request=request,
        )

        request_updated_fields_event.additional_properties = d
        return request_updated_fields_event

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
