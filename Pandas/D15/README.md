# D15: Pandas Split-Apply-Combine Strategy

*	groupby(): we can use groupby() to simplize the purpose we want, here is the example:<br>
if we want to get the boys' mean score, we will do like this from score_df:

```
boy_score_df = score_df.loc[score_df.sex == 'boy']
print(boy_score_df.mean())
```

but we can also do in this simple way:

```
score_df.groupby('sex').mean()
```

then it will return the dataframe with mean value of each column.

the way above we call: Split-Apply-Combine strategy. We split original data frame into small data frame, apply the analysis method, then combine each result of small data frame.

*	if we add multi-column into groupby, `groupby(['sex', 'class'])` for example, then it returns a multi-index data frame.

*	we can also do multi-analysis on the data frame by agg() function: `df.groupy([multi column]).agg([multi logical calculate])`, like 'mean', 'min', 'max', etc. For example:<br>
```
df.groupby(['sex', 'class']).agg(['min', 'max'])
```









