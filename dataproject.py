import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import yfinance as yf
from backtesting import Backtest, Strategy
from backtesting.lib import crossover
from backtesting.test import SMA
import time
import plotly.express as px
import plotly.graph_objects as go


st.title('Our backtesting portal :sunglasses:')

#st.selectbox('Select the stock',)

stockname = st.text_input("Please enter stock name eg: tcs ->> TCS.NS note add .ns in caps")

stname = str(stockname)

data = yf.Ticker(stname)

hist=pd.DataFrame(data.history(period="MAX"))
hist = hist.reset_index()
#hist.index = pd.to_datetime(hist.index)
st.write(hist.head())

printable_data = pd.DataFrame(hist,columns=['Date','Close'])

#st.write(printable_data)


data_hist = pd.DataFrame(hist,columns=['Date','Open', 'High', 'Low', 'Close'])
st.write(data_hist[{'Close','Date'}])
if st.checkbox('Show company info in table format'):
	chart_data = pd.DataFrame(printable_data)
	#chart_data
	st.write(type(chart_data))
	with st.spinner('Wait for it...  I am doing my work'):
		time.sleep(5)
	st.success('Done! you are good to go!')


	#chart_data.plot()
#"""fig = go.Figure(data=go.Ohlc(x=data_hist['Date'],
#                    open=data_hist['Open'],
#                   high=data_hist['High'],
#                   low=data_hist['Low'],
#                   close=data_hist['Close']))"""

#fig.show()
#fig = px.line(printable_data, x="Date", y="Close", title='Line plot of closing')
#fig.show()    
""" # sma backtesting
## deployed cash 1,00,000

""" 
class SmaCross(Strategy):
    n1 = 20
    n2 = 200

    def init(self):
        close = self.data.Close
        self.sma1 = self.I(SMA, close, self.n1)
        self.sma2 = self.I(SMA, close, self.n2)

    def next(self):
        if crossover(self.sma1, self.sma2):
            self.buy()
        elif crossover(self.sma2, self.sma1):
            self.sell()


bt = Backtest(data_hist, SmaCross,
              cash=100000, commission=0.001,
              exclusive_orders=True)

output = pd.DataFrame(bt.run())
#bt.plot()
output = output.reset_index()
#st.write(output)
st.write(output['index'][4]+'=')
d = output[0][4]
st.title(d)
 #final amount
st.write(output['index'][4]+' =',output[0][4]) #final amount
st.write(output['index'][17]+' =',output[0][17]) #no.of trades
st.write(output['index'][18]+' =',output[0][18]) #win rate[%]
st.write(output['index'][19]+' =',output[0][19])  #best trade
st.write(output['index'][20]+' =',output[0][20])   # worest trade
st.write(output['index'][13]+' =',output[0][13])


