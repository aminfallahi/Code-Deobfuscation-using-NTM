def id_modifier(expression):
	" Evaluate the provided expression, replacing any '%' symbol by a\n\t\tvariable that will contain the identifier to modify. If a '%' symbol\n\t\tis needed in the expression, escape it by doubling it (i.e., '%%')\n\n\t\tExample:\n\t\t\t% -> [identifier]\n\t\t\t%.split() -> [identifier].split()\n\t\t\t% %% 2 - > [identifier] % 2\n\t";placeholder=re.compile('(?<!%)%(?!%)')
	try:return eval('lambda item: '+placeholder.sub('item',expression).replace('%%','%'))
	except SyntaxError as e:error('invalid setter:\n%s\n%s^ syntax error'%(e.text,' '*(e.offset-1)))