import minecraft_launcher_lib
import os
def is_fabric(x):
    x = x.split(" ")
    if x[0] == "fabric" or x[0] == "Fabric":
        return True
    else:
        return False

def load_fabric(game_direct):
    for i in minecraft_launcher_lib.utils.get_installed_versions(minecraft_directory=game_direct):
        if i["id"].split("-")[0] == "fabric" and i["id"].split("-")[1] == "loader":
            return i["id"]

def version_list(game_direct):
    x = []
    for i in minecraft_launcher_lib.utils.get_installed_versions(minecraft_directory=game_direct):
        if i["id"].split("-")[0] == "fabric" and i["id"].split("-")[1] == "loader":
            x.append(f"fabric {i['id'].split('-')[3]}")
        else:
            x.append(i["id"])
    return x

def downloadeble_versions(x):
    w = []
    for i in minecraft_launcher_lib.utils.get_available_versions(x):
        if i["type"] == "snapshot" or i["type"] == "old_alpha" or i["type"] == "old_beta":
            pass
        else:
            w.append(i["id"])
    return w

def folder(x):
    os.startfile(x)