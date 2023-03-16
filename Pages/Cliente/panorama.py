# Importando bibliotecas
import pandas as pd
import streamlit as st
import numpy as np
from datetime import date
import time
import yfinance as yf
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns


fear_and_greed = """

<img src="https://alternative.me/crypto/fear-and-greed-index.png" alt="Latest Crypto Fear & Greed Index" />

"""

eua_widget = """

    <!-- TradingView Widget BEGIN -->
    <div class="tradingview-widget-container">
    <div class="tradingview-widget-container__widget"></div>
    <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-market-overview.js" async>
    {
    "colorTheme": "dark",
    "dateRange": "12M",
    "showChart": false,
    "locale": "en",
    "largeChartUrl": "",
    "isTransparent": true,
    "showSymbolLogo": true,
    "showFloatingTooltip": true,
    "width": "100%",
    "height": "400",
    "tabs": [
        {
        "title": "Indices",
        "symbols": [
            {
            "s": "INDEX:DXY"
            },
            {
            "s": "OANDA:SPX500USD"
            },
            {
            "s": "NASDAQ:NDX"
            },
            {
            "s": "FOREXCOM:DJI"
            },
            {
            "s": "CAPITALCOM:RTY"
            },
            {
            "s": "CAPITALCOM:VIX"
            }
        ],
        "originalTitle": "Indices"
        }
    ]
    }
    </script>
    </div>
    <!-- TradingView Widget END -->
"""

europa_widget = """
<!-- TradingView Widget BEGIN -->
<div class="tradingview-widget-container">
<div class="tradingview-widget-container__widget"></div>
<script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-market-overview.js" async>
{
"colorTheme": "dark",
"dateRange": "12M",
"showChart": false,
"locale": "en",
"largeChartUrl": "",
"isTransparent": true,
"showSymbolLogo": true,
"showFloatingTooltip": true,
"width": "100%",
"height": "400",
"tabs": [
    {
    "title": "Indices",
    "symbols": [
        {
        "s": "FXOPEN:ESX50"
        },
        {
        "s": "VANTAGE:DAX40"
        },
        {
        "s": "GLOBALPRIME:ES35"
        },
        {
        "s": "INDEX:CAC40"
        },
        {
        "s": "VANTAGE:FTSE100"
        },
        {
        "s": "INDEX:SMI"
        }
    ],
    "originalTitle": "Indices"
    }
]
}
</script>
</div>
<!-- TradingView Widget END -->
"""

asia_widget = """

<!-- TradingView Widget BEGIN -->
<div class="tradingview-widget-container">
<div class="tradingview-widget-container__widget"></div>
<script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-market-overview.js" async>
{
"colorTheme": "dark",
"dateRange": "12M",
"showChart": false,
"locale": "en",
"largeChartUrl": "",
"isTransparent": true,
"showSymbolLogo": true,
"showFloatingTooltip": true,
"width": "100%",
"height": "400",
"tabs": [
{
  "title": "Indices",
  "symbols": [
    {
      "s": "HSI:HSI"
    },
    {
      "s": "SPREADEX:AUS"
    },
    {
      "s": "BSE:SENSEX"
    },
    {
      "s": "HNX:HNXINDEX"
    },
    {
      "s": "SKILLING:CHINA50"
    },
    {
      "s": "INDEX:STI"
    }
  ],
  "originalTitle": "Indices"
}
]
}
</script>
</div>
<!-- TradingView Widget END -->

"""

commodity_widget = """

<!-- TradingView Widget BEGIN -->
<div class="tradingview-widget-container">
<div class="tradingview-widget-container__widget"></div>
<script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-market-overview.js" async>
{
"colorTheme": "dark",
"dateRange": "12M",
"showChart": false,
"locale": "en",
"largeChartUrl": "",
"isTransparent": true,
"showSymbolLogo": true,
"showFloatingTooltip": true,
"width": "100%",
"height": "400",
"tabs": [
{
  "title": "Futures",
  "symbols": [
    {
      "s": "COMEX:GC1!",
      "d": "Gold"
    },
    {
      "s": "NYMEX:CL1!",
      "d": "Crude Oil"
    },
    {
      "s": "NYMEX:NG1!",
      "d": "Natural Gas"
    },
    {
      "s": "CBOT:ZC1!",
      "d": "Corn"
    },
    {
      "s": "CBOT:ZS1!"
    },
    {
      "s": "COMEX:TIO1!"
    }
  ],
  "originalTitle": "Futures"
}
]
}
</script>
</div>
<!-- TradingView Widget END -->


"""

