import pandas as pd
import numpy as np
import re

@pd.api.extensions.register_dataframe_accessor("pw")

class App:

    def __init__(self, df):
        self.df = df

    def list_splitter(self, columns):
        df = self.df
        data = df.copy()
        new_col = []
        temp_col = []
        temp_dict = {}
        double_columns = df.columns[df.columns.duplicated()]
        double = []

        try:
            if isinstance(columns, list):
                pass
            else:
                raise TypeError
        except TypeError:
            print('A list was expected')
            return df

        try:
            if 'True' in df.columns or 'False' in df.columns:
                raise NameError
        except NameError:
            print('True and False cant be column names')
            return df

        [double.append(x) for x in columns if (x in double_columns.unique().values) and (x not in double)]
        try:
            if double:
                raise ValueError
        except ValueError:
            print('These columns cant be in the dataframe multiple times: {0}'.format(double))
            return df

        for col in columns:
            if isinstance(col, str):
                dummy_columns = pd.get_dummies(df[col].apply(pd.Series).stack()).sum(level=0)
                for i in dummy_columns:
                    if i not in new_col:
                        new_col.append(i)

        for new in new_col:
            if new not in df.columns:
                data[new] = False
            else:
                print('The column {0} exist already'.format(new))
                answer = None
                while answer not in ("yes", "no", "j", "n", "ja", "y", "ye", "ne", "nee"):
                    answer = input("Do you want to put the data in a different column?: ")

                    if re.match('yes|ja|j|ye|y', answer.lower()):
                        colname = ''
                        while colname in new_col or colname == '' or colname in df.columns or colname in temp_dict.values():
                            colname = input("What is the name of the new col?: ")
                        temp_dict[new] = colname
                        data[colname] = False

                    elif re.match('no|n|ne|nee', answer.lower()):
                        temp_col.append(new)

                    else:
                        print("Please enter yes or no.")

        new_col = [x for x in new_col if x not in temp_col]
        new_col = [x for x in new_col if x != True]
        new_col = [x for x in new_col if x != False]

        try:
            del data[True]
            del data[False]
        except:
            pass

        for col in columns:
            for index, value in df[col].items():
                for new in new_col:
                    if isinstance(value, list) and new in value and new in temp_dict.keys():
                        data[temp_dict[new]].loc[index] = True
                    elif isinstance(value, list) and new in value:
                        data[new].loc[index] = True
                    elif (isinstance(value, int) or isinstance(value, str)) and new == value and new in temp_dict.keys():
                        data[temp_dict[new]].loc[index] = True
                    elif (isinstance(value, int) or isinstance(value, str)) and new == value:
                        data[new].loc[index] = True
        return data

    @property
    def explore_column_names(self):
        df = self.df
        data = df.copy()
        wrong = []
        tomuch = {}

        double_columns = data.columns[data.columns.duplicated()]
        try:
            if double_columns.values:
                raise ValueError
        except ValueError:
            print('These columns cant be in the dataframe multiple times: {0}'.format(double_columns.unique().values))
            return

        data = data.rename(columns=str.lower)
        # removes all double spaces in column name
        data.columns = data.columns.str.replace('\s?\s+', ' ', regex=True)
        # Removes all spaces at the start and end
        data.columns = data.columns.str.strip()

        exceptions = {'ü': 'u', 'ä': 'a', 'ö': 'o', 'ë': 'e', 'ï': 'i', '%': '_procent_', '&': '_and_', ' ': '_', '-': '_'}

        for v, k in exceptions.items():
            data.columns = data.columns.str.replace(v, k)

        data.columns = data.columns.str.replace('__', '_')

        # removes all the values that Javascript doesnt allow
        data.columns = data.columns.str.replace('[^0-9_$a-z]', '', regex=True)

        for i in data.columns:
            original = i
            try:
                if re.match(r'[^_$a-z]', i[0]) or re.match(r'_', i[-1]):
                    while re.match(r'[^_$a-z]', i[0]):
                        i = i[1:]
                        if re.match(r'_', i[0]):
                            i = i[1:]

                    while re.match(r'_', i[-1]):
                        i = i[:-1]
                    data.rename(columns={original: i}, inplace=True)
            except IndexError as error:
                wrong.append(original)

        dup_columns = data.columns[data.columns.duplicated()]

        for index, (first, second) in enumerate(zip(df.columns, data.columns)):
            if first != second:
                print(first, 'has been changed to', second)
            if second in wrong:
                index = wrong.index(second)
                wrong[index] = first
            elif second in dup_columns.values:
                tomuch.setdefault(second, []).append(first)

        if tomuch:
            print('')
            for key, value in tomuch.items():
                print('The values {1} will be changed to: {0}'.format(key, value))

        if wrong:
            print('\nThe columnname(s) are invalid: {0}'.format(wrong))

    @property
    def explore_datatypes(self):
        df = self.df
        print(f"{'index' : <8}{'type' : <10}{'dtype' : <8}{'nulls' : <6}{'differences': <12}{'column' : <1}")
        for i in df:
            try:
                a = df[i].unique()
            except:
                type = 'list'
            else:
                if all(isinstance(element, (bool, np.bool_)) for element in a):
                    type = 'boolean'
                elif all(isinstance(element, (np.int64, np.float64, int, float)) for element in a):
                    type = 'number'
                elif all(isinstance(element, str) for element in a):
                    type = 'string'
                elif all(isinstance(element, (pd.Timestamp, np.datetime64)) for element in a):
                    type = 'datetime'
                else:
                    type = 'multiple'
            if type == 'list':
                print(
                    f"{df.columns.get_loc(i) : <8}{type : <10}{df[i].dtype.name: <8}{df[i].isna().sum(): <6}{'NaN': <12}{i : <1}")
            else:
                print(
                    f"{df.columns.get_loc(i) : <8}{type : <10}{df[i].dtype.name: <8}{df[i].isna().sum(): <6}{df[i].nunique(): <12}{i : <1}")
        pass

    def column_merge(self, columns, delete = False):
        df = self.df
        data = df.copy()
        dict = {}
        double_columns = df.columns[df.columns.duplicated()]
        double = []

        if not isinstance(delete, bool):
            print("delete is supposed to be a boolean")
            return df

        try:
            if isinstance(columns, list):
                pass
            else:
                raise TypeError
        except TypeError:
            print('A list was expected')
            return df

        try:
            if len(columns) <= 1:
                raise IndexError
        except IndexError:
            print('The list must have multiple values')
            return df

        [double.append(x) for x in columns if (x in double_columns.unique().values) and (x not in double)]

        try:
            if double:
                raise ValueError
        except ValueError:
            print('These columns cant be in the dataframe multiple times: {0}'.format(double))
            return df

        for c in columns:
            if c == columns[0]:
                pass
            else:
                dict[c] = columns[0]

        for k, v in dict.items():
            data[v] = np.where(data[v].isnull(), data[k], data[v])
            if delete == True:
                del data[k]

        return data

    def column_to_numeric(self, columns, force = False):
        df = self.df
        data = df.copy()
        error_value = []
        double_columns = df.columns[df.columns.duplicated()]
        double = []

        if not isinstance(force, bool):
            print("delete is supposed to be a boolean")
            return df

        try:
            if isinstance(columns, list):
                pass
            else:
                raise TypeError
        except TypeError:
            print('A list was expected')
            return df

        [double.append(x) for x in columns if (x in double_columns.unique().values) and (x not in double)]

        try:
            if double:
                raise ValueError
        except ValueError:
            print('These columns cant be in the dataframe multiple times: {0}'.format(double))
            return df

        if force:
            for col in columns:
                data[col] = data[col].apply(lambda x: pd.to_numeric(x) if (pd.isna(x) or re.match('([0-9]+(,[0-9]+)?)$', x)) else np.nan)
        else:
            for col in columns:
                try:
                    if all((isinstance(i, str) or pd.isna(i)) for i in df[col].unique()):
                        if all(pd.isna(i) or re.match('([0-9]+(,[0-9]+)?)$', i) for i in df[col].unique()):
                            data[col] = data[col].apply(lambda x: pd.to_numeric(x.replace(',', '.')) if isinstance(x, str) else x)
                        else:
                            for i in df[col].unique():
                                if not (re.match('([0-9]+(,[0-9]+)?)$', i)):
                                    error_value.append(i)
                            raise ValueError
                    else:
                        raise TypeError

                except TypeError:
                    print("the column {0} doesn't contain only strings".format(col))
                    return df

                except ValueError:
                    print("the column {0} has values which can't be converted to numbers: {1}".format(col, error_value))
                    return df

        return data

    def replace_double_column_names(self):
        df = self.df.copy()
        dup_columns = df.columns[df.columns.duplicated()]
        df_columns = df.columns
        new_columns = []
        dict = {}

        for item in df_columns:
            counter = 0
            newitem = item
            while newitem in new_columns:
                counter += 1
                newitem = "{}_{}".format(item, counter)
            new_columns.append(newitem)
        df.columns = new_columns

        for i, c in dup_columns.value_counts().iteritems():
            for c in range(c):
                dict['%s_%s' % (i, c + 1)] = i

        for k, v in dict.items():
            df[v] = np.where(df[v].isnull(), df[k], df[v])

        return df