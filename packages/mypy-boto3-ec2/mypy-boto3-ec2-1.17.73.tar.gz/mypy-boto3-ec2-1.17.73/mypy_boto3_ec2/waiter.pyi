"""
Type annotations for ec2 service client waiters.

[Open documentation](./waiters.md)

Usage::

    ```python
    import boto3

    from mypy_boto3_ec2 import EC2Client
    from mypy_boto3_ec2.waiter import (
        BundleTaskCompleteWaiter,
        ConversionTaskCancelledWaiter,
        ConversionTaskCompletedWaiter,
        ConversionTaskDeletedWaiter,
        CustomerGatewayAvailableWaiter,
        ExportTaskCancelledWaiter,
        ExportTaskCompletedWaiter,
        ImageAvailableWaiter,
        ImageExistsWaiter,
        InstanceExistsWaiter,
        InstanceRunningWaiter,
        InstanceStatusOkWaiter,
        InstanceStoppedWaiter,
        InstanceTerminatedWaiter,
        KeyPairExistsWaiter,
        NatGatewayAvailableWaiter,
        NetworkInterfaceAvailableWaiter,
        PasswordDataAvailableWaiter,
        SecurityGroupExistsWaiter,
        SnapshotCompletedWaiter,
        SpotInstanceRequestFulfilledWaiter,
        SubnetAvailableWaiter,
        SystemStatusOkWaiter,
        VolumeAvailableWaiter,
        VolumeDeletedWaiter,
        VolumeInUseWaiter,
        VpcAvailableWaiter,
        VpcExistsWaiter,
        VpcPeeringConnectionDeletedWaiter,
        VpcPeeringConnectionExistsWaiter,
        VpnConnectionAvailableWaiter,
        VpnConnectionDeletedWaiter,
    )

    client: EC2Client = boto3.client("ec2")

    bundle_task_complete_waiter: BundleTaskCompleteWaiter = client.get_waiter("bundle_task_complete")
    conversion_task_cancelled_waiter: ConversionTaskCancelledWaiter = client.get_waiter("conversion_task_cancelled")
    conversion_task_completed_waiter: ConversionTaskCompletedWaiter = client.get_waiter("conversion_task_completed")
    conversion_task_deleted_waiter: ConversionTaskDeletedWaiter = client.get_waiter("conversion_task_deleted")
    customer_gateway_available_waiter: CustomerGatewayAvailableWaiter = client.get_waiter("customer_gateway_available")
    export_task_cancelled_waiter: ExportTaskCancelledWaiter = client.get_waiter("export_task_cancelled")
    export_task_completed_waiter: ExportTaskCompletedWaiter = client.get_waiter("export_task_completed")
    image_available_waiter: ImageAvailableWaiter = client.get_waiter("image_available")
    image_exists_waiter: ImageExistsWaiter = client.get_waiter("image_exists")
    instance_exists_waiter: InstanceExistsWaiter = client.get_waiter("instance_exists")
    instance_running_waiter: InstanceRunningWaiter = client.get_waiter("instance_running")
    instance_status_ok_waiter: InstanceStatusOkWaiter = client.get_waiter("instance_status_ok")
    instance_stopped_waiter: InstanceStoppedWaiter = client.get_waiter("instance_stopped")
    instance_terminated_waiter: InstanceTerminatedWaiter = client.get_waiter("instance_terminated")
    key_pair_exists_waiter: KeyPairExistsWaiter = client.get_waiter("key_pair_exists")
    nat_gateway_available_waiter: NatGatewayAvailableWaiter = client.get_waiter("nat_gateway_available")
    network_interface_available_waiter: NetworkInterfaceAvailableWaiter = client.get_waiter("network_interface_available")
    password_data_available_waiter: PasswordDataAvailableWaiter = client.get_waiter("password_data_available")
    security_group_exists_waiter: SecurityGroupExistsWaiter = client.get_waiter("security_group_exists")
    snapshot_completed_waiter: SnapshotCompletedWaiter = client.get_waiter("snapshot_completed")
    spot_instance_request_fulfilled_waiter: SpotInstanceRequestFulfilledWaiter = client.get_waiter("spot_instance_request_fulfilled")
    subnet_available_waiter: SubnetAvailableWaiter = client.get_waiter("subnet_available")
    system_status_ok_waiter: SystemStatusOkWaiter = client.get_waiter("system_status_ok")
    volume_available_waiter: VolumeAvailableWaiter = client.get_waiter("volume_available")
    volume_deleted_waiter: VolumeDeletedWaiter = client.get_waiter("volume_deleted")
    volume_in_use_waiter: VolumeInUseWaiter = client.get_waiter("volume_in_use")
    vpc_available_waiter: VpcAvailableWaiter = client.get_waiter("vpc_available")
    vpc_exists_waiter: VpcExistsWaiter = client.get_waiter("vpc_exists")
    vpc_peering_connection_deleted_waiter: VpcPeeringConnectionDeletedWaiter = client.get_waiter("vpc_peering_connection_deleted")
    vpc_peering_connection_exists_waiter: VpcPeeringConnectionExistsWaiter = client.get_waiter("vpc_peering_connection_exists")
    vpn_connection_available_waiter: VpnConnectionAvailableWaiter = client.get_waiter("vpn_connection_available")
    vpn_connection_deleted_waiter: VpnConnectionDeletedWaiter = client.get_waiter("vpn_connection_deleted")
    ```
"""
from typing import List

