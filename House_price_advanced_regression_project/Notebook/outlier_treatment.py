import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv ("train.csv")

def p_outliers (df, cols, uv_f = 3, lv_f = 0.3):
    for col in cols:
        uv = np.percentile (df[col], [99])[0] * uv_f
        lv = np.percentile (df[col], [1])[0] * lv_f
        return "\nlower_limit: {} \nupper_limit: {} \n\n\n".format (lv, uv)
        #return "upper_limit: {} \n\n\n".format (uv)


def iqr_outliers (df, cols, factor = 1.5):
    for col in cols:
        q1 = df[col].quantile (0.25)
        q3 = df[col].quantile (0.75)
        iqr = q3 - q1
        upper_limit = q3 + (iqr * factor)
        lower_limit = q1 - (iqr * factor)
        #print (cols.columns)
        return "lower_limit: {} \nupper_limit: {} \n\nMin: {} \nMax: {}\n\n\n {}\n".format (lower_limit ,upper_limit, df[col].min (),df[col].max(), df[col].describe ())
        #return "Min: {} \nMax: {}\n\n".format (df[col].min (), df[col].max ())
        #return "upper_limit:  " + str (upper_limit) + "\n\n\n"
        
def view (df, cols, c = "green", b = 30):
    for col in cols:
        return "this is the histogram {} \n\n".format (plt.hist (df[col], color = c, bins = b))
    return plt.show ()
## Outlier treatment using percentile
        
#columns = df.iloc [:, [4]]
#print (columns)
#print (iqr_outliers(df, columns))



#a = p_outliers(df, columns)


