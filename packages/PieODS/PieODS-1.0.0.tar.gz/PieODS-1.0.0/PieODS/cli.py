"""Console script for PieODS."""
from . import Switch
import sys
import click



@click.command()
@click.option("--service",
            type=click.Choice(['start', 'stop', 'demolish'], case_sensitive=False),
            help="To start a PieODS instance: 'PieODS --service start'\nTo stop a PieODS instance: 'PieODS --service stop'\nTo demolis a PieODS instance: 'PieODS --service demolish'")
def main(service=None):
    """Console entry point for PieODS (Python interface to Jvalue ODS)."""
    client = Switch.ODSclient()
    if service=='stop':
        client.stop()
    elif service=='start':
        client.start()
    elif service=='demolish':
        client.demolish()
    else:
        ctx = click.get_current_context()
        click.echo(ctx.get_help())
        ctx.exit()        
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