cripto_widget = """
<!-- TradingView Widget BEGIN -->
<div class="tradingview-widget-container">
<div class="tradingview-widget-container__widget"></div>
<script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-market-overview.js" async>
{
"colorTheme": "dark",
"dateRange": "12M",
"showChart": false,
"locale": "en",
"largeChartUrl": "",
"isTransparent": true,
"showSymbolLogo": true,
"showFloatingTooltip": true,
"width": "100%",
"height": "500",
"tabs": [
{
  "title": "Indices",
  "symbols": [
    {
      "s": "BINANCE:BTCUSDT"
    },
    {
      "s": "BINANCE:ETHUSDT"
    },
    {
      "s": "BINANCE:ADAUSDT"
    },
    {
      "s": "BINANCE:BNBUSDT"
    },
    {
      "s": "BINANCE:AGIXUSDT"
    },
    {
      "s": "KUCOIN:SDAOUSDT"
    },
    {
      "s": "BINANCE:APEUSDT"
    },
    {
      "s": "BINANCE:GMXUSDT"
    }
  ],
  "originalTitle": "Indices"
}
]
}
</script>
</div>
<!-- TradingView Widget END -->

"""

cripto_widget1 = """
<!-- TradingView Widget BEGIN -->
<div class="tradingview-widget-container">
<script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-market-overview.js" async>
{
"colorTheme": "dark",
"dateRange": "12M",
"showChart": false,
"locale": "en",
"largeChartUrl": "",
"isTransparent": true,
"showSymbolLogo": true,
"showFloatingTooltip": true,
"width": "100%",
"height": "1600",
"tabs": [
{
  "title": "Indices",
  "symbols": [
    {
      "s": "BINANCE:BTCUSDT"
    },
    {
      "s": "BINANCE:ETHUSDT"
    },
    {
      "s": "BINANCE:ADAUSDT"
    },
    {
      "s": "BINANCE:BNBUSDT"
    },
    {
      "s": "BINANCE:AGIXUSDT"
    },
    {
      "s": "KUCOIN:SDAOUSDT"
    },
    {
      "s": "BINANCE:MATICUSDT"
    },
    {
      "s": "BINANCE:SNXUSDT"
    },
    {
      "s": "BINANCE:CRVUSDT"
    },
    {
      "s": "BINANCE:GMXUSDT"
    },
    {
      "s": "LINKUSDT"
    },
    {
      "s": "BINANCE:LDOUSDT"
    },
    {
      "s": "BINANCE:APEUSDT"
    },
    {
      "s": "BINANCE:PAXGUSDT"
    },
    {
      "s": "BINANCE:SOLUSDT"
    },
    {
      "s": "BINANCE:DOTUSDT"
    },
    {
      "s": "BINANCE:TRXUSDT"
    },
    {
      "s": "BINANCE:CHZUSDT"
    },
    {
      "s": "BINANCE:ZILUSDT"
    },
    {
      "s": "BINANCE:1INCHUSDT"
    },
    {
      "s": "BINANCE:DYDXUSDT"
    },
    {
      "s": "BINANCE:OPUSDT"
    },
    {
      "s": "BINANCE:MKRUSDT"
    }
    
  ],
  "originalTitle": "Indices"
}
]
}
</script>
</div>
<!-- TradingView Widget END -->

"""

