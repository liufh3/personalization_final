from fastFM import als
fm = als.FMRegression(n_iter=1000, init_stdev=0.1,rank = 2, l2_reg_w = 0.1, l2_reg_V = 0.5)
