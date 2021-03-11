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
		with two point <img src="http://latex.codecogs.com/svg.latex?A=(x_1,&space;...,&space;x_n)&space;and&space;B=(y_1,&space;...,&space;y_n)" /><br>
		- Euclidean distance:<br>
			<img src="http://latex.codecogs.com/svg.latex?D=\sqrt{\sum_{i=1}^n(x_i-y_i)}" /><br>
		- Manhattan distance:<br>
			<img src="http://latex.codecogs.com/svg.latex?D=\sum_{i=1}^n|x_i-y_i|" /><br>
	we use Euclidean distance in sklearn package in this lecture.<br>
2. find the nearest k values<br>
3. majority decision with those data<br>
(here ignore the coding part, you can check in exercise)<br>

* * *
when we repair the missing value, we can just use the nearest data to repair the missing one<br>
but in some situation, like boys' and girls' height, we can't use boys' height to estimate girls' height<br>
so maybe we should choose the other arguments to correct this error.<br>

* * *
# How do we check repair value is good or not?
we can use mean square error (MSE) to check whether the repair value is good.<br>
Small MSE means high accuracy.<br>




