# Data-Analysis-for-Hospitals-Jetbrains-Academy
This project jetbrains academy https://hyperskill.org/projects/152

## Work on project. Stage 5/5: Visualize it_
### Objectives

In this stage, your program should:

1. Read the CSV files with datasets
2. Change the column names. The column names of the sports and the prenatal tables must match the column names of the general table
3. Merge the data frames into one. Use the ignore_index = True parameter and the following order: ```general```, ```prenatal```, ```sports```
4. Delete the ```Unnamed: 0``` column
5. Delete all the empty rows
6. Correct all the gender column values to ```f``` and ```m``` respectively
7. Replace the ```NaN``` values in the gender column of the prenatal hospital with ```f```
8. Replace the ```NaN``` values in the ```bmi```, ```diagnosis```, ```blood_test```, ```ecg```, ```ultrasound```, ```mri```, ```xray```, ```children```, ```months``` columns with zeros
9. Answer questions 1-3. Output the answers in the specified format. The answers to the first two questions should be formatted as in the examples. No special form is required to answer the third question

#### Example
The input is 3 CSV files, ```test/general.csv```, ```test/prenatal.csv```, and ```test/sports.csv```.

The output is the following:
(This data is given for reference only, the actual values might be different)

```shell
The answer to the 1st question: 0-15
The answer to the 2nd question: flu
The answer to the 3rd question: It's because...
```
