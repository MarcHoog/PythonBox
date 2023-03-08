from proxmoxer import ProxmoxAPI 
from my_secrets import USERNAME, PASSWORD
import time
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
snapshot_name = input('snapshot name: ')
lxc_nodes = ['node-1','node-2','node-3']

proxmox = ProxmoxAPI(
    '10.0.0.253',port=8006, 
    user=USERNAME, 
    password=PASSWORD,
    verify_ssl=False,
    service="pve"
)

def get_my_containers():
    # this list comprehension is way to long lol
    return [container for container in 
            proxmox.nodes.ml350p.lxc.get() 
            if container['name'] in lxc_nodes]

def wait_for_task(task_id):
    node = proxmox.nodes.ml350p.tasks(task_id).status.get()['node']
    data = {"status": ""}
    while data["status"] != "stopped":
        data = proxmox.nodes(node).tasks(task_id).status.get()
        time.sleep(0.5)
    return data

for container in get_my_containers():
    shortcut = proxmox.nodes.ml350p.lxc(container['vmid'])
    taskuid = shortcut.snapshot.post(
                snapname=snapshot_name,vmid=container['vmid'],node='ml350p')
    wait_for_task(taskuid)

