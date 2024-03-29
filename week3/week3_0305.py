# -*- coding: utf-8 -*-
"""week3_0305.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ddj-jOTLQMc9NvaAWuz7cPrtXZ_OGZKX

from google colab import files #匯入套件

import pandas as pd

upload = files.upload() #開啟上傳介面並載入

data = pd.read_csv("剛剛上傳的檔案名稱")
"""

# from xxxx import yyyy 從xxxx函式庫中匯入yyyy模組
# import xxxx 匯入xxxx模組
# drive.mount 綁定雲端磁碟
# os.chdir 變更目錄
# ls -l 列出目錄下的檔案

from google.colab import drive
drive.mount('/content/gdrive/', force_remount=True)

import os
os.chdir("/content/gdrive/My Drive/112_2_LATIA/week3_030524/") # 切換目錄
!ls -l "/content/gdrive/My Drive/112_2_LATIA/week3_030524/" # 列出目錄下的檔案
#!ls -l "自行填寫正確的路徑"

# import xxxx as yy 匯入xxxx當作yy
# read_csv() 讀取csv檔案
# head() 顯示從頭(0)開始的資料行
# info() 顯示資料欄位基本資訊
# isna().sum() 計算缺失數量
# describe() 顯示資料的統計學資訊描述


import pandas as pd

csv_file = './112_student.csv'
#csv_file ="自行填寫正確的路徑"

#columns = [
#    "學年度","學校代碼","學校名稱","日間∕進修別","等級別","總計","男生計",
#    "女生計","一年級男","一年級女","二年級男","二年級女","三年級男","三年級女",
#    "四年級男","四年級女","五年級男","五年級女","六年級男","六年級女",
#    "七年級男","七年級女","延修生男","延修生女","縣市名稱","體系別"
#]
df = pd.read_csv(csv_file) # 讀取csv檔案
print(df.head(), '\n')

#查看資料欄位資訊
print('\n', df.info(verbose=True, show_counts=True))

print('\n', df.isna().sum()) # 計算缺失數量並印出來

#查看資料的統計學資訊描述
print('\n', df.describe(include='all'))

# import xxxx as yy 匯入xxxx當作yy
# set_printoptions() 設定列印的參數
# iloc[] 指定位置元素


import numpy as np
np.set_printoptions(precision=None, threshold=None, edgeitems=None, linewidth=None, suppress=None, nanstr=None, infstr=None, formatter=None, sign=None, floatmode=None)  # reset print options
##threshold
# 當要列印的陣列太大時，NumPy會自動以...代替一部分的內容，以減少篇幅！
# 但是可以透過全域設定set_printoptions設定threshold(門檻值)，
# 元素數量少於或等於門檻值的陣列就會全部列印出來，
# 相反地，元素數量高於門檻值，列印時就會省略部分內容。
# 陣列大小:20，門檻值20 => 陣列元素數量小於等於門檻值，應列印全部內容
# 讓列印出來的資料不斷行，使用lindwidth參數
# 讓列印出來的資料不斷列，使用threshold參數

# 查看 df 前幾筆資料並且讓列印出來的資料不斷行
np.set_printoptions(linewidth=np.inf, threshold=np.inf)
#np.set_printoptions(threshold=12, linewidth=30, edgeitems=0)
print(df.iloc[0:100,])

"""# 1.哪間大專院校有最多的博士生"""

# df['', ''] 取出想要觀看的欄位
# df1['等級別'] == 'D 博士' 篩選等級別為"D 博士"的資料
# sort_values(by='xx', ascending=False) 依據xx從大到小排序並印出結果 (sort_values, by, ascending)
# head(n) 顯示從頭(0)開始的資料行到n-1行，總共n行

df1 = df[['學年度', '學校代碼', '學校名稱', '等級別', '總計', '男生計', '女生計']] # 取出想要觀看的欄位
print("本資料集共有", len(df1), "筆紀錄")

df1_1 = df1[df1['等級別'] == 'D 博士']
print("有招生博士學制的學校數量為", len(df1_1), "\n")
df1_1_sorted = df1_1.sort_values(by='總計', ascending=False)
print(df1_1_sorted.head(), '\n')
print("112學年度在籍的博士生最多人數第1名為", df1_1_sorted.head(1)["學校名稱"].values)

"""# 2. 國立？所；私立？所"""

# 建立空字串
# 使用for in迴圈，配合if else條件，取出xx與yy並放入新的空字串中
# df["空字串的欄位名稱"] = 新的"空字串變數" 目的是在DataFrame尾巴處新增一個欄位
# drop_duplicates('xxxx') 篩選掉重複的xxxx資料
# value_counts(xxxx) 計算xxxx的筆數

type_list = []

for i in df['學校名稱']:
    if ('國立' in i) or ('市立' in i):
        type_list.append('國立')
    else:
        type_list.append('私立')

df['公私立'] = type_list # 將 Dataframe 新增「公私立」column

df2 = df.drop_duplicates('學校代碼')
count = df2['公私立'].value_counts()

print(df2)
print(f"本資料集共收集了 {len(df2)} 所學校，其中公立：{count['國立']} 所；私立：{count['私立']} 所。")

