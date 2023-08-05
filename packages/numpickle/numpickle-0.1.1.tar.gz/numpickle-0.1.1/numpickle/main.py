import pandas as pd
import numpy as np
import pickle

def save_numpickle(df, outfpath):
    arr, colnames, rownames = df.to_numpy(), df.columns, df.index
    np.save(arr=arr, file=outfpath)
    pickle.dump({'colnames': colnames, 'rownames': rownames}, 
                open(outfpath + ".pckl", "wb"))

def load_numpickle(fpath):
    df = pd.DataFrame(np.load(fpath))
    with open(fpath + ".pckl", "rb") as fin:
        meta = pickle.load(fin)
    df.index, df.columns = meta['rownames'], meta['colnames']
    return df
