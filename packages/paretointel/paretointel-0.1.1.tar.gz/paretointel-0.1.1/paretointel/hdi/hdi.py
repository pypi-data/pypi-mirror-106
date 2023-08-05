#-------------------------------------------------------------------------------------
# Purpose: These are a collection of common functions to be used in HDI development
# Created on: 04/20/2021
# Created by: George Asante
# Updated by: Ergels Gaxhaj
#
#---------------------------------------------------------------------------------------

from os import environ, listdir, path
import sys
import json
from pyspark.sql import functions as fn
from pyspark.sql.types import *
from pyspark.sql.utils import AnalysisException

def sayhi():
  print("hi")

def read_json(path_to_file):
    '''Load JSON file into dict

    :path_to_file: Path to JSON file 
    :return: Dict if load is successful. Empty dict otherwise.
    '''
    config_dict = {}
    try:
        path_to_file = path.normcase(path_to_file)
        print(path_to_file)
        with open(path_to_file, 'r') as json_file:
            config_dict = json.load(json_file)
    except:
        err = sys.exc_info()
        print(" Error loading JSON file >> {0}".format(err))

    return config_dict

def hdi_to_date(col):
    '''
    Purpose: Takes date columns and transform into appropriate format for processing. 
             Handle various date formats.

    :col : Column to check if exists?
    :return: True / False if column is present in the dataframe.
    '''
    formats=("MM/dd/yyyy", "yyyy-MM-dd","yyyy MM dd","yyyy MMMM dd", "ddMMMyyyy","yyyyMMdd", "yyyyMM","yymd")
    return fn.coalesce(*[fn.to_date(col, f) for f in formats])


def has_column(df, col):
    '''
    Purpose: This function checks if a column exists in a dataframe. 

    :df: The dataframe to check for columns
    :col: Column to check if exists?
    :return: True /  False if column is present in the dataframe.
    '''
    try:
        df[col]
        return True
    except AnalysisException:
        return False
        

def normalize_col_name(name):
    '''
    Purpose: This is a generic function that takes a columns name and normalize the name by:
             * Stripping leading / trailing spaces
             * Convert to lower case becuase spark is case sensitive on columns 
                    and would cause issues when columns are wrongely cased.
             * Replace spaces with underscore

    :name: Column name to normalize
    :reutrn: Newly normalized column
    '''
    _newCol = None
    try:
        _newCol = name.strip().lower().replace(" ","_")
        return _newCol
    except:
        err = sys.exc_info()[0]
        print(" Error normalizing columns >> {0}".format(err))
        return _newCol


def normalizeColumnsNames(df):
    '''
    Purpose: This function takes a dataframe and normalize its column names

    :df: Dataframe to normalize
    :return: Normalized dataframe
    '''
    ret_df = df
    try:
        _cols = ret_df.columns
        for _col in _cols:
            _newCol = normalize_col_name(_col)
            ret_df = ret_df.withColumnRenamed(_col,_newCol)
        return ret_df
    except:
        print("Error normalizing dataframe")
        return ret_df
    

def applyCCHierachy(df, set_col, hier_cols, modelnum):
    '''
    Purpose: This is a specific function to perform Hierarchical Condition Condition (HCC):
             * It takes a dataframe, set_col and hier_cols, loop through hier_cols and set them to zero when set_col is 1

    :df: Dataframe to perform HCC on
    :set_col: Column to Keep is value is 1
    :hier_cols: Columns to set 0 where `set_col` is 1
    :return: Returned dataframe -- where hcc has been applied
    '''
    ret_df = df
    try:
        for cc in hier_cols:
            #Check to make sure that column exists before performing tasks.
            if has_column(ret_df, cc) and has_column(ret_df, set_col):
                ret_df = ret_df.withColumn(cc, fn.when(((fn.col(set_col) == 1) 
                        & (fn.col("modelnum") == modelnum)), 0).otherwise(fn.col(cc)))
        return ret_df
    except:
        print('Error applying HCC logic')
        return ret_df


