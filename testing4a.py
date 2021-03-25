#from ib_insync import *
# util.startLoop()  # uncomment this line when in a notebook
import pandas
import numpy as np
#from talib import abstract
#from demo1functions import addindicators1
#import talib
import numpy as np
import time
import csv
import itertools
import datetime 
import calendar
import pandas as pd
import os
from datetime import datetime
from glob import iglob
import csv
from collections import OrderedDict
from timeit import default_timer as timer
from scipy.stats import weightedtau
from scipy import optimize
from itertools import combinations 
from scipy.optimize import minimize
import alpaca_trade_api as tradeapi
import threading
import time
import datetime
import math
from math import sin, log
from random import random


data = pd.read_excel('Data_Pathrise.xlsx')
#data_to_csv('Data_Pathrise.csv')
data.to_csv("Data_Pathrise.csv", index=False)

print(data.head())
data.info()

#print(data.head())





