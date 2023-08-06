from fabrictestbed.slice_manager import SliceManager, Status
from fabrictestbed.slice_editor import ExperimentTopology, Capacities, ComponentType

orchestrator_host = "<ORCHESTRATOR FQDN>"
credmgr_host = "<CREDENTIAL MANAGER FQDN>"
fabric_refresh_token = "<REFRESH TOKEN>"
# Create API Client object
# Users can request tokens with different Project and Scopes by altering `project_name` and `scope`
# parameters in the refresh call below.
client = SliceManager(oc_host=orchestrator_host, cm_host=credmgr_host,
                      refresh_token=fabric_refresh_token, project_name='all', scope='all')

# Get new Fabric Identity Token and update Fabric Refresh Token
try:
    id_token, refresh_token = client.refresh_tokens()
except Exception as e:
    print("Exception occurred while getting tokens:{}".format(e))

# User is expected to update the refresh token in JupyterHub environment such as below
# fabric_refresh_token=client.get_refresh_token()
# %store fabric_refresh_token

# Query Resources
status, advertised_topology = client.resources()

print(f"Status: {status}")
if status == Status.OK:
    print(f"Toplogy: {advertised_topology}")

# Create Slice
# Create topology
t = ExperimentTopology()

# Add node
n1 = t.add_node(name='n1', site='RENC')

# Set capacities
cap = Capacities()
cap.set_fields(core=4, ram=64, disk=500)

# Set Properties
n1.set_properties(capacities=cap, image_type='qcow2', image_ref='default_centos_8')

# Add PCI devices
n1.add_component(ctype=ComponentType.SmartNIC, model='ConnectX-5', name='nic1')

# Add node
n2 = t.add_node(name='n2', site='UKY')

# Set properties
n2.set_properties(capacities=cap, image_type='qcow2', image_ref='default_centos_8')

# Add PCI devices
n2.add_component(ctype=ComponentType.GPU, model='Tesla T4', name='nic2')

# Add node
n3 = t.add_node(name='n3', site='LBNL')

# Set properties
n3.set_properties(capacities=cap, image_type='qcow2', image_ref='default_centos_8')

# Add PCI devices
n3.add_component(ctype=ComponentType.GPU, model='Tesla T4', name='nic3')

# Generate Slice Graph
slice_graph = t.serialize()

ssh_key = None
with open("/home/fabric/.ssh/id_rsa.pub", "r") as myfile:
    ssh_key = myfile.read()
    ssh_key = ssh_key.strip()

# Request slice from Orchestrator
status, reservations = client.create(slice_name='JupyterSlice2', slice_graph=slice_graph, ssh_key=ssh_key)

print("Response Status {}".format(status))
if status == Status.OK:
    print("Reservations created {}".format(reservations))

slice_id = reservations[0].slice_id
# Delete Slice
status, result = client.delete(slice_id=slice_id)

print("Response Status {}".format(status))
if status == Status.OK:
    print("Response received {}".format(result))