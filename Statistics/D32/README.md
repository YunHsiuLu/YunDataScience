# D32: A/B assumption - advanced

when we check the sample with A or B result, we can assume H_0 by H_1 in several ways; here introduce chi-square distribution and Student's t distribution<br>

* * *
# Chi-Square distribution
<img src="http://latex.codecogs.com/svg.latex?X&space;~&space;\chi^2(k)" />
, where k is degree of freedom
it compares the difference of experiment results and expect results, if it has large difference, <img src="http://latex.codecogs.com/svg.latex?\chi^2(k)" /> would be large.<br>
it has a simple form: <img src="http://latex.codecogs.com/svg.latex?\chi^2(k)=\sum_{k}^{i=1}\frac{(A_i-np_i)^2}{np_i}" /><br>

* * *
# Student's t distribution
it is mainly used at few samples and unknown sigma positive distribution. Because of unknown sigma, we need to assume a <img src="http://latex.codecogs.com/svg.latex?S_n" /> to represent the sigma.<br>
<img src="http://latex.codecogs.com/svg.latex?t=\frac{\bar{X}-\mu}{S_n/\sqrt{n}}" /><br>
it compares to the normal distribution: <img src="http://latex.codecogs.com/svg.latex?Z=\frac{\bar{X}-\mu}{\sigma/\sqrt{n}}" /><br>
when n is large, t is approach to Z, where the degree of freedom is n-1.