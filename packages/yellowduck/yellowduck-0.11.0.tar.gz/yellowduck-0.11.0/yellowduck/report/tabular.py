# -*- coding: utf-8 -*-

# you can use this utility by export path as below code

# This one for deploy in airflow
# current_directory = os.path.dirname(os.path.realpath(__file__))
# sys.path.insert(0, os.path.join(current_directory, '../../library'))
# from dataops.schema_gen import SchemaGenerator

# This one for use only its function in any file such as Jupyter Notebook
# sys.path.insert(0, os.path.join(os.getcwd(), '../../library'))
# from dataops.schema_gen import SchemaGenerator

import os
from datetime import datetime

class SchemaGenerator():
    def __init__(self):
        self._current_directory = os.path.dirname(os.path.realpath(__file__))          
        self._report_directory = os.path.join(self._current_directory, '../../reports/schema_gen/')
        #self._time_stamp_start = datetime.now()
    
    def get_schema_report(self, my_table_name, expected_columns, all_present_columns):

        time_stamp_start = datetime.now()
        
        ##### Compare Schema #####
    
        if isinstance(expected_columns, str):
            expected_columns = expected_columns.split(',')
        
        set_expected_columns = set(expected_columns)
        set_all_present_columns = set(all_present_columns)
        set_intersect_columns = set(set_expected_columns.intersection(set_all_present_columns))

        num_expected_col = len(set_expected_columns)
        num_all_present_col = len(set_all_present_columns)
        num_intersect_col = len(set_intersect_columns)

        if set_expected_columns == set_intersect_columns:
            result = 'All Columns Included'
            status = 'passed'
            bin = True
        else:
            result = 'Columns Not Found!'
            status = 'failed'
            bin = False

        needed = list(set_expected_columns - set_intersect_columns)
        if not needed:
            needed = ' '
    
        timestamp_end = datetime.now()
        
        ##### Generate Report #####

        if not os.path.exists(self._report_directory):
            os.makedirs(self._report_directory)

        schema_report_dir_name = os.path.join(self._report_directory, 'schema_report_' + str(time_stamp_start.strftime("%Y%m%d_%H%M%S")) + '_' + my_table_name + '_' + status)
            
        with open(schema_report_dir_name, 'w') as f:
            start_time = str(time_stamp_start.strftime("%A, %d %B %Y, %I:%M %p"))
            end_time = str(timestamp_end.strftime("%A, %d %B %Y, %I:%M %p"))

            f.write('  # Schema Log #\n')

            f.write("----------------------------------------------------------------\n\n")

            f.write('[ General Information ]\n\n')
            
            f.write('Start Date:\t{}\n'.format(start_time))
            f.write('End Date:\t{}\n\n'.format(end_time))
            
            f.write('{}\n\n'.format(result))

            f.write("----------------------------------------------------------------\n\n")

            f.write('[ Schema Checking Result ]\n\n')
            
            f.write('Expected Columns:\t{}\n'.format(expected_columns))
            f.write('Intersect Columns:\t{}\n\n'.format(list(set_intersect_columns)))
            
            f.write('Number of All Column:\t{}\n'.format(str(num_all_present_col)))
            f.write('Number of Expected Column:\t{}\n'.format(str(num_expected_col)))
            f.write('Number of Intersect Column:\t{}\n\n'.format(str(num_intersect_col)))

            if not bin:
                f.write('Needed columns:\t{}'.format(needed))

            f.write("\n\n----------------------------------------------------------------\n\n")

            f.write('[ Raw Schema ]\n\n')
            
            f.write('All Columns:\t{}'.format(all_present_columns))
			
# -*- coding: utf-8 -*-

# you can use this utility by export path as below code

# This one for deploy in airflow
# current_directory = os.path.dirname(os.path.realpath(__file__))
# sys.path.insert(0, os.path.join(current_directory, '../../library'))
# from dataops.statistic_gen import StatisticGenerator

