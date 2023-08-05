Financedata allows you to extract daily financial data from yahoo.

Other sources will be added in the future.
===========================================================

Quick Start

Fetching Currency data



from DataFinder import data
df = data.financeFXData(
                    "USDTRY", ##Symbol
                    "2021-01-01", ##Start Date
                    "2021-05-11") ##End Date
					
					
df = data.financeFXData(##Symbol,##Start Date,##End Date) 

==============================
Fetching Stock data

df = data.financeData(
                    "TSLA",         
                    "NASDAQ",       
                    "2021-01-01",   
                    "2021-05-11")   
                    
df = data.financeData(##Symbol,##Stock Market,##Start Date,##End Date)   					
                    
*For BIST companies

df = data.financeData(
                    "CCOLA",         ##Symbol
                    "Bist",       ##Stock Market
                    "2021-01-01",   ##Start Date
                    "2021-05-11")   ##End Date
                    
df = data.financeData(##Symbol,"Bist",##Start Date,##End Date )                     
					
					
==============================

Get Companies Some Statistics

df = data.financeStockStat("TSLA","NASDAQ")

df = data.financeStockStat(##Symbol,##Stock Market)

==============================  