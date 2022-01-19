# Data-Analysis-for-Hospitals-Jetbrains-Academy
This project jetbrains academy https://hyperskill.org/projects/152

## Work on project. Stage 2/5: Merge them!
### Objectives

In this stage, your program should:

1. After all the libraries imports write the following line of code:
```python
pd.set_option('display.max_columns', 8)
```
2. Read 3 CSV files with datasets
3. Change the column names. All column names in the sports and prenatal tables must match the column names in the general table
4. Merge the data frames into one. Use the ```ignore_index = True``` parameter and the following order: ```general```, ```prenatal```, ```sports```
5. Delete the ```Unnamed: 0``` column
6. Print random 20 rows of the resulting data frame. For the reproducible output set ```random_state=30```

#### Example
The input is 3 CSV files, ```test/general.csv```, ```test/prenatal.csv```, and ```test/sports.csv```.

The output is the following:
(This data is given for reference only, the actual values might be different)

```shell
      hospital  gender   age  height  ...    mri  xray  children  months
148        NaN     man   NaN   163.0  ...   96.0   NaN       3.0     NaN
408  Cambridge  female   NaN   196.0  ...  189.0    no       NaN     2.0
214     Oxford     boy  51.0     NaN  ...   65.0   NaN       3.0     1.0
67      Oxford     NaN   NaN     NaN  ...   97.0    no       3.0     1.0
241  Cambridge     boy   NaN   199.0  ...  177.0   NaN       NaN     NaN
205        NaN     NaN  25.0   187.0  ...    NaN   NaN       0.0     2.0
126  Cambridge    girl  50.0     NaN  ...   99.0   yes       NaN     1.0
193   Brighton     man  26.0   195.0  ...  116.0    no       NaN     1.0
338  Cambridge     man  17.0   176.0  ...  214.0   NaN       NaN     1.0
317        NaN     man   NaN   153.0  ...  190.0   NaN       3.0     1.0
344   Brighton     boy   NaN     NaN  ...  200.0   yes       2.0     1.0
31         NaN     boy  65.0   156.0  ...   59.0    no       2.0     NaN
164        NaN     man  53.0   150.0  ...    NaN   yes       1.0     2.0
212   Brighton    girl  18.0     NaN  ...    NaN    no       0.0     NaN
213  Cambridge     NaN  55.0   172.0  ...    NaN   yes       2.0     2.0
201     Oxford    girl   NaN   183.0  ...    NaN   yes       3.0     1.0
342   Brighton    girl   NaN   189.0  ...  178.0   NaN       NaN     NaN
236        NaN     NaN   NaN   164.0  ...   67.0   yes       3.0     NaN
211        NaN     NaN  40.0   165.0  ...   70.0    no       NaN     1.0
384        NaN  female  29.0     NaN  ...   69.0   NaN       NaN     1.0

[20 rows x 14 columns]
```
