import pandas as pd
data = pd.read_stata('bruhn_gallego_data_restat.dta')
data.to_csv('regional_stats.csv')