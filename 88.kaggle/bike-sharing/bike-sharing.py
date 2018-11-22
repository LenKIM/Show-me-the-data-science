#!/usr/bin/python3

import numpy as np
import pandas as pd
import datetime
import csv
import seaborn as sns
import matplotlib.pyplot as plt

seed = 0
np.random.seed(seed)

# dataset = np.loadtxt('./bike-sharing/train.csv', dtype=str, delimiter=',', encoding='utf8')
dataset = pd.read_csv('./bike-sharing/train.csv', dtype=str, delimiter=',', encoding='utf8', skiprows=1, header=None)

print(dataset.head())

df = pd.DataFrame(dataset)
