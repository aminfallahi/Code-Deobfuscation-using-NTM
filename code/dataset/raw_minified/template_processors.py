from catwatch.lib.money import cents_to_dollars as B
def A(amount,convert_to_dollars=True):
	'\n    Pad currency with 2 decimals and commas,\n    optionally convert cents to dollars.\n\n    :param amount: Amount in cents or dollars\n    :type amount: int or float\n    :param convert_to_dollars: Convert cents to dollars\n    :type convert_to_dollars: bool\n    :return: str\n    ';A=amount
	if convert_to_dollars:A=B(A)
	return '{:,.2f}'.format(A)