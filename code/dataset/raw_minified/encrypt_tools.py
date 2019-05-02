import shell_tools as A
def B():'\n    status()\n\n    Returns whether or not filevault is active\n    ';return A.run('fdesetup isactive')['success']