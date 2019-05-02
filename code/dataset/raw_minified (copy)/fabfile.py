from fabric.api import local as A,cd
def B():A('./bin/docs');A('./bin/python3 setup.py upload_sphinx --upload-dir=docs/html')
def C():A('python3 setup.py bdist_egg sdist --formats=bztar,gztar,zip upload')