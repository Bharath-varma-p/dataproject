# Back testing Portal

Implementing the Stastical Concepts and Understanding!!!

## Requirements

Use the package manager [python](https://python.org) to install.


```bash
yfinance==0.1.63  #for fetching OHLC Data of indian Tickets
numpy==1.18.3     # Numeric computation
pandas==1.1.5     # Working with Data
plotly==4.6.0     # Data visualization
backtesting==0.3.2 # Backtesting library
streamlit==0.89.0  # used to build DS apps
```

## Usage

```python 
import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with data
import numpy as np
import pandas as pd
import yfinance as yf
from backtesting import Backtest, Strategy
from backtesting.lib import crossover
from backtesting.test import SMA
import time
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image            # for using images 
```

## Functions 
```python
class SmaCross(Strategy):  #this is a simple moving average strategy we used 20,200 as mention below
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

#Please make sure to update tests as appropriate.
```
## Hosting 
```heroku
with the help of proc file we host in Heroku 
web: sh setup.sh && streamlit run dataproject.py
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
