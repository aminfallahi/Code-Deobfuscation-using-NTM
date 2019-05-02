'Write back all data it receives.'
import sys as A
B=A.stdin.read(1)
while B:A.stdout.write(B);A.stdout.flush();B=A.stdin.read(1)
A.stderr.write('byebye')
A.stderr.flush()