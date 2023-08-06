import pandas as pd
import numpy as np
import xlsxwriter
import inspect, os, os.path
from pathlib import Path
import datetime as dt
import re
import sys
import csv
import boto3
import pickle
import rangerconfig
import rangerconnection
import utilexecpython
import time
import rangerlogging
from openpyxl import load_workbook
from operator import itemgetter
from itertools import groupby,count
from pandas import DataFrame
import warnings
import datetime
from dateutil.parser import parse
import os
from pandas.core.common import SettingWithCopyWarning
import math
from sklearn import metrics
import xgboost as xgboost
from xgboost import XGBClassifier
from scipy import stats
from sklearn import preprocessing,decomposition
from sklearn.model_selection import train_test_split 
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
import sklearn.pipeline as pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from collections import defaultdict
from sklearn.pipeline import Pipeline
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import GradientBoostingClassifier
import operator 
from sklearn.decomposition import PCA
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import GridSearchCV
from datetime import datetime as dt
import itertools

email='[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
phone_10digit='(\+91)?(-)?\s*?(91)?\s*?([6789]\d{9})'
credit_card_num='[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4}'
https='(\w+)://'
host_name='((http|https)?\:\/\/)?:[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*'
alpha_num =r'^(?=.*\d)(?=.*[a-zA-Z])[\da-zA-Z]+$'
num = r'\d+$'
alpha = r'[a-zA-Z]+$'
Date = r'^(?:(?:19|20)\d{2}([-/]?)\d{1,2}\1\d{1,2}|\d{1,2}([-/]?)\d{1,2}\2(?:19|20)\d{2})$'
Date_formats = {'YYYY/MM/DD' :'%Y/%m/%d','YYYY-MM-DD':'%Y-%m-%d','MM/DD/YYYY':'%m/%d/%Y','MM-DD-YYYY':'%m-%d-%Y','MM-DD-YY':'%m-%d-%y','MM/DD/YY':'%m/%d/%y','DD-MM-YYYY':'%d-%m-%Y',
         'DD/MM/YYYY':'%d/%m/%Y','MM-YYYY':'%m-%Y','MM-YYYY':'%m/%Y','MM-YY':'%m-%y','B-YYYY':'%b-%Y','BYYYY':'%b%Y','YYYY-B':'%Y-%b','YYYY.MM.DD':'%Y.%m.%d','YYYY.B.D':'%Y.%b.%d','YYYY/MM/DD HH:MM:SS':'%Y/%m/%d %H:%M:%S',
        'YYYY-MM-DD HH:MM:SS':'%Y-%m-%d %H:%M:%S','YYYY/MM/DD HH:MM:ss.SSS':'%Y/%m/%d %H:%M:%S.%f','YYYY-MM-DD HH:MM:ss.SSS':'%Y-%m-%d %H:%M:%S.%f','YYYYMMDD HH:MM:SS':'%Y%m%d %H:%M:%S',
        'MM/DD/YYYY HH:MM:SS':'%m/%d/%Y %H:%M:%S','MM-DD-YYYY HH:MM:SS':'%m-%d-%Y %H:%M:%S'}
age='^\d{3}$'
date='\d.*\/.*\d.*\/.*\d'
# currency='(?:[\£\$\€]{1}[,\d]+.?\d*)'
usd_to_inr=73

Email_id=None
PhoneNumber=None
creditNum=None
url=None
alphanumeric_op = None
Num_eric = None
Alp_habet = None
vr_date = None
hotname = None

rangerfilelogging = rangerlogging.get_logger(__name__)

#creating folders 
def fn_create_folder(p_folder_name):
	if not os.path.exists(p_folder_name):
		os.makedirs(p_folder_name)
	else:
		for root, directories, files in os.walk(p_folder_name):
			for filename in files:
				filepath = os.path.join(root, filename)
				os.remove(filepath)

#downloading files from s3 bucket to local folders
def fn_s3_download_files(p_inprogress_bucket,p_s3_file_name,p_local_folder_file_name):
    
    s3_connection = rangerconnection.ranger_s3_connection()
    s3_resource =s3_connection.fn_s3_resource()
    s3_resource.meta.client.download_file(p_inprogress_bucket, p_s3_file_name, p_local_folder_file_name)

#uploading files from s3 bucket
def fn_s3_upload_files(p_local_target_folder,p_s3_bucket,p_s3_file_location):
    s3_connection = rangerconnection.ranger_s3_connection()
    s3_resource =s3_connection.fn_s3_resource()
    for root, directories, files in os.walk(p_local_target_folder):
        for filename in files:
            filepath = os.path.join(root, filename)
            s3_location = p_s3_file_location  + filename
            s3_resource.meta.client.upload_file(filepath, p_s3_bucket, s3_location)

#listing the files present in s3 bucket
def fn_s3_get_files(p_landing_bucket,p_file_pattern):
    # print(p_landing_bucket)
    # print(p_file_pattern)
    s3_connection = rangerconnection.ranger_s3_connection()
    s3_client = s3_connection.fn_s3_client()

    kwargs = {'Bucket': p_landing_bucket , 'Prefix': p_file_pattern}
    
    while True:
        response = s3_client.list_objects_v2(**kwargs)
        for obj in response["Contents"]:
            key = obj['Key']
         
            if key.startswith(p_file_pattern):
                yield key
        try:
            kwargs['ContinuationToken'] = response['NextContinuationToken']
        except KeyError:
            break

def fn_s3_delete_files(p_s3_bucket,p_lst_s3_objects):
	s3_connection = rangerconnection.ranger_s3_connection()
	s3_resource =s3_connection.fn_s3_resource()
	for item in p_lst_s3_objects:
		obj = s3_resource.Object(p_s3_bucket, item)
		obj.delete()





