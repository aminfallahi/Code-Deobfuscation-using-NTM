from openrecipes.util import select_class as B
def A(scope,data={}):
	I='ingredients';H='duration';G='published';F='yield';D='.//text()';A=data;C=B(scope,'hrecipe');A['name']=B(C,'fn').select(D).extract();A[F]=B(C,F).select(D).extract();A[G]=B(C,G).select(D).extract();A['description']=B(C,'summary').select(D).extract();A[H]=B(C,H).select(D).extract();A['prepTime']=B(C,'preptime').select(D).extract();A['cookTime']=B(C,'cooktime').select(D).extract();A[I]=[]
	for E in B(C,'ingredient'):A[I].append(''.join(E.select(D).extract()))
	return A