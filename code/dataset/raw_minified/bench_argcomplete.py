_A='%s\n'
if __name__=='__main__':import sys,timeit;from argcomplete.completers import FilesCompleter;from _pytest._argcomplete import FastFilesCompleter;count=1000;setup='from __main__ import FastFilesCompleter\nfc = FastFilesCompleter()';run='fc("/d")';sys.stdout.write(_A%timeit.timeit(run,setup=setup.replace('Fast',''),number=count));sys.stdout.write(_A%timeit.timeit(run,setup=setup,number=count))