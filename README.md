### Date created: 2018-11-16

### Bikeshare Data Analyzer

### Description

A Python utility that analyzes data on bikesharing programs in Chicago, New York City, and Washington D.C., allowing users to filter data in various ways and generate visualizations of subsets of the data.

### Files used

bikeshare_2.py <br />
chicago.csv <br />
new_york_city.csv <br />
washington.csv <br />
README.md <br />
LICENSE <br />
requirements.txt <br />
.gitignore

Note that, due to their large size, the CSV files are not included in this repo. The most up-to-date data files are available for download [here](https://s3.amazonaws.com/capitalbikeshare-data/index.html).

### Credits

- `getch` for single character user input: https://stackoverflow.com/questions/510357/python-read-a-single-character-from-the-user

- To convert a list of integers to a list of strings, I adapted this (which works the other way around): https://stackoverflow.com/questions/7368789/convert-all-strings-in-a-list-to-int#7368801

- `groupby` and `idxmax` for calculating the most frequent combination of adjacent values across two dataframe columns: https://stackoverflow.com/questions/53037698/how-can-i-find-the-most-frequent-two-column-combination-in-a-dataframe-in-python

- `plotly` for creating interactive line charts of data:
	- https://plot.ly/pandas/line-charts/
	- https://plot.ly/python/figure-labels/
