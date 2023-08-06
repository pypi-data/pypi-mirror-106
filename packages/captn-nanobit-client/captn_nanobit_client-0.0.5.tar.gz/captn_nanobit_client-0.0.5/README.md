# Capt'n AI for Nanobit
> Marketing campaigns optimization


## Install

`pip install captn-nanobit-client`

## How to use 


```python
from captn_nanobit_client.api import authorize, predict
from captn_nanobit_client.testing import get_test_dataframe

# server is one of "staging" or "production"
server = "staging"

token = authorize(username=username, password=password, server=server)
```

Get pandas dataframe

```python

df = get_test_dataframe()
```

Run the code below to make a prediction

```python
prediction = predict(df, token=token)
```
