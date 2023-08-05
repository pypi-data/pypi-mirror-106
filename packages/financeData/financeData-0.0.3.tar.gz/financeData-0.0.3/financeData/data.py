# -*- coding: utf-8 -*-
"""
Created on Tue May 11 17:41:38 2021

@author: Berkay
"""

from . import GetStockData,GetFXData,GetStatData



def financeData(symbol,stockmarket=None,start=None,end=None):
    
    data_source="yahoo"
    
    
    if data_source != 'yahoo':
        msg = "Only yahoo available.Please try again next time." 
        raise NotImplementedError(msg)
    
    if data_source == "yahoo":
        return GetStockData(symbol = symbol,
                            market = stockmarket,
                            start =start,
                            end = end).GetData()
    
    
    
def financeFXData(symbol,start=None,end=None):
    return GetFXData(symbol = symbol,
                            start =start,
                            end = end).GetData()  



def financeStockStat(symbol,stockmarket=None):
    
    data_source="yahoo"
    if data_source != 'yahoo':
        msg = "Only yahoo available.Please try again next time." 
        raise NotImplementedError(msg)
    
    if data_source == "yahoo":
        return GetStatData(symbol = symbol,
                            market = stockmarket
                            ).GetData()    