def maindq(vr_param_args_location):
    try:
        
        vr_default_working_dir         = rangerconfig.cfg["pathsetting"]['tempdir'] # Temp Location
        rangerparams = pickle.load(open(vr_param_args_location, "rb" ))
        vr_data_domain_group_name      = rangerparams['p_data_domain_group_name'] 
        vr_s3_landing_bucket    = rangerparams['p_source_hostname'] # S3 Inprogress Bucet name
        vr_s3_inprogress_bucket = rangerparams['p_target_hostname'] # S3 Inprogress Bucet name
        vr_file_pattern_name    = rangerparams['p_source_data_entity_prefix'] # File name pattern to serch in S3 inprogress bucket. Patterns can be separated using semi-colon(;)
        vr_field_delimiter      = rangerparams['p_source_delimiter']  # File column separator
        vr_s3_file_location     = rangerparams['p_source_schema_name']  # File location within S3 bucket
        vr_field_enclosure      = rangerparams['p_source_field_enclosure']  # Any filed enclosure otherwise pass null string
        vr_skip_no_of_lines     = rangerparams['p_source_skip_number_of_lines']  # Number of lines to skip, like headers
        vr_file_suffix          = rangerparams['p_source_data_entity_extension']  # List of file suffix like .csv;.txt etc
        vr_data_pipe_layer      = rangerparams['p_dataparq_layer_name']
        vr_data_format          = rangerparams['p_data_format']
        vr_lst_s3_objects = []
        for i in range(len(vr_data_format)):
            if vr_data_format[i]==None:
                vr_data_format[i]=''
        
        vr_data_governance_short_code =rangerparams['p_data_governance_short_code']
        vr_data_governance_type_short_code =rangerparams['p_data_governance_type_short_code']
        vr_column_names =rangerparams['p_column_names']
        data_stages=1
        
        vr_s3_target        = rangerparams['p_data_domain_group_name'] + '/' + rangerparams['p_source_schema_name'] + '/' +  rangerparams['p_target_data_entity_name']  + '/' + 'output/'
        vr_local_base_folder = os.path.join(vr_default_working_dir, vr_data_domain_group_name, rangerparams['p_target_schema_name'],)
        
        l_file_list = vr_file_pattern_name.split(';')
        l_file_pattern = tuple(l_file_list)
        
        l_suffixes	   = vr_file_suffix.upper().split(';')
        l_tpl_suffixes = tuple(l_suffixes)
        l_source_folder = os.path.join(vr_local_base_folder , 'sourcedir')
        l_target_folder = os.path.join(vr_local_base_folder , 'targetdir')
        l_reject_folder = os.path.join(vr_local_base_folder , 'rejectdir')

        fn_create_folder(p_folder_name = l_source_folder)
        fn_create_folder(p_folder_name = l_target_folder)
        fn_create_folder(p_folder_name = l_reject_folder)
        vr_data_source_obj_name        = rangerparams['p_target_data_entity_prefix']   # To be file name for the merged files
        timestr = time.strftime("%Y%m%d")

        corrected_data_target   = os.path.join(l_target_folder, vr_data_source_obj_name +'_accepted_data'+ '.csv')
        rejected_data_target   = os.path.join(l_target_folder, vr_data_source_obj_name +'_rejected_data'+ '.csv')        
        
        notification_data_target =os.path.join(l_target_folder, vr_data_source_obj_name +'_notification_data'+ '.csv')
        freject_file   = os.path.join(l_reject_folder, vr_data_source_obj_name + '_ERROR_' + timestr + '.csv')
                      
        #File suffix
        l_suffixes     = vr_file_suffix.upper().split(';')
        l_tpl_suffixes = tuple(l_suffixes)
        
        for l_src_file_name in l_file_pattern:
            if vr_data_pipe_layer == 'dataquality':
                l_src_file_location = rangerparams['p_data_domain_group_name']  + '/' + vr_s3_file_location +  '/' + rangerparams['p_source_data_entity_name'] + '/output/' + l_src_file_name
                
            else:
                l_src_file_location = vr_s3_file_location + '/' + l_src_file_name
                
            #Get all the files 
            for key in fn_s3_get_files( p_landing_bucket = vr_s3_landing_bucket,
                                        p_file_pattern   = l_src_file_location):
                
                s3_file_name = key
                # print(s3_file_name)
                vr_lst_s3_objects.append(s3_file_name)
                local_s3_file_name = os.path.basename(key)
                local_folder_file_name      = os.path.join(l_source_folder, local_s3_file_name)                               
                
                vr_target_path =  rangerparams['p_data_domain_group_name'] + '/' + rangerparams['p_target_schema_name'] + '/' +  rangerparams['p_target_data_entity_name']  + '/' + 'input'
                vr_target_file_name =  rangerparams['p_data_domain_group_name'] + '/' + rangerparams['p_target_schema_name'] + '/' +  rangerparams['p_target_data_entity_name'] + '/' + rangerparams['p_target_data_entity_name'] + '.csv'
                               
                if local_s3_file_name.upper().endswith(l_tpl_suffixes):
                    vr_lst_s3_objects.append(s3_file_name)
                
                fn_s3_download_files(p_inprogress_bucket		 = vr_s3_landing_bucket,
                                    p_s3_file_name			     = s3_file_name,
                                    p_local_folder_file_name     = local_folder_file_name )  
            
    except Exception as msg:
           rangerfilelogging.error(msg)
           print(msg)
    
    
    for  path, dir, files in os.walk(l_source_folder):
        for filename in files:
            fr = path
            inputfilepath = path + os.sep + filename
            
            if inputfilepath.endswith(".xlsx"):
                xls = pd.ExcelFile(inputfilepath)
                if len(xls.sheet_names) == 1:
                    df = pd.read_excel(xls)
                    
                else:
                    wb = load_workbook(inputfilepath, read_only=True)
                    if sheet_name in wb:
                        df= pd.read_excel(xls, sheet_name)
                    else:
                        n = os.path.basename(inputfilepath)
                        rn = n.replace('.xls', '')
                        print('No sheet_name in ' + rn)
                 
            
            elif(inputfilepath.endswith(".csv")):
                df = pd.read_csv(inputfilepath,encoding='ISO-8859-1',sep=vr_field_delimiter)                  

   
    
    prm_df = pd.DataFrame(list(zip(vr_data_governance_short_code, vr_data_governance_type_short_code,vr_column_names,vr_data_format)), 
               columns =['method_name', 'rule_type','column_names','data_format'])        
    prm_df['rule_type'] = prm_df['rule_type'].map(str)
    prm_df['column_names'] = '['+prm_df['column_names'].map(str)+']'
    prm_df['data_format'] = prm_df['data_format'].map(str)
    prm_df['concat_rule_col_fmt']=prm_df['rule_type']+'+-'+prm_df['column_names']+'+-'+prm_df['data_format']
       
    prm_df=prm_df.drop(['rule_type','column_names','data_format'], axis = 1)
    prm_df['concat_rule_col_fmt']=prm_df.groupby(["method_name"])['concat_rule_col_fmt'].transform( 
                                              lambda x: '+-'.join(x))
    prm_df['All_columns_list']=prm_df['method_name']+'+-'+prm_df['concat_rule_col_fmt']  
    prm_df=prm_df.drop(['method_name','concat_rule_col_fmt'], axis = 1)
    prm_df=prm_df.drop_duplicates().reset_index(drop=True)   
    pd.set_option("display.max_rows", None, "display.max_columns", None)       
    ruletype=prm_df['All_columns_list'].tolist()    
    sc_df_list=df.columns.tolist()
    sr_df_list=df.columns.tolist()
    sn_df_list=df.columns.tolist()
    sr_df_list.append('Anomaly_Column')
    sr_df_list.append('rejection_reason')
    sn_df_list.append('Anomaly_Column')
    sn_df_list.append('notification_reason')

    ##--CALLING METHODS---##
    c_df,r_df,n_df = all_methods(df,ruletype)
    
    ##--ACCEPTED OUTPUT---##
    c_df=pd.DataFrame(c_df,columns=sc_df_list)
    c_df.to_csv(corrected_data_target,index=False,encoding='ISO-8859-1')
    
    ##--REJECTED OUTPUT---##
    if len(r_df)>0:
        r_df = r_df.replace(np.nan,'',regex=True)
        r_df=r_df.sort_index(axis=0)
        r_df_lst=r_df.columns.difference(['rejected_row','Anomaly_Column','notification_reason','rejection_reason']).tolist()    
        r_df['Anomaly_Column']=r_df.groupby(r_df_lst)['Anomaly_Column'].transform(lambda x: ','.join(x))         
        r_df['rejection_reason']=r_df.groupby(r_df_lst)['rejection_reason'].transform(lambda x: ','.join(x))             
        r_df=pd.DataFrame(r_df,columns=sr_df_list)
        r_df=r_df.drop_duplicates()
        r_df.to_csv(rejected_data_target,index=False,encoding='ISO-8859-1')

    ##--NOTIFICATION OUTPUT---##
    if len(n_df)>0:
        n_df = n_df.replace(np.nan,'',regex=True)
        n_df=n_df.sort_index(axis=0)
        n_df_lst=n_df.columns.difference(['rejected_row','Anomaly_Column','notification_reason','rejection_reason']).tolist()    
        n_df['Anomaly_Column']=n_df.groupby(n_df_lst)['Anomaly_Column'].transform(lambda x: ','.join(x))         
        n_df['notification_reason']=n_df.groupby(n_df_lst)['notification_reason'].transform(lambda x: ','.join(x))             
        n_df=pd.DataFrame(n_df,columns=sn_df_list)
        n_df=n_df.drop_duplicates()   
        n_df.to_csv(notification_data_target,index=False,encoding='ISO-8859-1')

    fn_s3_upload_files(p_local_target_folder   = l_target_folder,
                        p_s3_bucket			   = vr_s3_inprogress_bucket,
                        p_s3_file_location     = vr_s3_target)
    
    # print(vr_s3_landing_bucket,vr_lst_s3_objects)
    fn_s3_delete_files(p_s3_bucket = vr_s3_landing_bucket, p_lst_s3_objects = vr_lst_s3_objects)





