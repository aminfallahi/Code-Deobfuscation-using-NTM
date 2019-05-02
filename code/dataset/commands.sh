find . -type f -exec awk -v x=20 'NR==x{exit 1}' {} \; -exec wc -l {} \;
while :; do ls -la | wc -l; done
find ./data -type f | grep -i py$ | xargs -i cp {} ./asb
for i in `ls`; do cat $i | wc -l; done
