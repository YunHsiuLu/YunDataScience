# D11: Pandas Classification and Missing Value
we need to classify the data by their attribution, like colors, sexual, identity number, etc. We can separate them into roughly two kinds: order and general.<br>
Most of model are based on mathmetical calculation, but we can't do calculation on string, so we need to encoding, means that make all the classification data into numbers.

*	we can use LabelEncoder() in sklearn library for order encoding. use LabelEncoder() to make string data become order data, then we can easily analyze them.
*	we don't need order encoding for general data, so we can just use get_dummies() in pandas. we can add columns to represent their attributions. We usually call this one-by-one relation	'One-hot Encoding'.

[Most here](https://medium.com/@PatHuang/%E5%88%9D%E5%AD%B8python%E6%89%8B%E8%A8%98-3-%E8%B3%87%E6%96%99%E5%89%8D%E8%99%95%E7%90%86-label-encoding-one-hot-encoding-85c983d63f87)

* * *

data missing is very important we need to know because it often happenes. when we have data loss, we will replace them with NaN; but most of model can't deal with the NaN. In general, we delete the whole missing data, but it will miss other column data, so we tend to repair the data and there are two way for repair: constant repair and former or latter repair. 

*	constant value repair: df.fillna(). Replace all NaN with a constant, like 0.0, mean value, median value, etc. 
	`data.fillna(0.)`, `data.fillna(data.column_name.mean())`, `data.fillna(data.column_name.median())`
*	former or latter repair: `df.fillna(method='ffill')` or `df.fillna(method='bfill')`