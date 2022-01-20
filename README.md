# Data-Analysis-for-Hospitals-Jetbrains-Academy
This project jetbrains academy https://hyperskill.org/projects/152

## Work on project. Stage 3/5: Improve your dataset
### Objectives

In this stage, your program should:

1. After all the libraries imports write the following line of code:
```python
pd.set_option('display.max_columns', 8)
```
2. Read the CSV files with datasets
3. Change the column names. The column names of the sports and the prenatal tables must match the column names of the general table
4. Merge the data frames into one. Use the ignore_index = True parameter and the following order: ```general```, ```prenatal```, ```sports```
5. Delete the ```Unnamed: 0``` column
6. Delete all the empty rows
7. Correct all the gender column values to ```f``` and ```m``` respectively
8. Replace the ```NaN``` values in the gender column of the prenatal hospital with ```f```
9. Replace the ```NaN``` values in the ```bmi```, ```diagnosis```, ```blood_test```, ```ecg```, ```ultrasound```, ```mri```, ```xray```, ```children```, ```months``` columns with zeros
10. Print shape of the resulting data frame
11. Print random 20 rows of the resulting data frame. For the reproducible output set ```random_state=30```

#### Example
The input is 3 CSV files, ```test/general.csv```, ```test/prenatal.csv```, and ```test/sports.csv```.

The output is the following:
(This data is given for reference only, the actual values might be different)

```shell
Data shape: (442, 14)
      hospital gender   age  height  ...    mri  xray  children  months
148        NaN      m   NaN   163.0  ...   96.0     0       3.0     0.0
408  Cambridge      f   NaN   196.0  ...  189.0    no       0.0     2.0
214     Oxford      m  51.0     NaN  ...   65.0     0       3.0     1.0
67      Oxford      f   NaN     NaN  ...   97.0    no       3.0     1.0
241  Cambridge      m   NaN   199.0  ...  177.0     0       0.0     0.0
205        NaN      f  25.0   187.0  ...    0.0     0       0.0     2.0
126  Cambridge      f  50.0     NaN  ...   99.0   yes       0.0     1.0
193   Brighton      m  26.0   195.0  ...  116.0    no       0.0     1.0
338  Cambridge      m  17.0   176.0  ...  214.0     0       0.0     1.0
317        NaN      m   NaN   153.0  ...  190.0     0       3.0     1.0
344   Brighton      m   NaN     NaN  ...  200.0   yes       2.0     1.0
31         NaN      m  65.0   156.0  ...   59.0    no       2.0     0.0
164        NaN      m  53.0   150.0  ...    0.0   yes       1.0     2.0
212   Brighton      f  18.0     NaN  ...    0.0    no       0.0     0.0
213  Cambridge      f  55.0   172.0  ...    0.0   yes       2.0     2.0
201     Oxford      f   NaN   183.0  ...    0.0   yes       3.0     1.0
342   Brighton      f   NaN   189.0  ...  178.0     0       0.0     0.0
236        NaN      f   NaN   164.0  ...   67.0   yes       3.0     0.0
211        NaN      f  40.0   165.0  ...   70.0    no       0.0     1.0
384        NaN      f  29.0     NaN  ...   69.0     0       0.0     1.0

[20 rows x 14 columns]
```
