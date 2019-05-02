import djclick as A
@A.group(invoke_without_command=True)
def B():A.echo('group_command')
@B.command()
def C():A.echo('SUB1')
@B.command(name='subcmd3')
def D():A.echo('SUB2')