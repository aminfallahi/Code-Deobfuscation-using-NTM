def test_all(db):"\n        Unit Test all modules within Sahana using CherryPy's WebTest\n        NB This doesn't yet work\n    ";from applications.sahana.modules.test_cr import *;test_cr(db);from applications.sahana.modules.test_or import *;test_or(db);from applications.sahana.modules.test_pr import *;test_pr(db)
if __name__=='__main__':test_all(db)