cripto_widget2 = """
<!-- TradingView Widget BEGIN -->
<div class="tradingview-widget-container">
<div class="tradingview-widget-container__widget"></div>
<script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-market-overview.js" async>
{
"colorTheme": "dark",
"dateRange": "12M",
"showChart": false,
"locale": "en",
"largeChartUrl": "",
"isTransparent": true,
"showSymbolLogo": true,
"showFloatingTooltip": true,
"width": "100%",
"height": "1600",
"tabs": [
{
  "title": "Indices",
  "symbols": [
    {
      "s": "BINANCE:UNIUSDT"
    },
    {
      "s": "BINANCE:LTCUSDT"
    },
    {
      "s": "BINANCE:FILUSDT"
    },
    {
      "s": "BINANCE:APTUSDT"
    },
    {
      "s": "BINANCE:XLMUSDT"
    },
    {
      "s": "BINANCE:NEARUSDT"
    },
    {
      "s": "OKX:CROUSDT"
    },
    {
      "s": "BINANCE:HBARUSDT"
    },
    {
      "s": "BINANCE:VETUSDT"
    },
    {
      "s": "BINANCE:ICPUSDT"
    },
    {
      "s": "BINANCE:ALGOUSDT"
    },
    {
      "s": "BINANCE:QNTUSDT"
    },
    {
      "s": "BINANCE:GRTUSDT"
    },
    {
      "s": "BINANCE:STXUSDT"
    },
    {
      "s": "BINANCE:FTMUSDT"
    },
    {
      "s": "BINANCE:EOSUSDT"
    },
    {
      "s": "BINANCE:MANAUSDT"
    },
    {
      "s": "BINANCE:AAVEUSDT"
    },
    {
      "s": "BINANCE:XTZUSDT"
    },
    {
      "s": "BINANCE:IMXUSDT"
    },
    {
      "s": "BINANCE:AXSUSDT"
    },
    {
      "s": "BINANCE:SANDUSDT"
    },
    {
      "s": "KUCOIN:KCSUSDT"
    }
  ],
  "originalTitle": "Indices"
}
]
}
</script>
</div>
<!-- TradingView Widget END -->

"""

forex_widget = """
<!-- TradingView Widget BEGIN -->
<div class="tradingview-widget-container">
  <div class="tradingview-widget-container__widget"></div>
  <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-market-overview.js" async>
  {
  "colorTheme": "dark",
  "dateRange": "12M",
  "showChart": false,
  "locale": "en",
  "largeChartUrl": "",
  "isTransparent": true,
  "showSymbolLogo": true,
  "showFloatingTooltip": false,
  "width": "100%",
  "height": "500",
  "tabs": [
    {
      "title": "Forex",
      "symbols": [
        {
          "s": "FX:EURUSD",
          "d": "EUR/USD"
        },
        {
          "s": "FX:GBPUSD",
          "d": "GBP/USD"
        },
        {
          "s": "FX:USDJPY",
          "d": "USD/JPY"
        },
        {
          "s": "FX:USDCHF",
          "d": "USD/CHF"
        },
        {
          "s": "FX_IDC:BRLUSD"
        },
        {
          "s": "FX_IDC:USDBRL"
        }
      ],
      "originalTitle": "Forex"
    }
  ]
}
  </script>
</div>
<!-- TradingView Widget END -->


"""

calendario_widget = """

<iframe src="https://sslecal2.investing.com?ecoDayFontColor=%23000000&columns=exc_flags,exc_importance,exc_actual,exc_forecast,exc_previous&features=datepicker,timezone&countries=110,17,29,25,32,6,37,36,26,5,22,39,14,48,10,35,7,43,38,4,12,72&calType=day&timeZone=12&lang=12"
width="100%" height="467" frameborder="0" allowtransparency="true" marginwidth="0" marginheight="0"></iframe>
"""

grafico_widget = """
<!-- TradingView Widget BEGIN -->
<div class="tradingview-widget-container">
  <div id="tradingview_13d9d"></div>
  <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
  <script type="text/javascript">
  new TradingView.widget(
  {
  "width": 450,
  "height": 600,
  "symbol": "INDEX:BTCUSD",
  "interval": "D",
  "timezone": "Etc/UTC",
  "theme": "dark",
  "style": "1",
  "locale": "en",
  "toolbar_bg": "#f1f3f6",
  "enable_publishing": false,
  "allow_symbol_change": true,
  "save_image": false,
  "container_id": "tradingview_13d9d"
}
  );
  </script>
</div>
<!-- TradingView Widget END -->
    """

