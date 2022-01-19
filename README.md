# Data-Analysis-for-Hospitals-Jetbrains-Academy
This project jetbrains academy https://hyperskill.org/projects/152

## Work on project. Stage 1/5: Upload the data
### Objectives

In this stage, your program should:

1. After all the libraries imports write the following line of code:
```python
pd.set_option('display.max_columns', 8)
```
It sets the number of columns, which ```pandas``` lets to display in the terminal. Unfortunately,
this number differs occasionally and causes problems in the tests, so we need to fix the number.
2. Read 3 CSV files containing the datasets
3. Print the first 20 rows of each data frame. Use the following order: ```general```, ```prenatal```, ```sports```

#### Example
The input is 3 CSV files, ```test/general.csv```, ```test/prenatal.csv```, and ```test/sports.csv```. As mentioned above, the test directory is hidden. Don't worry that you can't see it,
just use the paths from the previous sentence. If it doesn't work try to download data as described in Objectives.

The output is the following:
(This data is given for reference only, the actual values might be different)

```shell
    hospital  gender   age  height  ...    mri  xray  children  months
8   Brighton    girl   NaN   169.0  ...    NaN    no       NaN     2.0
12  Brighton  female  16.0     NaN  ...    NaN    no       2.0     2.0
13  Brighton    girl  64.0     NaN  ...  185.0   yes       0.0     1.0
17  Brighton     NaN  33.0   199.0  ...    NaN   NaN       2.0     2.0
19  Brighton     NaN   NaN   191.0  ...  168.0   NaN       1.0     1.0
27  Brighton  female  30.0   160.0  ...   85.0   NaN       1.0     NaN
29  Brighton  female  51.0   195.0  ...    NaN    no       0.0     NaN
36  Brighton     NaN  29.0   160.0  ...    NaN   NaN       1.0     1.0
41  Brighton  female   NaN     NaN  ...   55.0   yes       NaN     NaN
45  Brighton     man  24.0   151.0  ...   53.0   NaN       3.0     NaN
50  Brighton  female  37.0   150.0  ...  155.0    no       NaN     2.0
51  Brighton    girl   NaN     NaN  ...    NaN   yes       NaN     2.0
52  Brighton    girl  40.0   194.0  ...   59.0    no       1.0     2.0
55  Brighton     NaN  56.0   181.0  ...    NaN    no       2.0     2.0
56  Brighton     man  41.0   156.0  ...   52.0   yes       NaN     NaN
61  Brighton     NaN  45.0     NaN  ...  144.0   NaN       1.0     1.0
64  Brighton  female  59.0     NaN  ...   71.0   NaN       3.0     1.0
74  Brighton     NaN  54.0     NaN  ...   85.0    no       1.0     1.0
75  Brighton     NaN  48.0     NaN  ...   42.0    no       NaN     NaN
77  Brighton     NaN  26.0   161.0  ...  200.0   NaN       3.0     NaN

[20 rows x 14 columns]
     hospital  gender   age  height  ...    mri  xray  children  months
0   Cambridge     boy  52.0     NaN  ...  151.0   yes       NaN     2.0
2   Cambridge  female  60.0   158.0  ...  141.0   yes       0.0     2.0
4   Cambridge     NaN   NaN   185.0  ...  135.0   yes       2.0     1.0
5   Cambridge  female   NaN     NaN  ...   97.0   yes       NaN     1.0
11  Cambridge     NaN   NaN   199.0  ...   69.0    no       0.0     1.0
16  Cambridge     NaN  33.0   188.0  ...    NaN    no       1.0     1.0
21  Cambridge    girl  21.0   153.0  ...   49.0   yes       2.0     2.0
26  Cambridge     boy   NaN   189.0  ...  137.0   NaN       3.0     1.0
32  Cambridge     NaN  48.0     NaN  ...  341.0   yes       1.0     NaN
35  Cambridge    girl   NaN   180.0  ...  102.0   NaN       1.0     2.0
37  Cambridge     boy  55.0     NaN  ...  276.0   yes       NaN     1.0
39  Cambridge     NaN  46.0   165.0  ...    NaN    no       3.0     2.0
49  Cambridge     man  51.0   151.0  ...  142.0   yes       3.0     2.0
58  Cambridge     man  29.0   160.0  ...    NaN    no       NaN     NaN
62  Cambridge     boy  64.0     NaN  ...    NaN    no       NaN     1.0
66  Cambridge     boy   NaN     NaN  ...  150.0   yes       2.0     1.0
68  Cambridge  female   NaN   167.0  ...  160.0   NaN       1.0     1.0
70  Cambridge     NaN   NaN   193.0  ...   48.0   NaN       2.0     1.0
72  Cambridge     man  56.0   199.0  ...    NaN    no       2.0     2.0
83  Cambridge  female  30.0     NaN  ...    NaN   yes       2.0     1.0

[20 rows x 14 columns]
   hospital  gender   age  height  ...    mri  xray  children  months
1    Oxford     boy  52.0   197.0  ...   75.0   yes       2.0     1.0
7    Oxford     NaN   NaN   161.0  ...   63.0    no       0.0     NaN
9    Oxford     man  18.0     NaN  ...  310.0   yes       0.0     2.0
10   Oxford     boy  56.0   177.0  ...    NaN    no       NaN     NaN
14   Oxford    girl   NaN     NaN  ...    NaN    no       1.0     NaN
23   Oxford     boy  61.0     NaN  ...  245.0   yes       0.0     NaN
25   Oxford     NaN  15.0     NaN  ...    NaN   yes       1.0     NaN
33   Oxford     man  43.0   175.0  ...   87.0   NaN       0.0     1.0
38   Oxford    girl   NaN   167.0  ...  252.0    no       1.0     1.0
43   Oxford     man  26.0   193.0  ...   92.0    no       NaN     2.0
44   Oxford     NaN  54.0   170.0  ...  259.0   yes       NaN     1.0
48   Oxford     NaN   NaN   162.0  ...   75.0   yes       1.0     1.0
54   Oxford     NaN  20.0     NaN  ...  182.0   yes       2.0     NaN
57   Oxford  female   NaN   152.0  ...   37.0   yes       2.0     NaN
60   Oxford  female   NaN   154.0  ...    NaN   yes       1.0     2.0
65   Oxford     NaN  49.0   183.0  ...  163.0   NaN       2.0     2.0
67   Oxford     NaN   NaN     NaN  ...   97.0    no       3.0     1.0
69   Oxford  female   NaN   166.0  ...  178.0    no       1.0     1.0
71   Oxford  female  66.0   186.0  ...  270.0   yes       3.0     2.0
73   Oxford  female   NaN   151.0  ...    NaN   NaN       NaN     NaN

[20 rows x 14 columns]
```
