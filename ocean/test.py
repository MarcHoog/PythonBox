import digitalocean
API_KEY = "dop_v1_064017ffe44209ab6662014057597a750c0ab340ca78b4ced0b7c70bac284838"
manager = digitalocean.Manager(token=API_KEY)
my_droplets = manager.get_all_droplets()
my_snapshots = manager.get_all_snapshots()
manager.get_droplet




def check_snapshot(droplet_name:str):
    for snapshot in my_snapshots:
        if snapshot.name == f"{droplet_name}-snapshot":
            return True
    return False

def destroy_droplet(name:str, snapshot:bool=True):
    for drop in my_droplets:
        if drop.name == "rust-desk":
            drop.shutdown()
            if snapshot:
                if check_snapshot(drop.name) is False:
                    print("No snapshot found, creating one")	
                    drop.take_snapshot(f"{drop.name}-snapshot")
                else:
                    print("Snapshot found, destroying droplet")
            drop.destroy()
            return True
    return False

def create_droplet(name:str,from_snapshot:bool=True):
    for snapshot in my_snapshots:
        if check_snapshot(name):
            print("snapshot found, creating droplet")
            image = snapshot.id
        else:
            print("Snapshot not found, creating droplet from image")
            image = "ubuntu-22-04-x64"	
            
        droplet = digitalocean.Droplet(
                               token=API_KEY,
                               name=name,
                               region='fra1', 
                               image=image, 
                               size_slug='s-1vcpu-1gb',  # 1GB RAM, 1 vCPU
                               backups=True)
    
        droplet.create()
    

create_droplet("rust-desk")