def nul_reg(c_df,lst,col_date):
    if col_date != []:
        c_df=c_df.drop(columns=col_date)
    col_name = c_df.select_dtypes(include=['object'])
    col_names=col_name.columns.tolist()
    c_df = pd.get_dummies(c_df, columns= col_names)
    df1 = c_df.iloc[:, :-1]
    X_train=[]
    Y_train=[]
    for i in lst:
        train_df = df1.dropna()
        X_train.append(train_df.drop(i,axis = 1))
        Y_train.append(train_df[i])
    X_test=[]
    for i in lst:
        test_df = df1[df1[i].isnull()]
        X_test.append(test_df.drop(i,axis = 1))
    pipe_dic = ['ExtremeGraidentBoosting']*len(lst)
    pipe_dict =  [el1+'_'+el2 for el1 in sorted(set(pipe_dic)) for el2 in lst]
    
    pipe_xgb1 = Pipeline([('scalar1',StandardScaler()),
                     ('pca1',PCA(n_components=2)) ,('xgb',xgboost.XGBRegressor(learning_rate =0.20, max_depth=30,min_child_weight=9,
              n_estimators=750,gamma=0.9))])
    
    score = []
    values =[]
    
    for (a,b,c) in zip(X_train,Y_train,X_test):
        pipe_xgb1.fit(a,b)
        score.append(pipe_xgb1.score(a,b))
        values.append(pipe_xgb1.predict(c))
    pred_score = {pipe_dict[i]: score[i] for i in range(len(pipe_dict))} 
    pred_value = {pipe_dict[i]: values[i] for i in range(len(pipe_dict))} 
    
    return pred_value


def null_class(c_df,lst,col_date):
    if col_date != []:
        c_df=c_df.drop(columns=col_date)
    col_name = c_df.select_dtypes(include=['object'])
    col_names=col_name.columns.tolist()
    r = [[c for c in col_names if c !=cn] for cn in lst]
    test=[]
    df3=[]
    for i in r:test.append(pd.get_dummies(c_df, columns= i))
    for i in test:df3.append(i.iloc[:, :-1])
    train_df=[]
    for c_df in df3:train_df.append(c_df.dropna())
    x=[]
    y=[]
    Y_train=[]
    for c_df in train_df:
        for col in lst:
            if col in c_df:
                lb = LabelEncoder()
                x.append(c_df[col])
    for c_df in x:y.append(lb.fit_transform(c_df))
    df12=[]
    for i in x:df12.append(i.to_frame())
    Y_train=[]
    for c_df in df12:
        Y_train.append(c_df)
    X_train = []   
    X =[]
    for i in x:Y_train.append(i)
    for c_df in train_df:
        for col in lst:
            if col in c_df:
                X_train.append(c_df.drop(col,axis = 1))
    test_df=[]
    test_df1 =[]
    for c_df in df3:
        for col in lst:
            if col in c_df:
                test_df1.append(c_df[c_df[col].isnull()])
    for c_df in test_df1:
        for col in lst:
            if col in c_df:
                test_df.append(c_df.drop(col,axis = 1))
        
    X_test=[]
    for c_df in test_df:
        for column in c_df:
            random_sample = c_df[column].dropna().sample(c_df[column].isnull().sum(),random_state =0)
            random_sample.index=c_df[c_df[column].isnull()].index
            c_df.loc[c_df[column].isnull(),column]=random_sample
    for c_df in test_df:X_test.append(c_df)
    pipe_dic = ['GraidentBoosting']*len(lst)
    
    pipe_gb1= Pipeline([('scalar1',StandardScaler()),
                     ('pca1',PCA(n_components=2)),('gb',GradientBoostingClassifier(learning_rate=0.05,n_estimators=500,max_depth=40,min_samples_split=60,
               min_samples_leaf=30))])
    
    pipe_dict = [el1+'_'+el2 for el1 in sorted(set(pipe_dic)) for el2 in lst]
    score = []
    values =[]
    
    for (a,b,c) in zip(X_train,Y_train,X_test):
        pipe_gb1.fit(a,b)
        score.append(pipe_gb1.score(a,b))
        values.append(pipe_gb1.predict(c))
    pred_score = {pipe_dict[i]: score[i] for i in range(len(pipe_dict))} 
    pred_value = {pipe_dict[i]: values[i] for i in range(len(pipe_dict))} 
    
    return pred_value

