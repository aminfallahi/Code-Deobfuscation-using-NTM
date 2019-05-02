import click
from complex.cli import pass_context as A
@click.command('status',short_help='Shows file changes.')
@A
def B(ctx):'Shows file changes in the current working directory.';ctx.log('Changed files: none');ctx.vlog('bla bla bla, debug info')