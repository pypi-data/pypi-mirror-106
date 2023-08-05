"""
Type annotations for rds service client.

[Open documentation](./client.md)

Usage::

    ```python
    import boto3
    from mypy_boto3_rds import RDSClient

    client: RDSClient = boto3.client("rds")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from .literals import (
    ActivityStreamModeType,
    DBProxyEndpointTargetRoleType,
    EngineFamilyType,
    ReplicaModeType,
    SourceTypeType,
)
from .paginator import (
    DescribeCertificatesPaginator,
    DescribeCustomAvailabilityZonesPaginator,
    DescribeDBClusterBacktracksPaginator,
    DescribeDBClusterEndpointsPaginator,
    DescribeDBClusterParameterGroupsPaginator,
    DescribeDBClusterParametersPaginator,
    DescribeDBClusterSnapshotsPaginator,
    DescribeDBClustersPaginator,
    DescribeDBEngineVersionsPaginator,
    DescribeDBInstanceAutomatedBackupsPaginator,
    DescribeDBInstancesPaginator,
    DescribeDBLogFilesPaginator,
    DescribeDBParameterGroupsPaginator,
    DescribeDBParametersPaginator,
    DescribeDBProxiesPaginator,
    DescribeDBProxyEndpointsPaginator,
    DescribeDBProxyTargetGroupsPaginator,
    DescribeDBProxyTargetsPaginator,
    DescribeDBSecurityGroupsPaginator,
    DescribeDBSnapshotsPaginator,
    DescribeDBSubnetGroupsPaginator,
    DescribeEngineDefaultClusterParametersPaginator,
    DescribeEngineDefaultParametersPaginator,
    DescribeEventsPaginator,
    DescribeEventSubscriptionsPaginator,
    DescribeExportTasksPaginator,
    DescribeGlobalClustersPaginator,
    DescribeInstallationMediaPaginator,
    DescribeOptionGroupOptionsPaginator,
    DescribeOptionGroupsPaginator,
    DescribeOrderableDBInstanceOptionsPaginator,
    DescribePendingMaintenanceActionsPaginator,
    DescribeReservedDBInstancesOfferingsPaginator,
    DescribeReservedDBInstancesPaginator,
    DescribeSourceRegionsPaginator,
    DownloadDBLogFilePortionPaginator,
)
from .type_defs import (
    AccountAttributesMessageTypeDef,
    AddSourceIdentifierToSubscriptionResultTypeDef,
    ApplyPendingMaintenanceActionResultTypeDef,
    AuthorizeDBSecurityGroupIngressResultTypeDef,
    CertificateMessageTypeDef,
    CloudwatchLogsExportConfigurationTypeDef,
    ConnectionPoolConfigurationTypeDef,
    CopyDBClusterParameterGroupResultTypeDef,
    CopyDBClusterSnapshotResultTypeDef,
    CopyDBParameterGroupResultTypeDef,
    CopyDBSnapshotResultTypeDef,
    CopyOptionGroupResultTypeDef,
    CreateCustomAvailabilityZoneResultTypeDef,
    CreateDBClusterParameterGroupResultTypeDef,
    CreateDBClusterResultTypeDef,
    CreateDBClusterSnapshotResultTypeDef,
    CreateDBInstanceReadReplicaResultTypeDef,
    CreateDBInstanceResultTypeDef,
    CreateDBParameterGroupResultTypeDef,
    CreateDBProxyEndpointResponseTypeDef,
    CreateDBProxyResponseTypeDef,
    CreateDBSecurityGroupResultTypeDef,
    CreateDBSnapshotResultTypeDef,
    CreateDBSubnetGroupResultTypeDef,
    CreateEventSubscriptionResultTypeDef,
    CreateGlobalClusterResultTypeDef,
    CreateOptionGroupResultTypeDef,
    CustomAvailabilityZoneMessageTypeDef,
    DBClusterBacktrackMessageTypeDef,
    DBClusterBacktrackTypeDef,
    DBClusterCapacityInfoTypeDef,
    DBClusterEndpointMessageTypeDef,
    DBClusterEndpointTypeDef,
    DBClusterMessageTypeDef,
    DBClusterParameterGroupDetailsTypeDef,
    DBClusterParameterGroupNameMessageTypeDef,
    DBClusterParameterGroupsMessageTypeDef,
    DBClusterSnapshotMessageTypeDef,
    DBEngineVersionMessageTypeDef,
    DBInstanceAutomatedBackupMessageTypeDef,
    DBInstanceMessageTypeDef,
    DBParameterGroupDetailsTypeDef,
    DBParameterGroupNameMessageTypeDef,
    DBParameterGroupsMessageTypeDef,
    DBSecurityGroupMessageTypeDef,
    DBSnapshotMessageTypeDef,
    DBSubnetGroupMessageTypeDef,
    DeleteCustomAvailabilityZoneResultTypeDef,
    DeleteDBClusterResultTypeDef,
    DeleteDBClusterSnapshotResultTypeDef,
    DeleteDBInstanceAutomatedBackupResultTypeDef,
    DeleteDBInstanceResultTypeDef,
    DeleteDBProxyEndpointResponseTypeDef,
    DeleteDBProxyResponseTypeDef,
    DeleteDBSnapshotResultTypeDef,
    DeleteEventSubscriptionResultTypeDef,
    DeleteGlobalClusterResultTypeDef,
    DescribeDBClusterSnapshotAttributesResultTypeDef,
    DescribeDBLogFilesResponseTypeDef,
    DescribeDBProxiesResponseTypeDef,
    DescribeDBProxyEndpointsResponseTypeDef,
    DescribeDBProxyTargetGroupsResponseTypeDef,
    DescribeDBProxyTargetsResponseTypeDef,
    DescribeDBSnapshotAttributesResultTypeDef,
    DescribeEngineDefaultClusterParametersResultTypeDef,
    DescribeEngineDefaultParametersResultTypeDef,
    DescribeValidDBInstanceModificationsResultTypeDef,
    DownloadDBLogFilePortionDetailsTypeDef,
    EventCategoriesMessageTypeDef,
    EventsMessageTypeDef,
    EventSubscriptionsMessageTypeDef,
    ExportTasksMessageTypeDef,
    ExportTaskTypeDef,
    FailoverDBClusterResultTypeDef,
    FailoverGlobalClusterResultTypeDef,
    FilterTypeDef,
    GlobalClustersMessageTypeDef,
    InstallationMediaMessageTypeDef,
    InstallationMediaTypeDef,
    ModifyCertificatesResultTypeDef,
    ModifyDBClusterResultTypeDef,
    ModifyDBClusterSnapshotAttributeResultTypeDef,
    ModifyDBInstanceResultTypeDef,
    ModifyDBProxyEndpointResponseTypeDef,
    ModifyDBProxyResponseTypeDef,
    ModifyDBProxyTargetGroupResponseTypeDef,
    ModifyDBSnapshotAttributeResultTypeDef,
    ModifyDBSnapshotResultTypeDef,
    ModifyDBSubnetGroupResultTypeDef,
    ModifyEventSubscriptionResultTypeDef,
    ModifyGlobalClusterResultTypeDef,
    ModifyOptionGroupResultTypeDef,
    OptionConfigurationTypeDef,
    OptionGroupOptionsMessageTypeDef,
    OptionGroupsTypeDef,
    OrderableDBInstanceOptionsMessageTypeDef,
    ParameterTypeDef,
    PendingMaintenanceActionsMessageTypeDef,
    ProcessorFeatureTypeDef,
    PromoteReadReplicaDBClusterResultTypeDef,
    PromoteReadReplicaResultTypeDef,
    PurchaseReservedDBInstancesOfferingResultTypeDef,
    RebootDBInstanceResultTypeDef,
    RegisterDBProxyTargetsResponseTypeDef,
    RemoveFromGlobalClusterResultTypeDef,
    RemoveSourceIdentifierFromSubscriptionResultTypeDef,
    ReservedDBInstanceMessageTypeDef,
    ReservedDBInstancesOfferingMessageTypeDef,
    RestoreDBClusterFromS3ResultTypeDef,
    RestoreDBClusterFromSnapshotResultTypeDef,
    RestoreDBClusterToPointInTimeResultTypeDef,
    RestoreDBInstanceFromDBSnapshotResultTypeDef,
    RestoreDBInstanceFromS3ResultTypeDef,
    RestoreDBInstanceToPointInTimeResultTypeDef,
    RevokeDBSecurityGroupIngressResultTypeDef,
    ScalingConfigurationTypeDef,
    SourceRegionMessageTypeDef,
    StartActivityStreamResponseTypeDef,
    StartDBClusterResultTypeDef,
    StartDBInstanceAutomatedBackupsReplicationResultTypeDef,
    StartDBInstanceResultTypeDef,
    StopActivityStreamResponseTypeDef,
    StopDBClusterResultTypeDef,
    StopDBInstanceAutomatedBackupsReplicationResultTypeDef,
    StopDBInstanceResultTypeDef,
    TagListMessageTypeDef,
    TagTypeDef,
    UserAuthConfigTypeDef,
)
from .waiter import (
    DBClusterSnapshotAvailableWaiter,
    DBClusterSnapshotDeletedWaiter,
    DBInstanceAvailableWaiter,
    DBInstanceDeletedWaiter,
    DBSnapshotAvailableWaiter,
    DBSnapshotCompletedWaiter,
    DBSnapshotDeletedWaiter,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("RDSClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str
    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AuthorizationAlreadyExistsFault: Type[BotocoreClientError]
    AuthorizationNotFoundFault: Type[BotocoreClientError]
    AuthorizationQuotaExceededFault: Type[BotocoreClientError]
    BackupPolicyNotFoundFault: Type[BotocoreClientError]
    CertificateNotFoundFault: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    CustomAvailabilityZoneAlreadyExistsFault: Type[BotocoreClientError]
    CustomAvailabilityZoneNotFoundFault: Type[BotocoreClientError]
    CustomAvailabilityZoneQuotaExceededFault: Type[BotocoreClientError]
    DBClusterAlreadyExistsFault: Type[BotocoreClientError]
    DBClusterBacktrackNotFoundFault: Type[BotocoreClientError]
    DBClusterEndpointAlreadyExistsFault: Type[BotocoreClientError]
    DBClusterEndpointNotFoundFault: Type[BotocoreClientError]
    DBClusterEndpointQuotaExceededFault: Type[BotocoreClientError]
    DBClusterNotFoundFault: Type[BotocoreClientError]
    DBClusterParameterGroupNotFoundFault: Type[BotocoreClientError]
    DBClusterQuotaExceededFault: Type[BotocoreClientError]
    DBClusterRoleAlreadyExistsFault: Type[BotocoreClientError]
    DBClusterRoleNotFoundFault: Type[BotocoreClientError]
    DBClusterRoleQuotaExceededFault: Type[BotocoreClientError]
    DBClusterSnapshotAlreadyExistsFault: Type[BotocoreClientError]
    DBClusterSnapshotNotFoundFault: Type[BotocoreClientError]
    DBInstanceAlreadyExistsFault: Type[BotocoreClientError]
    DBInstanceAutomatedBackupNotFoundFault: Type[BotocoreClientError]
    DBInstanceAutomatedBackupQuotaExceededFault: Type[BotocoreClientError]
    DBInstanceNotFoundFault: Type[BotocoreClientError]
    DBInstanceRoleAlreadyExistsFault: Type[BotocoreClientError]
    DBInstanceRoleNotFoundFault: Type[BotocoreClientError]
    DBInstanceRoleQuotaExceededFault: Type[BotocoreClientError]
    DBLogFileNotFoundFault: Type[BotocoreClientError]
    DBParameterGroupAlreadyExistsFault: Type[BotocoreClientError]
    DBParameterGroupNotFoundFault: Type[BotocoreClientError]
    DBParameterGroupQuotaExceededFault: Type[BotocoreClientError]
    DBProxyAlreadyExistsFault: Type[BotocoreClientError]
    DBProxyEndpointAlreadyExistsFault: Type[BotocoreClientError]
    DBProxyEndpointNotFoundFault: Type[BotocoreClientError]
    DBProxyEndpointQuotaExceededFault: Type[BotocoreClientError]
    DBProxyNotFoundFault: Type[BotocoreClientError]
    DBProxyQuotaExceededFault: Type[BotocoreClientError]
    DBProxyTargetAlreadyRegisteredFault: Type[BotocoreClientError]
    DBProxyTargetGroupNotFoundFault: Type[BotocoreClientError]
    DBProxyTargetNotFoundFault: Type[BotocoreClientError]
    DBSecurityGroupAlreadyExistsFault: Type[BotocoreClientError]
    DBSecurityGroupNotFoundFault: Type[BotocoreClientError]
    DBSecurityGroupNotSupportedFault: Type[BotocoreClientError]
    DBSecurityGroupQuotaExceededFault: Type[BotocoreClientError]
    DBSnapshotAlreadyExistsFault: Type[BotocoreClientError]
    DBSnapshotNotFoundFault: Type[BotocoreClientError]
    DBSubnetGroupAlreadyExistsFault: Type[BotocoreClientError]
    DBSubnetGroupDoesNotCoverEnoughAZs: Type[BotocoreClientError]
    DBSubnetGroupNotAllowedFault: Type[BotocoreClientError]
    DBSubnetGroupNotFoundFault: Type[BotocoreClientError]
    DBSubnetGroupQuotaExceededFault: Type[BotocoreClientError]
    DBSubnetQuotaExceededFault: Type[BotocoreClientError]
    DBUpgradeDependencyFailureFault: Type[BotocoreClientError]
    DomainNotFoundFault: Type[BotocoreClientError]
    EventSubscriptionQuotaExceededFault: Type[BotocoreClientError]
    ExportTaskAlreadyExistsFault: Type[BotocoreClientError]
    ExportTaskNotFoundFault: Type[BotocoreClientError]
    GlobalClusterAlreadyExistsFault: Type[BotocoreClientError]
    GlobalClusterNotFoundFault: Type[BotocoreClientError]
    GlobalClusterQuotaExceededFault: Type[BotocoreClientError]
    IamRoleMissingPermissionsFault: Type[BotocoreClientError]
    IamRoleNotFoundFault: Type[BotocoreClientError]
    InstallationMediaAlreadyExistsFault: Type[BotocoreClientError]
    InstallationMediaNotFoundFault: Type[BotocoreClientError]
    InstanceQuotaExceededFault: Type[BotocoreClientError]
    InsufficientAvailableIPsInSubnetFault: Type[BotocoreClientError]
    InsufficientDBClusterCapacityFault: Type[BotocoreClientError]
    InsufficientDBInstanceCapacityFault: Type[BotocoreClientError]
    InsufficientStorageClusterCapacityFault: Type[BotocoreClientError]
    InvalidDBClusterCapacityFault: Type[BotocoreClientError]
    InvalidDBClusterEndpointStateFault: Type[BotocoreClientError]
    InvalidDBClusterSnapshotStateFault: Type[BotocoreClientError]
    InvalidDBClusterStateFault: Type[BotocoreClientError]
    InvalidDBInstanceAutomatedBackupStateFault: Type[BotocoreClientError]
    InvalidDBInstanceStateFault: Type[BotocoreClientError]
    InvalidDBParameterGroupStateFault: Type[BotocoreClientError]
    InvalidDBProxyEndpointStateFault: Type[BotocoreClientError]
    InvalidDBProxyStateFault: Type[BotocoreClientError]
    InvalidDBSecurityGroupStateFault: Type[BotocoreClientError]
    InvalidDBSnapshotStateFault: Type[BotocoreClientError]
    InvalidDBSubnetGroupFault: Type[BotocoreClientError]
    InvalidDBSubnetGroupStateFault: Type[BotocoreClientError]
    InvalidDBSubnetStateFault: Type[BotocoreClientError]
    InvalidEventSubscriptionStateFault: Type[BotocoreClientError]
    InvalidExportOnlyFault: Type[BotocoreClientError]
    InvalidExportSourceStateFault: Type[BotocoreClientError]
    InvalidExportTaskStateFault: Type[BotocoreClientError]
    InvalidGlobalClusterStateFault: Type[BotocoreClientError]
    InvalidOptionGroupStateFault: Type[BotocoreClientError]
    InvalidRestoreFault: Type[BotocoreClientError]
    InvalidS3BucketFault: Type[BotocoreClientError]
    InvalidSubnet: Type[BotocoreClientError]
    InvalidVPCNetworkStateFault: Type[BotocoreClientError]
    KMSKeyNotAccessibleFault: Type[BotocoreClientError]
    OptionGroupAlreadyExistsFault: Type[BotocoreClientError]
    OptionGroupNotFoundFault: Type[BotocoreClientError]
    OptionGroupQuotaExceededFault: Type[BotocoreClientError]
    PointInTimeRestoreNotEnabledFault: Type[BotocoreClientError]
    ProvisionedIopsNotAvailableInAZFault: Type[BotocoreClientError]
    ReservedDBInstanceAlreadyExistsFault: Type[BotocoreClientError]
    ReservedDBInstanceNotFoundFault: Type[BotocoreClientError]
    ReservedDBInstanceQuotaExceededFault: Type[BotocoreClientError]
    ReservedDBInstancesOfferingNotFoundFault: Type[BotocoreClientError]
    ResourceNotFoundFault: Type[BotocoreClientError]
    SNSInvalidTopicFault: Type[BotocoreClientError]
    SNSNoAuthorizationFault: Type[BotocoreClientError]
    SNSTopicArnNotFoundFault: Type[BotocoreClientError]
    SharedSnapshotQuotaExceededFault: Type[BotocoreClientError]
    SnapshotQuotaExceededFault: Type[BotocoreClientError]
    SourceNotFoundFault: Type[BotocoreClientError]
    StorageQuotaExceededFault: Type[BotocoreClientError]
    StorageTypeNotSupportedFault: Type[BotocoreClientError]
    SubnetAlreadyInUse: Type[BotocoreClientError]
    SubscriptionAlreadyExistFault: Type[BotocoreClientError]
    SubscriptionCategoryNotFoundFault: Type[BotocoreClientError]
    SubscriptionNotFoundFault: Type[BotocoreClientError]

class RDSClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client)
    [Show boto3-stubs documentation](./client.md)
    """

    meta: ClientMeta
    exceptions: Exceptions
    def add_role_to_db_cluster(
        self, DBClusterIdentifier: str, RoleArn: str, FeatureName: str = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.add_role_to_db_cluster)
        [Show boto3-stubs documentation](./client.md#add_role_to_db_cluster)
        """
    def add_role_to_db_instance(
        self, DBInstanceIdentifier: str, RoleArn: str, FeatureName: str
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.add_role_to_db_instance)
        [Show boto3-stubs documentation](./client.md#add_role_to_db_instance)
        """
    def add_source_identifier_to_subscription(
        self, SubscriptionName: str, SourceIdentifier: str
    ) -> AddSourceIdentifierToSubscriptionResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.add_source_identifier_to_subscription)
        [Show boto3-stubs documentation](./client.md#add_source_identifier_to_subscription)
        """
    def add_tags_to_resource(self, ResourceName: str, Tags: List["TagTypeDef"]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.add_tags_to_resource)
        [Show boto3-stubs documentation](./client.md#add_tags_to_resource)
        """
    def apply_pending_maintenance_action(
        self, ResourceIdentifier: str, ApplyAction: str, OptInType: str
    ) -> ApplyPendingMaintenanceActionResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.apply_pending_maintenance_action)
        [Show boto3-stubs documentation](./client.md#apply_pending_maintenance_action)
        """
    def authorize_db_security_group_ingress(
        self,
        DBSecurityGroupName: str,
        CIDRIP: str = None,
        EC2SecurityGroupName: str = None,
        EC2SecurityGroupId: str = None,
        EC2SecurityGroupOwnerId: str = None,
    ) -> AuthorizeDBSecurityGroupIngressResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.authorize_db_security_group_ingress)
        [Show boto3-stubs documentation](./client.md#authorize_db_security_group_ingress)
        """
    def backtrack_db_cluster(
        self,
        DBClusterIdentifier: str,
        BacktrackTo: datetime,
        Force: bool = None,
        UseEarliestTimeOnPointInTimeUnavailable: bool = None,
    ) -> "DBClusterBacktrackTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.backtrack_db_cluster)
        [Show boto3-stubs documentation](./client.md#backtrack_db_cluster)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.can_paginate)
        [Show boto3-stubs documentation](./client.md#can_paginate)
        """
    def cancel_export_task(self, ExportTaskIdentifier: str) -> "ExportTaskTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.cancel_export_task)
        [Show boto3-stubs documentation](./client.md#cancel_export_task)
        """
    def copy_db_cluster_parameter_group(
        self,
        SourceDBClusterParameterGroupIdentifier: str,
        TargetDBClusterParameterGroupIdentifier: str,
        TargetDBClusterParameterGroupDescription: str,
        Tags: List["TagTypeDef"] = None,
    ) -> CopyDBClusterParameterGroupResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.copy_db_cluster_parameter_group)
        [Show boto3-stubs documentation](./client.md#copy_db_cluster_parameter_group)
        """
    def copy_db_cluster_snapshot(
        self,
        SourceDBClusterSnapshotIdentifier: str,
        TargetDBClusterSnapshotIdentifier: str,
        KmsKeyId: str = None,
        PreSignedUrl: str = None,
        CopyTags: bool = None,
        Tags: List["TagTypeDef"] = None,
        SourceRegion: str = None,
    ) -> CopyDBClusterSnapshotResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.copy_db_cluster_snapshot)
        [Show boto3-stubs documentation](./client.md#copy_db_cluster_snapshot)
        """
    def copy_db_parameter_group(
        self,
        SourceDBParameterGroupIdentifier: str,
        TargetDBParameterGroupIdentifier: str,
        TargetDBParameterGroupDescription: str,
        Tags: List["TagTypeDef"] = None,
    ) -> CopyDBParameterGroupResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.copy_db_parameter_group)
        [Show boto3-stubs documentation](./client.md#copy_db_parameter_group)
        """
    def copy_db_snapshot(
        self,
        SourceDBSnapshotIdentifier: str,
        TargetDBSnapshotIdentifier: str,
        KmsKeyId: str = None,
        Tags: List["TagTypeDef"] = None,
        CopyTags: bool = None,
        PreSignedUrl: str = None,
        OptionGroupName: str = None,
        TargetCustomAvailabilityZone: str = None,
        SourceRegion: str = None,
    ) -> CopyDBSnapshotResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.copy_db_snapshot)
        [Show boto3-stubs documentation](./client.md#copy_db_snapshot)
        """
    def copy_option_group(
        self,
        SourceOptionGroupIdentifier: str,
        TargetOptionGroupIdentifier: str,
        TargetOptionGroupDescription: str,
        Tags: List["TagTypeDef"] = None,
    ) -> CopyOptionGroupResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.copy_option_group)
        [Show boto3-stubs documentation](./client.md#copy_option_group)
        """
    def create_custom_availability_zone(
        self,
        CustomAvailabilityZoneName: str,
        ExistingVpnId: str = None,
        NewVpnTunnelName: str = None,
        VpnTunnelOriginatorIP: str = None,
    ) -> CreateCustomAvailabilityZoneResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.create_custom_availability_zone)
        [Show boto3-stubs documentation](./client.md#create_custom_availability_zone)
        """
    def create_db_cluster(
        self,
        DBClusterIdentifier: str,
        Engine: str,
        AvailabilityZones: List[str] = None,
        BackupRetentionPeriod: int = None,
        CharacterSetName: str = None,
        DatabaseName: str = None,
        DBClusterParameterGroupName: str = None,
        VpcSecurityGroupIds: List[str] = None,
        DBSubnetGroupName: str = None,
        EngineVersion: str = None,
        Port: int = None,
        MasterUsername: str = None,
        MasterUserPassword: str = None,
        OptionGroupName: str = None,
        PreferredBackupWindow: str = None,
        PreferredMaintenanceWindow: str = None,
        ReplicationSourceIdentifier: str = None,
        Tags: List["TagTypeDef"] = None,
        StorageEncrypted: bool = None,
        KmsKeyId: str = None,
        PreSignedUrl: str = None,
        EnableIAMDatabaseAuthentication: bool = None,
        BacktrackWindow: int = None,
        EnableCloudwatchLogsExports: List[str] = None,
        EngineMode: str = None,
        ScalingConfiguration: ScalingConfigurationTypeDef = None,
        DeletionProtection: bool = None,
        GlobalClusterIdentifier: str = None,
        EnableHttpEndpoint: bool = None,
        CopyTagsToSnapshot: bool = None,
        Domain: str = None,
        DomainIAMRoleName: str = None,
        EnableGlobalWriteForwarding: bool = None,
        SourceRegion: str = None,
    ) -> CreateDBClusterResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.create_db_cluster)
        [Show boto3-stubs documentation](./client.md#create_db_cluster)
        """
    def create_db_cluster_endpoint(
        self,
        DBClusterIdentifier: str,
        DBClusterEndpointIdentifier: str,
        EndpointType: str,
        StaticMembers: List[str] = None,
        ExcludedMembers: List[str] = None,
        Tags: List["TagTypeDef"] = None,
    ) -> "DBClusterEndpointTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.create_db_cluster_endpoint)
        [Show boto3-stubs documentation](./client.md#create_db_cluster_endpoint)
        """
    def create_db_cluster_parameter_group(
        self,
        DBClusterParameterGroupName: str,
        DBParameterGroupFamily: str,
        Description: str,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateDBClusterParameterGroupResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.create_db_cluster_parameter_group)
        [Show boto3-stubs documentation](./client.md#create_db_cluster_parameter_group)
        """
    def create_db_cluster_snapshot(
        self,
        DBClusterSnapshotIdentifier: str,
        DBClusterIdentifier: str,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateDBClusterSnapshotResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.create_db_cluster_snapshot)
        [Show boto3-stubs documentation](./client.md#create_db_cluster_snapshot)
        """
    def create_db_instance(
        self,
        DBInstanceIdentifier: str,
        DBInstanceClass: str,
        Engine: str,
        DBName: str = None,
        AllocatedStorage: int = None,
        MasterUsername: str = None,
        MasterUserPassword: str = None,
        DBSecurityGroups: List[str] = None,
        VpcSecurityGroupIds: List[str] = None,
        AvailabilityZone: str = None,
        DBSubnetGroupName: str = None,
        PreferredMaintenanceWindow: str = None,
        DBParameterGroupName: str = None,
        BackupRetentionPeriod: int = None,
        PreferredBackupWindow: str = None,
        Port: int = None,
        MultiAZ: bool = None,
        EngineVersion: str = None,
        AutoMinorVersionUpgrade: bool = None,
        LicenseModel: str = None,
        Iops: int = None,
        OptionGroupName: str = None,
        CharacterSetName: str = None,
        NcharCharacterSetName: str = None,
        PubliclyAccessible: bool = None,
        Tags: List["TagTypeDef"] = None,
        DBClusterIdentifier: str = None,
        StorageType: str = None,
        TdeCredentialArn: str = None,
        TdeCredentialPassword: str = None,
        StorageEncrypted: bool = None,
        KmsKeyId: str = None,
        Domain: str = None,
        CopyTagsToSnapshot: bool = None,
        MonitoringInterval: int = None,
        MonitoringRoleArn: str = None,
        DomainIAMRoleName: str = None,
        PromotionTier: int = None,
        Timezone: str = None,
        EnableIAMDatabaseAuthentication: bool = None,
        EnablePerformanceInsights: bool = None,
        PerformanceInsightsKMSKeyId: str = None,
        PerformanceInsightsRetentionPeriod: int = None,
        EnableCloudwatchLogsExports: List[str] = None,
        ProcessorFeatures: List["ProcessorFeatureTypeDef"] = None,
        DeletionProtection: bool = None,
        MaxAllocatedStorage: int = None,
        EnableCustomerOwnedIp: bool = None,
    ) -> CreateDBInstanceResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.create_db_instance)
        [Show boto3-stubs documentation](./client.md#create_db_instance)
        """
    def create_db_instance_read_replica(
        self,
        DBInstanceIdentifier: str,
        SourceDBInstanceIdentifier: str,
        DBInstanceClass: str = None,
        AvailabilityZone: str = None,
        Port: int = None,
        MultiAZ: bool = None,
        AutoMinorVersionUpgrade: bool = None,
        Iops: int = None,
        OptionGroupName: str = None,
        DBParameterGroupName: str = None,
        PubliclyAccessible: bool = None,
        Tags: List["TagTypeDef"] = None,
        DBSubnetGroupName: str = None,
        VpcSecurityGroupIds: List[str] = None,
        StorageType: str = None,
        CopyTagsToSnapshot: bool = None,
        MonitoringInterval: int = None,
        MonitoringRoleArn: str = None,
        KmsKeyId: str = None,
        PreSignedUrl: str = None,
        EnableIAMDatabaseAuthentication: bool = None,
        EnablePerformanceInsights: bool = None,
        PerformanceInsightsKMSKeyId: str = None,
        PerformanceInsightsRetentionPeriod: int = None,
        EnableCloudwatchLogsExports: List[str] = None,
        ProcessorFeatures: List["ProcessorFeatureTypeDef"] = None,
        UseDefaultProcessorFeatures: bool = None,
        DeletionProtection: bool = None,
        Domain: str = None,
        DomainIAMRoleName: str = None,
        ReplicaMode: ReplicaModeType = None,
        MaxAllocatedStorage: int = None,
        SourceRegion: str = None,
    ) -> CreateDBInstanceReadReplicaResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.create_db_instance_read_replica)
        [Show boto3-stubs documentation](./client.md#create_db_instance_read_replica)
        """
    def create_db_parameter_group(
        self,
        DBParameterGroupName: str,
        DBParameterGroupFamily: str,
        Description: str,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateDBParameterGroupResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.create_db_parameter_group)
        [Show boto3-stubs documentation](./client.md#create_db_parameter_group)
        """
    def create_db_proxy(
        self,
        DBProxyName: str,
        EngineFamily: EngineFamilyType,
        Auth: List[UserAuthConfigTypeDef],
        RoleArn: str,
        VpcSubnetIds: List[str],
        VpcSecurityGroupIds: List[str] = None,
        RequireTLS: bool = None,
        IdleClientTimeout: int = None,
        DebugLogging: bool = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateDBProxyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.create_db_proxy)
        [Show boto3-stubs documentation](./client.md#create_db_proxy)
        """
    def create_db_proxy_endpoint(
        self,
        DBProxyName: str,
        DBProxyEndpointName: str,
        VpcSubnetIds: List[str],
        VpcSecurityGroupIds: List[str] = None,
        TargetRole: DBProxyEndpointTargetRoleType = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateDBProxyEndpointResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.create_db_proxy_endpoint)
        [Show boto3-stubs documentation](./client.md#create_db_proxy_endpoint)
        """
    def create_db_security_group(
        self,
        DBSecurityGroupName: str,
        DBSecurityGroupDescription: str,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateDBSecurityGroupResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.create_db_security_group)
        [Show boto3-stubs documentation](./client.md#create_db_security_group)
        """
    def create_db_snapshot(
        self, DBSnapshotIdentifier: str, DBInstanceIdentifier: str, Tags: List["TagTypeDef"] = None
    ) -> CreateDBSnapshotResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.create_db_snapshot)
        [Show boto3-stubs documentation](./client.md#create_db_snapshot)
        """
    def create_db_subnet_group(
        self,
        DBSubnetGroupName: str,
        DBSubnetGroupDescription: str,
        SubnetIds: List[str],
        Tags: List["TagTypeDef"] = None,
    ) -> CreateDBSubnetGroupResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.create_db_subnet_group)
        [Show boto3-stubs documentation](./client.md#create_db_subnet_group)
        """
    def create_event_subscription(
        self,
        SubscriptionName: str,
        SnsTopicArn: str,
        SourceType: str = None,
        EventCategories: List[str] = None,
        SourceIds: List[str] = None,
        Enabled: bool = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateEventSubscriptionResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.create_event_subscription)
        [Show boto3-stubs documentation](./client.md#create_event_subscription)
        """
    def create_global_cluster(
        self,
        GlobalClusterIdentifier: str = None,
        SourceDBClusterIdentifier: str = None,
        Engine: str = None,
        EngineVersion: str = None,
        DeletionProtection: bool = None,
        DatabaseName: str = None,
        StorageEncrypted: bool = None,
    ) -> CreateGlobalClusterResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.create_global_cluster)
        [Show boto3-stubs documentation](./client.md#create_global_cluster)
        """
    def create_option_group(
        self,
        OptionGroupName: str,
        EngineName: str,
        MajorEngineVersion: str,
        OptionGroupDescription: str,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateOptionGroupResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.create_option_group)
        [Show boto3-stubs documentation](./client.md#create_option_group)
        """
    def delete_custom_availability_zone(
        self, CustomAvailabilityZoneId: str
    ) -> DeleteCustomAvailabilityZoneResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.delete_custom_availability_zone)
        [Show boto3-stubs documentation](./client.md#delete_custom_availability_zone)
        """
    def delete_db_cluster(
        self,
        DBClusterIdentifier: str,
        SkipFinalSnapshot: bool = None,
        FinalDBSnapshotIdentifier: str = None,
    ) -> DeleteDBClusterResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.delete_db_cluster)
        [Show boto3-stubs documentation](./client.md#delete_db_cluster)
        """
    def delete_db_cluster_endpoint(
        self, DBClusterEndpointIdentifier: str
    ) -> "DBClusterEndpointTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.delete_db_cluster_endpoint)
        [Show boto3-stubs documentation](./client.md#delete_db_cluster_endpoint)
        """
    def delete_db_cluster_parameter_group(self, DBClusterParameterGroupName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.delete_db_cluster_parameter_group)
        [Show boto3-stubs documentation](./client.md#delete_db_cluster_parameter_group)
        """
    def delete_db_cluster_snapshot(
        self, DBClusterSnapshotIdentifier: str
    ) -> DeleteDBClusterSnapshotResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.delete_db_cluster_snapshot)
        [Show boto3-stubs documentation](./client.md#delete_db_cluster_snapshot)
        """
    def delete_db_instance(
        self,
        DBInstanceIdentifier: str,
        SkipFinalSnapshot: bool = None,
        FinalDBSnapshotIdentifier: str = None,
        DeleteAutomatedBackups: bool = None,
    ) -> DeleteDBInstanceResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.delete_db_instance)
        [Show boto3-stubs documentation](./client.md#delete_db_instance)
        """
    def delete_db_instance_automated_backup(
        self, DbiResourceId: str = None, DBInstanceAutomatedBackupsArn: str = None
    ) -> DeleteDBInstanceAutomatedBackupResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.delete_db_instance_automated_backup)
        [Show boto3-stubs documentation](./client.md#delete_db_instance_automated_backup)
        """
    def delete_db_parameter_group(self, DBParameterGroupName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.delete_db_parameter_group)
        [Show boto3-stubs documentation](./client.md#delete_db_parameter_group)
        """
    def delete_db_proxy(self, DBProxyName: str) -> DeleteDBProxyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.delete_db_proxy)
        [Show boto3-stubs documentation](./client.md#delete_db_proxy)
        """
    def delete_db_proxy_endpoint(
        self, DBProxyEndpointName: str
    ) -> DeleteDBProxyEndpointResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.delete_db_proxy_endpoint)
        [Show boto3-stubs documentation](./client.md#delete_db_proxy_endpoint)
        """
    def delete_db_security_group(self, DBSecurityGroupName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.delete_db_security_group)
        [Show boto3-stubs documentation](./client.md#delete_db_security_group)
        """
    def delete_db_snapshot(self, DBSnapshotIdentifier: str) -> DeleteDBSnapshotResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.delete_db_snapshot)
        [Show boto3-stubs documentation](./client.md#delete_db_snapshot)
        """
    def delete_db_subnet_group(self, DBSubnetGroupName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.delete_db_subnet_group)
        [Show boto3-stubs documentation](./client.md#delete_db_subnet_group)
        """
    def delete_event_subscription(
        self, SubscriptionName: str
    ) -> DeleteEventSubscriptionResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.delete_event_subscription)
        [Show boto3-stubs documentation](./client.md#delete_event_subscription)
        """
    def delete_global_cluster(
        self, GlobalClusterIdentifier: str
    ) -> DeleteGlobalClusterResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.delete_global_cluster)
        [Show boto3-stubs documentation](./client.md#delete_global_cluster)
        """
    def delete_installation_media(self, InstallationMediaId: str) -> "InstallationMediaTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.delete_installation_media)
        [Show boto3-stubs documentation](./client.md#delete_installation_media)
        """
    def delete_option_group(self, OptionGroupName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.delete_option_group)
        [Show boto3-stubs documentation](./client.md#delete_option_group)
        """
    def deregister_db_proxy_targets(
        self,
        DBProxyName: str,
        TargetGroupName: str = None,
        DBInstanceIdentifiers: List[str] = None,
        DBClusterIdentifiers: List[str] = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.deregister_db_proxy_targets)
        [Show boto3-stubs documentation](./client.md#deregister_db_proxy_targets)
        """
    def describe_account_attributes(self) -> AccountAttributesMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.describe_account_attributes)
        [Show boto3-stubs documentation](./client.md#describe_account_attributes)
        """
    def describe_certificates(
        self,
        CertificateIdentifier: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> CertificateMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.describe_certificates)
        [Show boto3-stubs documentation](./client.md#describe_certificates)
        """
    def describe_custom_availability_zones(
        self,
        CustomAvailabilityZoneId: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> CustomAvailabilityZoneMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.describe_custom_availability_zones)
        [Show boto3-stubs documentation](./client.md#describe_custom_availability_zones)
        """
    def describe_db_cluster_backtracks(
        self,
        DBClusterIdentifier: str,
        BacktrackIdentifier: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> DBClusterBacktrackMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.describe_db_cluster_backtracks)
        [Show boto3-stubs documentation](./client.md#describe_db_cluster_backtracks)
        """
    def describe_db_cluster_endpoints(
        self,
        DBClusterIdentifier: str = None,
        DBClusterEndpointIdentifier: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> DBClusterEndpointMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.describe_db_cluster_endpoints)
        [Show boto3-stubs documentation](./client.md#describe_db_cluster_endpoints)
        """
    def describe_db_cluster_parameter_groups(
        self,
        DBClusterParameterGroupName: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> DBClusterParameterGroupsMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.describe_db_cluster_parameter_groups)
        [Show boto3-stubs documentation](./client.md#describe_db_cluster_parameter_groups)
        """
    def describe_db_cluster_parameters(
        self,
        DBClusterParameterGroupName: str,
        Source: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> DBClusterParameterGroupDetailsTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.describe_db_cluster_parameters)
        [Show boto3-stubs documentation](./client.md#describe_db_cluster_parameters)
        """
    def describe_db_cluster_snapshot_attributes(
        self, DBClusterSnapshotIdentifier: str
    ) -> DescribeDBClusterSnapshotAttributesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.describe_db_cluster_snapshot_attributes)
        [Show boto3-stubs documentation](./client.md#describe_db_cluster_snapshot_attributes)
        """
    def describe_db_cluster_snapshots(
        self,
        DBClusterIdentifier: str = None,
        DBClusterSnapshotIdentifier: str = None,
        SnapshotType: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        IncludeShared: bool = None,
        IncludePublic: bool = None,
    ) -> DBClusterSnapshotMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.describe_db_cluster_snapshots)
        [Show boto3-stubs documentation](./client.md#describe_db_cluster_snapshots)
        """
    def describe_db_clusters(
        self,
        DBClusterIdentifier: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        IncludeShared: bool = None,
    ) -> DBClusterMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.describe_db_clusters)
        [Show boto3-stubs documentation](./client.md#describe_db_clusters)
        """
    def describe_db_engine_versions(
        self,
        Engine: str = None,
        EngineVersion: str = None,
        DBParameterGroupFamily: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        DefaultOnly: bool = None,
        ListSupportedCharacterSets: bool = None,
        ListSupportedTimezones: bool = None,
        IncludeAll: bool = None,
    ) -> DBEngineVersionMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.describe_db_engine_versions)
        [Show boto3-stubs documentation](./client.md#describe_db_engine_versions)
        """
    def describe_db_instance_automated_backups(
        self,
        DbiResourceId: str = None,
        DBInstanceIdentifier: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        DBInstanceAutomatedBackupsArn: str = None,
    ) -> DBInstanceAutomatedBackupMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.describe_db_instance_automated_backups)
        [Show boto3-stubs documentation](./client.md#describe_db_instance_automated_backups)
        """
    def describe_db_instances(
        self,
        DBInstanceIdentifier: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> DBInstanceMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.describe_db_instances)
        [Show boto3-stubs documentation](./client.md#describe_db_instances)
        """
    def describe_db_log_files(
        self,
        DBInstanceIdentifier: str,
        FilenameContains: str = None,
        FileLastWritten: int = None,
        FileSize: int = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> DescribeDBLogFilesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.describe_db_log_files)
        [Show boto3-stubs documentation](./client.md#describe_db_log_files)
        """
    def describe_db_parameter_groups(
        self,
        DBParameterGroupName: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> DBParameterGroupsMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.describe_db_parameter_groups)
        [Show boto3-stubs documentation](./client.md#describe_db_parameter_groups)
        """
    def describe_db_parameters(
        self,
        DBParameterGroupName: str,
        Source: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> DBParameterGroupDetailsTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.describe_db_parameters)
        [Show boto3-stubs documentation](./client.md#describe_db_parameters)
        """
    def describe_db_proxies(
        self,
        DBProxyName: str = None,
        Filters: List[FilterTypeDef] = None,
        Marker: str = None,
        MaxRecords: int = None,
    ) -> DescribeDBProxiesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.describe_db_proxies)
        [Show boto3-stubs documentation](./client.md#describe_db_proxies)
        """
    def describe_db_proxy_endpoints(
        self,
        DBProxyName: str = None,
        DBProxyEndpointName: str = None,
        Filters: List[FilterTypeDef] = None,
        Marker: str = None,
        MaxRecords: int = None,
    ) -> DescribeDBProxyEndpointsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.describe_db_proxy_endpoints)
        [Show boto3-stubs documentation](./client.md#describe_db_proxy_endpoints)
        """
    def describe_db_proxy_target_groups(
        self,
        DBProxyName: str,
        TargetGroupName: str = None,
        Filters: List[FilterTypeDef] = None,
        Marker: str = None,
        MaxRecords: int = None,
    ) -> DescribeDBProxyTargetGroupsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.describe_db_proxy_target_groups)
        [Show boto3-stubs documentation](./client.md#describe_db_proxy_target_groups)
        """
    def describe_db_proxy_targets(
        self,
        DBProxyName: str,
        TargetGroupName: str = None,
        Filters: List[FilterTypeDef] = None,
        Marker: str = None,
        MaxRecords: int = None,
    ) -> DescribeDBProxyTargetsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.describe_db_proxy_targets)
        [Show boto3-stubs documentation](./client.md#describe_db_proxy_targets)
        """
    def describe_db_security_groups(
        self,
        DBSecurityGroupName: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> DBSecurityGroupMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.describe_db_security_groups)
        [Show boto3-stubs documentation](./client.md#describe_db_security_groups)
        """
    def describe_db_snapshot_attributes(
        self, DBSnapshotIdentifier: str
    ) -> DescribeDBSnapshotAttributesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.describe_db_snapshot_attributes)
        [Show boto3-stubs documentation](./client.md#describe_db_snapshot_attributes)
        """
    def describe_db_snapshots(
        self,
        DBInstanceIdentifier: str = None,
        DBSnapshotIdentifier: str = None,
        SnapshotType: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        IncludeShared: bool = None,
        IncludePublic: bool = None,
        DbiResourceId: str = None,
    ) -> DBSnapshotMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.describe_db_snapshots)
        [Show boto3-stubs documentation](./client.md#describe_db_snapshots)
        """
    def describe_db_subnet_groups(
        self,
        DBSubnetGroupName: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> DBSubnetGroupMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.describe_db_subnet_groups)
        [Show boto3-stubs documentation](./client.md#describe_db_subnet_groups)
        """
    def describe_engine_default_cluster_parameters(
        self,
        DBParameterGroupFamily: str,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> DescribeEngineDefaultClusterParametersResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.describe_engine_default_cluster_parameters)
        [Show boto3-stubs documentation](./client.md#describe_engine_default_cluster_parameters)
        """
    def describe_engine_default_parameters(
        self,
        DBParameterGroupFamily: str,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> DescribeEngineDefaultParametersResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.describe_engine_default_parameters)
        [Show boto3-stubs documentation](./client.md#describe_engine_default_parameters)
        """
    def describe_event_categories(
        self, SourceType: str = None, Filters: List[FilterTypeDef] = None
    ) -> EventCategoriesMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.describe_event_categories)
        [Show boto3-stubs documentation](./client.md#describe_event_categories)
        """
    def describe_event_subscriptions(
        self,
        SubscriptionName: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> EventSubscriptionsMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.describe_event_subscriptions)
        [Show boto3-stubs documentation](./client.md#describe_event_subscriptions)
        """
    def describe_events(
        self,
        SourceIdentifier: str = None,
        SourceType: SourceTypeType = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        Duration: int = None,
        EventCategories: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> EventsMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.describe_events)
        [Show boto3-stubs documentation](./client.md#describe_events)
        """
    def describe_export_tasks(
        self,
        ExportTaskIdentifier: str = None,
        SourceArn: str = None,
        Filters: List[FilterTypeDef] = None,
        Marker: str = None,
        MaxRecords: int = None,
    ) -> ExportTasksMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.describe_export_tasks)
        [Show boto3-stubs documentation](./client.md#describe_export_tasks)
        """
    def describe_global_clusters(
        self,
        GlobalClusterIdentifier: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> GlobalClustersMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.describe_global_clusters)
        [Show boto3-stubs documentation](./client.md#describe_global_clusters)
        """
    def describe_installation_media(
        self,
        InstallationMediaId: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> InstallationMediaMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.describe_installation_media)
        [Show boto3-stubs documentation](./client.md#describe_installation_media)
        """
    def describe_option_group_options(
        self,
        EngineName: str,
        MajorEngineVersion: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> OptionGroupOptionsMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.describe_option_group_options)
        [Show boto3-stubs documentation](./client.md#describe_option_group_options)
        """
    def describe_option_groups(
        self,
        OptionGroupName: str = None,
        Filters: List[FilterTypeDef] = None,
        Marker: str = None,
        MaxRecords: int = None,
        EngineName: str = None,
        MajorEngineVersion: str = None,
    ) -> OptionGroupsTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.describe_option_groups)
        [Show boto3-stubs documentation](./client.md#describe_option_groups)
        """
    def describe_orderable_db_instance_options(
        self,
        Engine: str,
        EngineVersion: str = None,
        DBInstanceClass: str = None,
        LicenseModel: str = None,
        AvailabilityZoneGroup: str = None,
        Vpc: bool = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> OrderableDBInstanceOptionsMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.describe_orderable_db_instance_options)
        [Show boto3-stubs documentation](./client.md#describe_orderable_db_instance_options)
        """
    def describe_pending_maintenance_actions(
        self,
        ResourceIdentifier: str = None,
        Filters: List[FilterTypeDef] = None,
        Marker: str = None,
        MaxRecords: int = None,
    ) -> PendingMaintenanceActionsMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.describe_pending_maintenance_actions)
        [Show boto3-stubs documentation](./client.md#describe_pending_maintenance_actions)
        """
    def describe_reserved_db_instances(
        self,
        ReservedDBInstanceId: str = None,
        ReservedDBInstancesOfferingId: str = None,
        DBInstanceClass: str = None,
        Duration: str = None,
        ProductDescription: str = None,
        OfferingType: str = None,
        MultiAZ: bool = None,
        LeaseId: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ReservedDBInstanceMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.describe_reserved_db_instances)
        [Show boto3-stubs documentation](./client.md#describe_reserved_db_instances)
        """
    def describe_reserved_db_instances_offerings(
        self,
        ReservedDBInstancesOfferingId: str = None,
        DBInstanceClass: str = None,
        Duration: str = None,
        ProductDescription: str = None,
        OfferingType: str = None,
        MultiAZ: bool = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ReservedDBInstancesOfferingMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.describe_reserved_db_instances_offerings)
        [Show boto3-stubs documentation](./client.md#describe_reserved_db_instances_offerings)
        """
    def describe_source_regions(
        self,
        RegionName: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        Filters: List[FilterTypeDef] = None,
    ) -> SourceRegionMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.describe_source_regions)
        [Show boto3-stubs documentation](./client.md#describe_source_regions)
        """
    def describe_valid_db_instance_modifications(
        self, DBInstanceIdentifier: str
    ) -> DescribeValidDBInstanceModificationsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.describe_valid_db_instance_modifications)
        [Show boto3-stubs documentation](./client.md#describe_valid_db_instance_modifications)
        """
    def download_db_log_file_portion(
        self,
        DBInstanceIdentifier: str,
        LogFileName: str,
        Marker: str = None,
        NumberOfLines: int = None,
    ) -> DownloadDBLogFilePortionDetailsTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.download_db_log_file_portion)
        [Show boto3-stubs documentation](./client.md#download_db_log_file_portion)
        """
    def failover_db_cluster(
        self, DBClusterIdentifier: str, TargetDBInstanceIdentifier: str = None
    ) -> FailoverDBClusterResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.failover_db_cluster)
        [Show boto3-stubs documentation](./client.md#failover_db_cluster)
        """
    def failover_global_cluster(
        self, GlobalClusterIdentifier: str, TargetDbClusterIdentifier: str
    ) -> FailoverGlobalClusterResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.failover_global_cluster)
        [Show boto3-stubs documentation](./client.md#failover_global_cluster)
        """
    def generate_db_auth_token(
        self, DBHostname: str, Port: int, DBUsername: str, Region: str = None
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.generate_db_auth_token)
        [Show boto3-stubs documentation](./client.md#generate_db_auth_token)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.generate_presigned_url)
        [Show boto3-stubs documentation](./client.md#generate_presigned_url)
        """
    def import_installation_media(
        self,
        CustomAvailabilityZoneId: str,
        Engine: str,
        EngineVersion: str,
        EngineInstallationMediaPath: str,
        OSInstallationMediaPath: str,
    ) -> "InstallationMediaTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.import_installation_media)
        [Show boto3-stubs documentation](./client.md#import_installation_media)
        """
    def list_tags_for_resource(
        self, ResourceName: str, Filters: List[FilterTypeDef] = None
    ) -> TagListMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](./client.md#list_tags_for_resource)
        """
    def modify_certificates(
        self, CertificateIdentifier: str = None, RemoveCustomerOverride: bool = None
    ) -> ModifyCertificatesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.modify_certificates)
        [Show boto3-stubs documentation](./client.md#modify_certificates)
        """
    def modify_current_db_cluster_capacity(
        self,
        DBClusterIdentifier: str,
        Capacity: int = None,
        SecondsBeforeTimeout: int = None,
        TimeoutAction: str = None,
    ) -> DBClusterCapacityInfoTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.modify_current_db_cluster_capacity)
        [Show boto3-stubs documentation](./client.md#modify_current_db_cluster_capacity)
        """
    def modify_db_cluster(
        self,
        DBClusterIdentifier: str,
        NewDBClusterIdentifier: str = None,
        ApplyImmediately: bool = None,
        BackupRetentionPeriod: int = None,
        DBClusterParameterGroupName: str = None,
        VpcSecurityGroupIds: List[str] = None,
        Port: int = None,
        MasterUserPassword: str = None,
        OptionGroupName: str = None,
        PreferredBackupWindow: str = None,
        PreferredMaintenanceWindow: str = None,
        EnableIAMDatabaseAuthentication: bool = None,
        BacktrackWindow: int = None,
        CloudwatchLogsExportConfiguration: CloudwatchLogsExportConfigurationTypeDef = None,
        EngineVersion: str = None,
        AllowMajorVersionUpgrade: bool = None,
        DBInstanceParameterGroupName: str = None,
        Domain: str = None,
        DomainIAMRoleName: str = None,
        ScalingConfiguration: ScalingConfigurationTypeDef = None,
        DeletionProtection: bool = None,
        EnableHttpEndpoint: bool = None,
        CopyTagsToSnapshot: bool = None,
        EnableGlobalWriteForwarding: bool = None,
    ) -> ModifyDBClusterResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.modify_db_cluster)
        [Show boto3-stubs documentation](./client.md#modify_db_cluster)
        """
    def modify_db_cluster_endpoint(
        self,
        DBClusterEndpointIdentifier: str,
        EndpointType: str = None,
        StaticMembers: List[str] = None,
        ExcludedMembers: List[str] = None,
    ) -> "DBClusterEndpointTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.modify_db_cluster_endpoint)
        [Show boto3-stubs documentation](./client.md#modify_db_cluster_endpoint)
        """
    def modify_db_cluster_parameter_group(
        self, DBClusterParameterGroupName: str, Parameters: List["ParameterTypeDef"]
    ) -> DBClusterParameterGroupNameMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.modify_db_cluster_parameter_group)
        [Show boto3-stubs documentation](./client.md#modify_db_cluster_parameter_group)
        """
    def modify_db_cluster_snapshot_attribute(
        self,
        DBClusterSnapshotIdentifier: str,
        AttributeName: str,
        ValuesToAdd: List[str] = None,
        ValuesToRemove: List[str] = None,
    ) -> ModifyDBClusterSnapshotAttributeResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.modify_db_cluster_snapshot_attribute)
        [Show boto3-stubs documentation](./client.md#modify_db_cluster_snapshot_attribute)
        """
    def modify_db_instance(
        self,
        DBInstanceIdentifier: str,
        AllocatedStorage: int = None,
        DBInstanceClass: str = None,
        DBSubnetGroupName: str = None,
        DBSecurityGroups: List[str] = None,
        VpcSecurityGroupIds: List[str] = None,
        ApplyImmediately: bool = None,
        MasterUserPassword: str = None,
        DBParameterGroupName: str = None,
        BackupRetentionPeriod: int = None,
        PreferredBackupWindow: str = None,
        PreferredMaintenanceWindow: str = None,
        MultiAZ: bool = None,
        EngineVersion: str = None,
        AllowMajorVersionUpgrade: bool = None,
        AutoMinorVersionUpgrade: bool = None,
        LicenseModel: str = None,
        Iops: int = None,
        OptionGroupName: str = None,
        NewDBInstanceIdentifier: str = None,
        StorageType: str = None,
        TdeCredentialArn: str = None,
        TdeCredentialPassword: str = None,
        CACertificateIdentifier: str = None,
        Domain: str = None,
        CopyTagsToSnapshot: bool = None,
        MonitoringInterval: int = None,
        DBPortNumber: int = None,
        PubliclyAccessible: bool = None,
        MonitoringRoleArn: str = None,
        DomainIAMRoleName: str = None,
        PromotionTier: int = None,
        EnableIAMDatabaseAuthentication: bool = None,
        EnablePerformanceInsights: bool = None,
        PerformanceInsightsKMSKeyId: str = None,
        PerformanceInsightsRetentionPeriod: int = None,
        CloudwatchLogsExportConfiguration: CloudwatchLogsExportConfigurationTypeDef = None,
        ProcessorFeatures: List["ProcessorFeatureTypeDef"] = None,
        UseDefaultProcessorFeatures: bool = None,
        DeletionProtection: bool = None,
        MaxAllocatedStorage: int = None,
        CertificateRotationRestart: bool = None,
        ReplicaMode: ReplicaModeType = None,
        EnableCustomerOwnedIp: bool = None,
        AwsBackupRecoveryPointArn: str = None,
    ) -> ModifyDBInstanceResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.modify_db_instance)
        [Show boto3-stubs documentation](./client.md#modify_db_instance)
        """
    def modify_db_parameter_group(
        self, DBParameterGroupName: str, Parameters: List["ParameterTypeDef"]
    ) -> DBParameterGroupNameMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.modify_db_parameter_group)
        [Show boto3-stubs documentation](./client.md#modify_db_parameter_group)
        """
    def modify_db_proxy(
        self,
        DBProxyName: str,
        NewDBProxyName: str = None,
        Auth: List[UserAuthConfigTypeDef] = None,
        RequireTLS: bool = None,
        IdleClientTimeout: int = None,
        DebugLogging: bool = None,
        RoleArn: str = None,
        SecurityGroups: List[str] = None,
    ) -> ModifyDBProxyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.modify_db_proxy)
        [Show boto3-stubs documentation](./client.md#modify_db_proxy)
        """
    def modify_db_proxy_endpoint(
        self,
        DBProxyEndpointName: str,
        NewDBProxyEndpointName: str = None,
        VpcSecurityGroupIds: List[str] = None,
    ) -> ModifyDBProxyEndpointResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.modify_db_proxy_endpoint)
        [Show boto3-stubs documentation](./client.md#modify_db_proxy_endpoint)
        """
    def modify_db_proxy_target_group(
        self,
        TargetGroupName: str,
        DBProxyName: str,
        ConnectionPoolConfig: ConnectionPoolConfigurationTypeDef = None,
        NewName: str = None,
    ) -> ModifyDBProxyTargetGroupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.modify_db_proxy_target_group)
        [Show boto3-stubs documentation](./client.md#modify_db_proxy_target_group)
        """
    def modify_db_snapshot(
        self, DBSnapshotIdentifier: str, EngineVersion: str = None, OptionGroupName: str = None
    ) -> ModifyDBSnapshotResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.modify_db_snapshot)
        [Show boto3-stubs documentation](./client.md#modify_db_snapshot)
        """
    def modify_db_snapshot_attribute(
        self,
        DBSnapshotIdentifier: str,
        AttributeName: str,
        ValuesToAdd: List[str] = None,
        ValuesToRemove: List[str] = None,
    ) -> ModifyDBSnapshotAttributeResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.modify_db_snapshot_attribute)
        [Show boto3-stubs documentation](./client.md#modify_db_snapshot_attribute)
        """
    def modify_db_subnet_group(
        self, DBSubnetGroupName: str, SubnetIds: List[str], DBSubnetGroupDescription: str = None
    ) -> ModifyDBSubnetGroupResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.modify_db_subnet_group)
        [Show boto3-stubs documentation](./client.md#modify_db_subnet_group)
        """
    def modify_event_subscription(
        self,
        SubscriptionName: str,
        SnsTopicArn: str = None,
        SourceType: str = None,
        EventCategories: List[str] = None,
        Enabled: bool = None,
    ) -> ModifyEventSubscriptionResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.modify_event_subscription)
        [Show boto3-stubs documentation](./client.md#modify_event_subscription)
        """
    def modify_global_cluster(
        self,
        GlobalClusterIdentifier: str = None,
        NewGlobalClusterIdentifier: str = None,
        DeletionProtection: bool = None,
        EngineVersion: str = None,
        AllowMajorVersionUpgrade: bool = None,
    ) -> ModifyGlobalClusterResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.modify_global_cluster)
        [Show boto3-stubs documentation](./client.md#modify_global_cluster)
        """
    def modify_option_group(
        self,
        OptionGroupName: str,
        OptionsToInclude: List[OptionConfigurationTypeDef] = None,
        OptionsToRemove: List[str] = None,
        ApplyImmediately: bool = None,
    ) -> ModifyOptionGroupResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.modify_option_group)
        [Show boto3-stubs documentation](./client.md#modify_option_group)
        """
    def promote_read_replica(
        self,
        DBInstanceIdentifier: str,
        BackupRetentionPeriod: int = None,
        PreferredBackupWindow: str = None,
    ) -> PromoteReadReplicaResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.promote_read_replica)
        [Show boto3-stubs documentation](./client.md#promote_read_replica)
        """
    def promote_read_replica_db_cluster(
        self, DBClusterIdentifier: str
    ) -> PromoteReadReplicaDBClusterResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.promote_read_replica_db_cluster)
        [Show boto3-stubs documentation](./client.md#promote_read_replica_db_cluster)
        """
    def purchase_reserved_db_instances_offering(
        self,
        ReservedDBInstancesOfferingId: str,
        ReservedDBInstanceId: str = None,
        DBInstanceCount: int = None,
        Tags: List["TagTypeDef"] = None,
    ) -> PurchaseReservedDBInstancesOfferingResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.purchase_reserved_db_instances_offering)
        [Show boto3-stubs documentation](./client.md#purchase_reserved_db_instances_offering)
        """
    def reboot_db_instance(
        self, DBInstanceIdentifier: str, ForceFailover: bool = None
    ) -> RebootDBInstanceResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.reboot_db_instance)
        [Show boto3-stubs documentation](./client.md#reboot_db_instance)
        """
    def register_db_proxy_targets(
        self,
        DBProxyName: str,
        TargetGroupName: str = None,
        DBInstanceIdentifiers: List[str] = None,
        DBClusterIdentifiers: List[str] = None,
    ) -> RegisterDBProxyTargetsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.register_db_proxy_targets)
        [Show boto3-stubs documentation](./client.md#register_db_proxy_targets)
        """
    def remove_from_global_cluster(
        self, GlobalClusterIdentifier: str = None, DbClusterIdentifier: str = None
    ) -> RemoveFromGlobalClusterResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.remove_from_global_cluster)
        [Show boto3-stubs documentation](./client.md#remove_from_global_cluster)
        """
    def remove_role_from_db_cluster(
        self, DBClusterIdentifier: str, RoleArn: str, FeatureName: str = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.remove_role_from_db_cluster)
        [Show boto3-stubs documentation](./client.md#remove_role_from_db_cluster)
        """
    def remove_role_from_db_instance(
        self, DBInstanceIdentifier: str, RoleArn: str, FeatureName: str
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.remove_role_from_db_instance)
        [Show boto3-stubs documentation](./client.md#remove_role_from_db_instance)
        """
    def remove_source_identifier_from_subscription(
        self, SubscriptionName: str, SourceIdentifier: str
    ) -> RemoveSourceIdentifierFromSubscriptionResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.remove_source_identifier_from_subscription)
        [Show boto3-stubs documentation](./client.md#remove_source_identifier_from_subscription)
        """
    def remove_tags_from_resource(self, ResourceName: str, TagKeys: List[str]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.remove_tags_from_resource)
        [Show boto3-stubs documentation](./client.md#remove_tags_from_resource)
        """
    def reset_db_cluster_parameter_group(
        self,
        DBClusterParameterGroupName: str,
        ResetAllParameters: bool = None,
        Parameters: List["ParameterTypeDef"] = None,
    ) -> DBClusterParameterGroupNameMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.reset_db_cluster_parameter_group)
        [Show boto3-stubs documentation](./client.md#reset_db_cluster_parameter_group)
        """
    def reset_db_parameter_group(
        self,
        DBParameterGroupName: str,
        ResetAllParameters: bool = None,
        Parameters: List["ParameterTypeDef"] = None,
    ) -> DBParameterGroupNameMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.reset_db_parameter_group)
        [Show boto3-stubs documentation](./client.md#reset_db_parameter_group)
        """
    def restore_db_cluster_from_s3(
        self,
        DBClusterIdentifier: str,
        Engine: str,
        MasterUsername: str,
        MasterUserPassword: str,
        SourceEngine: str,
        SourceEngineVersion: str,
        S3BucketName: str,
        S3IngestionRoleArn: str,
        AvailabilityZones: List[str] = None,
        BackupRetentionPeriod: int = None,
        CharacterSetName: str = None,
        DatabaseName: str = None,
        DBClusterParameterGroupName: str = None,
        VpcSecurityGroupIds: List[str] = None,
        DBSubnetGroupName: str = None,
        EngineVersion: str = None,
        Port: int = None,
        OptionGroupName: str = None,
        PreferredBackupWindow: str = None,
        PreferredMaintenanceWindow: str = None,
        Tags: List["TagTypeDef"] = None,
        StorageEncrypted: bool = None,
        KmsKeyId: str = None,
        EnableIAMDatabaseAuthentication: bool = None,
        S3Prefix: str = None,
        BacktrackWindow: int = None,
        EnableCloudwatchLogsExports: List[str] = None,
        DeletionProtection: bool = None,
        CopyTagsToSnapshot: bool = None,
        Domain: str = None,
        DomainIAMRoleName: str = None,
    ) -> RestoreDBClusterFromS3ResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.restore_db_cluster_from_s3)
        [Show boto3-stubs documentation](./client.md#restore_db_cluster_from_s3)
        """
    def restore_db_cluster_from_snapshot(
        self,
        DBClusterIdentifier: str,
        SnapshotIdentifier: str,
        Engine: str,
        AvailabilityZones: List[str] = None,
        EngineVersion: str = None,
        Port: int = None,
        DBSubnetGroupName: str = None,
        DatabaseName: str = None,
        OptionGroupName: str = None,
        VpcSecurityGroupIds: List[str] = None,
        Tags: List["TagTypeDef"] = None,
        KmsKeyId: str = None,
        EnableIAMDatabaseAuthentication: bool = None,
        BacktrackWindow: int = None,
        EnableCloudwatchLogsExports: List[str] = None,
        EngineMode: str = None,
        ScalingConfiguration: ScalingConfigurationTypeDef = None,
        DBClusterParameterGroupName: str = None,
        DeletionProtection: bool = None,
        CopyTagsToSnapshot: bool = None,
        Domain: str = None,
        DomainIAMRoleName: str = None,
    ) -> RestoreDBClusterFromSnapshotResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.restore_db_cluster_from_snapshot)
        [Show boto3-stubs documentation](./client.md#restore_db_cluster_from_snapshot)
        """
    def restore_db_cluster_to_point_in_time(
        self,
        DBClusterIdentifier: str,
        SourceDBClusterIdentifier: str,
        RestoreType: str = None,
        RestoreToTime: datetime = None,
        UseLatestRestorableTime: bool = None,
        Port: int = None,
        DBSubnetGroupName: str = None,
        OptionGroupName: str = None,
        VpcSecurityGroupIds: List[str] = None,
        Tags: List["TagTypeDef"] = None,
        KmsKeyId: str = None,
        EnableIAMDatabaseAuthentication: bool = None,
        BacktrackWindow: int = None,
        EnableCloudwatchLogsExports: List[str] = None,
        DBClusterParameterGroupName: str = None,
        DeletionProtection: bool = None,
        CopyTagsToSnapshot: bool = None,
        Domain: str = None,
        DomainIAMRoleName: str = None,
    ) -> RestoreDBClusterToPointInTimeResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.restore_db_cluster_to_point_in_time)
        [Show boto3-stubs documentation](./client.md#restore_db_cluster_to_point_in_time)
        """
    def restore_db_instance_from_db_snapshot(
        self,
        DBInstanceIdentifier: str,
        DBSnapshotIdentifier: str,
        DBInstanceClass: str = None,
        Port: int = None,
        AvailabilityZone: str = None,
        DBSubnetGroupName: str = None,
        MultiAZ: bool = None,
        PubliclyAccessible: bool = None,
        AutoMinorVersionUpgrade: bool = None,
        LicenseModel: str = None,
        DBName: str = None,
        Engine: str = None,
        Iops: int = None,
        OptionGroupName: str = None,
        Tags: List["TagTypeDef"] = None,
        StorageType: str = None,
        TdeCredentialArn: str = None,
        TdeCredentialPassword: str = None,
        VpcSecurityGroupIds: List[str] = None,
        Domain: str = None,
        CopyTagsToSnapshot: bool = None,
        DomainIAMRoleName: str = None,
        EnableIAMDatabaseAuthentication: bool = None,
        EnableCloudwatchLogsExports: List[str] = None,
        ProcessorFeatures: List["ProcessorFeatureTypeDef"] = None,
        UseDefaultProcessorFeatures: bool = None,
        DBParameterGroupName: str = None,
        DeletionProtection: bool = None,
        EnableCustomerOwnedIp: bool = None,
    ) -> RestoreDBInstanceFromDBSnapshotResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.restore_db_instance_from_db_snapshot)
        [Show boto3-stubs documentation](./client.md#restore_db_instance_from_db_snapshot)
        """
    def restore_db_instance_from_s3(
        self,
        DBInstanceIdentifier: str,
        DBInstanceClass: str,
        Engine: str,
        SourceEngine: str,
        SourceEngineVersion: str,
        S3BucketName: str,
        S3IngestionRoleArn: str,
        DBName: str = None,
        AllocatedStorage: int = None,
        MasterUsername: str = None,
        MasterUserPassword: str = None,
        DBSecurityGroups: List[str] = None,
        VpcSecurityGroupIds: List[str] = None,
        AvailabilityZone: str = None,
        DBSubnetGroupName: str = None,
        PreferredMaintenanceWindow: str = None,
        DBParameterGroupName: str = None,
        BackupRetentionPeriod: int = None,
        PreferredBackupWindow: str = None,
        Port: int = None,
        MultiAZ: bool = None,
        EngineVersion: str = None,
        AutoMinorVersionUpgrade: bool = None,
        LicenseModel: str = None,
        Iops: int = None,
        OptionGroupName: str = None,
        PubliclyAccessible: bool = None,
        Tags: List["TagTypeDef"] = None,
        StorageType: str = None,
        StorageEncrypted: bool = None,
        KmsKeyId: str = None,
        CopyTagsToSnapshot: bool = None,
        MonitoringInterval: int = None,
        MonitoringRoleArn: str = None,
        EnableIAMDatabaseAuthentication: bool = None,
        S3Prefix: str = None,
        EnablePerformanceInsights: bool = None,
        PerformanceInsightsKMSKeyId: str = None,
        PerformanceInsightsRetentionPeriod: int = None,
        EnableCloudwatchLogsExports: List[str] = None,
        ProcessorFeatures: List["ProcessorFeatureTypeDef"] = None,
        UseDefaultProcessorFeatures: bool = None,
        DeletionProtection: bool = None,
        MaxAllocatedStorage: int = None,
    ) -> RestoreDBInstanceFromS3ResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.restore_db_instance_from_s3)
        [Show boto3-stubs documentation](./client.md#restore_db_instance_from_s3)
        """
    def restore_db_instance_to_point_in_time(
        self,
        TargetDBInstanceIdentifier: str,
        SourceDBInstanceIdentifier: str = None,
        RestoreTime: datetime = None,
        UseLatestRestorableTime: bool = None,
        DBInstanceClass: str = None,
        Port: int = None,
        AvailabilityZone: str = None,
        DBSubnetGroupName: str = None,
        MultiAZ: bool = None,
        PubliclyAccessible: bool = None,
        AutoMinorVersionUpgrade: bool = None,
        LicenseModel: str = None,
        DBName: str = None,
        Engine: str = None,
        Iops: int = None,
        OptionGroupName: str = None,
        CopyTagsToSnapshot: bool = None,
        Tags: List["TagTypeDef"] = None,
        StorageType: str = None,
        TdeCredentialArn: str = None,
        TdeCredentialPassword: str = None,
        VpcSecurityGroupIds: List[str] = None,
        Domain: str = None,
        DomainIAMRoleName: str = None,
        EnableIAMDatabaseAuthentication: bool = None,
        EnableCloudwatchLogsExports: List[str] = None,
        ProcessorFeatures: List["ProcessorFeatureTypeDef"] = None,
        UseDefaultProcessorFeatures: bool = None,
        DBParameterGroupName: str = None,
        DeletionProtection: bool = None,
        SourceDbiResourceId: str = None,
        MaxAllocatedStorage: int = None,
        SourceDBInstanceAutomatedBackupsArn: str = None,
        EnableCustomerOwnedIp: bool = None,
    ) -> RestoreDBInstanceToPointInTimeResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.restore_db_instance_to_point_in_time)
        [Show boto3-stubs documentation](./client.md#restore_db_instance_to_point_in_time)
        """
    def revoke_db_security_group_ingress(
        self,
        DBSecurityGroupName: str,
        CIDRIP: str = None,
        EC2SecurityGroupName: str = None,
        EC2SecurityGroupId: str = None,
        EC2SecurityGroupOwnerId: str = None,
    ) -> RevokeDBSecurityGroupIngressResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.revoke_db_security_group_ingress)
        [Show boto3-stubs documentation](./client.md#revoke_db_security_group_ingress)
        """
    def start_activity_stream(
        self,
        ResourceArn: str,
        Mode: ActivityStreamModeType,
        KmsKeyId: str,
        ApplyImmediately: bool = None,
    ) -> StartActivityStreamResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.start_activity_stream)
        [Show boto3-stubs documentation](./client.md#start_activity_stream)
        """
    def start_db_cluster(self, DBClusterIdentifier: str) -> StartDBClusterResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.start_db_cluster)
        [Show boto3-stubs documentation](./client.md#start_db_cluster)
        """
    def start_db_instance(self, DBInstanceIdentifier: str) -> StartDBInstanceResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.start_db_instance)
        [Show boto3-stubs documentation](./client.md#start_db_instance)
        """
    def start_db_instance_automated_backups_replication(
        self,
        SourceDBInstanceArn: str,
        BackupRetentionPeriod: int = None,
        KmsKeyId: str = None,
        PreSignedUrl: str = None,
        SourceRegion: str = None,
    ) -> StartDBInstanceAutomatedBackupsReplicationResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.start_db_instance_automated_backups_replication)
        [Show boto3-stubs documentation](./client.md#start_db_instance_automated_backups_replication)
        """
    def start_export_task(
        self,
        ExportTaskIdentifier: str,
        SourceArn: str,
        S3BucketName: str,
        IamRoleArn: str,
        KmsKeyId: str,
        S3Prefix: str = None,
        ExportOnly: List[str] = None,
    ) -> "ExportTaskTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.start_export_task)
        [Show boto3-stubs documentation](./client.md#start_export_task)
        """
    def stop_activity_stream(
        self, ResourceArn: str, ApplyImmediately: bool = None
    ) -> StopActivityStreamResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.stop_activity_stream)
        [Show boto3-stubs documentation](./client.md#stop_activity_stream)
        """
    def stop_db_cluster(self, DBClusterIdentifier: str) -> StopDBClusterResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.stop_db_cluster)
        [Show boto3-stubs documentation](./client.md#stop_db_cluster)
        """
    def stop_db_instance(
        self, DBInstanceIdentifier: str, DBSnapshotIdentifier: str = None
    ) -> StopDBInstanceResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.stop_db_instance)
        [Show boto3-stubs documentation](./client.md#stop_db_instance)
        """
    def stop_db_instance_automated_backups_replication(
        self, SourceDBInstanceArn: str
    ) -> StopDBInstanceAutomatedBackupsReplicationResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Client.stop_db_instance_automated_backups_replication)
        [Show boto3-stubs documentation](./client.md#stop_db_instance_automated_backups_replication)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_certificates"]
    ) -> DescribeCertificatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Paginator.DescribeCertificates)[Show boto3-stubs documentation](./paginators.md#describecertificatespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_custom_availability_zones"]
    ) -> DescribeCustomAvailabilityZonesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Paginator.DescribeCustomAvailabilityZones)[Show boto3-stubs documentation](./paginators.md#describecustomavailabilityzonespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_cluster_backtracks"]
    ) -> DescribeDBClusterBacktracksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Paginator.DescribeDBClusterBacktracks)[Show boto3-stubs documentation](./paginators.md#describedbclusterbacktrackspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_cluster_endpoints"]
    ) -> DescribeDBClusterEndpointsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Paginator.DescribeDBClusterEndpoints)[Show boto3-stubs documentation](./paginators.md#describedbclusterendpointspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_cluster_parameter_groups"]
    ) -> DescribeDBClusterParameterGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Paginator.DescribeDBClusterParameterGroups)[Show boto3-stubs documentation](./paginators.md#describedbclusterparametergroupspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_cluster_parameters"]
    ) -> DescribeDBClusterParametersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Paginator.DescribeDBClusterParameters)[Show boto3-stubs documentation](./paginators.md#describedbclusterparameterspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_cluster_snapshots"]
    ) -> DescribeDBClusterSnapshotsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Paginator.DescribeDBClusterSnapshots)[Show boto3-stubs documentation](./paginators.md#describedbclustersnapshotspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_clusters"]
    ) -> DescribeDBClustersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Paginator.DescribeDBClusters)[Show boto3-stubs documentation](./paginators.md#describedbclusterspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_engine_versions"]
    ) -> DescribeDBEngineVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Paginator.DescribeDBEngineVersions)[Show boto3-stubs documentation](./paginators.md#describedbengineversionspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_instance_automated_backups"]
    ) -> DescribeDBInstanceAutomatedBackupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Paginator.DescribeDBInstanceAutomatedBackups)[Show boto3-stubs documentation](./paginators.md#describedbinstanceautomatedbackupspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_instances"]
    ) -> DescribeDBInstancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Paginator.DescribeDBInstances)[Show boto3-stubs documentation](./paginators.md#describedbinstancespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_log_files"]
    ) -> DescribeDBLogFilesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Paginator.DescribeDBLogFiles)[Show boto3-stubs documentation](./paginators.md#describedblogfilespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_parameter_groups"]
    ) -> DescribeDBParameterGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Paginator.DescribeDBParameterGroups)[Show boto3-stubs documentation](./paginators.md#describedbparametergroupspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_parameters"]
    ) -> DescribeDBParametersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Paginator.DescribeDBParameters)[Show boto3-stubs documentation](./paginators.md#describedbparameterspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_proxies"]
    ) -> DescribeDBProxiesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Paginator.DescribeDBProxies)[Show boto3-stubs documentation](./paginators.md#describedbproxiespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_proxy_endpoints"]
    ) -> DescribeDBProxyEndpointsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Paginator.DescribeDBProxyEndpoints)[Show boto3-stubs documentation](./paginators.md#describedbproxyendpointspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_proxy_target_groups"]
    ) -> DescribeDBProxyTargetGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Paginator.DescribeDBProxyTargetGroups)[Show boto3-stubs documentation](./paginators.md#describedbproxytargetgroupspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_proxy_targets"]
    ) -> DescribeDBProxyTargetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Paginator.DescribeDBProxyTargets)[Show boto3-stubs documentation](./paginators.md#describedbproxytargetspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_security_groups"]
    ) -> DescribeDBSecurityGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Paginator.DescribeDBSecurityGroups)[Show boto3-stubs documentation](./paginators.md#describedbsecuritygroupspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_snapshots"]
    ) -> DescribeDBSnapshotsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Paginator.DescribeDBSnapshots)[Show boto3-stubs documentation](./paginators.md#describedbsnapshotspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_subnet_groups"]
    ) -> DescribeDBSubnetGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Paginator.DescribeDBSubnetGroups)[Show boto3-stubs documentation](./paginators.md#describedbsubnetgroupspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_engine_default_cluster_parameters"]
    ) -> DescribeEngineDefaultClusterParametersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Paginator.DescribeEngineDefaultClusterParameters)[Show boto3-stubs documentation](./paginators.md#describeenginedefaultclusterparameterspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_engine_default_parameters"]
    ) -> DescribeEngineDefaultParametersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Paginator.DescribeEngineDefaultParameters)[Show boto3-stubs documentation](./paginators.md#describeenginedefaultparameterspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_event_subscriptions"]
    ) -> DescribeEventSubscriptionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Paginator.DescribeEventSubscriptions)[Show boto3-stubs documentation](./paginators.md#describeeventsubscriptionspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["describe_events"]) -> DescribeEventsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Paginator.DescribeEvents)[Show boto3-stubs documentation](./paginators.md#describeeventspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_export_tasks"]
    ) -> DescribeExportTasksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Paginator.DescribeExportTasks)[Show boto3-stubs documentation](./paginators.md#describeexporttaskspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_global_clusters"]
    ) -> DescribeGlobalClustersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Paginator.DescribeGlobalClusters)[Show boto3-stubs documentation](./paginators.md#describeglobalclusterspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_installation_media"]
    ) -> DescribeInstallationMediaPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Paginator.DescribeInstallationMedia)[Show boto3-stubs documentation](./paginators.md#describeinstallationmediapaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_option_group_options"]
    ) -> DescribeOptionGroupOptionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Paginator.DescribeOptionGroupOptions)[Show boto3-stubs documentation](./paginators.md#describeoptiongroupoptionspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_option_groups"]
    ) -> DescribeOptionGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Paginator.DescribeOptionGroups)[Show boto3-stubs documentation](./paginators.md#describeoptiongroupspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_orderable_db_instance_options"]
    ) -> DescribeOrderableDBInstanceOptionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Paginator.DescribeOrderableDBInstanceOptions)[Show boto3-stubs documentation](./paginators.md#describeorderabledbinstanceoptionspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_pending_maintenance_actions"]
    ) -> DescribePendingMaintenanceActionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Paginator.DescribePendingMaintenanceActions)[Show boto3-stubs documentation](./paginators.md#describependingmaintenanceactionspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_reserved_db_instances"]
    ) -> DescribeReservedDBInstancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Paginator.DescribeReservedDBInstances)[Show boto3-stubs documentation](./paginators.md#describereserveddbinstancespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_reserved_db_instances_offerings"]
    ) -> DescribeReservedDBInstancesOfferingsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Paginator.DescribeReservedDBInstancesOfferings)[Show boto3-stubs documentation](./paginators.md#describereserveddbinstancesofferingspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_source_regions"]
    ) -> DescribeSourceRegionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Paginator.DescribeSourceRegions)[Show boto3-stubs documentation](./paginators.md#describesourceregionspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["download_db_log_file_portion"]
    ) -> DownloadDBLogFilePortionPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Paginator.DownloadDBLogFilePortion)[Show boto3-stubs documentation](./paginators.md#downloaddblogfileportionpaginator)
        """
    @overload
    def get_waiter(
        self, waiter_name: Literal["db_cluster_snapshot_available"]
    ) -> DBClusterSnapshotAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Waiter.db_cluster_snapshot_available)[Show boto3-stubs documentation](./waiters.md#dbclustersnapshotavailablewaiter)
        """
    @overload
    def get_waiter(
        self, waiter_name: Literal["db_cluster_snapshot_deleted"]
    ) -> DBClusterSnapshotDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Waiter.db_cluster_snapshot_deleted)[Show boto3-stubs documentation](./waiters.md#dbclustersnapshotdeletedwaiter)
        """
    @overload
    def get_waiter(
        self, waiter_name: Literal["db_instance_available"]
    ) -> DBInstanceAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Waiter.db_instance_available)[Show boto3-stubs documentation](./waiters.md#dbinstanceavailablewaiter)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["db_instance_deleted"]) -> DBInstanceDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Waiter.db_instance_deleted)[Show boto3-stubs documentation](./waiters.md#dbinstancedeletedwaiter)
        """
    @overload
    def get_waiter(
        self, waiter_name: Literal["db_snapshot_available"]
    ) -> DBSnapshotAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Waiter.db_snapshot_available)[Show boto3-stubs documentation](./waiters.md#dbsnapshotavailablewaiter)
        """
    @overload
    def get_waiter(
        self, waiter_name: Literal["db_snapshot_completed"]
    ) -> DBSnapshotCompletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Waiter.db_snapshot_completed)[Show boto3-stubs documentation](./waiters.md#dbsnapshotcompletedwaiter)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["db_snapshot_deleted"]) -> DBSnapshotDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/rds.html#RDS.Waiter.db_snapshot_deleted)[Show boto3-stubs documentation](./waiters.md#dbsnapshotdeletedwaiter)
        """
