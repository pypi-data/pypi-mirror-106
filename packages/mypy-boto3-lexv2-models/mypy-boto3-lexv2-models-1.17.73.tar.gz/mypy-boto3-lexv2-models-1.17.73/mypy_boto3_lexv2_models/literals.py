"""
Type annotations for lexv2-models service literal definitions.

[Open documentation](./literals.md)

Usage::

    ```python
    from mypy_boto3_lexv2_models.literals import BotAliasStatusType

    data: BotAliasStatusType = "Available"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "BotAliasStatusType",
    "BotFilterNameType",
    "BotFilterOperatorType",
    "BotLocaleFilterNameType",
    "BotLocaleFilterOperatorType",
    "BotLocaleSortAttributeType",
    "BotLocaleStatusType",
    "BotSortAttributeType",
    "BotStatusType",
    "BotVersionSortAttributeType",
    "BuiltInIntentSortAttributeType",
    "BuiltInSlotTypeSortAttributeType",
    "IntentFilterNameType",
    "IntentFilterOperatorType",
    "IntentSortAttributeType",
    "ObfuscationSettingTypeType",
    "SlotConstraintType",
    "SlotFilterNameType",
    "SlotFilterOperatorType",
    "SlotSortAttributeType",
    "SlotTypeFilterNameType",
    "SlotTypeFilterOperatorType",
    "SlotTypeSortAttributeType",
    "SlotValueResolutionStrategyType",
    "SortOrderType",
)


BotAliasStatusType = Literal["Available", "Creating", "Deleting", "Failed"]
BotFilterNameType = Literal["BotName"]
BotFilterOperatorType = Literal["CO", "EQ"]
BotLocaleFilterNameType = Literal["BotLocaleName"]
BotLocaleFilterOperatorType = Literal["CO", "EQ"]
BotLocaleSortAttributeType = Literal["BotLocaleName"]
BotLocaleStatusType = Literal[
    "Building", "Built", "Creating", "Deleting", "Failed", "NotBuilt", "ReadyExpressTesting"
]
BotSortAttributeType = Literal["BotName"]
BotStatusType = Literal["Available", "Creating", "Deleting", "Failed", "Inactive", "Versioning"]
BotVersionSortAttributeType = Literal["BotVersion"]
BuiltInIntentSortAttributeType = Literal["IntentSignature"]
BuiltInSlotTypeSortAttributeType = Literal["SlotTypeSignature"]
IntentFilterNameType = Literal["IntentName"]
IntentFilterOperatorType = Literal["CO", "EQ"]
IntentSortAttributeType = Literal["IntentName", "LastUpdatedDateTime"]
ObfuscationSettingTypeType = Literal["DefaultObfuscation", "None"]
SlotConstraintType = Literal["Optional", "Required"]
SlotFilterNameType = Literal["SlotName"]
SlotFilterOperatorType = Literal["CO", "EQ"]
SlotSortAttributeType = Literal["LastUpdatedDateTime", "SlotName"]
SlotTypeFilterNameType = Literal["SlotTypeName"]
SlotTypeFilterOperatorType = Literal["CO", "EQ"]
SlotTypeSortAttributeType = Literal["LastUpdatedDateTime", "SlotTypeName"]
SlotValueResolutionStrategyType = Literal["OriginalValue", "TopResolution"]
SortOrderType = Literal["Ascending", "Descending"]
