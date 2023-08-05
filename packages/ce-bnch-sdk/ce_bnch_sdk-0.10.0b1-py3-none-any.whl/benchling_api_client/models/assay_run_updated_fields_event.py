from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.assay_run import AssayRun
from ..models.assay_run_updated_fields_event_event_type import AssayRunUpdatedFieldsEventEventType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AssayRunUpdatedFieldsEvent")


@attr.s(auto_attribs=True)
class AssayRunUpdatedFieldsEvent:
    """  """

    assay_run: Union[Unset, AssayRun] = UNSET
    event_type: Union[Unset, AssayRunUpdatedFieldsEventEventType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        assay_run: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.assay_run, Unset):
            assay_run = self.assay_run.to_dict()

        event_type: Union[Unset, int] = UNSET
        if not isinstance(self.event_type, Unset):
            event_type = self.event_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assay_run is not UNSET:
            field_dict["assayRun"] = assay_run
        if event_type is not UNSET:
            field_dict["eventType"] = event_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        assay_run: Union[Unset, AssayRun] = UNSET
        _assay_run = d.pop("assayRun", UNSET)
        if not isinstance(_assay_run, Unset):
            assay_run = AssayRun.from_dict(_assay_run)

        event_type = None
        _event_type = d.pop("eventType", UNSET)
        if _event_type is not None and _event_type is not UNSET:
            event_type = AssayRunUpdatedFieldsEventEventType(_event_type)

        assay_run_updated_fields_event = cls(
            assay_run=assay_run,
            event_type=event_type,
        )

        assay_run_updated_fields_event.additional_properties = d
        return assay_run_updated_fields_event

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
