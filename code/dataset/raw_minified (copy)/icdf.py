import numpy as A
from scipy.special import erfinv as B
def D(sample,lo=-1,hi=1):return lo+(hi-lo)*sample
def C(sample,avg=0.0,std=1.0):return avg+std*A.sqrt(2)*B(2*sample-1)
def E(sample,avg=0.0,std=1.0):return A.exp(C(sample,avg,std))
def F(sample,p=0.5):return sample>p