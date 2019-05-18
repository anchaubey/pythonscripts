from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.compute import *
from azure.mgmt.resource.resources import ResourceManagementClient

subscription_id = '726edce6-f6f5-4770-ab05-770f8efd2f0a'
client_id = 'facde157-0ce7-4af3-83bc-4353692d771d'
secret = '}X.(j((-MP^Pt+*]=&otE^A#&;.}H%*S7;!%:v&jL=@2}s'
tenant = '802cfbcb-dea0-4b56-8f93-7c52299a8cde'

def get_credentials():
    return ServicePrincipalCredentials(
        client_id=client_id,
        secret=secret,
        tenant=tenant,
    )

def get_compute():
    return ComputeManagementClient(ComputeManagementClientConfiguration(
        get_credentials(),
        subscription_id
    ))

def get_resource():
    return ResourceManagementClient(
    ResourceManagementClientConfiguration(
        get_credentials(),
        subscription_id
    )
)

def main():
    
    print("{:<20} {:<20}".format("Resoruce Group", "VM name"))
    res = get_resource()
    resource_groups = res.resource_groups.list()
    for group in resource_groups:

        com = get_compute()
        vms = com.virtual_machines
        for vm in vms.list(resource_group_name=group.name):
            print("{:<20} {:<20}".format(group.name, vm.name))

if __name__ == '__main__':
    main()
