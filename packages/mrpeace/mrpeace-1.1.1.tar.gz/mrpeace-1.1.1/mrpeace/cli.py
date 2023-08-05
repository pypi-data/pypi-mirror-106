#!/usr/bin/env python3

import click
from .commands import Welcome, Mail
from mrpeace import info


@click.group()
@click.version_option(version=info.VERSION)
def cli():
    pass


@cli.command()
def hi():
    click.secho(Welcome().hello(), bg="blue")


@cli.command()
@click.option("--account", prompt="Your account", help="Provide your account")
@click.option("-password", prompt="Your password", help="Provide your password")
def automail(account, password):
    click.confirm("Do you want to continue?", abort=True)
    Mail(account, password).send()
