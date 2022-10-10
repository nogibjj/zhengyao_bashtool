#!/usr/bin/env python

from email.policy import default
from xml.etree.ElementInclude import default_loader
import click
from dblib.querydb import querydb
from dblib.querydb import querybydirector
from dblib.querydb import sortbyyear

# build a click group
@click.group()
def cli():
    """A simple CLI to query a SQL database"""


# build a click command
@cli.command()
@click.option(
    "--query",
    default="SELECT * FROM default.netflix1_csv LIMIT 2",
    help="SQL query to execute",
)
def cli_query(query):
    """Execute a SQL query"""
    querydb(query)

# 1. build a command to do data cleaning (select works directed by one director)
# 2. and do data sorting for the works directed by this director based on released year in ascending order

# Data cleaning
default_director = "Suhas Kadav"
@cli.command()
@click.option(
    "--director",
    default=default_director,
    help="select works directed by Suhas Kadav",
)
def select_by_director(director):
    """select works directed by a specific director"""
    querybydirector(director)


# Sorting
@cli.command()
@click.option(
    "--director",
    default=default_director,
    help="sort works directed by Suhas Kadav based on released year",
)
def sort_by_year(director):
    """sort works directed by a specific director based on released year"""
    sortbyyear(director)


# run the CLI
if __name__ == "__main__":
    cli()
