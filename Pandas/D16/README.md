# D16: Pandas Time Order

*	Time data:<br>
df =

|     |     |
| :-- | --: |
| 2020-01-31 | 1.296478 |
| 2020-02-29 | 1.484486 |
| 2020-03-31 | -0.386317 |
| 2020-04-30 | -0.013741 |
| 2020-05-31 | -0.735426 |
| 2020-06-30 | 0.617767 |
| 2020-07-31 | 0.898438 |
| 2020-08-31 | 0.771031 |
| 2020-09-30 | 1.757624 |
| 2020-10-31 | -0.656737 |

`df.to_period(freq='Y')`

|     |     |
| :-- | --: |
| 2020 | 1.296478 |
| 2020 | 1.484486 |
| 2020 | -0.386317 |
| 2020 | -0.013741 |
| 2020 | -0.735426 |
| 2020 | 0.617767 |
| 2020 | 0.898438 |
| 2020 | 0.771031 |
| 2020 | 1.757624 |
| 2020 | -0.656737 |

`df.to_period(freq='M')`

|     |     |
| :-- | --: |
| 2020-01 | 1.296478 |
| 2020-02 | 1.484486 |
| 2020-03 | -0.386317 |
| 2020-04 | -0.013741 |
| 2020-05 | -0.735426 |
| 2020-06 | 0.617767 |
| 2020-07 | 0.898438 |
| 2020-08 | 0.771031 |
| 2020-09 | 1.757624 |
| 2020-10 | -0.656737 |

`df.to_period(freq='D')`

|     |     |
| :-- | --: |
| 2020-01-31 | 1.296478 |
| 2020-02-29 | 1.484486 |
| 2020-03-31 | -0.386317 |
| 2020-04-30 | -0.013741 |
| 2020-05-31 | -0.735426 |
| 2020-06-30 | 0.617767 |
| 2020-07-31 | 0.898438 |
| 2020-08-31 | 0.771031 |
| 2020-09-30 | 1.757624 |
| 2020-10-31 | -0.656737 |

`df.to_period(freq='H')`

|     |     |
| :-- | --: |
| 2020-01-31 00:00 | 1.296478 |
| 2020-02-29 00:00 | 1.484486 |
| 2020-03-31 00:00 | -0.386317 |
| 2020-04-30 00:00 | -0.013741 |
| 2020-05-31 00:00 | -0.735426 |
| 2020-06-30 00:00 | 0.617767 |
| 2020-07-31 00:00 | 0.898438 |
| 2020-08-31 00:00 | 0.771031 |
| 2020-09-30 00:00 | 1.757624 |
| 2020-10-31 00:00 | -0.656737 |

we can also find some certain time data by date or by month:<br>
`df['2020-03-31' : '2020-07-31']`<br>

|     |     |
| :-- | --: |
| 2020-03-31 | -0.386317 |
| 2020-04-30 | -0.013741 |
| 2020-05-31 | -0.735426 |
| 2020-06-30 | 0.617767 |
| 2020-07-31 | 0.898438 |

or if we want to change time period from a year to a season, we can use `resample` to change the period.<br>

```
>>> s = pd.Series([1, 2], index=pd.period_range('2018-01-01', freq='Y', periods=2))
>>> s
```
|     |     |
| :-- | --: |
| 2018 | 1 |
| 2019 | 2 |

`>>> s.resample('Q', convention='start').asfreq()`<br>

|     |     |
| :-- | --: |
| 2018Q1 | 1.0 |
| 2018Q2 | NaN |
| 2018Q3 | NaN |
| 2018Q4 | NaN |
| 2019Q1 | 2.0 |
| 2019Q2 | NaN |
| 2019Q3 | NaN |
| 2019Q4 | NaN |

when using `.shift()`, we can shift the date with argument.<br>
`df.shift(2, freq='D')`<br>

|     |     |
| :-- | --: |
| 2020-02-02 | 1.296478 |
| 2020-03-02 | 1.484486 |
| 2020-04-02 | -0.386317 |
| 2020-05-02 | -0.013741 |
| 2020-06-02 | -0.735426 |
| 2020-07-02 | 0.617767 |
| 2020-08-02 | 0.898438 |
| 2020-09-02 | 0.771031 |
| 2020-10-02 | 1.757624 |
| 2020-11-02 | -0.656737 |

we mentioned above is the date data with string, we can also set the date data by date type: `pd.Timestamp(year, month, day)`<br>

date and string can be transformed:<br>
`date2str = date.strftime(%Y-%m-%d)` or `str2date = pd.to_datetime(str)`<br>

* * *

* Timestampes functions:
`date = pd.Timestamp(2020,10,10)`<br>
	*	we can call year, month, date by: `date.year, date.month, date.day`; also the day name and week number: `date.day_name(), date.weekofyear`<br>
	*	time difference or time addition: <br>
	```
	>>> date1 = pd.Timestamp(2020,10,10)
	>>> date2 = pd.Timestamp(2020,11,10)
	>>> date2 - date1
	Timedelta('31 days 00:00:00')
	>>> date1 + pd.Timedelta(days=1)
	Timestamp('2020-10-11 00:00:00')
	```
	*	also calculate business days:
	```
	>>> two_business_days = 2 * pd.offsets.BDay()
	>>> date1_add_two_business_days = date1 + two_business_days
	>>> date1.day_name(), date1_add_two_business_days.day_name()
	('Saturday', 'Tuesday')
	```






