btc_card_widget = """

<!-- TradingView Widget BEGIN -->
<div class="tradingview-widget-container">
  <div class="tradingview-widget-container__widget"></div>
  <div class="tradingview-widget-copyright"><a href="https://www.tradingview.com/symbols/BTCUSD/?exchange=INDEX" rel="noopener" target="_blank"><span class="blue-text">Bitcoin rates</span></a> by TradingView</div>
  <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-symbol-info.js" async>
  {
  "symbol": "INDEX:BTCUSD",
  "width": "100%",
  "locale": "en",
  "colorTheme": "dark",
  "isTransparent": true
}
  </script>
</div>
<!-- TradingView Widget END -->


"""  

spx_card_widget = """

<!-- TradingView Widget BEGIN -->
<div class="tradingview-widget-container">
  <div class="tradingview-widget-container__widget"></div>
  <div class="tradingview-widget-copyright"><a href="https://www.tradingview.com/symbols/FOREXCOM-SPXUSD/" rel="noopener" target="_blank"><span class="blue-text">SPXUSD quotes</span></a> by TradingView</div>
  <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-symbol-info.js" async>
  {
  "symbol": "FOREXCOM:SPXUSD",
  "width": "100%",
  "locale": "en",
  "colorTheme": "dark",
  "isTransparent": true
}
  </script>
</div>
<!-- TradingView Widget END -->


"""

dxy_card_widget = """

<!-- TradingView Widget BEGIN -->
<div class="tradingview-widget-container">
  <div class="tradingview-widget-container__widget"></div>
  <div class="tradingview-widget-copyright"><a href="https://www.tradingview.com/symbols/CAPITALCOM-DXY/" rel="noopener" target="_blank"><span class="blue-text">DXY quotes</span></a> by TradingView</div>
  <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-symbol-info.js" async>
  {
  "symbol": "CAPITALCOM:DXY",
  "width": "100%",
  "locale": "en",
  "colorTheme": "dark",
  "isTransparent": true
}
  </script>
</div>
<!-- TradingView Widget END -->


"""
  
  
  # Panorama -> Screener dos principais ativos e índices do mercado
def panorama():
    st.title("Panorama Do Mercado")
    

    geral, criptos, spx, cambio = st.tabs(["Geral", "Criptomoedas","EUA","Câmbio"])

    with geral:
      #Definindo layout 
      # PLOTANDO CRIPTOS

      col1, col2 = st.columns(2)

      with col1:
        st.subheader("Criptomoedas")
        st.components.v1.html(cripto_widget, height=360)

      with col2:
        st.subheader("Dólar")
        st.components.v1.html(forex_widget, height=360)

      col1, col2= st.columns(2)

      with col1:
        st.subheader("Comodities")
        st.components.v1.html(commodity_widget, height=360)
          

      with col2:
        st.subheader("EUA")
        st.components.v1.html(eua_widget, height=360)
      col1, col2= st.columns(2)
      
      with col1:
        st.subheader("Europa")
        st.components.v1.html(europa_widget, height=360)
          
      with col2:
        st.subheader("Ásia")
        st.components.v1.html(asia_widget, height=360)
          
      st.markdown("---")

      st.subheader("Calendário Econômico")
      st.components.v1.html(calendario_widget, height=500)


      st.components.v1.html(grafico_widget, height=700)
      
      st.markdown("---")

    with criptos:
        st.components.v1.html(btc_card_widget, height=180)
        col1, col2 = st.columns(2)

        with col1:
          st.components.v1.html(cripto_widget1, height=1400)

        with col2:
          st.components.v1.html(cripto_widget2, height=1450)

      
    
    with spx:
      st.components.v1.html(dxy_card_widget, height=160)
      st.components.v1.html(spx_card_widget, height=160)
      
      pass
    with cambio:
      pass