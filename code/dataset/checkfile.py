import os
for filename in os.listdir('./raw'):
	exists = os.path.isfile('./raw_minified/'+filename)
	if not exists:
		print(filename)
