import clg,yaml
def A():A=clg.CommandLine(yaml.load(open('exclusive_groups.yml')));print(A.parse())
if __name__=='__main__':A()