import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import click
from taskmanager.manager import TaskManager
from taskmanager.database import init_db

@click.group()
def cli():
    pass

@cli.command()
def initdb():
    init_db()
    click.echo("Initialized the database")

@cli.command()
@click.argument('name')
def add_category(name):
    manager = TaskManager()
    manager.create_category(name)
    click.echo(f"Category '{name}' added")

@cli.command()
def list_categories():
    manager = TaskManager()
    categories = manager.list_categories()
    for category in categories:
        click.echo(f"{category.id}: {category.name}")

@cli.command()
@click.argument('description')
@click.argument('category_id', type=int)
def add_task(description, category_id):
    manager = TaskManager()
    manager.create_task(description, category_id)
    click.echo(f"Task '{description}' added to category {category_id}")

@cli.command()
@click.option('--category_id', type=int, default=None, help='Filter tasks by category')
def list_tasks(category_id):
    manager = TaskManager()
    tasks = manager.list_tasks(category_id)
    for task in tasks:
        click.echo(f"{task.id}: {task.description} (Category: {task.category.name})")

@cli.command()
@click.argument('task_id', type=int)
def delete_task(task_id):
    manager = TaskManager()
    manager.delete_task(task_id)
    click.echo(f"Task {task_id} deleted")

if __name__ == "__main__":
    cli()
