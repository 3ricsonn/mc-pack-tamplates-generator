import argparse

from .create_templates import SmartFormatter, create_resourcepack, creat_datapack

__version__ = "0.1.0"


def start():
    """Starts skript and process command line arguments"""
    parser = argparse.ArgumentParser(
        prog="mc_pack_template",
        description="mc_pack_template creates a basic directory structure for a new mc-datapack "
        "or mc-resourcepack project",
        formatter_class=SmartFormatter,
    )

    parser.add_argument(
        "-V", "--version", action="version", version=f"%(prog)s {__version__}"
    )

    parser.add_argument(
        "type",
        action="store",
        nargs=1,
        choices=["datapack", "dp", "resourcepack", "rp"],
        metavar="TYPE",
        help="R|Specify the type of the project to create\n"
        "datapack|dp for a datapack\n"
        "resourcepack|rp for a resourcepack",
    )

    parser.add_argument(
        "name",
        action="store",
        nargs=1,
        metavar="NAME",
        help="The name of the datapack or resourcepack",
    )

    parser.add_argument(
        "-n",
        "--namespace",
        action="store",
        dest="namespace",
        nargs=1,
        metavar="NAMESPACE",
        help="Specify the namespace of the datapack or resourcepack.\n"
        "Default is the lowercase name of the datapack or resourcepack",
    )

    parser.add_argument(
        "-v",
        "--pack-version",
        action="store",
        dest="version",
        nargs=1,
        metavar="VERSION",
        help="Specify the pack version stored in pack_format.\n"
        "Default is 61 (latest version, for minecraft 1.21.4)",
        default=[61],
    )

    parser.add_argument(
        "-t",
        "--template",
        action="store_true",
        dest="template",
        help="Create some template functions",
    )

    parser.add_argument(
        "-d",
        "--dry-run",
        action="store_true",
        dest="dry_run",
        help="Print file paths to stout but don't create any files",
    )

    cmd_args = parser.parse_args()
    if cmd_args.type[0] == "datapack" or cmd_args.type[0] == "dp":
        creat_datapack(cmd_args)
    elif cmd_args.type[0] == "resourcepack" or cmd_args.type[0] == "rp":
        create_resourcepack(cmd_args)


if __name__ == "__main__":
    start()
