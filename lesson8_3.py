import pandas as pd

def main():
    df = pd.read_csv('上市公司資料.csv')
    df1 = df.dropna()
    df2 = df1.reindex(columns=['公司代號','出表日期','公司名稱','產業別','營業收入-當月營收','營業收入-上月營收'])
    df3 = df2.rename(columns={
        '營業收入-上月營收':'上月營收',
        '營業收入-當月營收':'當月營收'
        })
    df3.to_csv('上市公司資料整理.csv',encoding = 'utf-8')
    df3.to_excel('上市公司資料整理.xlsx')
    print("存檔完成")
import pandas as pd
import numpy as np

# 建立一個包含 NaN 值的 DataFrame
data = {'col1': [10, np.nan, 30, np.nan],
        'col2': [40, 50, np.nan, 70],
        'col3': [np.nan, np.nan, np.nan, np.nan]}
df = pd.DataFrame(data, index=['A','B','C','D'])
print("\n原始 DataFrame:\n", df)

# 刪除任何欄位中含有 NaN 值的欄位
df_dropped_cols = df.dropna(axis=1)
print("\n刪除任何欄位中含有 NaN 值的 DataFrame:\n", df_dropped_cols)

#刪除只包含NaN的欄位
df_dropped_cols_all = df.dropna(axis=1, how='all')
print("\n刪除只包含NaN的欄位的DataFrame:\n", df_dropped_cols_all)

if __name__ == "__main__" :
    main()