"""# 3. 各等級別學制共有？所"""

# drop_duplicates(subset=['xxxx']) 篩選掉重複的xxxx資料(2種以上)
# value_counts(xxxx) 計算xxxx的筆數
# 使用for in迴圈，依序列出所有xxxx的數量(count[]), 並顯示xxxx[2:]從第2個字元到結束的所有字元

df3 = df.drop_duplicates(subset=['學校名稱', '等級別'])
count = df3['等級別'].value_counts()
degree_list = list(df['等級別'].unique())

print(f"本資料集總共收集了 {len(set(df['學校代碼']))} 所學校，各等級學制當中：")
for degree in degree_list:
    print(f"一共有{count[degree]} 所學校， 有招收{degree[2:]}。")

# Colab 進行matplotlib繪圖時顯示繁體中文
# 下載台北思源黑體並命名taipei_sans_tc_beta.ttf，移至指定路徑
!wget -O TaipeiSansTCBeta-Regular.ttf https://drive.google.com/uc?id=1eGAsTN1HBpJAkeVM57_C7ccp7hbgSz3_&export=download

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.font_manager import fontManager

# 改style要在改font之前
# plt.style.use('seaborn')

fontManager.addfont('TaipeiSansTCBeta-Regular.ttf')
mpl.rc('font', family='Taipei Sans TC Beta')

df3_1 = df.drop_duplicates(subset=['學校名稱', '等級別'])
count = df3_1['等級別'].value_counts()
listx = [x[2:] for x in list(df['等級別'].unique())]
listy = [count[x] for x in list(df['等級別'].unique())]

plt.bar(listx, listy, width=0.5, color='#93282c')
plt.title('各學位等級招收校數')
plt.xlabel('學位等級別')
plt.ylabel('學校數')
plt.show()

"""# 4. 各縣市分別有？所，位於新北市的大專院校總共有幾所"""

city_list = []

for i in df['縣市名稱']:
    city_list.append(i[3:])
df['縣市名'] = city_list # 將 Dataframe 新增「縣市名」column
#print(city_list)

df4 = df.drop_duplicates('學校代碼')
count = df4['縣市名'].value_counts()
city_list = df4['縣市名'].unique()
print(f"本資料集共收集了 {len(df4)} 學校，其中：")
for city in city_list:
    print(f"{city}有 {count[city]} 所")

newtaipei = df4[df4['縣市名'] == '新北市']
print('\n',newtaipei['縣市名'].value_counts())

#顯示長條圖
plt.figure(figsize=(10, 6))  # 設定圖形大小
bars = plt.bar(count.index, count.values, color='skyblue')  # 使用 bar 函數繪製長條圖，可以自訂顏色 # 使用 bar 函數繪製長條圖，可以自訂顏色
plt.xlabel('縣市名稱')
plt.ylabel('學校數量')
plt.title('各縣市學校數量長條圖')
plt.xticks(rotation=45)  # 調整 x 軸標籤的角度

#在頭頂顯示數值
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height, str(int(height)), ha='center', va='bottom')
plt.show()

"""# 5. 北中南東區分別有？所

都市及區域發展統計彙編 - 國發會 https://www.ndc.gov.tw/nc_77_4402

北部區域：包括臺北市、新北市、基隆市、新竹市、桃園市、新竹縣及宜蘭縣。

中部區域：包括臺中市、苗栗縣、彰化縣、南投縣及雲林縣。

南部區域：包括高雄市、臺南市、嘉義市、嘉義縣、屏東縣及澎湖縣。

東部區域：包括花蓮縣及臺東縣。

福建省：包括金門縣與連江縣。
"""

city_to_area = {'臺北市':'北部',
         '新北市':'北部',
         '基隆市':'北部',
         '新竹市':'北部',
         '桃園市':'北部',
         '新竹縣':'北部',
         '宜蘭縣':'北部',
         '臺中市':'中部',
         '苗栗縣':'中部',
         '彰化縣':'中部',
         '南投縣':'中部',
         '雲林縣':'中部',
         '高雄市':'南部',
         '臺南市':'南部',
         '嘉義市':'南部',
         '嘉義縣':'南部',
         '屏東縣':'南部',
         '澎湖縣':'南部',
         '花蓮縣':'東部',
         '臺東縣':'東部',
         '金門縣':'福建省'}

df['區域'] = df['縣市名'].map(city_to_area)

df5 = df.drop_duplicates('學校代碼')
count = df5['區域'].value_counts()
#print(count)
print(f"本資料集共收集了 {len(df5)} 所學校，其中：")
print(f"北部區域有 {count['北部']} 所；\n中部區域有 {count['中部']} 所；\n南部區域有 {count['南部']} 所；\n東部區域有 {count['東部']} 所；\n福建省區域有 {count['福建省']} 所。")

df5_1 = df.drop_duplicates('學校代碼')
count = df5_1['區域'].value_counts()
listx = [count[x] for x in list(df['區域'].unique())]
listy = df['區域'].unique()

