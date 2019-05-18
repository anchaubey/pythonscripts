import azurerm

# create an authentication token (use a Service Principal or call get_access_token_from_cli())
# Service principal example:
tenant_id = '802cfbcb-dea0-4b56-8f93-7c52299a8cde'
application_id = 'facde157-0ce7-4af3-83bc-4353692d771d'
application_secret = '}X.(j((-MP^Pt+*]=&otE^A#&;.}H%*S7;!%:v&jL=@2}s'
subscription_id = '726edce6-f6f5-4770-ab05-770f8efd2f0a'
resource_group = 'aws-azure-peered-vnetRG'

vmss_name = 'linux1'

access_token = azurerm.get_access_token(tenant_id, application_id, application_secret)

list_vmss_vms(access_token, subscription_id, resource_group, vmss_name)
