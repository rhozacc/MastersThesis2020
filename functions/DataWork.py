# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np



def PairUp1 (ETF, UI):
    pair = pd.merge(ETF, UI, how='inner', left_index=True, right_index=True)
    pair.dropna(inplace=True)
    
    # Discard anomalies
    pair = pair[(pair["Return_x"] < 0.5) & (pair["Return_x"] > -0.5)]
    pair["DIFF"] = pair["lnClose_y"] - pair["lnClose_x"]
    pair["GAP"] = np.abs(pair["lnReturn_y"] - pair["lnReturn_x"])
    
    # Indices
    pair["Close_x_INDEX"] = pair["Close_x"]/pair["Close_x"][0]
    pair["Close_y_INDEX"] = pair["Close_y"]/pair["Close_y"][0]
    
    return pair



def PairUp2 (pairs, data_world, detrend=True):
    pairs2 = []
    dw = pd.DataFrame()
    
    dw["lnReturn_world"] = data_world[0]["lnReturn"]
    
    for i, pair in enumerate(pairs):
    
        pair2 = pd.merge(pair, dw, how="inner", left_index=True, right_index=True)
        pairs2.append(pair2)
    
    return pairs2





def GetPairs (data_etf, data_ui):
    if len(data_etf) == len(data_ui):
        pairs = [PairUp1(data_etf[i], data_ui[i]) for i, _ in enumerate(data_etf)]
    return(pairs)
 
    


# TO-DO [0] will still cut index at the first entry, not Dmin
def DateCUT (pairs, Dmin=None, Dmax=None):
    new = []
    for i, pair in enumerate(pairs):
        new.append(pair.loc[Dmin:Dmax])
        pair["Close_x_INDEX"] = pair["Close_x"]/pair["Close_x"][0]
        # pair["Close_y_INDEX"] = pair["Close_y"]/pair["Close_y"][0]
    return new




