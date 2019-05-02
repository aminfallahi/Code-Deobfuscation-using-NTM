from click.testing import CliRunner as B
from turnstile.version import version as C
from turnstile.manager_subcommands.version import cmd
def A():D=B();A=D.invoke(cmd);assert A.output.startswith('Zalando Turnstile');assert C in A.output;assert A.exit_code==0