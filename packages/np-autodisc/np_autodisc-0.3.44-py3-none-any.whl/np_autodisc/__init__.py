# __init__.py

from extras.plugins import PluginConfig

class NPAutoDiscoveryPluginConfig(PluginConfig):
    name = 'np_autodisc'
    verbose_name = 'Auto Discovery'
    description = 'New Netbox Autodiscovery Plugin'
    version = '0.1'
    author = 'Majik'
    author_email = 'MMajik@BlackWillow.com'
    base_url = 'np-autodisc'
    required_settings = []
    default_settings = {}
    # netbox_min_version = ''
    # netbox_max_version = ''
    
#    nav_links = [
#       {
#           'primary': {
#               'name': 'Discovery Requests',
#               'view': 'discoveryrequest_list',
#               'permission': 'view_discoveryrequest'
#           },
#           'add': {
#               'view': 'discoveryrequest_add',
#               'permission': 'add_discoveryrequest'
#           },
#           'import': {
#               'view': 'hello_world'
#           }
#       }
#   ]

config = NPAutoDiscoveryPluginConfig
