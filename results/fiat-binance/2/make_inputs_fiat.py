import numpy as np
from math import log10
import json
import itertools
from copy import copy


X = np.logspace(log10(7), log10(10000), 32)
Xname = "A"
Y = np.logspace(log10(1e-8), log10(1e-4), 32)
Yname = "gamma"

other_params = dict(
    D=10e6,
    adjustment_step=1.5e-5,
    fee_gamma=2e-8,
    ma_half_time=600,
    mid_fee=3e-5,
    out_fee=6e-5,
    n=2,
    log=0,
    price_threshold=1.5e-5,
    gamma=1.4e-8,
    ext_fee=0.0,
    A=100.0)

config = {
    'configuration': [],
    'datafile': [
        'eurusdt'],
    'debug': 0}

for x, y in itertools.product(X, Y):
    params = copy(other_params)
    params[Xname] = x
    params[Yname] = y
    if Xname == 'mid_fee':
        other_params['price_threshold'] = x / 2
        other_params['adjustment_step'] = x / 2
    config['configuration'].append(params)

with open('configuration.json', 'w') as f:
    json.dump(config, f)
