"""
Type annotations for mediaconnect service literal definitions.

[Open documentation](./literals.md)

Usage::

    ```python
    from mypy_boto3_mediaconnect.literals import AlgorithmType

    data: AlgorithmType = "aes128"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AlgorithmType",
    "DurationUnitsType",
    "EntitlementStatusType",
    "FlowActiveWaiterName",
    "FlowDeletedWaiterName",
    "FlowStandbyWaiterName",
    "KeyTypeType",
    "ListEntitlementsPaginatorName",
    "ListFlowsPaginatorName",
    "ListOfferingsPaginatorName",
    "ListReservationsPaginatorName",
    "PriceUnitsType",
    "ProtocolType",
    "ReservationStateType",
    "ResourceTypeType",
    "SourceTypeType",
    "StateType",
    "StatusType",
)


AlgorithmType = Literal["aes128", "aes192", "aes256"]
DurationUnitsType = Literal["MONTHS"]
EntitlementStatusType = Literal["DISABLED", "ENABLED"]
FlowActiveWaiterName = Literal["flow_active"]
FlowDeletedWaiterName = Literal["flow_deleted"]
FlowStandbyWaiterName = Literal["flow_standby"]
KeyTypeType = Literal["speke", "srt-password", "static-key"]
ListEntitlementsPaginatorName = Literal["list_entitlements"]
ListFlowsPaginatorName = Literal["list_flows"]
ListOfferingsPaginatorName = Literal["list_offerings"]
ListReservationsPaginatorName = Literal["list_reservations"]
PriceUnitsType = Literal["HOURLY"]
ProtocolType = Literal["rist", "rtp", "rtp-fec", "srt-listener", "zixi-pull", "zixi-push"]
ReservationStateType = Literal["ACTIVE", "CANCELED", "EXPIRED", "PROCESSING"]
ResourceTypeType = Literal["Mbps_Outbound_Bandwidth"]
SourceTypeType = Literal["ENTITLED", "OWNED"]
StateType = Literal["DISABLED", "ENABLED"]
StatusType = Literal["ACTIVE", "DELETING", "ERROR", "STANDBY", "STARTING", "STOPPING", "UPDATING"]
