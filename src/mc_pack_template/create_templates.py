import argparse
import os

cwd = os.getcwd()


class SmartFormatter(argparse.HelpFormatter):

    def _split_lines(self, text, width):
        if text.startswith("R|"):
            return text[2:].splitlines()
        # this is the RawTextHelpFormatter._split_lines
        return argparse.HelpFormatter._split_lines(self, text, width)


def creat_datapack(args: argparse.Namespace):
    # create datapack folder
    datapack_folder = os.path.join(cwd, args.name[0])

    # create /data/minecraft/tags/functions folder
    entry_points_folder = os.path.join(
        datapack_folder, "data", "minecraft", "tags", "function"
    )

    # create /namespace/functions folder
    namespace = args.namespace[0] if args.namespace else args.name[0].lower()
    namespace_folder = os.path.join(datapack_folder, "data", namespace, "function")

    if args.dry_run:
        print(datapack_folder)

        # create meta-data file
        print(os.path.join(datapack_folder, "pack.mcmeta"))
        print(
            f'pack.mcmeta: {{"pack":{{"pack_format":{args.version[0]},"description":"{args.name[0]} datapack"}}}}'
        )

        print(entry_points_folder)
        print(namespace_folder)

        # create templates
        if args.template:
            print(os.path.join(entry_points_folder, "load.json"))
            print(f'load.json: {{"values": ["{namespace}:load"]}}')
            print(os.path.join(entry_points_folder, "tick.json"))
            print(f'tick.json: {{"values": ["{namespace}:tick"]}}')

            print(os.path.join(namespace_folder, "load.mcfunction"))
            print("load.mcfunction: msg @a Hello World!")
            print(os.path.join(namespace_folder, "tick.mcfunction"))
            print("tick.mcfunction: # tick function")
    else:
        os.mkdir(datapack_folder)

        # create meta-data file
        with open(os.path.join(datapack_folder, "pack.mcmeta"), "a") as file:
            file.write(
                f'{{"pack":{{"pack_format":{args.version[0]},"description":"{args.name[0]} datapack"}}}}'
            )

        os.makedirs(entry_points_folder)
        os.makedirs(namespace_folder)

        # create templates
        if args.template:
            with open(os.path.join(entry_points_folder, "load.json"), "a") as file:
                file.write(f'{{"values": ["{namespace}:load"]}}')
            with open(os.path.join(entry_points_folder, "tick.json"), "a") as file:
                file.write(f'{{"values": ["{namespace}:tick"]}}')

            with open(os.path.join(namespace_folder, "load.mcfunction"), "a") as file:
                file.write("msg @a Hello World!")
            with open(os.path.join(namespace_folder, "tick.mcfunction"), "a") as file:
                file.write("# tick function")


def create_resourcepack(args: argparse.Namespace):
    # create the resource pack folder
    resourcepack_folder = os.path.join(cwd, args.name[0])

    # create /data/minecraft/tags/functions folder
    entry_points_folder = os.path.join(resourcepack_folder, "assets", "minecraft")

    # create /namespace/functions folder
    namespace = args.namespace[0] if args.namespace else args.name[0].lower()
    namespace_folder = os.path.join(resourcepack_folder, "assets", namespace)

    if args.dry_run:
        print(resourcepack_folder)

        # create meta-data file
        print(os.path.join(resourcepack_folder, "pack.mcmeta"))
        print(
            f'pack.mcmeta: {{"pack":{{"pack_format":{args.version[0]},"description":"{args.name[0]} resourcepack"}}}}'
        )

        print(entry_points_folder)
        print(namespace_folder)

    else:
        os.mkdir(resourcepack_folder)

        # create meta-data file
        with open(os.path.join(resourcepack_folder, "pack.mcmeta"), "a") as file:
            file.write(
                f'{{"pack":{{"pack_format":{args.version[0]},"description":"{args.name[0]} datapack"}}}}'
            )

        os.makedirs(entry_points_folder)
        os.makedirs(namespace_folder)
