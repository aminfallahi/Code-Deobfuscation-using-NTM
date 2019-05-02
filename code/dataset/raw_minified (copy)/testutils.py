import equip
def A(code):return compile(code,'<string>','exec')
def B(co):return equip.BytecodeObject.get_parsed_code(co)