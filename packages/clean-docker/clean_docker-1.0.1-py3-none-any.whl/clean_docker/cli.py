import click

from clean_docker.main import main


def cli() -> int:
    if click.confirm("Remove all Docker artifacts?"):
        return main()
    else:
        click.echo("Abort", err=True)
        return 1


if __name__ == "__main__":
    cli()
