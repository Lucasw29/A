import sqlite3
import numpy as np
import pandas as pd
import os
import boto
from boto.s3.key import Key
import seaborn as sn
import matplotlib.pyplot as plt


def getTables(sql, DBName):
    conn = sqlite3.connect(DBName)
    cursor = conn.cursor()
    cursor.execute(sql)
    feat = cursor.fetchall()
    feat = pd.DataFrame(feat)
    return feat

def dataClean(data):
    nan = data.isnull()
    num_nonvalue = 0
    [num_nonvalue + 1 for i in nan if i is True]
    print("There are", num_nonvalue, "non-values in this dataset")
    df1 = data.dropna(axis=0, how='any')
    print("Delete", num_nonvalue, "non-values from dataset")
    df_modelA = df1.loc[df1[4] == "Model A"]
    df_modelB = df1.loc[df1[4] == "Model B"]
    cleanmA = remove_outlier_IQR(df_modelA[2])
    cleanmB = remove_outlier_IQR(df_modelB[2])
    cleanedmA = assignValue(df_modelA, 6, cleanmA)
    cleanedmB = assignValue(df_modelB, 6, cleanmB)
    cleanedmA = cleanedmA.values
    cleanedmB = cleanedmB.values
    return cleanedmA, cleanedmB

def remove_outlier_IQR(df):
    Q1 = df.quantile(0.25)
    Q3 = df.quantile(0.75)
    IQR = Q3 - Q1
    df_final = df[~((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR)))]
    return df_final

def assignValue(df, inx, value):
    df[inx] = np.nan
    for i in value.index:
        df.loc[i, 6] = value.loc[i]
    df.drop(df.columns[2], axis=1, inplace=True)
    df.dropna(inplace=True, how='any')
    df.reset_index(drop=True, inplace=True)
    return df

def convertArray(*df):
    arrays = np.array(df, dtype=object)
    return arrays


def upload_to_s3(aws_access_key_id, aws_secret_access_key, file, bucket, key, callback=None, md5=None,
                 reduced_redundancy=False, content_type=None):
    """
    Uploads the given file to the AWS S3
    bucket and key specified.

    callback is a function of the form:

    def callback(complete, total)

    The callback should accept two integer parameters,
    the first representing the number of bytes that
    have been successfully transmitted to S3 and the
    second representing the size of the to be transmitted
    object.

    Returns boolean indicating success/failure of upload.
    """
    try:
        size = os.fstat(file.fileno()).st_size
    except:
        # Not all file objects implement fileno(),
        # so we fall back on this
        file.seek(0, os.SEEK_END)
        size = file.tell()

    conn = boto.connect_s3(aws_access_key_id, aws_secret_access_key)
    bucket = conn.get_bucket(bucket, validate=True)
    k = Key(bucket)
    k.key = key
    if content_type:
        k.set_metadata('Content-Type', content_type)
    sent = k.set_contents_from_file(file, cb=callback, md5=md5, reduced_redundancy=reduced_redundancy, rewind=True)

    # Rewind for later use
    file.seek(0)

    if sent == size:
        return True
    return False






if __name__ == '__main__':
    feat0 = getTables("""select timestamp, machine, value, install_date, model, room from feat_0 f0 join static_data s on f0.machine = s.machine_id""", "C:\\Users\\xg811\\Desktop\\Resume\\Interview\\Tagup\\exampleco_db.db")
    feat1 = getTables("""select timestamp, machine, value, install_date, model, room from feat_1 f1 join static_data s on f1.machine = s.machine_id""", "C:\\Users\\xg811\\Desktop\\Resume\\Interview\\Tagup\\exampleco_db.db")
    feat2 = getTables("""select timestamp, machine, value, install_date, model, room from feat_2 f2 join static_data s on f2.machine = s.machine_id""", "C:\\Users\\xg811\\Desktop\\Resume\\Interview\\Tagup\\exampleco_db.db")
    feat3 = getTables("""select timestamp, machine, value, install_date, model, room from feat_3 f3 join static_data s on f3.machine = s.machine_id""", "C:\\Users\\xg811\\Desktop\\Resume\\Interview\\Tagup\\exampleco_db.db")
    f0mA = dataClean(feat0)[0]
    f0mB = dataClean(feat0)[1]
    f1mA = dataClean(feat1)[0]
    f1mB = dataClean(feat1)[1]
    f2mA = dataClean(feat2)[0]
    f2mB = dataClean(feat2)[1]
    f3mA = dataClean(feat3)[0]
    f3mB = dataClean(feat3)[1]
    array = convertArray(f0mA, f0mB, f1mA, f1mB, f2mA, f2mB, f3mA, f3mB)
    # np.save("data.npy", array)
"""
This is upload array to S3. It works but I won't my keys to Git. So I'll annotate it
"""
    # AWS_ACCESS_KEY = 'your_access_key'
    # AWS_ACCESS_SECRET_KEY = 'your_secret_key'
    # file = open('data.npy', 'r+')
    # key = file.name
    # bucket = 'your-bucket'
    # if upload_to_s3(AWS_ACCESS_KEY, AWS_ACCESS_SECRET_KEY, file, bucket, key):
    #     print('Upload success')
    # else:
    #     print('Upload failed')
