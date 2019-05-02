import compago as B
A=B.Application()
@A.command
def C(name):A.logger.error('Yes! This is logging at its finest!');A.logger.info(A.config['TEST_OPTION'])
if __name__=='__main__':A.run()