def hdi_concat(cols, delimiter="|"):
    '''
    Purpose: This function takes an array of columns and concatenate them into a single column with values separated by                 
    the supplied delimiter. It excludes columns with empty or null values.

    :cols: Arrary of columns to concat
    :delimiter: The delimiter to use for concatenate
    :return: A column with concatenated values  
    '''
    ret_col = None
    try:
        ret_col = fn.trim(fn.concat_ws(delimiter, *[fn.when(fn.col(c) !='', fn.col(c)) for c in cols]))
        return ret_col
    except:
        return ret_col
    

def cols2Int(df, cols):
    '''
    Purpose: This is a generic function that takes a dataframe and a collect on columns and convert them to Int data type
             
    :df: Dataframe with columns to convert
    :cols: An array of columns in the dataframe to converted into Int Type
    :return: Returned dataframe with converted data types 
    '''
    ret_df = df
    try:
        for _col in cols:
            if has_column(df, _col):
                ret_df = ret_df.withColumn(_col,  fn.col(_col).cast(IntegerType()) )
        return ret_df
    except:
        print('Error converting data to int ')
        return ret_df
    

def cols2Double(_df, _cols):
    '''
    Purpose: This is a generic function that takes a dataframe and a collect on columns and convert them to Double data              
    type
             

    Args:
        _df   : Dataframe with columns to convert
        _cols : An array of columns in the dataframe to converted into Double Type
    
    Returns: 
        ret_df: Returned dataframe with converted data types 
        
    '''
    ret_df =  _df
    try:
        for _col in _cols:
            if has_column(_df, _col):
                ret_df = ret_df.withColumn(_col,  fn.col(_col).cast(DoubleType()) )
        return ret_df
    except:
        print('Error converting data to int ')
        return ret_df
  

def cols2Date(_df, _cols):
    '''
    Purpose: This is a generic function that takes a dataframe and a collect on columns and convert them to date data      
    type
             

    Args:
        _df   : Dataframe with columns to convert
        _cols : An array of columns in the dataframe to converted into Date Type
    
    Returns: 
        ret_df: Returned dataframe with converted data types 
        
    '''
    ret_df =  _df
    try:
        for _col in _cols:
            if has_column(_df, _col):
                ret_df = ret_df.withColumn(_col, hdi_to_date(_col)) 
        return ret_df
    except:
        print('Error converting data to int ')
        return ret_df


def trim_columns(_df, _cols=[]):
    '''
    Purpose: This is a generic function that takes a dataframe and a collect on columns and convert them to Int data type
             

    Args:
        _df   : Dataframe with columns to trim
        _cols : An array of columns in the dataframe to converted into Int Type
    
    Returns: 
        ret_df: Returned dataframe with converted data types 
        
    '''
    ret_df = _df
    try:
        if len(_cols) == 0: 
            # all columns if array of columns not provided
            _cols = ret_df.columns
        for _col in _cols:
            ret_df = ret_df.withColumn(_col,  fn.ltrim(fn.rtrim(fn.col(_col))) )
        return ret_df
    except:
        print("Error triming dataframe")
        return ret_df


def display_df(_df, show_rows = 12, show_truncate = False):
    '''
        This function takes a dataframe and displays records
    '''
    try:
        _df.show(show_rows, show_truncate)
    except:
        print("Error displaying {0}".format(_df))
        

def joinDataframes(_df1, _df2, join_cond, select_cols, _how='inner', dropDuplicates = False):
    '''
        This function takes a dataframe and displays records
    '''
    ret_df = None
    try:
        ret_df = (_df1
                    .join(_df2, join_cond, how=_how)
                    .selectExpr(select_cols)
                 )
        if dropDuplicates:
            ret_df = ret_df.dropDuplicates()
        return ret_df
    except:
        print("Error displaying {0}".format(ret_df))
