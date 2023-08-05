#!/usr/bin/env python3


import click
from .commands import Welcome, Mail, CheckAuth
from mrpeace import info


@click.group()
@click.version_option(version=info.VERSION)
def cli():
    pass


@cli.command()
def hi():
    """Print welcome message."""
    click.secho(Welcome().hello(), bg="blue")


@cli.command()
@click.option("--account", prompt="Your account", help="Provide your account")
@click.option("-password", prompt="Your password", help="Provide your password")
def automail(account, password):
    """Send default email to self."""
    click.confirm("Do you want to continue?", abort=True)
    Mail(account, password).send()


@cli.command()
@click.option("-check", prompt="entire url link", help="Provide url path")
def url(check):
    """Send request and checks response body"""
    click.confirm("Enter url path", abort=True)
    click.echo(CheckAuth(check).json())
