import clg,yaml,yamlordereddictloader as A
def B():B=clg.CommandLine(yaml.load(open('subparsers.yml'),Loader=A.Loader));print(B.parse())
if __name__=='__main__':B()