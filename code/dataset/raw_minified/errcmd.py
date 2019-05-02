from django.core.management import CommandError as A
import djclick as B
@B.command(version='20.0')
def C():raise A('Raised error description')