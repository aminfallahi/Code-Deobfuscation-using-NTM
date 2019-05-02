from pyalgotrade.optimizer import worker as A
import rsi2
if __name__=='__main__':A.run(rsi2.RSI2,'localhost',5000,workerName='localworker')