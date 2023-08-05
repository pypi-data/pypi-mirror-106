"""
db.py
~~~~~~~~

Module containing helper function for use with Apache Spark to read from SQL databases.
"""

import sys

def read_from_sql(spark, host, database, table, config):
  """Read from a SQL Server Database

  :spark: Spark session
  :database: Database to work with
  :table: Table to read data from
  :config: Database configuration options
      url: connection string URL
      connectionProperties: {
        driver: "",
        authenticationScheme: "",
        domainName: "",
        integratedSecurity: ""
      }
  """
  try:
    url = config['url'].format(host, database)
    connectionProperties = config['connectionProperties']
    
    jdbcDF = spark.read \
      .jdbc(url, table, properties = connectionProperties)

    return jdbcDF
  except:
    err = sys.exc_info()
    print("Error loading datafrom from SQL >> {0}".format(err))


def write_to_sql(df, host, database, table, config):
  """Read from a SQL Server Database

  :df: Dataframe to write to sql 
  :host: SQL hostname
  :database: Database to work with
  :table: Table to write data to
  :config: Database configuration options
      url: ""
      connectionProperties: {
        driver: "",
        authenticationScheme: "",
        domainName: "",
        integratedSecurity: "",
      }
  """
  try:
    url = config['url'].format(host, database)
    connectionProperties = config['connectionProperties']

    jdbcDF = df.write \
      .jdbc(url, table, properties = connectionProperties)

    return jdbcDF
  except:
    err = sys.exc_info()
    print("Error writing dataframe to SQL Server >> {0}".format(err))


def readFromSQLServer( hostname, database, dbtable, userName, password,  port = 1433):

    '''
    Purpose: This function reads a data table from SQL Server database into a dataframe.
    Args:
        hostname : SQL Server name ( fully qualified name -- 'servername.healthscapeadvisors.net')
        database : Database name
        dbtable  : Table name 
        userName : User ID of person /  system executing the notebook
        password : Password of person /  system executing the notebook
        port     : The server port is default is 1433.
    
    Returns:
        ret_df: Return dataframe 
    '''
    ret_df = None # Default is set to none or null
    try:

        url = f"jdbc:sqlserver://{hostname}:{port};database={database}"
        connectionProperties = {
            "integratedSecurity" : "true",
            "driver" : "com.microsoft.sqlserver.jdbc.SQLServerDriver",
            "authenticationScheme" :"NTLM",
            "domainName" : "healthscapeadvisors.net",
            "userName"   : userName,
            "password"   : password
        }
        
        #jdbc(url=, query=sql_query, properties=connectionProperties)
        ret_df = spark.read.jdbc(url=url, table=dbtable, properties=connectionProperties)
        return ret_df
    except:
         err = sys.exc_info()[0]
         print("Error loading datafrom SQL >> {0}".format(err))
         return ret_df
    

def writeToSQLServer(df, hostname, database, dbtable, userName, password, writeMode='overwrite', port = 1433):
    '''
    Purpose: This function takes a dataframe and write it into SQL Server database as a table.
    Args:
        hostname : SQL Server name ( fully qualified name -- 'servername.healthscapeadvisors.net')
        database : Database name
        dbtable  : Table name 
        userName : User ID of person /  system executing the notebook
        password : Password of person /  system executing the notebook
        writeMode: The write model, which is either `append` or `overwrite` (overwrite is the default)
        port     : The server port is default is 1433.
    
    Returns:
        retVal: True /  False if write was successful
    '''
    retVal = False

    try:
        url = f"jdbc:sqlserver://{hostname}:{port};database={database}"
        connectionProperties = {
            "integratedSecurity" : "true",
            "driver" : "com.microsoft.sqlserver.jdbc.SQLServerDriver",
            "authenticationScheme" :"NTLM",
            "domainName" : "healthscapeadvisors.net",
            "userName"   : "gasante",
            "password"   : password
        }
        df.write \
        .jdbc(url=url, table=dbtable, properties=connectionProperties, mode=writeMode)
        retVal =True
    except:
        err = sys.exc_info()[0]
        print(" Error writing dataframe to SQL Server {0}".format(err))

    return retVal
