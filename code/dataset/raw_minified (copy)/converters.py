import subprocess as A
def B(docx_path,file_path):'\n    This will convert ``file_path`` to docx and place the converted file at\n    ``docx_path``\n    ';A.call(['abiword','--to=docx','--to-name',docx_path,file_path])