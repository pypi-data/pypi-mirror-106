from fabrictestbed_cli.api import OrchestratorProxy, CredmgrProxy, CmStatus
from fabrictestbed_cli.api.api_client import ApiClient

from fabrictestbed_cli.user import ExperimentTopology, Capacities, ComponentType
t = ExperimentTopology()
n1 = t.add_node(name='n1', site='RENC')
cap = Capacities()
cap.set_fields(core=4, ram=64, disk=500)
n1.set_properties(capacities=cap, image_type='qcow2', image_ref='default_centos_8')
n1.add_component(ctype=ComponentType.SmartNIC, model='ConnectX-6', name='nic1')
n2 = t.add_node(name='n2', site='RENC')
n2.set_properties(capacities=cap, image_type='qcow2', image_ref='default_centos_8')
n2.add_component(ctype=ComponentType.GPU, model='RTX6000', name='nic2')
slice_graph = t.serialize()
print(slice_graph)
status = CredmgrProxy().refresh()
status != CmStatus.OK