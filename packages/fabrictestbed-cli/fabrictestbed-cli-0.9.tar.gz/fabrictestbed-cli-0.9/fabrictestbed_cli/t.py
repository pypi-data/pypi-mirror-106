from fabrictestbed_cli.api import OrchestratorProxy, CredmgrProxy

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
oc = OrchestratorProxy(orchestrator_host="localhost:8700")
status = oc.slice_status(token="test-token", slice_id="test-slice")
cm = CredmgrProxy(credmgr_host="localhost:8700")