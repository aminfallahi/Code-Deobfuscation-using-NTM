'\nA unit test for the train.py script\n'
import os,pylearn2 as A
from pylearn2.scripts.train import train
def B():'\n    Calls the train.py script with a short YAML file\n    to see if it trains without error\n    ';train(os.path.join(A.__path__[0],'scripts/autoencoder_example/dae.yaml'))