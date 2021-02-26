# D28: Describe the world by possibility distribution - discrete distribution(2)

# Negative Binomial Distribution(NB)
we have binomial distribution(B) last lecture, and there is negative binomial distribution(NB), meaning that the distribution of fail times when a set of Bernoulli experiments achieve success times.<br>
For example, we want red point of a dice, we might throw once with 1(red), or throw three times with 6(black), 5(black), 4(red). Them the NBD is 1, 3.<br>
The equation is:<br>
<img src="https://latex.codecogs.com/gif.latex?P(X&space;=&space;x)&space;=&space;C^{x-1}_{k-1}&space;p^k&space;(1-p)^{x-k}" /><br>
<img src="https://latex.codecogs.com/gif.latex?x&space;=&space;k,&space;k+1,&space;k+2,&space;..." /><br>
* * *
# Hypergeometric Distribution(HG)
It represents that how many time we need when we get the success event from a limit set. The equation is:<br>
<img src="https://latex.codecogs.com/gif.latex?P(X&space;=&space;x)&space;=&space;\frac{\binom{K}{x}\binom{N-K}{n-x}}{\binom{N}{n}}" /><br>
It can be seen as we select a sample which agreed with the condition. Take the example: choose 10 times(n) results from 50 times(N) results, we ask for 3 times(x) success in choosing sample.<br>