# This one for use only its function in any file such as Jupyter Notebook
# sys.path.insert(0, os.path.join(os.getcwd(), '../../library'))
# from dataops.statistic_gen import StatisticGenerator

import os
import numpy as np
import pandas as pd
import pyspark
from datetime import datetime
from pyspark.sql.functions import col, skewness, kurtosis

current_directory = os.path.dirname(os.getcwd())          
stat_directory = os.path.join(current_directory, '../../reports/statistic_gen/')
argparse_directory = os.path.join(stat_directory, 'argparse')        
        

def describe_table(my_table_name, dataframe, numerical_col = [], categorical_col = []):
        
    time_stamp_start = datetime.now()

    numerical_stat_pd = ['count','mean','std','min','25%','50%','75%','max']
    
    categorical_stat = ['count','unique','top','freq']
    
    ############################################################
    ##################### Calculation Part #####################
    ############################################################
    
    if len(numerical_col) > 0 or len(categorical_col) > 0:
        all_columns = numerical_col + categorical_col
#         print('yes we have')
    else:
        all_columns = list(dataframe.columns)
#         print('its all columns')

    dataframe = dataframe[all_columns]


    #### For Pandas dataframe and data size more than 0 ####
    
    if (type(dataframe) == pd.DataFrame) and dataframe.size > 0:
        
        type_of_dataframe = 'Pandas Dataframe'
        
        # Count Number of Row in Dataframe 
        num_of_row = len(dataframe)
        
        # Print Original Data Type 
        datatype = dataframe.dtypes.to_string()
        
        # Count Null and Empty String
        df_null_row = pd.DataFrame(dataframe.isna().sum()).rename(columns = {0:'Count Null'})
        df_empty_string = pd.DataFrame()
   
        for col in dataframe.columns:
            df_empty_string.loc['Count Empty String',col] = len(df[df[col] == ''])

        null_n_empty = pd.concat([df_null_row,df_empty_string.T.astype('int64')], axis = 1).to_string()

        
        if len(numerical_col) > 0 or len(categorical_col) > 0:
        
        ## Numerical Variable ##
        
            describe_df = dataframe[numerical_col].dropna().describe(include = 'all')
            describe_df = describe_df.loc[numerical_stat_pd,:]

            for col in describe_df.columns:
                describe_df.loc['skewness',col] = dataframe[col].skew()
                describe_df.loc['kurtosis',col] = dataframe[col].kurt()

            describe_df = describe_df.round(2).T.to_string()

        ## Categorical Variable ##
        
        
        
        cat_describe_df =
        
        
        unique_value_count =        
        
        


        else:
    
            all_column_describe = dataframe.describe(include = 'all').to_string()
    
    

    #### For Pyspark dataframe and data size more than 0 ####
   
    elif (type(dataframe) == pyspark.sql.dataframe.DataFrame and pd.DataFrame(dataframe.take(1)).size > 0):        

        type_of_dataframe = 'Pyspark Dataframe'        
        
        # Count Number of Row in Dataframe 
        num_of_row = dataframe.count()
        
        # Print Original Data Type 
        datatype = pd.DataFrame(dataframe.take(1), columns = all_columns)
        datatype = datatype.dtypes

        # Count Null and Empty String
        df_null_row = dataframe.select([count(when(isnan(c) | column(c).isNull(), c)).alias(c) for c in dataframe.columns])\
        .toPandas().rename(index={0:'Count Null'}).T

        df_empty_string = dataframe.select([count(when(column(c) == '', c)).alias(c) for c in dataframe.columns])\
        .toPandas().rename(index={0:'Count Empty String'}).T
        
        null_n_empty = pd.concat([df_null_row,df_empty_string.astype('int64')], axis = 1).to_string()
        
        if len(numerical_col) > 0 or len(categorical_col) > 0:
        
        ## Numerical Variable ##
        
            describe_df = sdf.select(numerical_col).describe().toPandas()
            describe_df.rename(index = describe_df['summary'], inplace = True)
            describe_df = describe_df.drop(columns = ['summary']).astype('float64')

            for col in describe_sdf.columns:
                describe_sdf.loc['skewness',col] = sdf.select(skewness(col)).toPandas().iloc[0,0]
                describe_sdf.loc['kurtosis',col] = sdf.select(kurtosis(col)).toPandas().iloc[0,0]

            describe_df = describe_df.round(2).T.to_string()

        ## Categorical Variable ##

        cat_describe_df =
        
        
        unique_value_count =
        
        

        else:        

            all_column_describe = dataframe.describe().toPandas().to_string()
        
        
    else:
        status = 'Error in some way :P'
        print(status)
        exit(1)        
    
    
    timestamp_end = datetime.now()
        
        
    ###################################################    
    ################# Report Part #####################
    ###################################################
    
    if not os.path.exists(stat_directory):
            os.makedirs(stat_directory)
        
        
    if not os.path.exists(argparse_directory):
        os.makedirs(argparse_directory)               
            
    stat_report_dir_name = os.path.join(stat_directory, 'stat_report_' + \
                                              str(time_stamp_start.strftime("%Y%m%d_%H%M%S")) + '_' + \
                                              my_table_name)
        
    argparse_dir_name = os.path.join(argparse_directory, 'arg_' + \
                                              str(time_stamp_start.strftime("%Y%m%d_%H%M%S")) + '_' + \
                                              my_table_name)
        
    with open(stat_report_dir_name, 'w') as f:
        start_time = str(time_stamp_start.strftime("%A, %d %B %Y, %I:%M %p"))
        end_time = str(timestamp_end.strftime("%A, %d %B %Y, %I:%M %p"))
            
        f.write('  # Statistic Log #\n')
            
        f.write("----------------------------------------------------------------\n\n")

        f.write('[ General Information ]\n\n')
        
        f.write('Start Date:\t{}\n'.format(start_time))
        f.write('End Date:\t{}\n\n'.format(end_time))
        
        f.write('Table name:\t\t\t{}\n'.format(my_table_name))
        f.write('Number of rows:\t\t{}\n'.format(num_of_row))
        f.write("Dataframe's Type:\t{}\n\n".format(type_of_dataframe))
            
        f.write("----------------------------------------------------------------\n\n")            

        f.write('[ Data Type ]\n\n')
        f.write('{}\n\n'.format(datatype))

            
        f.write("----------------------------------------------------------------\n\n")
            
        f.write('[ Count Null Row ]\n\n')
        f.write('{}\n\n'.format(null_n_empty))
            
    
        # In case of columns are determined manually.
        # We sure that data type will be the right one.
        if len(numerical_col) > 0 or len(categorical_col) > 0:    
            if len(numerical_col) > 0:

                f.write("----------------------------------------------------------------\n\n")  
                f.write('[ Numerical Variable Stat ]\n\n')  
            
                f.write('{}\n\n'.format(describe_df))
            
            if len(categorical_col) > 0:

                f.write("----------------------------------------------------------------\n\n")
                f.write('[ Categorical Variable Stat ]\n\n')

                f.write('{}\n\n'.format(cat_describe_df))               
                
                f.write('{}\n\n'.format(unique_value_count))
        
        # In case of columns aren't determined. (It's automatically determined in the above function)
        # We cannot automatically specify what exactly data type of each column by use programming.
        else:
                
                f.write("----------------------------------------------------------------\n\n")  
                f.write('[ Variable Stat ]\n\n')
                
                f.write('{}\n\n'.format(all_column_describe))
                
                f.write('Note: Specify the data type by yourself to will make the statistical value to be more accurate.\n') 
                f.write('By give us 2 more argument as follow \n\n')
                f.write('describe_table(my_table_name, dataframe, numerical_col = [], categorical_col = [])')

            
    with open(argparse_dir_name, 'w') as f:
            
        for var_name in all_columns:
            f.write('[{}]\n\n\n'.format(var_name))
            
            
    with open(stat_report_dir_name, 'r') as f:
        my_data = f.read()

    print(my_data)
