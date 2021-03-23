# Use Neptune API to log your first run

# Before you start

get_ipython().system(' pip install --quiet git+https://github.com/neptune-ai/neptune-client.git@alpha')

get_ipython().system(' pip install --upgrade --quiet git+https://github.com/neptune-ai/neptune-client.git@alpha')

# Step 1: Initialize Neptune and create new run

import neptune.new as neptune

run = neptune.init(project='common/quickstarts',
                   api_token='ANONYMOUS')

# Step 2 - Log metrics during training

import numpy as np
from time import sleep

# log score
run['single_metric'] = 0.62

for i in range(100):
    sleep(0.2) # to see logging live
    run['random_training_metric'].log(i * np.random.random())
    run['other_random_training_metric'].log(0.5 * i * np.random.random())

# tests
run.wait()

# check score
sm = 0.62

assert run['single_metric'].get() == sm, 'Expected: {}, Actual: {}'.format(sm, run['single_metric'].get())

# check metrics
assert isinstance(run['random_training_metric'].get_last(), float), 'Incorrect metric type'
assert isinstance(run['other_random_training_metric'].get_last(), float), 'Incorrect metric type'