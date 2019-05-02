from pyalgotrade.bitcoincharts import barfeed as B
from pyalgotrade.tools import resample as C
from pyalgotrade import bar
import datetime as D
def A():A=B.CSVTradeFeed();A.addBarsFromCSV('bitstampUSD.csv',fromDateTime=D.datetime(2014,1,1));C.resample_to_csv(A,bar.Frequency.MINUTE*30,'30min-bitstampUSD.csv')
if __name__=='__main__':A()