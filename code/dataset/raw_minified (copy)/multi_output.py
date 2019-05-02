import argparse as B,sys
A=B.ArgumentParser(description='Something')
A.add_argument('--output_filename',type=B.FileType('w'),required=True,help='Name of Excel output file.',nargs='+')
A.add_argument('--due_date_field',type=str,help="Column name for due date field. 'Due Date' by default.")
if __name__=='__main__':C=A.parse_args()