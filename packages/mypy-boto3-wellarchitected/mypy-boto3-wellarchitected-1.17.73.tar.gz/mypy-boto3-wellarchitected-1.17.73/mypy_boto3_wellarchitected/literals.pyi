"""
Type annotations for wellarchitected service literal definitions.

[Open documentation](./literals.md)

Usage::

    ```python
    from mypy_boto3_wellarchitected.literals import DifferenceStatusType

    data: DifferenceStatusType = "DELETED"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "DifferenceStatusType",
    "LensStatusType",
    "NotificationTypeType",
    "PermissionTypeType",
    "RiskType",
    "ShareInvitationActionType",
    "ShareStatusType",
    "WorkloadEnvironmentType",
    "WorkloadImprovementStatusType",
)

DifferenceStatusType = Literal["DELETED", "NEW", "UPDATED"]
LensStatusType = Literal["CURRENT", "DEPRECATED", "NOT_CURRENT"]
NotificationTypeType = Literal["LENS_VERSION_DEPRECATED", "LENS_VERSION_UPGRADED"]
PermissionTypeType = Literal["CONTRIBUTOR", "READONLY"]
RiskType = Literal["HIGH", "MEDIUM", "NONE", "NOT_APPLICABLE", "UNANSWERED"]
ShareInvitationActionType = Literal["ACCEPT", "REJECT"]
ShareStatusType = Literal["ACCEPTED", "EXPIRED", "PENDING", "REJECTED", "REVOKED"]
WorkloadEnvironmentType = Literal["PREPRODUCTION", "PRODUCTION"]
WorkloadImprovementStatusType = Literal[
    "COMPLETE", "IN_PROGRESS", "NOT_APPLICABLE", "NOT_STARTED", "RISK_ACKNOWLEDGED"
]
