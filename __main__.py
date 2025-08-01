import argparse
import os

__version__ = "0.1.0"

cwd = os.getcwd()

class SmartFormatter(argparse.HelpFormatter):

    def _split_lines(self, text, width):
        if text.startswith('R|'):
            return text[2:].splitlines()
        # this is the RawTextHelpFormatter._split_lines
        return argparse.HelpFormatter._split_lines(self, text, width)

def creat_datapack(args: argparse.Namespace):
    # create datapack folder
    datapack_folder = os.path.join(cwd, args.name[0])

    # create /data/minecraft/tags/functions folder
    entry_points_folder = os.path.join(datapack_folder, "data", "minecraft", "tags", "functions")

    # create /namespace/functions folder
    namespace = args.namespace[0] if args.namespace else args.name[0].lower()
    namespace_folder = os.path.join(datapack_folder, "data", namespace, "functions")

    if args.dry_run:
        print(datapack_folder)

        # create meta-data file
        print(os.path.join(datapack_folder, "pack.mcmeta"))
        print(f'pack.mcmeta: {{"pack":{{"pack_format":{args.version[0]},"description":"{args.name[0]} datapack"}}}}')

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
    print("resourcepack")

if __name__ =="__main__":
    parser = argparse.ArgumentParser(
        prog="mc-pack-template",
        description="mc-pack-template creates a basic directory structure for a new mc-datapack "
             "or mc-resourcepack project",
     formatter_class=SmartFormatter
    )

    parser.add_argument(
        "-V", "--version",
        action="version",
        version=f"%(prog)s {__version__}"
    )

    parser.add_argument(
        "type",
        action="store",
        nargs=1,
        choices=["datapack", "dp", "resourcepack", "rp"],
        metavar="TYPE",
        help="R|Specify the type of the project to create\n"
             "datapack|dp for a datapack\n"
            "resourcepack|rp for a resourcepack"
    )

    parser.add_argument(
        "name",
        action="store",
        nargs=1,
        metavar="NAME",
        help="The name of the datapack or resourcepack"
    )

    parser.add_argument(
        "-n", "--namespace",
        action="store",
        dest="namespace",
        nargs=1,
        metavar="NAMESPACE",
        help="Specify the namespace of the datapack or resourcepack.\n"
             "Default is the lowercase name of the datapack or resourcepack",
    )

    parser.add_argument(
       "-v", "--pack-version",
        action="store",
        dest="version",
        nargs=1,
        metavar="VERSION",
        help="Specify the pack version stored in pack_format.\n"
             "Default is 61 (latest version, for minecraft 1.21.4)",
        default=[61]
    )

    parser.add_argument(
        "-t", "--template",
        action="store_true",
        dest="template",
        help="Create some template functions"
    )

    parser.add_argument(
        "-d", "--dry-run",
        action="store_true",
        dest="dry_run",
        help="Print file paths to stout but don't create any files"
    )

    cmd_args = parser.parse_args()
    if cmd_args.type[0] == "datapack" or cmd_args.type[0] == "dp":
        creat_datapack(cmd_args)
    elif cmd_args.type[0] == "resourcepack" or cmd_args.type[0] == "rp":
        create_resourcepack(cmd_args)