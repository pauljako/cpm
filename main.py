import argparse
import requests


def main():
    # Creates the Parser
    argument_parser = argparse.ArgumentParser(prog="cpm", description="The Cool Package Manager")

    # Adds the subparser
    argument_sub_parser = argument_parser.add_subparsers()

    # Adds the installation command
    install_command_parser = argument_sub_parser.add_parser("install", help="Install a Package")
    install_command_parser.add_argument("package", help="The Package to install")

    # Parses the Arguments
    argument_parser.parse_args()


if __name__ == '__main__':
    main()
