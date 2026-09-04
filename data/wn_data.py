import numpy as np
import pandas as pd

random = np.random.RandomState(1039834) 
ls_wn = [] 
cant = 0 
rng = np.random.default_rng()

for _ in range(4): 
    cant += 50 
    wn_df = pd.DataFrame({ 
        "ds": np.arange(1, cant + 1), 
        "white_noise": rng.normal(0,1,cant) }) 
    ls_wn.append(wn_df)
    wn_df.to_parquet(f"data/wn_{cant}.parquet", index=False)
