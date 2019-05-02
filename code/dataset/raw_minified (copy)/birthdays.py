'\nPrints a list of birthdays in your address book (in days from now).\n\nNOTE: This script requires access to your contacts in order to work.\n'
E='days'
import contacts as B,datetime as C
def D(date):A=date;B=C.datetime.now();D=int(C.datetime(B.year,A.month,A.day)<B);return (C.datetime(B.year+D,A.month,A.day)-B).days
A='\n'.join(('* {p.first_name} in {days} days'.format(**A)for A in sorted(({'p':A,E:D(A.birthday)}for A in B.get_all_people()if A.birthday),key=lambda x:x[E])))
print('Upcoming Birthdays:\n{}\n{}'.format('='*19,A)if A else"You don't have any birthdays in your address book.")