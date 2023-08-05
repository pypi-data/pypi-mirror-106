import  requests
import re
from json import loads
import time
from urllib.parse import urlencode
from pandas import to_datetime,DataFrame, isnull, notnull

class GetStatData():
    def __init__(self,symbol=None,market=None):

        self.symbol = symbol
        self.market = market
        
     
        if self.market == "Bist":
            self.symbol = symbol + '.IS'
        else:
            self.symbol = symbol
            
    def getParameter(self):

     
        params={
                      
                      "filter": "history",
                      "symbol": self.symbol,
                     
                    }
        return params   
    
    @property
    def url(self):
        return "https://finance.yahoo.com/quote/{}/key-statistics"
    

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
        except KeyError:    
            msg = "Error While Fetching Price" 
        try:
             trailingPE = j["context"]["dispatcher"]["stores"]["QuoteSummaryStore"]["summaryDetail"]["trailingPE"]["fmt"]
        except:    
            trailingPE = "-" 
        try:
            forwardPE = j["context"]["dispatcher"]["stores"]["QuoteSummaryStore"]["summaryDetail"]["forwardPE"]["fmt"]
        except:
            forwardPE = "-" 
        try:
            enterpriseValue = j["context"]["dispatcher"]["stores"]["QuoteSummaryStore"]["defaultKeyStatistics"]["enterpriseValue"]["fmt"]
        except KeyError:    
            enterpriseValue = "-"     
        try:
            pegRatio5yrexpected= j["context"]["dispatcher"]["stores"]["QuoteSummaryStore"]["defaultKeyStatistics"]["pegRatio"]["fmt"]
        except KeyError:    
            pegRatio5yrexpected = "-"  
        try:
            pricetoSales = j["context"]["dispatcher"]["stores"]["QuoteSummaryStore"]["summaryDetail"]["priceToSalesTrailing12Months"]["fmt"]
        except KeyError:    
            pricetoSales = "-"  
        try:
            pricetoBook = j["context"]["dispatcher"]["stores"]["QuoteSummaryStore"]["defaultKeyStatistics"]["priceToBook"]["fmt"]
        except KeyError:    
            pricetoBook = "-"  
        try:
            enterpriseValueRevenue = j["context"]["dispatcher"]["stores"]["QuoteSummaryStore"]["defaultKeyStatistics"]["enterpriseToRevenue"]["fmt"]
        except KeyError:    
            enterpriseValueRevenue = "-"              
        try:
            enterpriseToEbitda = j["context"]["dispatcher"]["stores"]["QuoteSummaryStore"]["defaultKeyStatistics"]["enterpriseToEbitda"]["fmt"]  
        except KeyError:    
            enterpriseToEbitda = "-"             
            
            
         
        valuationMeasuresdf = DataFrame({ "Enterprise Value":enterpriseValue,
                                  "Trailing P/E":trailingPE,
                                 "Forward P/E":forwardPE,
                                 "PEG Ratio (5 yr expected)":pegRatio5yrexpected,
                                 "Price/Sales (ttm)":pricetoSales,
                                 "Price/Book (mrq)":pricetoBook,
                                 "Enterprise Value/Revenue":enterpriseValueRevenue,
                                 "Enterprise Value/EBITDA":enterpriseToEbitda
            
                                },index=[self.symbol[:-3]])
        
        return valuationMeasuresdf
        
        
