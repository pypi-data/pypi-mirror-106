import click
from primerobotcli.primerobot import TaskRegister


@click.group()
@click.version_option('1.0.0')
def cli():
    pass


@cli.command()
def register():
    task_register = TaskRegister()
    task_register.register()
