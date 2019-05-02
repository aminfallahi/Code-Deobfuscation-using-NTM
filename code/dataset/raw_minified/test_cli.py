from click.testing import CliRunner as B
from pyskel.scripts.cli import cli
def A():C=B();A=C.invoke(cli,['3']);assert A.exit_code==0;assert A.output=='False\nFalse\nFalse\n'