def outliers_reg(c_df,key,lst,lower,upper): 
    col_name = c_df.select_dtypes(include=['object'])
    col_names=col_name.columns.tolist()
    c_df=c_df.fillna(c_df.mean())
    
    ohe_df=pd.get_dummies(c_df,columns= col_names)
    train_df=ohe_df.copy()
    outliers = ohe_df[((ohe_df[key] > upper) | (ohe_df[key] < lower))]
    
    train_df=train_df[~train_df.isin(outliers)].dropna(how='all')
    pred_df=pd.DataFrame(columns=[key])

    if key in lst:      
        X_train=train_df.drop(key,axis=1)
        Y_train=train_df[key]
        X_test=outliers.drop(key,axis=1) 
        #Normalization
        sc= StandardScaler()
        X_train = sc.fit_transform(X_train)
        X_test=sc.transform(X_test)
        
        xgb=xgboost.XGBRegressor(learning_rate=0.05,n_estimators=500,max_depth=20,min_child_weight=5,
               gamma=0.5)
        xgb_model=xgb.fit(X_train,Y_train)
        # Trains the model and predicts on outlier data, total fits = cv * n_ter  for each column                                                                   
        #rd_search_xgb.fit(X_train,Y_train)
        y_pred=xgb_model.predict(X_test)
        acc=xgb_model.score(X_train,Y_train)
        pred_df[key]=y_pred
    return pred_df