from botocore.waiter import Waiter as Boto3Waiter

from .type_defs import FilterTypeDef, WaiterConfigTypeDef

__all__ = (
    "BundleTaskCompleteWaiter",
    "ConversionTaskCancelledWaiter",
    "ConversionTaskCompletedWaiter",
    "ConversionTaskDeletedWaiter",
    "CustomerGatewayAvailableWaiter",
    "ExportTaskCancelledWaiter",
    "ExportTaskCompletedWaiter",
    "ImageAvailableWaiter",
    "ImageExistsWaiter",
    "InstanceExistsWaiter",
    "InstanceRunningWaiter",
    "InstanceStatusOkWaiter",
    "InstanceStoppedWaiter",
    "InstanceTerminatedWaiter",
    "KeyPairExistsWaiter",
    "NatGatewayAvailableWaiter",
    "NetworkInterfaceAvailableWaiter",
    "PasswordDataAvailableWaiter",
    "SecurityGroupExistsWaiter",
    "SnapshotCompletedWaiter",
    "SpotInstanceRequestFulfilledWaiter",
    "SubnetAvailableWaiter",
    "SystemStatusOkWaiter",
    "VolumeAvailableWaiter",
    "VolumeDeletedWaiter",
    "VolumeInUseWaiter",
    "VpcAvailableWaiter",
    "VpcExistsWaiter",
    "VpcPeeringConnectionDeletedWaiter",
    "VpcPeeringConnectionExistsWaiter",
    "VpnConnectionAvailableWaiter",
    "VpnConnectionDeletedWaiter",
)

class BundleTaskCompleteWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ec2.html#EC2.Waiter.bundle_task_complete)[Show boto3-stubs documentation](./waiters.md#bundletaskcompletewaiter)
    """

    def wait(
        self,
        BundleIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ec2.html#EC2.Waiter.BundleTaskCompleteWaiter)
        [Show boto3-stubs documentation](./waiters.md#bundletaskcomplete)
        """

class ConversionTaskCancelledWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ec2.html#EC2.Waiter.conversion_task_cancelled)[Show boto3-stubs documentation](./waiters.md#conversiontaskcancelledwaiter)
    """

    def wait(
        self,
        ConversionTaskIds: List[str] = None,
        DryRun: bool = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ec2.html#EC2.Waiter.ConversionTaskCancelledWaiter)
        [Show boto3-stubs documentation](./waiters.md#conversiontaskcancelled)
        """

class ConversionTaskCompletedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ec2.html#EC2.Waiter.conversion_task_completed)[Show boto3-stubs documentation](./waiters.md#conversiontaskcompletedwaiter)
    """

    def wait(
        self,
        ConversionTaskIds: List[str] = None,
        DryRun: bool = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ec2.html#EC2.Waiter.ConversionTaskCompletedWaiter)
        [Show boto3-stubs documentation](./waiters.md#conversiontaskcompleted)
        """

class ConversionTaskDeletedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ec2.html#EC2.Waiter.conversion_task_deleted)[Show boto3-stubs documentation](./waiters.md#conversiontaskdeletedwaiter)
    """

    def wait(
        self,
        ConversionTaskIds: List[str] = None,
        DryRun: bool = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ec2.html#EC2.Waiter.ConversionTaskDeletedWaiter)
        [Show boto3-stubs documentation](./waiters.md#conversiontaskdeleted)
        """

class CustomerGatewayAvailableWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ec2.html#EC2.Waiter.customer_gateway_available)[Show boto3-stubs documentation](./waiters.md#customergatewayavailablewaiter)
    """

    def wait(
        self,
        CustomerGatewayIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ec2.html#EC2.Waiter.CustomerGatewayAvailableWaiter)
        [Show boto3-stubs documentation](./waiters.md#customergatewayavailable)
        """

class ExportTaskCancelledWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ec2.html#EC2.Waiter.export_task_cancelled)[Show boto3-stubs documentation](./waiters.md#exporttaskcancelledwaiter)
    """

    def wait(
        self,
        ExportTaskIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ec2.html#EC2.Waiter.ExportTaskCancelledWaiter)
        [Show boto3-stubs documentation](./waiters.md#exporttaskcancelled)
        """

class ExportTaskCompletedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ec2.html#EC2.Waiter.export_task_completed)[Show boto3-stubs documentation](./waiters.md#exporttaskcompletedwaiter)
    """

    def wait(
        self,
        ExportTaskIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ec2.html#EC2.Waiter.ExportTaskCompletedWaiter)
        [Show boto3-stubs documentation](./waiters.md#exporttaskcompleted)
        """

class ImageAvailableWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ec2.html#EC2.Waiter.image_available)[Show boto3-stubs documentation](./waiters.md#imageavailablewaiter)
    """

    def wait(
        self,
        ExecutableUsers: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        ImageIds: List[str] = None,
        Owners: List[str] = None,
        DryRun: bool = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ec2.html#EC2.Waiter.ImageAvailableWaiter)
        [Show boto3-stubs documentation](./waiters.md#imageavailable)
        """

class ImageExistsWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ec2.html#EC2.Waiter.image_exists)[Show boto3-stubs documentation](./waiters.md#imageexistswaiter)
    """

    def wait(
        self,
        ExecutableUsers: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        ImageIds: List[str] = None,
        Owners: List[str] = None,
        DryRun: bool = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ec2.html#EC2.Waiter.ImageExistsWaiter)
        [Show boto3-stubs documentation](./waiters.md#imageexists)
        """

class InstanceExistsWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ec2.html#EC2.Waiter.instance_exists)[Show boto3-stubs documentation](./waiters.md#instanceexistswaiter)
    """

    def wait(
        self,
        Filters: List[FilterTypeDef] = None,
        InstanceIds: List[str] = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ec2.html#EC2.Waiter.InstanceExistsWaiter)
        [Show boto3-stubs documentation](./waiters.md#instanceexists)
        """

class InstanceRunningWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ec2.html#EC2.Waiter.instance_running)[Show boto3-stubs documentation](./waiters.md#instancerunningwaiter)
    """

    def wait(
        self,
        Filters: List[FilterTypeDef] = None,
        InstanceIds: List[str] = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ec2.html#EC2.Waiter.InstanceRunningWaiter)
        [Show boto3-stubs documentation](./waiters.md#instancerunning)
        """

class InstanceStatusOkWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ec2.html#EC2.Waiter.instance_status_ok)[Show boto3-stubs documentation](./waiters.md#instancestatusokwaiter)
    """

    def wait(
        self,
        Filters: List[FilterTypeDef] = None,
        InstanceIds: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
        IncludeAllInstances: bool = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ec2.html#EC2.Waiter.InstanceStatusOkWaiter)
        [Show boto3-stubs documentation](./waiters.md#instancestatusok)
        """

class InstanceStoppedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ec2.html#EC2.Waiter.instance_stopped)[Show boto3-stubs documentation](./waiters.md#instancestoppedwaiter)
    """

    def wait(
        self,
        Filters: List[FilterTypeDef] = None,
        InstanceIds: List[str] = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ec2.html#EC2.Waiter.InstanceStoppedWaiter)
        [Show boto3-stubs documentation](./waiters.md#instancestopped)
        """

class InstanceTerminatedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ec2.html#EC2.Waiter.instance_terminated)[Show boto3-stubs documentation](./waiters.md#instanceterminatedwaiter)
    """

    def wait(
        self,
        Filters: List[FilterTypeDef] = None,
        InstanceIds: List[str] = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ec2.html#EC2.Waiter.InstanceTerminatedWaiter)
        [Show boto3-stubs documentation](./waiters.md#instanceterminated)
        """

class KeyPairExistsWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ec2.html#EC2.Waiter.key_pair_exists)[Show boto3-stubs documentation](./waiters.md#keypairexistswaiter)
    """

    def wait(
        self,
        Filters: List[FilterTypeDef] = None,
        KeyNames: List[str] = None,
        KeyPairIds: List[str] = None,
        DryRun: bool = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ec2.html#EC2.Waiter.KeyPairExistsWaiter)
        [Show boto3-stubs documentation](./waiters.md#keypairexists)
        """

class NatGatewayAvailableWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ec2.html#EC2.Waiter.nat_gateway_available)[Show boto3-stubs documentation](./waiters.md#natgatewayavailablewaiter)
    """

    def wait(
        self,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NatGatewayIds: List[str] = None,
        NextToken: str = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ec2.html#EC2.Waiter.NatGatewayAvailableWaiter)
        [Show boto3-stubs documentation](./waiters.md#natgatewayavailable)
        """

class NetworkInterfaceAvailableWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ec2.html#EC2.Waiter.network_interface_available)[Show boto3-stubs documentation](./waiters.md#networkinterfaceavailablewaiter)
    """

    def wait(
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        NetworkInterfaceIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ec2.html#EC2.Waiter.NetworkInterfaceAvailableWaiter)
        [Show boto3-stubs documentation](./waiters.md#networkinterfaceavailable)
        """

class PasswordDataAvailableWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ec2.html#EC2.Waiter.password_data_available)[Show boto3-stubs documentation](./waiters.md#passworddataavailablewaiter)
    """

    def wait(
        self, InstanceId: str, DryRun: bool = None, WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ec2.html#EC2.Waiter.PasswordDataAvailableWaiter)
        [Show boto3-stubs documentation](./waiters.md#passworddataavailable)
        """

class SecurityGroupExistsWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ec2.html#EC2.Waiter.security_group_exists)[Show boto3-stubs documentation](./waiters.md#securitygroupexistswaiter)
    """

    def wait(
        self,
        Filters: List[FilterTypeDef] = None,
        GroupIds: List[str] = None,
        GroupNames: List[str] = None,
        DryRun: bool = None,
        NextToken: str = None,
        MaxResults: int = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ec2.html#EC2.Waiter.SecurityGroupExistsWaiter)
        [Show boto3-stubs documentation](./waiters.md#securitygroupexists)
        """

class SnapshotCompletedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ec2.html#EC2.Waiter.snapshot_completed)[Show boto3-stubs documentation](./waiters.md#snapshotcompletedwaiter)
    """

    def wait(
        self,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        OwnerIds: List[str] = None,
        RestorableByUserIds: List[str] = None,
        SnapshotIds: List[str] = None,
        DryRun: bool = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ec2.html#EC2.Waiter.SnapshotCompletedWaiter)
        [Show boto3-stubs documentation](./waiters.md#snapshotcompleted)
        """

class SpotInstanceRequestFulfilledWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ec2.html#EC2.Waiter.spot_instance_request_fulfilled)[Show boto3-stubs documentation](./waiters.md#spotinstancerequestfulfilledwaiter)
    """

    def wait(
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        SpotInstanceRequestIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ec2.html#EC2.Waiter.SpotInstanceRequestFulfilledWaiter)
        [Show boto3-stubs documentation](./waiters.md#spotinstancerequestfulfilled)
        """

class SubnetAvailableWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ec2.html#EC2.Waiter.subnet_available)[Show boto3-stubs documentation](./waiters.md#subnetavailablewaiter)
    """

    def wait(
        self,
        Filters: List[FilterTypeDef] = None,
        SubnetIds: List[str] = None,
        DryRun: bool = None,
        NextToken: str = None,
        MaxResults: int = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ec2.html#EC2.Waiter.SubnetAvailableWaiter)
        [Show boto3-stubs documentation](./waiters.md#subnetavailable)
        """

class SystemStatusOkWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ec2.html#EC2.Waiter.system_status_ok)[Show boto3-stubs documentation](./waiters.md#systemstatusokwaiter)
    """

    def wait(
        self,
        Filters: List[FilterTypeDef] = None,
        InstanceIds: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
        IncludeAllInstances: bool = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ec2.html#EC2.Waiter.SystemStatusOkWaiter)
        [Show boto3-stubs documentation](./waiters.md#systemstatusok)
        """

class VolumeAvailableWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ec2.html#EC2.Waiter.volume_available)[Show boto3-stubs documentation](./waiters.md#volumeavailablewaiter)
    """

    def wait(
        self,
        Filters: List[FilterTypeDef] = None,
        VolumeIds: List[str] = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ec2.html#EC2.Waiter.VolumeAvailableWaiter)
        [Show boto3-stubs documentation](./waiters.md#volumeavailable)
        """

class VolumeDeletedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ec2.html#EC2.Waiter.volume_deleted)[Show boto3-stubs documentation](./waiters.md#volumedeletedwaiter)
    """

    def wait(
        self,
        Filters: List[FilterTypeDef] = None,
        VolumeIds: List[str] = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ec2.html#EC2.Waiter.VolumeDeletedWaiter)
        [Show boto3-stubs documentation](./waiters.md#volumedeleted)
        """

class VolumeInUseWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ec2.html#EC2.Waiter.volume_in_use)[Show boto3-stubs documentation](./waiters.md#volumeinusewaiter)
    """

    def wait(
        self,
        Filters: List[FilterTypeDef] = None,
        VolumeIds: List[str] = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ec2.html#EC2.Waiter.VolumeInUseWaiter)
        [Show boto3-stubs documentation](./waiters.md#volumeinuse)
        """

class VpcAvailableWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ec2.html#EC2.Waiter.vpc_available)[Show boto3-stubs documentation](./waiters.md#vpcavailablewaiter)
    """

    def wait(
        self,
        Filters: List[FilterTypeDef] = None,
        VpcIds: List[str] = None,
        DryRun: bool = None,
        NextToken: str = None,
        MaxResults: int = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ec2.html#EC2.Waiter.VpcAvailableWaiter)
        [Show boto3-stubs documentation](./waiters.md#vpcavailable)
        """

class VpcExistsWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ec2.html#EC2.Waiter.vpc_exists)[Show boto3-stubs documentation](./waiters.md#vpcexistswaiter)
    """

    def wait(
        self,
        Filters: List[FilterTypeDef] = None,
        VpcIds: List[str] = None,
        DryRun: bool = None,
        NextToken: str = None,
        MaxResults: int = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ec2.html#EC2.Waiter.VpcExistsWaiter)
        [Show boto3-stubs documentation](./waiters.md#vpcexists)
        """

class VpcPeeringConnectionDeletedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ec2.html#EC2.Waiter.vpc_peering_connection_deleted)[Show boto3-stubs documentation](./waiters.md#vpcpeeringconnectiondeletedwaiter)
    """

    def wait(
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        VpcPeeringConnectionIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ec2.html#EC2.Waiter.VpcPeeringConnectionDeletedWaiter)
        [Show boto3-stubs documentation](./waiters.md#vpcpeeringconnectiondeleted)
        """

class VpcPeeringConnectionExistsWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ec2.html#EC2.Waiter.vpc_peering_connection_exists)[Show boto3-stubs documentation](./waiters.md#vpcpeeringconnectionexistswaiter)
    """

    def wait(
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        VpcPeeringConnectionIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ec2.html#EC2.Waiter.VpcPeeringConnectionExistsWaiter)
        [Show boto3-stubs documentation](./waiters.md#vpcpeeringconnectionexists)
        """

class VpnConnectionAvailableWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ec2.html#EC2.Waiter.vpn_connection_available)[Show boto3-stubs documentation](./waiters.md#vpnconnectionavailablewaiter)
    """

    def wait(
        self,
        Filters: List[FilterTypeDef] = None,
        VpnConnectionIds: List[str] = None,
        DryRun: bool = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ec2.html#EC2.Waiter.VpnConnectionAvailableWaiter)
        [Show boto3-stubs documentation](./waiters.md#vpnconnectionavailable)
        """

class VpnConnectionDeletedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ec2.html#EC2.Waiter.vpn_connection_deleted)[Show boto3-stubs documentation](./waiters.md#vpnconnectiondeletedwaiter)
    """

    def wait(
        self,
        Filters: List[FilterTypeDef] = None,
        VpnConnectionIds: List[str] = None,
        DryRun: bool = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ec2.html#EC2.Waiter.VpnConnectionDeletedWaiter)
        [Show boto3-stubs documentation](./waiters.md#vpnconnectiondeleted)
        """
