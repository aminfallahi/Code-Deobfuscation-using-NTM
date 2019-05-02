import begin as A,logging as B
@A.subcommand
def C(name):'Say hello';B.info('Hello {0}'.format(name))
@A.subcommand
def D(name):'Say goodbye';B.info('Goodbye {0}'.format(name))
@A.start
@A.logging
def E():'Greetings and salutations'