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


class ArmDisasterRecovery(Resource):
    """Single item in List or Get Alias(Disaster Recovery configuration)
    operation.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :ivar provisioning_state: Provisioning state of the Alias(Disaster
     Recovery configuration) - possible values 'Accepted' or 'Succeeded' or
     'Failed'. Possible values include: 'Accepted', 'Succeeded', 'Failed'
    :vartype provisioning_state: str or
     ~azure.mgmt.servicebus.models.ProvisioningStateDR
    :ivar pending_replication_operations_count: Number of entities pending to
     be replicated.
    :vartype pending_replication_operations_count: long
    :param partner_namespace: ARM Id of the Primary/Secondary eventhub
     namespace name, which is part of GEO DR pairing
    :type partner_namespace: str
    :param alternate_name: Primary/Secondary eventhub namespace name, which is
     part of GEO DR pairing
    :type alternate_name: str
    :ivar role: role of namespace in GEO DR - possible values 'Primary' or
     'PrimaryNotReplicating' or 'Secondary'. Possible values include:
     'Primary', 'PrimaryNotReplicating', 'Secondary'
    :vartype role: str or ~azure.mgmt.servicebus.models.RoleDisasterRecovery
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'pending_replication_operations_count': {'readonly': True},
        'role': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'ProvisioningStateDR'},
        'pending_replication_operations_count': {'key': 'properties.pendingReplicationOperationsCount', 'type': 'long'},
        'partner_namespace': {'key': 'properties.partnerNamespace', 'type': 'str'},
        'alternate_name': {'key': 'properties.alternateName', 'type': 'str'},
        'role': {'key': 'properties.role', 'type': 'RoleDisasterRecovery'},
    }

    def __init__(self, **kwargs):
        super(ArmDisasterRecovery, self).__init__(**kwargs)
        self.provisioning_state = None
        self.pending_replication_operations_count = None
        self.partner_namespace = kwargs.get('partner_namespace', None)
        self.alternate_name = kwargs.get('alternate_name', None)
        self.role = None
