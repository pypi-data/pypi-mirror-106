"""
Type annotations for iam service client waiters.

[Open documentation](./waiters.md)

Usage::

    ```python
    import boto3

    from mypy_boto3_iam import IAMClient
    from mypy_boto3_iam.waiter import (
        InstanceProfileExistsWaiter,
        PolicyExistsWaiter,
        RoleExistsWaiter,
        UserExistsWaiter,
    )

    client: IAMClient = boto3.client("iam")

    instance_profile_exists_waiter: InstanceProfileExistsWaiter = client.get_waiter("instance_profile_exists")
    policy_exists_waiter: PolicyExistsWaiter = client.get_waiter("policy_exists")
    role_exists_waiter: RoleExistsWaiter = client.get_waiter("role_exists")
    user_exists_waiter: UserExistsWaiter = client.get_waiter("user_exists")
    ```
"""
from botocore.waiter import Waiter as Boto3Waiter

from .type_defs import WaiterConfigTypeDef

__all__ = (
    "InstanceProfileExistsWaiter",
    "PolicyExistsWaiter",
    "RoleExistsWaiter",
    "UserExistsWaiter",
)


class InstanceProfileExistsWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/iam.html#IAM.Waiter.instance_profile_exists)[Show boto3-stubs documentation](./waiters.md#instanceprofileexistswaiter)
    """

    def wait(self, InstanceProfileName: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/iam.html#IAM.Waiter.InstanceProfileExistsWaiter)
        [Show boto3-stubs documentation](./waiters.md#instanceprofileexists)
        """


class PolicyExistsWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/iam.html#IAM.Waiter.policy_exists)[Show boto3-stubs documentation](./waiters.md#policyexistswaiter)
    """

    def wait(self, PolicyArn: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/iam.html#IAM.Waiter.PolicyExistsWaiter)
        [Show boto3-stubs documentation](./waiters.md#policyexists)
        """


class RoleExistsWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/iam.html#IAM.Waiter.role_exists)[Show boto3-stubs documentation](./waiters.md#roleexistswaiter)
    """

    def wait(self, RoleName: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/iam.html#IAM.Waiter.RoleExistsWaiter)
        [Show boto3-stubs documentation](./waiters.md#roleexists)
        """


class UserExistsWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/iam.html#IAM.Waiter.user_exists)[Show boto3-stubs documentation](./waiters.md#userexistswaiter)
    """

    def wait(self, UserName: str = None, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/iam.html#IAM.Waiter.UserExistsWaiter)
        [Show boto3-stubs documentation](./waiters.md#userexists)
        """
