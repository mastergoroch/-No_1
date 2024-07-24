def ignore_command(command): return True if command in ['alias', 'configuration','ip','sql', 'delect', 'update', 'exec', 'del', 'trincate'] else False
print(ignore_command('alias'))