F='r'
D='*'
C='+'
import argparse as B,sys
A=B.ArgumentParser(description='Something')
A.add_argument('--one-choice',choices=[0,1,2,3],nargs=1)
A.add_argument('--two-choices',choices=[0,1,2,3],nargs=2)
A.add_argument('--at-least-one-choice',choices=[0,1,2,3],nargs=C)
A.add_argument('--all-choices',choices=[0,1,2,3],nargs=D)
A.add_argument('--need-at-least-one-numbers',type=int,nargs=C,required=True)
A.add_argument('--choices-str',nargs=C,type=str)
A.add_argument('--multiple-file-choices',type=B.FileType(F),nargs=D)
A.add_argument('--more-multiple-file-choices',type=B.FileType(F),nargs=D)
if __name__=='__main__':E=A.parse_args();sys.stdout.write('{}'.format(E.multiple_file_choices))