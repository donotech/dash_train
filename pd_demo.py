import pandas as pd

# Create empty dataframe
from pandas import DataFrame

df = pd.DataFrame()

# Creating a simple dataframe
df['name'] = ['Reema', 'Shyam', 'Jai',
              'Nimisha', 'Rohit', 'Riya']
df['gender'] = ['Female', 'Male', 'Male',
                'Female', 'Male', 'Female']
df['age'] = [31, 32, 19, 23, 28, 33]

# View dataframe
print(df)


# function to find mean
def mean_age_by_group(dataframe: DataFrame, col):
    # groups the data by a column and
    # returns the mean age per group
    return dataframe.groupby(col).mean(numeric_only=True)


# function to convert to uppercase
def uppercase_column_name(dataframe):
    # Converts all the column names into uppercase
    dataframe.columns = dataframe.columns.str.upper()

    # And returns them
    return dataframe


# Create a pipeline that applies both the functions created above
pipeline: DataFrame = df.pipe(mean_age_by_group, col='gender').pipe(uppercase_column_name)

# calling pipeline
print(pipeline)

#pd pipes

import pdpipe as pdp
import pandas as pd

# creating a empty dataframe named dataset
dataset = pd.DataFrame()

# Creating a simple dataframe
dataset['name'] = ['Reema', 'Shyam', 'Jai',
                   'Nimisha', 'Rohit', 'Riya']

dataset['gender'] = ['Female', 'Male', 'Male',
                     'Female', 'Male', 'Female']

dataset['age'] = [31, 32, 19, 23, 28, 33]

dataset['department'] = ['Accounts', 'Management',
                         'IT', 'IT', 'Management',
                         'Advertising']

dataset['index'] = [1, 2, 3, 4, 5, 6]

dropCol = pdp.ColDrop("index").apply(dataset)
print(dropCol)