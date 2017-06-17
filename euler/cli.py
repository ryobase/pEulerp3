""" Entry point for command line interface (or CLI) """

import importlib
import click

@click.command()
def main():
    click.echo("Hello")

if __name__ == "__main__":
    main()