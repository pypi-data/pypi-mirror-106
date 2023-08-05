"""
Type annotations for compute-optimizer service literal definitions.

[Open documentation](./literals.md)

Usage::

    ```python
    from mypy_boto3_compute_optimizer.literals import EBSFilterNameType

    data: EBSFilterNameType = "Finding"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "EBSFilterNameType",
    "EBSFindingType",
    "EBSMetricNameType",
    "ExportableAutoScalingGroupFieldType",
    "ExportableInstanceFieldType",
    "FileFormatType",
    "FilterNameType",
    "FindingReasonCodeType",
    "FindingType",
    "JobFilterNameType",
    "JobStatusType",
    "LambdaFunctionMemoryMetricNameType",
    "LambdaFunctionMemoryMetricStatisticType",
    "LambdaFunctionMetricNameType",
    "LambdaFunctionMetricStatisticType",
    "LambdaFunctionRecommendationFilterNameType",
    "LambdaFunctionRecommendationFindingReasonCodeType",
    "LambdaFunctionRecommendationFindingType",
    "MetricNameType",
    "MetricStatisticType",
    "RecommendationSourceTypeType",
    "ResourceTypeType",
    "StatusType",
)

EBSFilterNameType = Literal["Finding"]
EBSFindingType = Literal["NotOptimized", "Optimized"]
EBSMetricNameType = Literal[
    "VolumeReadBytesPerSecond",
    "VolumeReadOpsPerSecond",
    "VolumeWriteBytesPerSecond",
    "VolumeWriteOpsPerSecond",
]
ExportableAutoScalingGroupFieldType = Literal[
    "AccountId",
    "AutoScalingGroupArn",
    "AutoScalingGroupName",
    "CurrentConfigurationDesiredCapacity",
    "CurrentConfigurationInstanceType",
    "CurrentConfigurationMaxSize",
    "CurrentConfigurationMinSize",
    "CurrentMemory",
    "CurrentNetwork",
    "CurrentOnDemandPrice",
    "CurrentStandardOneYearNoUpfrontReservedPrice",
    "CurrentStandardThreeYearNoUpfrontReservedPrice",
    "CurrentStorage",
    "CurrentVCpus",
    "Finding",
    "LastRefreshTimestamp",
    "LookbackPeriodInDays",
    "RecommendationOptionsConfigurationDesiredCapacity",
    "RecommendationOptionsConfigurationInstanceType",
    "RecommendationOptionsConfigurationMaxSize",
    "RecommendationOptionsConfigurationMinSize",
    "RecommendationOptionsMemory",
    "RecommendationOptionsNetwork",
    "RecommendationOptionsOnDemandPrice",
    "RecommendationOptionsPerformanceRisk",
    "RecommendationOptionsProjectedUtilizationMetricsCpuMaximum",
    "RecommendationOptionsProjectedUtilizationMetricsMemoryMaximum",
    "RecommendationOptionsStandardOneYearNoUpfrontReservedPrice",
    "RecommendationOptionsStandardThreeYearNoUpfrontReservedPrice",
    "RecommendationOptionsStorage",
    "RecommendationOptionsVcpus",
    "UtilizationMetricsCpuMaximum",
    "UtilizationMetricsEbsReadBytesPerSecondMaximum",
    "UtilizationMetricsEbsReadOpsPerSecondMaximum",
    "UtilizationMetricsEbsWriteBytesPerSecondMaximum",
    "UtilizationMetricsEbsWriteOpsPerSecondMaximum",
    "UtilizationMetricsMemoryMaximum",
]
ExportableInstanceFieldType = Literal[
    "AccountId",
    "CurrentInstanceType",
    "CurrentMemory",
    "CurrentNetwork",
    "CurrentOnDemandPrice",
    "CurrentStandardOneYearNoUpfrontReservedPrice",
    "CurrentStandardThreeYearNoUpfrontReservedPrice",
    "CurrentStorage",
    "CurrentVCpus",
    "Finding",
    "InstanceArn",
    "InstanceName",
    "LastRefreshTimestamp",
    "LookbackPeriodInDays",
    "RecommendationOptionsInstanceType",
    "RecommendationOptionsMemory",
    "RecommendationOptionsNetwork",
    "RecommendationOptionsOnDemandPrice",
    "RecommendationOptionsPerformanceRisk",
    "RecommendationOptionsProjectedUtilizationMetricsCpuMaximum",
    "RecommendationOptionsProjectedUtilizationMetricsMemoryMaximum",
    "RecommendationOptionsStandardOneYearNoUpfrontReservedPrice",
    "RecommendationOptionsStandardThreeYearNoUpfrontReservedPrice",
    "RecommendationOptionsStorage",
    "RecommendationOptionsVcpus",
    "RecommendationsSourcesRecommendationSourceArn",
    "RecommendationsSourcesRecommendationSourceType",
    "UtilizationMetricsCpuMaximum",
    "UtilizationMetricsEbsReadBytesPerSecondMaximum",
    "UtilizationMetricsEbsReadOpsPerSecondMaximum",
    "UtilizationMetricsEbsWriteBytesPerSecondMaximum",
    "UtilizationMetricsEbsWriteOpsPerSecondMaximum",
    "UtilizationMetricsMemoryMaximum",
]
FileFormatType = Literal["Csv"]
FilterNameType = Literal["Finding", "RecommendationSourceType"]
FindingReasonCodeType = Literal["MemoryOverprovisioned", "MemoryUnderprovisioned"]
FindingType = Literal["NotOptimized", "Optimized", "Overprovisioned", "Underprovisioned"]
JobFilterNameType = Literal["JobStatus", "ResourceType"]
JobStatusType = Literal["Complete", "Failed", "InProgress", "Queued"]
LambdaFunctionMemoryMetricNameType = Literal["Duration"]
LambdaFunctionMemoryMetricStatisticType = Literal["Expected", "LowerBound", "UpperBound"]
LambdaFunctionMetricNameType = Literal["Duration", "Memory"]
LambdaFunctionMetricStatisticType = Literal["Average", "Maximum"]
LambdaFunctionRecommendationFilterNameType = Literal["Finding", "FindingReasonCode"]
LambdaFunctionRecommendationFindingReasonCodeType = Literal[
    "Inconclusive", "InsufficientData", "MemoryOverprovisioned", "MemoryUnderprovisioned"
]
LambdaFunctionRecommendationFindingType = Literal["NotOptimized", "Optimized", "Unavailable"]
MetricNameType = Literal[
    "Cpu",
    "EBS_READ_BYTES_PER_SECOND",
    "EBS_READ_OPS_PER_SECOND",
    "EBS_WRITE_BYTES_PER_SECOND",
    "EBS_WRITE_OPS_PER_SECOND",
    "Memory",
]
MetricStatisticType = Literal["Average", "Maximum"]
RecommendationSourceTypeType = Literal[
    "AutoScalingGroup", "EbsVolume", "Ec2Instance", "LambdaFunction"
]
ResourceTypeType = Literal["AutoScalingGroup", "Ec2Instance"]
StatusType = Literal["Active", "Failed", "Inactive", "Pending"]
