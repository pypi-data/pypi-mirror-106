import argparse
import os
import pandas as pd
import hashlib

def main():
    COLUMN_NAME_ID = 'Id'
    COLUMN_NAME_APP_KEY = 'AppKey'
    COLUNM_NAME_APP_SECRTE = 'AppSecret'
    COLUNM_NAME_CUR_TIME = 'CurTime'
    COLUMN_NAME_CHECK_SUM = 'CheckSum'
    COLUMN_NAME_MD5 = 'MD5'
    COLUMN_NAME_BODY = 'Body'

    parser = argparse.ArgumentParser()
    parser.add_argument('--input-file', required=True, help='输入文件')
    parser.add_argument('--output-file', required=False, help='输出文件, 不填写将使用"${输入文件文件名}_signed.${输入文件扩展名}"')
    args = parser.parse_args()

    input_file = args.input_file
    if not os.path.isfile(input_file):
        print('--input-file 指定的文件不存在')
        exit(-1)

    output_file = args.output_file
    if output_file == None:
        output_file = os.path.splitext(input_file)[0] + '_signed' + os.path.splitext(input_file)[-1]
    if os.path.isfile(output_file):
        try:
            os.remove(output_file)
        except Exception:
            print('已存在的输出文件无法删除: ' + output_file)
            exit(-1)

    df = pd.read_excel(input_file)
    columnValues = df.columns.values

    hasIdColumn = True
    if not COLUMN_NAME_ID in columnValues:
        hasIdColumn = False
    if not COLUMN_NAME_APP_KEY in columnValues:
        print('列名缺失: ' + COLUMN_NAME_APP_KEY)
        exit(-1)
    if not COLUNM_NAME_APP_SECRTE in columnValues:
        print('列名缺失: ' + COLUNM_NAME_APP_SECRTE)
        exit(-1)
    if not COLUNM_NAME_CUR_TIME in columnValues:
        print('列名缺失: ' + COLUNM_NAME_CUR_TIME)
        exit(-1)
    if not COLUMN_NAME_BODY in columnValues:
        print('列名缺失: ' + COLUMN_NAME_BODY)
        exit(-1)

    result = []

    for index, row in df.iterrows():

        columnId = None
        if hasIdColumn:
            columnId = row[COLUMN_NAME_ID]
        appKey = row[COLUMN_NAME_APP_KEY]
        appSecret = row[COLUNM_NAME_APP_SECRTE]
        curTime = row[COLUNM_NAME_CUR_TIME]
        body = row[COLUMN_NAME_BODY]
        calMD5 = hashlib.md5(body.encode('utf-8')).hexdigest()
        calCheckSum = hashlib.sha1((str(appSecret) + calMD5 + str(curTime)).encode('utf-8')).hexdigest()
        result.append((columnId, appKey, appSecret, curTime, calCheckSum, calMD5, body))

    writer = pd.ExcelWriter(output_file, engine='openpyxl')
    df2 = pd.DataFrame(result, columns=[COLUMN_NAME_ID, COLUMN_NAME_APP_KEY, COLUNM_NAME_APP_SECRTE, COLUNM_NAME_CUR_TIME, COLUMN_NAME_CHECK_SUM, COLUMN_NAME_MD5, COLUMN_NAME_BODY])
    df2.to_excel(writer, index=False)
    writer.save()

if __name__ == '__main__':
    main()