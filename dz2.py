ignore_command= lambda command: True if command in ['alias', 'configuration','ip','sql', 'delect', 'update', 'exec', 'del', 'trincate'] else False
print(ignore_command('alias'))