####ALL_METHODS####
def all_methods(df,ruletype):    
    pd.set_option('mode.chained_assignment', None)
    c_df=df.copy()
    col_list_c_df=c_df.columns.tolist()
    n_df=pd.DataFrame()    
    r_df=pd.DataFrame()
    r_df_ac2=pd.DataFrame()
    n_df_ac2=pd.DataFrame()
    df_rejected_dmy = pd.DataFrame()
    lst=[]
    df_rej =[]
    counter=0
    counter1=0
    counter2=0
    counter3=0
    counter4=0
    counter5=0
    counter6=0
    c_df['rejected_row'] = 'No'
    # print(c_df.head(30))

    for features in df.columns:
        # print(c_df.head(30))
        for  i,rules in enumerate(ruletype):
            if 'Special_characters' in rules:
                if 'Auto_correction1' in rules and features in rules.split('Auto_correction1+-')[1].split('+-')[0]:
                    if c_df[features].dtype==np.object:
                        if not c_df[features].astype(str).str.contains(credit_card_num).any():
                            if not c_df[features].astype(str).str.contains(date).any():
                                if c_df[features].astype(str).str.contains(r"[^a-zA-Z0-9]+|[\s]").any():
                                    j=c_df[features].astype(str).str.contains(r"[^a-zA-Z0-9]+|[\s]")
                                    index_c_df=c_df.loc[j].index
                                    c_df.at[index_c_df,'rejected_row']='Yes'
                                    good_rec=c_df['rejected_row']=='No'
                                    c_df=c_df.where(good_rec).dropna(how='all')                                  

                
                if 'Auto_correction2' in rules and features in rules.split('Auto_correction2+-')[1].split('+-')[0]:
                    data_format=list(rules.split('Auto_correction2+-')[1].split('+-')[1].split(','))
                    if len(data_format)==1 and len(data_format[0])==0:
                        data_format=[""]
                        counter=0
                    if c_df[features].dtype==np.object :
                        if not c_df[features].astype(str).str.contains(credit_card_num).any(): 
                                if not c_df[features].astype(str).str.contains(date).any():                       
                                    if c_df[features].astype(str).str.contains(r"[^a-zA-Z0-9]+|[\s]").any():
                                        c_df[features]=c_df[features].replace(to_replace="[^a-zA-Z0-9]+|[\s]", value=data_format[counter], regex=True)
                                        counter=counter+1
                                        

                if 'Rejection' in rules and features in rules.split('Rejection+-')[1].split('+-')[0]:
                    if df[features].dtype==np.object:
                        if not df[features].astype(str).str.contains(credit_card_num).any():   
                            if not df[features].astype(str).str.contains(date).any():                               
                                if df[features].astype(str).str.contains(r"[^a-zA-Z0-9]+|[\s]").any():
                                    j=df[features].astype(str).str.contains(r"[^a-zA-Z0-9]+|[\s]")
                                    index_df=df.loc[j].index
                                    df.at[index_df,'rejected_row']='Yes'
                                    rows = df.loc[j]
                                    rows['Anomaly_Column']=features
                                    rows['rejection_reason']='special_characters'
                                    r_df=pd.concat([r_df,rows])
                                    
                                
                
                if 'Notification' in rules and features in rules.split('Notification+-')[1].split('+-')[0]:
                    if df[features].dtype==np.object:  
                        if not df[features].astype(str).str.contains(credit_card_num).any():  
                            if not df[features].astype(str).str.contains(date).any():                 
                                if df[features].astype(str).str.contains(r"[^a-zA-Z0-9]+|[\s]").any():
                                    j=df[features].astype(str).str.contains(r"[^a-zA-Z0-9]+|[\s]")
                                    rows = df.loc[j]                  
                                    rows['Anomaly_Column']=features
                                    rows['notification_reason']='special_characters'                                    
                                    n_df=pd.concat([n_df,rows])                                    
                                                                        
    
            if 'Null_values' in rules:
                if 'Auto_correction1' in rules and features in rules.split('Auto_correction1+-')[1].split('+-')[0]:
                    lst.append(features)
                    c_df= c_df.dropna(subset=lst)
                if 'Auto_correction2' in rules and features in rules.split('Auto_correction2+-')[1].split('+-')[0]:
                    if c_df[features].dtype == float or c_df[features].dtype == int:
                        c_df[features] = c_df[features].fillna(value=c_df[features].mean())
                    elif c_df[features].dtype == object:
                        c_df[features] = c_df[features].fillna(c_df[features].mode()[0])
                    if df[features].dtype == 'int':
                        c_df[features]=c_df[features].round(0)
                    elif df[features].dtype == 'float':
                        c_df[features]=c_df[features].round(decimals=2)
                if 'Auto_correction3' in rules and features in rules.split('Auto_correction3+-')[1].split('+-')[0]:
                    random_sample = c_df[features].dropna().sample(c_df[features].isnull().sum(),random_state =1,replace=True)
                    ind_list = c_df[c_df[features].isnull()].index
                    for ind,r in zip(ind_list,random_sample):
                        c_df[features].loc[ind]=r
                    if df[features].dtype == 'int':
                        c_df[features]=c_df[features].round(0)
                    elif df[features].dtype == 'float':
                        c_df[features]=c_df[features].round(decimals=2)
                if 'Auto_correction4' in rules and features in rules.split('Auto_correction4+-')[1].split('+-')[0]:
                    new_col_lst_1=list(rules.split('Auto_correction4+-')[1].split('+-')[0].replace('[','').replace(']','').split(","))                                      
                    selected_columns = c_df[new_col_lst_1]
                    c_df_new = selected_columns.copy()
                    c_df_new = c_df_new.loc[:, c_df_new.isnull().any()]
                    col_int = (c_df_new.select_dtypes(include=['int','float']).columns).tolist()
                    df_new_null = c_df_new.dropna()
                    col_str_name =[]
                    valid=[]
                    invaild=[]
                    col_date=[]
                    for col_name in df_new_null:
                        if df_new_null[col_name].dtypes== np.object:
                            for i in df_new_null[col_name]:
                                try:
                                    valid.append(pd.Timestamp(i))
                                except ValueError:
                                    invaild.append(i)
                            if valid ==[]:
                                col_str_name.append(col_name)
                            elif valid != []:
                                col_date.append(col_name)
                                        
                    col_str= col_str_name
                    if len(col_int)!= 0:
                        lst = col_int
                        t = nul_reg(c_df,lst,col_date)
                        for key1 in t :
                            column_name = key1.split('_')[-1]
                            val = t[key1]
                            for j,v in zip(c_df[c_df[column_name].isna()].index, val):
                                c_df.loc[j, column_name] = v
                                if c_df[features].dtype == np.int64:
                                    c_df[features]=c_df[features].round(0)
                                elif c_df[features].dtype == np.float64:
                                    c_df[features]=c_df[features].round(decimals=2)
                    elif len(col_str)!=0:
                        lst = col_str
                        r= null_class(c_df,lst,col_date)
                        for key1 in r :
                            column_name = key1.split('_')[-1]
                            val = r[key1]
                            for j,v in zip(c_df[c_df[column_name].isna()].index, val):
                                c_df.loc[j, column_name] = v

                if 'Rejection' in rules and features in rules.split('Rejection+-')[1].split('+-')[0]:
                    if df[features].isnull().sum() >0:
                            rows=df[df[features].isnull()]                        
                            rows['Anomaly_Column']=features
                            rows['rejection_reason']='null_values'                                                       
                            r_df=pd.concat([r_df,rows])                           

                if 'Notification' in rules and features in rules.split('Rejection+-')[1].split('+-')[0]:
                    if df[features].isnull().sum() >0:                        
                        rows=df[df[features].isnull()]                        
                        rows['Anomaly_Column']=features
                        rows['notification_reason']='null_values'
                        n_df=pd.concat([n_df,rows])     
        
            ####----OUTLIER------###
            if 'outliers' in rules:
                if c_df[features].dtype==np.int64 or c_df[features].dtype==np.float64:           
                    # calculating lower and upper limit using IQR             
                    q1,q3 = c_df[key].quantile(0.25),c_df[key].quantile(0.75)
                    IQR = q3-q1
                    lower = q1 - 1.5*IQR
                    upper = q3+ 1.5*IQR   
                    print(lower,upper)  
            
            # Auto_correction1 for dropping the records having outliers 
                if 'Auto_correction1' in rules and features in rules.split('Auto_correction1+-')[1].split('+-')[0]:
                    if (c_df[features] > upper).any() | (c_df[features] < lower).any():                             
                        rows = c_df[(c_df[features] > upper) | (c_df[features] < lower)]
                        c_df=c_df[~c_df.isin(rows)].dropna(how='all')
            
            # Auto_correction2 for treatment of outliers with mean value
                if 'Auto_correction2' in rules and features in rules.split('Auto_correction2+-')[1].split('+-')[0]:
                    if (c_df[features] > upper).any() | (c_df[features] < lower).any():
                        c_df[features] = np.where((c_df[features] > upper) | (c_df[features] < lower),c_df[features].mean(),c_df[features])                                                                                          
                    if  df[features].dtype == np.int64:
                        c_df[features]=c_df[features].round(0)
                    else:
                        c_df[features]=c_df[features].round(decimals=2)
            
            # Auto_correction3 for treatment of outliers using sampling method
                if 'Auto_correction3' in rules and features in rules.split('Auto_correction3+-')[1].split('+-')[0]:
                    if (c_df[features] > upper).any() | (c_df[features] < lower).any():  
                        rows = c_df[(c_df[features] > upper) | (c_df[features] < lower)] 
                        l=len(rows[features]) 
                        ind_list=c_df.index[(c_df[features] > upper) | (c_df[features] < lower)].tolist()               
                        random_sample = c_df[features].sample(n=l,weights=((c_df[features]>lower) & (c_df[features]<upper)))  #;print("r",random_sample)
                        for ind,r in zip(ind_list,random_sample):
                            c_df[features].loc[ind]=r
            
            # Auto_correction4 for treatment of outliers with predicted values from the regression model
                if 'Auto_correction4' in rules and features in rules.split('Auto_correction4+-')[1].split('+-')[0]:
                    new_col_lst_1=list(rules.split('Auto_correction4+-')[1].split('+-')[0].replace('[','').replace(']','').split(","))
                    q1_all,q3_all = c_df.quantile(0.25),c_df.quantile(0.75)
                    IQR_all = q3_all-q1_all
                    lower_all = q1_all - 1.5*IQR_all
                    upper_all = q3_all+ 1.5*IQR_all  
                    df_new = c_df[new_col_lst_1].copy()
                    df_new = df_new.loc[:, (df_new > upper_all).any() | (df_new < lower_all).any()]
                    col_int = (df_new.select_dtypes(include=[np.int64,np.float64]).columns).tolist() 

                    if len(col_int)!= 0:
                        lst = col_int
                        predicted_val = outliers_reg(c_df,features,lst,lower,upper)              
                        if predicted_val is None:
                            continue
                        else:
                            for i in predicted_val :
                                val = predicted_val[i]
                                for j,v in zip(c_df[(c_df[features] > upper) | (c_df[features] < lower)].index, val):                           
                                    c_df.loc[j, i] = v                                              
                                    if df[features].dtype == np.int64:
                                        c_df[features]=c_df[features].round(0)
                                    elif df[features].dtype == np.float64:
                                        c_df[features]=c_df[features].round(decimals=2)
                        
                # Rejection having those dropped records or outliers from Auto_correction1,
                # r_df and n_df contains the outlier data     
                if 'Rejection' in rules and features in rules.split('Rejection+-')[1].split('+-')[0]:                
                    if (df[features] > upper).any() | (df[features] < lower).any():                                   
                        rows = df[(df[features] > upper) | (df[features] < lower)]
                        rows['Anomaly_Column']=features
                        rows['rejection_reason']='Outliers'
                        # r_df=[r_df,rows]
                        r_df=pd.concat([r_df,rows])

                if 'Notification' in rules and features in rules.split('Notification+-')[1].split('+-')[0]:
                    if (df[features] > upper).any() | (df[features] < lower).any():                                 
                        rows = df[(df[features] > upper) | (df[features] < lower)]
                        rows['Anomaly_Column']=features
                        rows['notification_reason']='Outliers'
                        # n_df=[n_df,rows]
                        n_df=pd.concat([n_df,rows])
    

            ##--------------------------------STANDARD FORMAT--------------------------------------------------------------

            if 'Standard_formats' in rules:
                if 'Auto_correction1' in rules and features in list(rules.split('Auto_correction1+-')[1].split('+-')[0].replace('[','').replace(']','').split(',')):
                        data_format=list(rules.split('Auto_correction1+-')[1].split('+-')[1].replace('[','').replace(']','').split(','))
                        counter_con=list(rules.split('Auto_correction1+-')[1].split('+-')[0].replace('[','').replace(']','').split(','))
                        if len(counter_con)>counter1:                       
                            if 'numeric' in data_format[counter1]:
                                c_df = c_df[c_df[features].str.contains(num, na=True)]                               
                                
                            if 'alphabet' in data_format[counter1]:
                                c_df = c_df[c_df[features].str.contains(alpha, na=True)]                               
                            
                            if 'alphanum' in data_format[counter1]:
                                c_df = c_df[c_df[features].str.contains(alpha_num, na=True)]                                
                            
                            if re.search('MM',str(data_format[counter1])) or re.search('HH',str(data_format[counter1])):
                                for k, value in Date_formats.items():
                                    if k == data_format[counter1]:
                                        d_t = value
                                nulls=c_df[c_df[features].isnull()].index.tolist()
                                w_df=pd.to_datetime(c_df[features], format = d_t, errors='coerce')
                                w_df=w_df.to_frame()
                                w_df.columns = ['date']
                                w_df=w_df.drop(nulls)
                                c_null_to_drop=w_df[w_df['date'].isnull()].index.tolist()
                                c_df=c_df.drop(c_null_to_drop)
                            counter1=counter1+1
                            
                if 'Auto_correction2' in rules and features in list(rules.split('Auto_correction2+-')[1].split('+-')[0].replace('[','').replace(']','').split(',')):
                        data_format=list(rules.split('Auto_correction2+-')[1].split('+-')[1].replace('[','').replace(']','').split(','))
                        counter_con=list(rules.split('Auto_correction2+-')[1].split('+-')[0].replace('[','').replace(']','').split(','))
                        if len(counter_con)>counter2:
                            if 'numeric' in data_format[counter2]:
                                c_df[features] = c_df[features].str.replace(r"\D+", '')
                        
                            if 'alphabet' in data_format[counter2]:
                                c_df[features] = c_df[features].str.replace(r"[\d\W+]", '')
                            
                            if 'alphanum' in data_format[counter2]:
                                c_df[features] = c_df[features].str.replace(r'[\W]+', '')

                            if re.search('MM',str(data_format[counter2])) or re.search('HH',str(data_format[counter2])):                               
                                for k, value in Date_formats.items():
                                    if k == data_format[counter2]:
                                        d_t = value
                                nulls=c_df[c_df[features].isnull()].index.tolist()
                                df1=pd.to_datetime(c_df[features],errors='coerce')
                                df1_mdy=pd.to_datetime(c_df[features], format= '%m%d%Y',errors='coerce')
                                df1_dmy=pd.to_datetime(c_df[features], format= '%d%m%Y',errors='coerce')                                
                                df1=df1.dt.strftime(d_t)
                                df2=df1.to_frame()
                                df2.columns = ['date']
                                df2=df2.drop(nulls)
                                df2_nulls=df2[df2['date'].isnull()].index.tolist()
                                df2_notnulls=df2[df2['date'].notnull()].index.tolist()
                                cdf2=df2.dropna()                                
                                df1_mdy=df1_mdy.dt.strftime(d_t)
                                df2_mdy=df1_mdy.to_frame()
                                df2_mdy.columns = ['date']
                                df2_mdy=df2_mdy.drop(nulls)
                                df2_nulls_mdy=df2_mdy[df2_mdy['date'].isnull()].index.tolist()
                                df2_notnulls_mdy=df2_mdy[df2_mdy['date'].notnull()].index.tolist()
                                cdf2_mdy=df2_mdy.dropna()                                
                                df1_dmy=df1_dmy.dt.strftime(d_t)
                                df2_dmy=df1_dmy.to_frame()
                                df2_dmy.columns = ['date']
                                df2_dmy=df2_dmy.drop(nulls)
                                df2_nulls_dmy=df2_dmy[df2_dmy['date'].isnull()].index.tolist()
                                df2_notnulls_dmy=df2_dmy[df2_dmy['date'].notnull()].index.tolist()
                                cdf2_dmy=df2_dmy.dropna()
                                s_c=set(df2_nulls) & set(df2_nulls_mdy) & set(df2_nulls_dmy)
                                w_df_c=list(s_c)
                                c_df=c_df.drop(w_df_c)
                                c_df.loc[cdf2.index,[features]] = cdf2.values
                                c_df.loc[cdf2_mdy.index,[features]] = cdf2_mdy.values
                                c_df.loc[cdf2_dmy.index,[features]] = cdf2_dmy.values
                                ab = itertools.chain(df2_notnulls, df2_notnulls_mdy, df2_notnulls_dmy,nulls)
                                w_df_r=list(ab)
                                c_df_1 = df
                                r_df_ac2=c_df_1.drop(w_df_r)
                                n_df_ac2=c_df_1.drop(w_df_r)                                
                            counter2=counter2+1
                                
                if 'Rejection' in rules and features in list(rules.split('Rejection+-')[1].split('+-')[0].replace('[','').replace(']','').split(',')):
                        data_format=list(rules.split('Rejection+-')[1].split('+-')[1].replace('[','').replace(']','').split(','))
                        counter_con=list(rules.split('Rejection+-')[1].split('+-')[0].replace('[','').replace(']','').split(','))
                        if len(counter_con)>counter3:                
                            if 'numeric' in data_format[counter3]:
                                rows = df[~df[features].str.contains(num, na=True)]
                                rows['Anomaly_Column']=features
                                rows['rejection_reason']='Standard_formats'                                
                                r_df=pd.concat([r_df,rows])                                
                                                                        
                            if 'alphabet' in data_format[counter3]:
                                rows = df[~df[features].str.contains(alpha, na=True)]
                                rows['Anomaly_Column']=features
                                rows['rejection_reason']='Standard_formats'
                                r_df=pd.concat([r_df,rows])                               
                                
                            if 'alphanum' in data_format[counter3]:
                                rows = df[~df[features].str.contains(alpha_num, na=True)]
                                rows['Anomaly_Column']=features
                                rows['rejection_reason']='Standard_formats'
                                r_df=pd.concat([r_df,rows])                               
                                
                            if re.search('MM',str(data_format[counter3])) or re.search('HH',str(data_format[counter3])):
                                for k, value in Date_formats.items():
                                    if k == data_format[counter3]:
                                        d_t = value
                                invalid_rows=[]
                                nulls=df[df[features].isnull()].index.tolist()
                                w_df=pd.to_datetime(df[features], format = d_t, errors='coerce')
                                w_df=w_df.to_frame()
                                w_df.columns = ['date']
                                w_df=w_df.drop(nulls)
                                r_null_to_drop=w_df[w_df['date'].notnull()].index.tolist()
                                rej_df=df.drop(r_null_to_drop)
                                rej_df = rej_df[features].dropna()
                                if r_df_ac2.shape[0] == [0]:
                                    rows = rej_df 
                                else:
                                    ind=rej_df.index.tolist()                             
                                    new_rows=df.loc[ind]
                                    new_rows['Anomaly_Column']=features
                                    new_rows['rejection_reason']='Standard_formats'                                    
                                    r_df=pd.concat([r_df,new_rows])
                                counter3=counter3+1
                                
                if 'Notification' in rules and features in list(rules.split('Notification+-')[1].split('+-')[0].replace('[','').replace(']','').split(',')):
                        data_format=list(rules.split('Notification+-')[1].split('+-')[1].replace('[','').replace(']','').split(','))
                        counter_con=list(rules.split('Notification+-')[1].split('+-')[0].replace('[','').replace(']','').split(','))
                        if len(counter_con)>counter4:                
                            if 'numeric' in data_format[counter4]:
                                rows = df[~df[features].str.contains(num, na=True)]
                                rows['Anomaly_Column']=features
                                rows['notification_reason']='Standard_formats'                                
                                n_df=pd.concat([n_df,rows])                                

                            if 'alphabet' in data_format[counter4]:
                                rows = df[~df[features].str.contains(alpha, na=True)]
                                rows['Anomaly_Column']=features
                                rows['notification_reason']='Standard_formats'                                
                                n_df=pd.concat([n_df,rows])                                
                            
                            if 'alphanum' in data_format[counter4]:
                                rows = df[~df[features].str.contains(alpha_num, na=True)]
                                rows['Anomaly_Column']=features
                                rows['notification_reason']='Standard_formats'                                
                                n_df=pd.concat([n_df,rows])                                
                            
                            if re.search('MM',str(data_format[counter4])) or re.search('HH',str(data_format[counter4])):
                                for k, value in Date_formats.items():
                                    if k == data_format[counter4]:
                                        d_t = value
                                invalid_rows=[]
                                nulls=df[df[features].isnull()].index.tolist()
                                w_df=pd.to_datetime(df[features], format = d_t, errors='coerce')
                                w_df=w_df.to_frame()
                                w_df.columns = ['date']
                                w_df=w_df.drop(nulls)
                                r_null_to_drop=w_df[w_df['date'].notnull()].index.tolist()
                                rej_df=df.drop(r_null_to_drop)
                                rej_df = rej_df[features].dropna()
                                if r_df_ac2.shape[0] == [0]:
                                    rows = rej_df 
                                else:
                                    ind=rej_df.index.tolist()                             
                                    new_rows=df.loc[ind]
                                    new_rows['Anomaly_Column']=features
                                    new_rows['notification_reason']='Standard_formats'
                                    n_df=pd.concat([n_df,new_rows])
                                counter4=counter4+1    
    
    
            #####--Business DQ Rules--#####

            if 'Business_dq_rules' in rules:                
                ####filter####
                if 'Auto_correction1' in rules and features in rules.split('Auto_correction1+-')[1].split('+-')[0]:
                    data_format=list(rules.split('Auto_correction1+-')[1].split('+-')[1].replace('[','').replace(']','').split(','))
                    data_format=''.join(data_format)            
                    if c_df[features].dtype == np.object:
                        df_correct = c_df.query(data_format)
                        c_df=df_correct
                        index = c_df.index
                        rows_r=pd.DataFrame()                                  
                        rows_r=df.drop(index)
                        rows_n=pd.DataFrame()                                  
                        rows_n=df.drop(index)                  
                        rows_r['Anomaly_Column']=features
                        rows_n['Anomaly_Column']=features
                        rows_r['rejection_reason']='Business_dq_rules'
                        rows_n['notification_reason']='Business_dq_rules'                      
                        r_df=pd.concat([r_df,rows_r])
                        n_df=pd.concat([n_df,rows_n])
                        if c_df.empty:
                            print("except")
                            temp_df=''
                            n_df='Enter a value which matches the d-type of the column'+temp_df
                            r_df='Enter a value which matches the d-type of the column'+temp_df                
                    else:
                        df_correct = c_df.query(data_format)
                        c_df=df_correct
                        index = c_df.index
                        rows_r=pd.DataFrame()                                  
                        rows_r=df.drop(index)
                        rows_n=pd.DataFrame()                                  
                        rows_n=df.drop(index)                   
                        rows_r['Anomaly_Column']=features
                        rows_r['rejection_reason']='Business_dq_rules' 
                        rows_n['Anomaly_Column']=features
                        rows_n['notification_reason']='Business_dq_rules'
                        r_df=pd.concat([r_df,rows_r])
                        n_df=pd.concat([n_df,rows_n]) 
                                                            
                # pattern matching    
                if 'Auto_correction2' in rules and features in rules.split('Auto_correction2+-')[1].split('+-')[0]:                        
                        data_format=list(rules.split('Auto_correction2+-')[1].split('+-')[1].replace('[','').replace(']','').split(','))                        
                        counter_con=list(rules.split('Auto_correction2+-')[1].split('+-')[0].replace('[','').replace(']','').split(','))                        # print(counter5)
                        c_df = c_df.replace(np.nan,'',regex=True)
                        df = df.replace(np.nan,'',regex=True)
                        if len(counter_con)>counter5:
                            if '\d' in data_format[counter5]:                                
                                c_df = c_df[c_df[features].str.match(data_format[counter5])]                                
                                rows_r = df[~df[features].str.match(data_format[counter5])]
                                rows_n = df[~df[features].str.match(data_format[counter5])]                                                                            
                                rows_r['Anomaly_Column']=features
                                rows_r['rejection_reason']='Business_dq_rules' 
                                rows_n['Anomaly_Column']=features
                                rows_n['notification_reason']='Business_dq_rules' 
                                r_df=[r_df,rows_r]
                                r_df=pd.concat(r_df)                     
                                n_df=[n_df,rows_n]
                                n_df=pd.concat(n_df)                                
                        
                            if '\S' in data_format[counter5]:
                                c_df = c_df[c_df[features].str.match(data_format[counter5])]                          
                                rows_r = df[~df[features].str.match(data_format[counter5])]
                                rows_n = df[~df[features].str.match(data_format[counter5])]
                                rows_r['Anomaly_Column']=features
                                rows_r['rejection_reason']='Business_dq_rules'
                                rows_n['Anomaly_Column']=features
                                rows_n['notification_reason']='Business_dq_rules'                    
                                r_df=[r_df,rows_r]
                                r_df=pd.concat(r_df)                     
                                n_df=[n_df,rows_n]
                                n_df=pd.concat(n_df)
                            counter5=counter5+1           
                                        
                # add postfix/prefix to columns
                if 'Auto_correction3' in rules and features in rules.split('Auto_correction3+-')[1].split('+-')[0]:
                    r_df=pd.DataFrame()
                    n_df=pd.DataFrame()
                    data_format=list(rules.split('Auto_correction3+-')[1].split('+-')[1].replace('[','').replace(']','').split(','))
                    counter_con=list(rules.split('Auto_correction3+-')[1].split('+-')[0].replace('[','').replace(']','').split(','))
                    # print(counter6)
                    if len(counter_con)>counter6:
                        # print(data_format[counter6])
                        test_values=data_format[counter6].replace(features,'')
                        if data_format[counter6].startswith(features):
                            c_df[features] = c_df[features].astype(str)+test_values                       
                        elif data_format[counter6].endswith(features):
                            c_df[features] = test_values+c_df[features].astype(str)
                        counter6=counter6+1 
    
    ###### DUPLICATE CHECK #######   
    rule=[str for str in ruletype if re.match(r'[Duplicate_rows]+|^', str).group(0) in ['Duplicate_rows']]
    rule_str = ' '.join(map(str, rule))   
    a_c_df=c_df.copy(deep=True)
    n_c_df=c_df.copy(deep=True)   
    
    if 'Duplicate_rows' in rule_str:
        ##all columns
        if 'Auto_correction1' in rule_str:
            c_df['rejected_row'] = 'No'
            c_df_index=c_df[c_df.duplicated(subset=col_list_c_df,keep='last')].index
            c_df.at[c_df_index,'rejected_row']='Yes'            
            no_dup=c_df['rejected_row']=='No'
            c_df=c_df.where(no_dup).dropna(how='all').drop(['rejected_row'],axis=1)
        
        ##Based on column names     
        if 'Auto_correction2' in rule_str:
            col_lst_1=list(rule_str.split('Auto_correction2+-')[1].split('+-')[0].replace('[','').replace(']','').split(','))                                
            c_df['rejected_row'] = 'No'
            c_df_index=c_df[c_df.duplicated(subset=col_lst_1,keep='last')].index
            c_df.at[c_df_index,'rejected_row']='Yes'
            no_dup=c_df['rejected_row']=='No'
            c_df=c_df.where(no_dup).dropna(how='all').drop(['rejected_row'],axis=1)
        
        ##  DEDUP BASED ON ORDER BY COLUMNS  ##
        if 'Auto_correction3' in rule_str:
            col_lst_1=list(rule_str.split('Auto_correction3+-')[1].split('+-')[0].replace('[','').replace(']','').split(','))
            c_df['concat_cols'] = eval("c_df['"+"'].apply(str)+'#'+c_df['".join(col_lst_1)+"'].apply(str)")
            data_format=list(rules.split('Auto_correction3+-')[1].split('+-')[1].replace('[','').replace(']','').split(','))                
            two_split = np.array_split(data_format, 2)                
            sort_col=two_split[0].tolist()
            sort_order=two_split[1].tolist()
            # sort_order = [x.upper() for x in sort_order]
            sort_order = [False if i.upper()=='DESC' else True for i in sort_order]
            d = defaultdict(count)
            c_df = c_df.sort_values(by=sort_col, ascending=sort_order)
            c_df["rank"] = (c_df.groupby(sort_col, sort=False)['concat_cols'].transform(lambda x: [next(d[v]) for v in x]))
            c_df = c_df.loc[c_df['rank']==0]               

        # print(a_c_df)
        if 'Rejection' in rule_str:        
            col_lst_1=list(rule_str.split('Rejection+-')[1].split('+-')[0].replace('[','').replace(']','').split(','))                
            if len(col_lst_1)==0 or col_lst_1[0]=='None':
                print('HI')
                col_lst_1=col_list_c_df                    
            a_c_df['rejected_row'] = 'No'
            # print(a_c_df)
            a_c_df_index=a_c_df[a_c_df.duplicated(subset=col_lst_1,keep='last')].index
            a_c_df.at[a_c_df_index,'rejected_row']='Yes'
            dup=a_c_df['rejected_row']=='Yes'
            a_c_df=a_c_df.where(dup).dropna(how='all').drop(['rejected_row'],axis=1)
            a_c_df['Anomaly_Column']='All_Columns'
            a_c_df['rejection_reason']='duplicate_rows'
            r_df=pd.concat([r_df,a_c_df],ignore_index=True)
        
        if 'Notification' in rule_str:        
            col_lst_1=list(rule_str.split('Notification+-')[1].split('+-')[0].replace('[','').replace(']','').split(','))
            if len(col_lst_1)==0 or col_lst_1[0]=='None':
                col_lst_1=col_list_c_df
            n_c_df['rejected_row'] = 'No'
            n_c_df_index=n_c_df[n_c_df.duplicated(subset=col_lst_1,keep='last')].index
            n_c_df.at[n_c_df_index,'rejected_row']='Yes'
            dup=n_c_df['rejected_row']=='Yes'
            n_c_df=n_c_df.where(dup).dropna(how='all').drop(['rejected_row'],axis=1)
            n_c_df['Anomaly_Column']='All_Columns'
            n_c_df['notification_reason']='duplicate_rows'
            n_df=pd.concat([n_df,n_c_df],ignore_index=True)
            
    return c_df,r_df,n_df 
    
if __name__ == "__main__":    
    vr_param_args_location = sys.argv[1]
    maindq(vr_param_args_location)        