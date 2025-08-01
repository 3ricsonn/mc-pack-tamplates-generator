<h1 align="center">MC-Pack Templates Generator</h1>

The mc-pack templates generator, as the name suggests, takes on the tedious task of creating a basic file structure 
for minecraft data packs and resource pack.

## Usage
```
usage: mc-pack-template [-h] [-V] [-n NAMESPACE] [-v VERSION] [-t] [-d] TYPE NAME

mc-pack-template creates a basic directory structure for a new mc-datapack or
mc-resourcepack project

positional arguments:
  TYPE                  Specify the type of the project to create
                        datapack|dp for a datapack
                        resourcepack|rp for a resourcepack
  NAME                  The name of the datapack or resourcepack

options:
  -h, --help            show this help message and exit
  -V, --version         show program's version number and exit
  -n NAMESPACE, --namespace NAMESPACE
                        Specify the namespace of the datapack or resourcepack.
                        Default is the lowercase name of the datapack or
                        resourcepack
  -v VERSION, --pack-version VERSION
                        Specify the pack version stored in pack_format.
                        Default is 61 (latest version, for minecraft 1.21.4)
  -t, --template        Create some template functions
  -d, --dry-run         Print file paths to stout but don't create any files
```

## Installation

## Uninstallation

## Data pack Structure
The data pack files are store in the `datapacks` folder of the corresponding Minecraft world. To find your world folder, 
you can either locate it via your game directory `.mincraft/saves/(World Name)/datapacks` (on Windows accessible through 
the `%APPDATA%` folder) or open your world directory via the game by selecting your world and clicking "Edit" -> 
"Open world folder". <br>
The basic data pack structure looks like the following:
```
.mincraft
└── saves
    └── (World Name)
        └── datapacks
            └── NAME                          (Name of the data pack)
                ├── pack.mcmeta               (contains name and version)
                ├── data
                │   └── minecraft
                │       └── tags
                │           └── functions
                │               ├── load.json (contains referenc to function called 
                │               │               when data pack us loaded)
                │               └── tick.json (contains referenc to function called 
                │                               every tick)
                └── NAMESPACE                 (namespace of the data pack, used to 
                    │                           refer to the data pack functions)
                    └── funcions
                        └── *.mcfunction      (each file is a function, accessed 
                                                via "namespace:file_name")
```

## Further Information
For more indepth information, please refer to the minecraft wiki on 
[data packs](https://minecraft.fandom.com/wiki/Tutorials/Creating_a_data_pack) and 
[resource packs](https://minecraft.fandom.com/wiki/Resource_pack)