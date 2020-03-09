import fxcmpy
import socketio
import pandas as pd
import datetime as dt

import seaborn as sns
# from pylab import plt
import matplotlib.pyplot as plt



print (fxcmpy.__version__)
TOKEN = '10f9d062d912141e50a310bc0d887f1aa63f02b3'
# con = fxcmpy.fxcmpy(config_file='fxcm.cfg')
con = fxcmpy.fxcmpy(access_token=TOKEN, log_level='error',server='demo')
print(con.is_connected())
instruments = con.get_instruments_for_candles()
for i in range(int(len(instruments)/4)):
    print(instruments[i*4:(i+1)*4])
print(instruments[(i+1)*4:])
# print(con.get_candles('USD/JPY', period='D1')) #recall D1 of USD/JPY


# start = dt.datetime(2017, 7, 15)
# stop = dt.datetime(2017, 8, 1)
# con.get_candles('EUR/USD', period='D1', start=start, stop=stop)


data = con.get_candles('EUR/USD', period='m1',columns=['askopen'], number=500)
data.plot(figsize=(10, 6), lw=0.8);
