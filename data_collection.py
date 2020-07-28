# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 10:37:47 2020

@author: swapnil patel
"""

import glassdoor_scraper as gs
import pandas as pd

path= 'C:/Users/swapnil patel/Documents/ds_salary/chromedriver'

df = gs.get_jobs('data scientist',1000, False, path, 15)

df.to_csv('glassdoor_jobs.csv', index = False)