import minecraft_launcher_lib
import dearpygui.dearpygui as dpg
import subprocess
import func
import json
import os

dpg.create_context()
#game options
direct = json.load(open("C:\JLauncher\data.json"))
game_direct = direct["direct_game"]
print(game_direct)

def down_version():
    version = dpg.get_value("download_version")
    print("Download Version")
    minecraft_launcher_lib.install.install_minecraft_version(versionid=version, minecraft_directory=game_direct)
    print("Download completely")

def open_foldir():
    func.folder(game_direct)

def play():
    version = dpg.get_value("input_version")
    game_name = dpg.get_value("input_name")

    options = {
        "username": game_name,
        "uuid": "",
        "token": ""
    }
    
    try:
        if func.is_fabric(version):
            print(f"download Minecraft {version}")
            version = version.split(" ")[1]
            minecraft_launcher_lib.fabric.install_fabric(version, minecraft_directory=game_direct)
            minecraft_launcher_lib.install.install_minecraft_version(versionid=version, minecraft_directory=game_direct)
            print("Load Minecraft")
            subprocess.call(minecraft_launcher_lib.command.get_minecraft_command(version=func.load_fabric(game_direct), minecraft_directory=game_direct, options=options))

        else:
            print(f"download Minecraft {version}")
            minecraft_launcher_lib.install.install_minecraft_version(versionid=version, minecraft_directory=game_direct)
            print("Load Minecraft")
            subprocess.call(minecraft_launcher_lib.command.get_minecraft_command(version=version, minecraft_directory=game_direct, options=options))
    except:
        print("iq issue")
        pass

def versiont_opt():
    with dpg.window(label="JLauncher", width=250, height=275, tag="Download"):
        dpg.add_text("Download version")
        dpg.add_text("\n")
        dpg.add_combo(func.downloadeble_versions(game_direct), label="Choose version", width=75, tag="download_version")
        dpg.add_text("\n")
        dpg.add_button(label="Download", callback=down_version)
        dpg.add_button(label="return", callback=lambda:[dpg.delete_item("Download"), welcome()])

def welcome():
    with dpg.window(label="JLauncher", width=250, height=275, tag="Main"):
        dpg.add_text("50x50 logo png мне впадлу чето делать")
        dpg.add_text("\n")
        dpg.add_combo(func.version_list(game_direct), label="Choose version", width=75, tag="input_version")
        dpg.add_input_text(label="Player name", width=75, tag="input_name")
        dpg.add_button(label="Play", callback=play)
        dpg.add_text("\n")
        dpg.add_button(label="game folder", callback=open_foldir)
        dpg.add_button(label="download version", callback=lambda:[dpg.delete_item("Main"), versiont_opt()])

if __name__ == __name__:
    welcome()

dpg.create_viewport(title='JLauncher', width=250, height=275)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()