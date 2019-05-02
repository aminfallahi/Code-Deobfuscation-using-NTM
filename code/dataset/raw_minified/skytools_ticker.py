from kokki import File,Template as A
env.include_recipe('postgresql84.skytools')
File('/etc/skytools/ticker.ini',owner='root',content=A('postgresql84/skytools-ticker.ini.j2'))