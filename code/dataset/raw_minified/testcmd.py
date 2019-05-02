import djclick as A
@A.command()
@A.option('--raise','raise_when_called',is_flag=True)
def B(raise_when_called):
	if raise_when_called:raise RuntimeError()