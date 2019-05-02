import os,re
def update_dependencies(directory,dependency):
	C='app.js';B='app';A='assets'
	with open(os.path.join(directory,A,B,C),'r')as f:
		data=f.read();search=re.search('angular\\.module\\(.*(\\[.*\\])\\)',data).groups(0)[0];dependencies=eval(search)
		if dependency not in dependencies:dependencies.append(dependency)
		replace=str(dependencies);updated=data.replace(search,replace)
	with open(os.path.join(directory,A,B,C),'w')as f:f.write(updated)