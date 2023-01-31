

# Don't read this file before solving the tasks in script1.

import numpy as np
import pandas as pd
def rw(start):
    x = np.cumsum(np.random.normal(size=10))
    return start + np.round(x,1)
np.random.seed(12345)

walk = pd.DataFrame({'rw20':rw(20),'rw60':rw(60),'rw80':rw(80)})
walk.rw20[5] = None
walk.rw60[5:7] = None
walk.rw80[5:8] = None
