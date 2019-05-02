from .model_list import ModelList as A
class B(A):
	def has_more_results(A):return A.meta['total_pages']>A.meta['current_page']