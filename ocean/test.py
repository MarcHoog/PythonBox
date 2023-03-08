import digitalocean
API_KEY = "dop_v1_88d813702c1e3ca720c59d9fea6abb7fdf6629fdbcf17d4574dbd8f1bf667e91"
manager = digitalocean.Manager(token=API_KEY)
my_droplets = manager.get_all_droplets( )
my_snapshots = manager.get_all_snapshots()


class DropletCache:
    def __init__(self, manager:digitalocean.Manager) -> None:
        self.manager = manager
        self.droplets = self.manager.get_all_droplets()

    def index_droplets_by_name(self, list):
        dict = {i.name: [] for i in list}
        for x in my_droplets:
            dict[x.name].append(x)
        return dict
    
    def index_droplets_by_id(self, list):
        return {i.id: i for i in list}
    
    def get_drop_by_name(self, name:str): 
        return self.index_droplets_by_name(self.my_droplets)[name]
    
    def get_drop_by_id(self, id:int):
        return self.index_droplets_by_id(self.my_droplets)[id]
    
    def refresh_droplets(self):
        self.my_droplets = self.manager.get_all_droplets()


class OceanicBeingOfDegitalness:
    def __init__(self) -> None:
        self.api_key = "dop_v1_88d813702c1e3ca720c59d9fea6abb7fdf6629fdbcf17d4574dbd8f1bf667e91"
        self.manager = digitalocean.Manager(token=self.api_key)
        self.my_droplets = self.manager.get_all_droplets()
        self.my_snapshots = self.manager.get_all_snapshots()


    
def check_snapshot(droplet_name:str):
    for snapshot in my_snapshots:
        if snapshot.name == f"{droplet_name}-snapshot":
            return snapshot
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

def create_droplet(name:str):
    image = None
    for drop in my_droplets:
        if drop.name == name:
            print("Droplet already exists")
            return False
    
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
    
if __name__ == "__main__":
    test = DropletCache(manager)
    print(dict(test))