import fxcmpy
import socketio

print (fxcmpy.__version__)
TOKEN = '67932040d63246639f24cc5c4170ad3dc5cd3b8d'
# con = fxcmpy.fxcmpy(config_file='fxcm.cfg')
con = fxcmpy.fxcmpy(config_file='fxcm.cfg', server='demo')
# con = fxcmpy.fxcmpy(access_token = TOKEN, log_level = 'error')
# instruments = con.get_instruments()
# print(instruments[:5]) ['EUR/USD', 'USD/JPY', 'GBP/USD', 'USD/CHF', 'EUR/CHF']
# print(con.get_instruments())

# print(con.get_instruments())
# TOKEN = "c6436d54530a85bef95c5f4f61c003dde3f7a2ce"
# con = fxcmpy.fxcmpy(access_token = TOKEN, log_level = 'error')
# instruments = con.get_instruments()
# print(instruments[:5]) ['EUR/USD', 'USD/JPY', 'GBP/USD', 'USD/CHF', 'EUR/CHF']
