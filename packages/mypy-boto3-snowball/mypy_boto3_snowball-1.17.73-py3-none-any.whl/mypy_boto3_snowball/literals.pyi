"""
Type annotations for snowball service literal definitions.

[Open documentation](./literals.md)

Usage::

    ```python
    from mypy_boto3_snowball.literals import ClusterStateType

    data: ClusterStateType = "AwaitingQuorum"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ClusterStateType",
    "DescribeAddressesPaginatorName",
    "JobStateType",
    "JobTypeType",
    "ListClusterJobsPaginatorName",
    "ListClustersPaginatorName",
    "ListCompatibleImagesPaginatorName",
    "ListJobsPaginatorName",
    "LongTermPricingTypeType",
    "ShipmentStateType",
    "ShippingLabelStatusType",
    "ShippingOptionType",
    "SnowballCapacityType",
    "SnowballTypeType",
)

ClusterStateType = Literal["AwaitingQuorum", "Cancelled", "Complete", "InUse", "Pending"]
DescribeAddressesPaginatorName = Literal["describe_addresses"]
JobStateType = Literal[
    "Cancelled",
    "Complete",
    "InProgress",
    "InTransitToAWS",
    "InTransitToCustomer",
    "Listing",
    "New",
    "Pending",
    "PreparingAppliance",
    "PreparingShipment",
    "WithAWS",
    "WithAWSSortingFacility",
    "WithCustomer",
]
JobTypeType = Literal["EXPORT", "IMPORT", "LOCAL_USE"]
ListClusterJobsPaginatorName = Literal["list_cluster_jobs"]
ListClustersPaginatorName = Literal["list_clusters"]
ListCompatibleImagesPaginatorName = Literal["list_compatible_images"]
ListJobsPaginatorName = Literal["list_jobs"]
LongTermPricingTypeType = Literal["OneYear", "ThreeYear"]
ShipmentStateType = Literal["RECEIVED", "RETURNED"]
ShippingLabelStatusType = Literal["Failed", "InProgress", "Succeeded", "TimedOut"]
ShippingOptionType = Literal["EXPRESS", "NEXT_DAY", "SECOND_DAY", "STANDARD"]
SnowballCapacityType = Literal["NoPreference", "T100", "T14", "T42", "T50", "T8", "T80", "T98"]
SnowballTypeType = Literal[
    "EDGE", "EDGE_C", "EDGE_CG", "EDGE_S", "SNC1_HDD", "SNC1_SSD", "STANDARD"
]
