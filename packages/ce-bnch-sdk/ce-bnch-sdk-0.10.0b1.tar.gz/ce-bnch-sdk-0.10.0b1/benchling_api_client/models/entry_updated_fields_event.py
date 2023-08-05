from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.entry import Entry
from ..models.entry_updated_fields_event_event_type import EntryUpdatedFieldsEventEventType
from ..types import UNSET, Unset

T = TypeVar("T", bound="EntryUpdatedFieldsEvent")


@attr.s(auto_attribs=True)
class EntryUpdatedFieldsEvent:
    """  """

    entry: Union[Unset, Entry] = UNSET
    event_type: Union[Unset, EntryUpdatedFieldsEventEventType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        entry: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.entry, Unset):
            entry = self.entry.to_dict()

        event_type: Union[Unset, int] = UNSET
        if not isinstance(self.event_type, Unset):
            event_type = self.event_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entry is not UNSET:
            field_dict["entry"] = entry
        if event_type is not UNSET:
            field_dict["eventType"] = event_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        entry: Union[Unset, Entry] = UNSET
        _entry = d.pop("entry", UNSET)
        if not isinstance(_entry, Unset):
            entry = Entry.from_dict(_entry)

        event_type = None
        _event_type = d.pop("eventType", UNSET)
        if _event_type is not None and _event_type is not UNSET:
            event_type = EntryUpdatedFieldsEventEventType(_event_type)

        entry_updated_fields_event = cls(
            entry=entry,
            event_type=event_type,
        )

        entry_updated_fields_event.additional_properties = d
        return entry_updated_fields_event

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
