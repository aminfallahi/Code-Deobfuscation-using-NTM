'\nUtility script to execute the main executable as if it would have been\ninstalled and available in the path.\n'
import sys,os
sys.path.insert(0,os.getcwd())
from trader.cli import main
main(prog_name='trader')