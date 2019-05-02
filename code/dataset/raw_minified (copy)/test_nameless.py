from click.testing import CliRunner as B
from nameless.cli import main
def A():C=B();A=C.invoke(main,[]);assert A.output=='()\n';assert A.exit_code==0