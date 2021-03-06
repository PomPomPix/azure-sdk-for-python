# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .resource import Resource


class Lab(Resource):
    """A lab.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The identifier of the resource.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource.
    :vartype type: str
    :param location: The location of the resource.
    :type location: str
    :param tags: The tags of the resource.
    :type tags: dict[str, str]
    :ivar default_storage_account: The lab's default storage account.
    :vartype default_storage_account: str
    :ivar default_premium_storage_account: The lab's default premium storage
     account.
    :vartype default_premium_storage_account: str
    :ivar artifacts_storage_account: The lab's artifact storage account.
    :vartype artifacts_storage_account: str
    :ivar premium_data_disk_storage_account: The lab's premium data disk
     storage account.
    :vartype premium_data_disk_storage_account: str
    :ivar vault_name: The lab's Key vault.
    :vartype vault_name: str
    :param lab_storage_type: Type of storage used by the lab. It can be either
     Premium or Standard. Default is Premium. Possible values include:
     'Standard', 'Premium'
    :type lab_storage_type: str or ~azure.mgmt.devtestlabs.models.StorageType
    :param mandatory_artifacts_resource_ids_linux: The ordered list of
     artifact resource IDs that should be applied on all Linux VM creations by
     default, prior to the artifacts specified by the user.
    :type mandatory_artifacts_resource_ids_linux: list[str]
    :param mandatory_artifacts_resource_ids_windows: The ordered list of
     artifact resource IDs that should be applied on all Windows VM creations
     by default, prior to the artifacts specified by the user.
    :type mandatory_artifacts_resource_ids_windows: list[str]
    :ivar created_date: The creation date of the lab.
    :vartype created_date: datetime
    :param premium_data_disks: The setting to enable usage of premium data
     disks.
     When its value is 'Enabled', creation of standard or premium data disks is
     allowed.
     When its value is 'Disabled', only creation of standard data disks is
     allowed. Possible values include: 'Disabled', 'Enabled'
    :type premium_data_disks: str or
     ~azure.mgmt.devtestlabs.models.PremiumDataDisk
    :param environment_permission: The access rights to be granted to the user
     when provisioning an environment. Possible values include: 'Reader',
     'Contributor'
    :type environment_permission: str or
     ~azure.mgmt.devtestlabs.models.EnvironmentPermission
    :param announcement: The properties of any lab announcement associated
     with this lab
    :type announcement:
     ~azure.mgmt.devtestlabs.models.LabAnnouncementProperties
    :param support: The properties of any lab support message associated with
     this lab
    :type support: ~azure.mgmt.devtestlabs.models.LabSupportProperties
    :ivar vm_creation_resource_group: The resource group in which lab virtual
     machines will be created in.
    :vartype vm_creation_resource_group: str
    :ivar public_ip_id: The public IP address for the lab's load balancer.
    :vartype public_ip_id: str
    :ivar load_balancer_id: The load balancer used to for lab VMs that use
     shared IP address.
    :vartype load_balancer_id: str
    :ivar network_security_group_id: The Network Security Group attached to
     the lab VMs Network interfaces to restrict open ports.
    :vartype network_security_group_id: str
    :param extended_properties: Extended properties of the lab used for
     experimental features
    :type extended_properties: dict[str, str]
    :ivar provisioning_state: The provisioning status of the resource.
    :vartype provisioning_state: str
    :ivar unique_identifier: The unique immutable identifier of a resource
     (Guid).
    :vartype unique_identifier: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'default_storage_account': {'readonly': True},
        'default_premium_storage_account': {'readonly': True},
        'artifacts_storage_account': {'readonly': True},
        'premium_data_disk_storage_account': {'readonly': True},
        'vault_name': {'readonly': True},
        'created_date': {'readonly': True},
        'vm_creation_resource_group': {'readonly': True},
        'public_ip_id': {'readonly': True},
        'load_balancer_id': {'readonly': True},
        'network_security_group_id': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'unique_identifier': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'default_storage_account': {'key': 'properties.defaultStorageAccount', 'type': 'str'},
        'default_premium_storage_account': {'key': 'properties.defaultPremiumStorageAccount', 'type': 'str'},
        'artifacts_storage_account': {'key': 'properties.artifactsStorageAccount', 'type': 'str'},
        'premium_data_disk_storage_account': {'key': 'properties.premiumDataDiskStorageAccount', 'type': 'str'},
        'vault_name': {'key': 'properties.vaultName', 'type': 'str'},
        'lab_storage_type': {'key': 'properties.labStorageType', 'type': 'str'},
        'mandatory_artifacts_resource_ids_linux': {'key': 'properties.mandatoryArtifactsResourceIdsLinux', 'type': '[str]'},
        'mandatory_artifacts_resource_ids_windows': {'key': 'properties.mandatoryArtifactsResourceIdsWindows', 'type': '[str]'},
        'created_date': {'key': 'properties.createdDate', 'type': 'iso-8601'},
        'premium_data_disks': {'key': 'properties.premiumDataDisks', 'type': 'str'},
        'environment_permission': {'key': 'properties.environmentPermission', 'type': 'str'},
        'announcement': {'key': 'properties.announcement', 'type': 'LabAnnouncementProperties'},
        'support': {'key': 'properties.support', 'type': 'LabSupportProperties'},
        'vm_creation_resource_group': {'key': 'properties.vmCreationResourceGroup', 'type': 'str'},
        'public_ip_id': {'key': 'properties.publicIpId', 'type': 'str'},
        'load_balancer_id': {'key': 'properties.loadBalancerId', 'type': 'str'},
        'network_security_group_id': {'key': 'properties.networkSecurityGroupId', 'type': 'str'},
        'extended_properties': {'key': 'properties.extendedProperties', 'type': '{str}'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'unique_identifier': {'key': 'properties.uniqueIdentifier', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Lab, self).__init__(**kwargs)
        self.default_storage_account = None
        self.default_premium_storage_account = None
        self.artifacts_storage_account = None
        self.premium_data_disk_storage_account = None
        self.vault_name = None
        self.lab_storage_type = kwargs.get('lab_storage_type', None)
        self.mandatory_artifacts_resource_ids_linux = kwargs.get('mandatory_artifacts_resource_ids_linux', None)
        self.mandatory_artifacts_resource_ids_windows = kwargs.get('mandatory_artifacts_resource_ids_windows', None)
        self.created_date = None
        self.premium_data_disks = kwargs.get('premium_data_disks', None)
        self.environment_permission = kwargs.get('environment_permission', None)
        self.announcement = kwargs.get('announcement', None)
        self.support = kwargs.get('support', None)
        self.vm_creation_resource_group = None
        self.public_ip_id = None
        self.load_balancer_id = None
        self.network_security_group_id = None
        self.extended_properties = kwargs.get('extended_properties', None)
        self.provisioning_state = None
        self.unique_identifier = None