# 使用bar而不是barh來繪製垂直條形圖
plt.bar(listy, listx, width=0.5, color='skyblue')

# 在每個條形圖上方添加數值
for i, value in enumerate(listx):
    plt.text(listy[i], value, str(value), ha='center', va='bottom')

plt.title('各地區學校數')
plt.xlabel('地區')
plt.ylabel('學校數')
plt.xticks(rotation=45)  # 調整x軸標籤的旋轉角度
plt.tight_layout()  # 調整圖的布局以確保標籤可見
plt.show()

"""# 6. 各體系別分別有？所"""

df6 = df.drop_duplicates('學校代碼')
count = df6['體系別'].value_counts()

print(f"本資料集共收集了 {len(df6)} 所學校，其中：技職體系有 {count['2 技職']} 所；一般體系有 {count['1 一般']} 所；師範體系有 {count['3 師範']} 所。")

"""# 7. 國立/私立與男女比
請問國立大學與私立大學在學男生女生比例為何? 延修生男生女生比例為何?
"""

# 空白值補零
#df = df.replace('-', 0, regex=True)
#df

count = {}

def create_count_dict(df, count): # 建立多層 dict 結構來儲存各校在學與延修生的男女生數
    df7 = df.drop_duplicates('學校代碼')
    for i in df7['學校名稱']:
        count[i] = {}
        count[i]['在學生'] = {}
        count[i]['在學生']['男生數'] = 0
        count[i]['在學生']['女生數'] = 0
        count[i]['延修生'] = {}
        count[i]['延修生']['男生數'] = 0
        count[i]['延修生']['女生數'] = 0


def count_every_schools_data(df):
    for j in range(len(df)):
        count[df.iloc[j,2]]['在學生']['男生數'] += (int(df.iloc[j,8]) + int(df.iloc[j,10]) + int(df.iloc[j,12]) + int(df.iloc[j,14]) + int(df.iloc[j,16]) + int(df.iloc[j,18]) + int(df.iloc[j,20]))
        count[df.iloc[j,2]]['在學生']['女生數'] += (int(df.iloc[j,9]) + int(df.iloc[j,11]) + int(df.iloc[j,13]) + int(df.iloc[j,15]) + int(df.iloc[j,17]) + int(df.iloc[j,19]) + int(df.iloc[j,21]))
        count[df.iloc[j,2]]['延修生']['男生數'] += int(df.iloc[j,22])
        count[df.iloc[j,2]]['延修生']['女生數'] += int(df.iloc[j,23])

create_count_dict(df, count)
count_every_schools_data(df)

"""# 8. 國立大學在學生男女比"""

public_current_male = 0
public_current_female = 0

df7_1 = df.drop_duplicates('學校代碼', ignore_index=True)
for i in range(len(df7_1)):
    if df7_1.loc[i,'公私立'] == '國立':
        public_current_male += count[df7_1.loc[i,'學校名稱']]['在學生']['男生數']
        public_current_female += count[df7_1.loc[i,'學校名稱']]['在學生']['女生數']

ratio = public_current_male/public_current_female*100 # 男女比計算公式
print(f'國立大學在學生男女比：{ratio} ≑ {round(ratio,2)}') # 四捨五入至小數點後兩位

""" # 9. 每校平均最多與最少人的體系"""

df11 = df.drop_duplicates('學校代碼')
system_count = df11['體系別'].value_counts()

system_list = list(df['體系別'].unique())
count_student = 0
result_dict = {}

for system in system_list:
    for i in range(len(df)):
        if df.loc[i,'體系別'] == system:
            count_student += int(df.loc[i, '總計'])
    result_dict[system[2:]] = count_student/system_count[system]
    count_student = 0

max_value = max(result_dict.values())
min_value = min(result_dict.values())
max_key = next(key for key, value in result_dict.items() if value == max_value)
min_key = next(key for key, value in result_dict.items() if value == min_value)

print(f"每校平均最多人的是{max_key}體系，平均每校 {round(max_value,2)} 人；")
print(f"每校平均最少人的是{min_key}體系，平均每校 {round(min_value,2)} 人。")

all_male = 0
all_female = 0

df7 = df.drop_duplicates('學校代碼', ignore_index=True)
for i in range(len(df7)):
   # if df1.loc[i,'公私立'] == '國立':
        all_male += count[df7.loc[i,'學校名稱']]['在學生']['男生數']
        all_female += count[df7.loc[i,'學校名稱']]['在學生']['女生數']

ratio = all_male/all_female*100 # 男女比計算公式
print(f'所有大學學生男女比：{ratio} ≑ {round(ratio,2)}') # 四捨五入至小數點後兩位

#數據
labels = ['男生', '女生']
sizes = [all_male, all_female]
colors = ['lightblue', 'pink']
explode = (0, 0.05)

#繪製圓餅圖
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # 使圓餅圖為等比例
plt.title('所有學校學生的男女比例')
plt.show()

"""# 10. 將新增的欄位寫入並儲存成新的CSV檔案，並命名為112_students_tf.csv"""

df.head(2)
df.to_csv('112_students_tf.csv', encoding='utf-8', sep=',')