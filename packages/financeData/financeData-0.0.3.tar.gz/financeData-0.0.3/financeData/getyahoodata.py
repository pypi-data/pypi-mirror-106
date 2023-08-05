import  requests
import re
from json import loads
import time
from urllib.parse import urlencode
from pandas import to_datetime,DataFrame, isnull, notnull

class GetStockData():
    def __init__(self,symbol=None,market=None,start=None,end=None):

        self.symbol = symbol
        self.market = market
        self.start = start
        self.end = end
     
        if self.market == "Bist":
            self.symbol = symbol + '.IS'
        else:
            self.symbol = symbol
            
    def getParameter(self):
        end = to_datetime(self.end)
        start=to_datetime(self.start)
        four_hours_in_seconds = 14400
        unix_start = int(time.mktime(start.timetuple()))
        unix_start += four_hours_in_seconds
        day_end = end.replace(hour=23, minute=59, second=59)
        unix_end = int(time.mktime(day_end.timetuple()))
        unix_end += four_hours_in_seconds
     
        params={
                      "period1": unix_start,
                      "period2": unix_end,
                      "interval": "1d",
                      "frequency": "1d",
                      "filter": "history",
                      "symbol": self.symbol,
                     
                    }
        return params   
    
    @property
    def url(self):
        return "https://finance.yahoo.com/quote/{}/history"
    

    def GetUrl(self):
        return self.url.format(self.symbol)
        
    
    def GetResponse(self,url,params):
         retry_count=3
         session =requests.Session()
         timeout=30
         pause=0.1
         last_response_text = ""
         headers = None
         
         for _ in range(retry_count + 1):
             response = session.get(url, params=params, headers=headers, timeout=timeout)
             if response.status_code == requests.codes.ok:
                 return response

             if response.encoding:
                 last_response_text = response.text.encode(response.encoding)
                 time.sleep(pause)
             if params is not None and len(params) > 0:
                 url = url + "?" + urlencode(params)
                 
             msg = "Cannot read URL".format(url)
             if last_response_text:
                 msg += "\Text:\n{0}".format(last_response_text)    
            
    def GetData(self):
        response = self.GetResponse(self.GetUrl(),self.getParameter())
        patern = r"root\.App\.main = (.*?);\n}\(this\)\);"
        try:
            j = loads(re.search(patern,response.text,re.DOTALL).group(1))
            data = j["context"]["dispatcher"]["stores"]["HistoricalPriceStore"]
        except KeyError:    
            msg = "Error While Fetching Price"
        prices = DataFrame(data["prices"])
        prices.columns = [col.capitalize() for col in prices.columns]   
        prices["Date"] = to_datetime(to_datetime(prices["Date"], unit="s").dt.date)
        if "Data" in prices.columns:
            prices = prices[prices["Data"].isnull()]
        prices = prices[["Date", "High", "Low", "Open", "Close", "Volume", "Adjclose"]]
        
        prices = prices.rename(columns={"Adjclose": "Adj Close"})
        prices = prices.set_index("Date")
        prices = prices.sort_index().dropna(how="all")    
        return prices
         
        ##Divindends eklenecek 
         
         
         
         
         
