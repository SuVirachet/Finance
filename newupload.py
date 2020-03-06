import fxcmpy
import socketio
import pandas as pd
import datetime as dt

print (fxcmpy.__version__)
TOKEN = '4b089f39a07dbb5f50d6a6a80c22aa81b055fe7e'
# con = fxcmpy.fxcmpy(config_file='fxcm.cfg')
con = fxcmpy.fxcmpy(access_token=TOKEN, log_level='error',server='demo')
print(con.is_connected())
print(con.get_instruments())
instruments = con.get_instruments_for_candles()
for i in range(int(len(instruments)/4)):
    print(instruments[i*4:(i+1)*4])
print(instruments[(i+1)*4:])
print(con.get_candles('USD/JPY', period='D1'))

# con = fxcmpy.fxcmpy(access_token = TOKEN, log_level = 'error')
# instruments = con.get_instruments()
# print(con.get_instruments())

# print(con.get_instruments())
