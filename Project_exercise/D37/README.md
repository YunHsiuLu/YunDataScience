# D37: EDA missing value and abnormal value advanced repair strategy
Here we have a data with sex, age, height, and weight. If there are some missing value, we need to repair them with some strategies, like mean value repairing.<br>
But sometimes the result is not agreed with some truth, for example someone is 176 cm tall, but the repair weight is 47kg by mean value. It's weird, right? Is there a better strategy?<br>
* * *
# K-Nearest Neighbor (KNN)
It's a non-probability distribution algorithm, estimate the missing value with the nearest k values.<br>
![plot](Fig1.png)

because KNN is using majority decision, so it's better to choose odd "k".<br>
* * *
# KNN three steps
1. calculate the distance<br>
	there are two definitions of distance:<br>
		with two point <img src="http://latex.codecogs.com/svg.latex?A=(x_1, ..., x_n)" /> and <img src="http://latex.codecogs.com/svg.latex?B=(y_1, ..., y_n)" /><br>
		- Euclidean distance:<br>
			<img src="http://latex.codecogs.com/svg.latex?D=\sqrt{\sum^n_{i=1}(x_i-y_i)}" /><br>
		- Manhattan distance:<br>
			<img src="http://latex.codecogs.com/svg.latex?D=\sum^n_{i=1}|x_i-y_i|" /><br>
	we use Euclidean distance in this lecture.<br>
2. find the nearest k values<br>
3. majority decision with those data<br>










