import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")

# Custom functions
from functions.Bloomberg import BloombergTickers, GetDataBloomberg
from functions.YFinance import YFTickers, GetDataYF
from functions.DataWork import GetPairs
from functions.Econometrics import Regress1
from functions.Descriptives import DescriptivePlots, PairsDescriptiveInfo   
import functions.Plots as plots


importData = 0

####    IMPORT USING YF
# ETFs, UIs, MSCI = YFinance.YFTickers()
# data_etf, data_ui, data_world = YFinance.GetDataYF()


####     IMPORT USING BLOOMBERG EXPORT
if importData == 1:
    ETFs, UIs, MSCI = BloombergTickers()
    data_etf, data_ui, data_world = GetDataBloomberg("/Users/alenrozac/Desktop/Code/20200310 Bloomberg OHLCV.xlsx")
    pairs = GetPairs(data_etf, data_ui)




import functions.Plots as plots
# PairsDescriptiveInfo(pairs, ETFs, UIs, ProfileReport=True)
plots.Price(pairs, ETFs, UIs)
plots.PriceIndex(pairs, ETFs, UIs, paired=True)
plots.Returns(pairs, ETFs, UIs)
plots.ReturnsDist(pairs, ETFs, UIs, hist=False, xlim=(-0.05, 0.05))
plots.DiffGap(pairs, ETFs, UIs)
plots.Joint(pairs, ETFs, UIs)


# Econometrics
reg1, resids1 = Regress1(pairs, ETFs, UIs, plot=False)





# =============================================================================
#  TESTING / BUILDING





    
from statsmodels.tsa.vector_ar.vecm import coint_johansen
x = pairs[1][["Return_x", "Return_y"]] # dataframe of n series for cointegration analysis
jres = coint_johansen(x, det_order=0, k_ar_diff=1)










# =============================================================================
#  DUMP

# from functools import reduce
# df_merged = reduce(lambda left,right: pd.merge(left,right, how='inner', left_index=True, right_index=True), pairs)


# print(np.argmin([len(pair) for pair in pairs]))
# mindate = pairs[3].index[-1]

for pair in pairs:
    print(pair.index[0])

# maxdate = 

