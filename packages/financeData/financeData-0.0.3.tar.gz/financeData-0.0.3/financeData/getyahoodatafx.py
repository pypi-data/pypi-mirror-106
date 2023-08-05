import  requests
import re
from json import loads
import time
from urllib.parse import urlencode
from pandas import to_datetime,DataFrame, isnull, notnull
from datetime import datetime
import numpy as np

class GetFXData():
    def __init__(self,symbol=None,start=None,end=None):
    
        self.symbol = symbol
        self.start = start
        self.end = end
        
        
    def getParameter(self):
        
         start=to_datetime(self.start)
         end = to_datetime(self.end)

         if isinstance(start, datetime):
             start = int(time.mktime(start.timetuple()))
         else:
             start = int(time.mktime(time.strptime(str(start), '%Y-%m-%d')))
        
         if isinstance(end, datetime):
             end = int(time.mktime(end.timetuple()))
         else:
             end = int(time.mktime(time.strptime(str(end), '%Y-%m-%d')))
        
        

         prepost = False
        
        
         params={
                      "period1": start,
                      "period2": end,
                      "interval": "1d",
                      "includePrePost": prepost,
                      "events" :"div,splits"
                     
                    }

         return params


    @property
    def url(self):
         return "https://query1.finance.yahoo.com/v8/finance/chart/{}=X"
    
    def GetUrl(self):
        return self.url.format(self.symbol)
    
    
    def GetResponse(self,url,params):
        session =requests.Session()
        response = session.get(url, params=params)
        if response.status_code == requests.codes.ok:
            return response    
        

                 
    def GetData(self):
        data = self.GetResponse(self.GetUrl(),self.getParameter())
        try:
          data = data.json()  
        except KeyError: 
            msg = "Data Fetch Error"
            
        timestamps = data["chart"]["result"][0]["timestamp"]
        prices = data["chart"]["result"][0]["indicators"]["quote"][0]
        opens = prices["open"]
        closes = prices["close"]
        lows = prices["low"]
        highs = prices["high"]
         
        pricesdf = DataFrame({"Open": opens,"High": highs,"Low": lows,"Close": closes}) 
        pricesdf.index = to_datetime(timestamps, unit="s")
        pricesdf.sort_index(inplace=True)
        pricesdf = np.round(pricesdf, data["chart"]["result"][0]["meta"]["priceHint"])
        pricesdf.index =pricesdf.index.tz_localize("UTC").tz_convert(data["chart"]["result"][0]["meta"]["exchangeTimezoneName"])
        pricesdf.index= to_datetime(pricesdf.index.date)

        return pricesdf
         
                          
                 
                 
                 
                 
                 
                 
                 