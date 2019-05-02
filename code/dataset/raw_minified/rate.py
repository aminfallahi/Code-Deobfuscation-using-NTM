'Give a 5-star rating to 3 lucky 24-year-old straight/gay/bi women/men.'
import okcupyd as A
B=A.User()
C=B.search(location='minneapolis, mn',keywords='arrested development',age_min=24,age_max=24)
for D in C[:3]:D.rate(5)