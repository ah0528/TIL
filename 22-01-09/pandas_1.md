# pandas
* 파이썬에서 데이터 분석과 처리를 쉽게 할 수 있게 도와주는 pandas 라이브러리
* NumPy를 기반으로 만들어졌지만 좀 더 복잡한 데이터 분석에 특화
* 같은 데이터 타입의 배열만 처리할 수 있는 NumPy에 반해 pandas는 데이터 타입이 다양하게 섞여 있어도 처리 가능
* pandas홈페이지(https://pandas.pydata.org)

## 구조적 데이터 생성하기
* pandas도 NumPy처럼 불러와야 함
* `import pandas as pd`
### 1. Series를 활용한 데이터 생성
`s = pd.Series(seq_data)`

* pandas에서 데이터를 생성하는 가장 기본적인 방법 : Series() 이용
* Series를 이용하면 Series 형식의 구조적 데이터(라벨을 갖는 1차원 데이터) 생성가능
* seq_data(시퀀스 데이터)로는 리스트와 튜플 타입의 데이터를 모두 사용 가능(주로 리스트 데이터를 이용)
* 인자로 넣은 시퀀스 데이터에 순서를 표시하는 라벨이 자동으로 부여됨
* 세로축 라벨을 index라고 하고, 입력한 시퀀스 데이터를 values라고 함
* index는 데이터를 처리할 때 이용


```python
import pandas as pd
s1 = pd.Series([10,20,30,40,50])
s1
```




    0    10
    1    20
    2    30
    3    40
    4    50
    dtype: int64



**Series 데이터는 index와 values를 분리해서 가져올 수 있음**

`s.index` : index 가져오기

`s.values` : values 가져오기


```python
s1.index
```




    RangeIndex(start=0, stop=5, step=1)




```python
s1.values
```




    array([10, 20, 30, 40, 50], dtype=int64)



**Series()로 데이터를 생성할 때 문자와 숫자가 혼합된 리스트를 인자로 사용 가능**


```python
s2 = pd.Series(['a','b','c',1,2,3])
s2
```




    0    a
    1    b
    2    c
    3    1
    4    2
    5    3
    dtype: object



**np.nan를 이용하여 Series 데이터에 특정 원소가 없음을 표시하기**

Nan은 데이터가 없다는 것을 의미 (데이터를 위한 index는 있지만 실제 값은 없음)


```python
import numpy as np
s3 = pd.Series([np.nan,10,30])
s3
```




    0     NaN
    1    10.0
    2    30.0
    dtype: float64



**Series 데이터를 생성할 때 인자로 index를 추가 가능**

`s = pd.Series(seq_data, index = index_seq)`
* index_seq도 리스트와 튜플 타입의 데이터를 모두 사용 가능(주로 리스트 데이터를 이용)

* ※주의 : seq_data의 항목 개수와 index_seq의 항목 개수는 같아야 함


```python
s4 = pd.Series([200,195,np.nan,205],index=['2018-10-07','2018-10-08','2018-10-09','2018-10-10'])
s4
```




    2018-10-07    200.0
    2018-10-08    195.0
    2018-10-09      NaN
    2018-10-10    205.0
    dtype: float64



**파이썬의 딕셔너리를 이용해 데이터 생성하기**

`s = pd.Series(dict_data)` : 딕셔너리 형태로 입력하면 데이터의 키(keys)와 값(values)이 각각 Series 데이터의 index와 values가 됨


```python
s5 = pd.Series({'국어':100,'수학':90,'영어':95})
s5
```




    국어    100
    수학     90
    영어     95
    dtype: int64



### 2. 날짜 자동 생성 : data_range
`pd.date_range(start=None, end=None, periods=None, freq='D)` : 원하는 날짜를 자동으로 생성
* steart는 반드시 있어야하고, end나 periods는 둘 중 하나만 있어도 됨
* freq를 입력하지 않으면 'D'옵션이 설정되어 달력 날짜 기준으로 하루씩 증가함
* 날짜를 입력할 때는 다양한 형식(yyyy-mm-dd, yyyy/mm/dd, yyyy.mm.dd, mm-dd-yyyy, mm/dd/yyyy, mm.dd.yyyy)으로 입력할 수 있고, 생성된 날짜 데이터의 형식은 모두 yyyy-mm-dd임

**freq 옵션**

|약어|설명|예|
|---|--------------------|------------------------------------------|
|D|하루 주기|freq='D' : 하루 주기, freq='2D' : 이틀 주기|
|B|업무날짜 기준 하루 주기|업무일(월~금) 기준으로 생성|
|W|요일 시작 기준 일주일 주기|freq='W', freq='W-SUN' : 일요일로 일주일 시작, freq='W-MON' : 월요일로 일주일 시작|
|M|월말 날짜 기준 주기|freq='M' : 한달 주기, freq='3M' : 세 달 주기|
|BM|업무 월말 날짜 기준 주기|freq='2BM'|
|MS|월초 날짜 기준 주기|freq='MS'|
|BMS|업무 월초 날짜 기준 주기|freq='BMS'|
|Q|분기 끝 날짜 기준 주기|freq='Q'|
|BQ|업무 분기 끝 날짜 기준 주기|freq='BQ'|
|QS|분기 시작 날짜 기준 주기|freq='QS'|
|BQS|업무 분기 시작 날짜 기준 주기|freq='BQS'|
|A|일년 끝 날짜 기준 주기|freq='A'|
|BA|업무 일년 끝 날짜 기준 주기|freq='BA'|
|AS|일년 시작 날짜 기준 주기|freq='AS'|
|BAS|업무 일년 시작 날짜 기준 주기|freq='BAS'|
|H|시간 기준 주기|freq='2H' : 2시간 주기|
|BH|업무 시간 기준 주기|업무 시간(09:00 ~ 17:00)기준으로 생성|
|T, min|분 주기|freq='10T' : 10분 주기, freq='30min' : 30분 주기|
|S|초 주기|freq='30S' : 30초 주기|


```python
import pandas as pd
pd.date_range(start='2022-01-09',end='2022-02-10')
```




    DatetimeIndex(['2022-01-09', '2022-01-10', '2022-01-11', '2022-01-12',
                   '2022-01-13', '2022-01-14', '2022-01-15', '2022-01-16',
                   '2022-01-17', '2022-01-18', '2022-01-19', '2022-01-20',
                   '2022-01-21', '2022-01-22', '2022-01-23', '2022-01-24',
                   '2022-01-25', '2022-01-26', '2022-01-27', '2022-01-28',
                   '2022-01-29', '2022-01-30', '2022-01-31', '2022-02-01',
                   '2022-02-02', '2022-02-03', '2022-02-04', '2022-02-05',
                   '2022-02-06', '2022-02-07', '2022-02-08', '2022-02-09',
                   '2022-02-10'],
                  dtype='datetime64[ns]', freq='D')




```python
pd.date_range(start='2022-01-09', periods=3)
```




    DatetimeIndex(['2022-01-09', '2022-01-10', '2022-01-11'], dtype='datetime64[ns]', freq='D')




```python
pd.date_range(start='2022-01-08',periods=3,freq='B') # 업무일로 3일 선택하기
```




    DatetimeIndex(['2022-01-10', '2022-01-11', '2022-01-12'], dtype='datetime64[ns]', freq='B')




```python
pd.date_range(start='2022-01-10',periods=3,freq='W') # 주 시작일(일요일)로 3번 선택하기
```




    DatetimeIndex(['2022-01-16', '2022-01-23', '2022-01-30'], dtype='datetime64[ns]', freq='W-SUN')




```python
pd.date_range(start='2022-01-10',periods=3,freq='W-MON') # 주 시작일(월요일)로 3번 선택하기
```




    DatetimeIndex(['2022-01-10', '2022-01-17', '2022-01-24'], dtype='datetime64[ns]', freq='W-MON')




```python
pd.date_range(start='2022-01-10',periods=3,freq='M') # 월 말 날짜로 3달 추출
```




    DatetimeIndex(['2022-01-31', '2022-02-28', '2022-03-31'], dtype='datetime64[ns]', freq='M')




```python
pd.date_range(start='2022-04-10',periods=3,freq='BM')
```




    DatetimeIndex(['2022-04-29', '2022-05-31', '2022-06-30'], dtype='datetime64[ns]', freq='BM')




```python
pd.date_range(start='2022-01-09',periods=4,freq='Q') # 분기 끝 날짜 기준으로 4개
```




    DatetimeIndex(['2022-03-31', '2022-06-30', '2022-09-30', '2022-12-31'], dtype='datetime64[ns]', freq='Q-DEC')




```python
pd.date_range(start='2022-01-09',periods=3,freq='A')
```




    DatetimeIndex(['2022-12-31', '2023-12-31', '2024-12-31'], dtype='datetime64[ns]', freq='A-DEC')




```python
pd.date_range(start='2022-01-09',periods=3,freq='AS')
```




    DatetimeIndex(['2023-01-01', '2024-01-01', '2025-01-01'], dtype='datetime64[ns]', freq='AS-JAN')




```python
pd.date_range(start='2022-01-09',periods=3,freq='M')
```




    DatetimeIndex(['2022-01-31', '2022-02-28', '2022-03-31'], dtype='datetime64[ns]', freq='M')




```python
pd.date_range(start='2022-01-09',periods=3,freq='2H')
```




    DatetimeIndex(['2022-01-09 00:00:00', '2022-01-09 02:00:00',
                   '2022-01-09 04:00:00'],
                  dtype='datetime64[ns]', freq='2H')




```python
pd.date_range(start='2022-01-09 09:00:00',periods=3,freq='3H')
```




    DatetimeIndex(['2022-01-09 09:00:00', '2022-01-09 12:00:00',
                   '2022-01-09 15:00:00'],
                  dtype='datetime64[ns]', freq='3H')




```python
pd.date_range(start='2022-01-09 09:00:00',periods=3,freq='30T')
```




    DatetimeIndex(['2022-01-09 09:00:00', '2022-01-09 09:30:00',
                   '2022-01-09 10:00:00'],
                  dtype='datetime64[ns]', freq='30T')




```python
pd.date_range(start='2022-01-09 09:00:00',periods=3,freq='30min')
```




    DatetimeIndex(['2022-01-09 09:00:00', '2022-01-09 09:30:00',
                   '2022-01-09 10:00:00'],
                  dtype='datetime64[ns]', freq='30T')




```python
pd.date_range(start='2022-01-09 09:00:00',periods=3,freq='30S')
```




    DatetimeIndex(['2022-01-09 09:00:00', '2022-01-09 09:00:30',
                   '2022-01-09 09:01:00'],
                  dtype='datetime64[ns]', freq='30S')




```python
index_date = pd.date_range(start='2022.01.09',periods=5,freq='B')
pd.Series([32,50,43,29,61], index=index_date)
```




    2022-01-10    32
    2022-01-11    50
    2022-01-12    43
    2022-01-13    29
    2022-01-14    61
    Freq: B, dtype: int64



### 3. DataFrame을 활용한 데이터 생성
DateFrame을 이용하면 index가 있는 2차원 데이터를 생성하고 처리할 수 있다

`df = pd.DataFrame(data [, index=index_data, columns=columns_datd])`

* data에는 리스트, 딕셔너리, NumPy의 배열, Series 데이터, DataFrame 데이터를 입력 가능
* 세로축 라벨 : index, 가로축 라벨 : columns
* index와 columns를 입력하지 않으면 0부터 숫자가 작성됨
* ※주의 : data의 행 개수와 index 요소의 개수, data의 열 개수와 columns 요소의 개수가 같아야함


```python
pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4</td>
      <td>5</td>
      <td>6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>7</td>
      <td>8</td>
      <td>9</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.DataFrame([[10,20,30],[40,50,60],[70,80,90]])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>10</td>
      <td>20</td>
      <td>30</td>
    </tr>
    <tr>
      <th>1</th>
      <td>40</td>
      <td>50</td>
      <td>60</td>
    </tr>
    <tr>
      <th>2</th>
      <td>70</td>
      <td>80</td>
      <td>90</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_index = pd.date_range(start='2019-09-01',periods=4)
pd.DataFrame([[1,2,3],[4,5,6],[7,8,9],[10,11,12]],index=df_index,columns=['A','B','C'])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2019-09-01</th>
      <td>1</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2019-09-02</th>
      <td>4</td>
      <td>5</td>
      <td>6</td>
    </tr>
    <tr>
      <th>2019-09-03</th>
      <td>7</td>
      <td>8</td>
      <td>9</td>
    </tr>
    <tr>
      <th>2019-09-04</th>
      <td>10</td>
      <td>11</td>
      <td>12</td>
    </tr>
  </tbody>
</table>
</div>



* 딕셔너리를 사용하면 딕셔너리 데이터의 키는 DataFrame에서 columns로 지정됨


```python
table_data = {'연도':[2015,2016,2016,2017,2017],'지사':['한국','한국','미국','한국','미국'],'고객수':[200,250,450,300,500]}
table_data
```




    {'연도': [2015, 2016, 2016, 2017, 2017],
     '지사': ['한국', '한국', '미국', '한국', '미국'],
     '고객수': [200, 250, 450, 300, 500]}




```python
df_a = pd.DataFrame(table_data)
df_a
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>연도</th>
      <th>지사</th>
      <th>고객수</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2015</td>
      <td>한국</td>
      <td>200</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2016</td>
      <td>한국</td>
      <td>250</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2016</td>
      <td>미국</td>
      <td>450</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2017</td>
      <td>한국</td>
      <td>300</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2017</td>
      <td>미국</td>
      <td>500</td>
    </tr>
  </tbody>
</table>
</div>



* DataFrame 데이터에서 index, columns, values 확인 가능

`DataFrame.index`, `DataFrame.columns`, `DataFrame.values`


```python
df_a.index
```




    RangeIndex(start=0, stop=5, step=1)




```python
df_a.columns
```




    Index(['연도', '지사', '고객수'], dtype='object')




```python
df_a.values
```




    array([[2015, '한국', 200],
           [2016, '한국', 250],
           [2016, '미국', 450],
           [2017, '한국', 300],
           [2017, '미국', 500]], dtype=object)



## 데이터 연산
* pandas의 Series()와 DataFrame()으로 생성한 데이터끼리는 사칙연산이 가능
* pandas의 데이터끼리는 서로 크기가 달라도 연산이 가능 : 연산을 할 수 있는 항목만 연산을 수행하고, 할 수 없는 부분은 Nan으로 표시


```python
s1 = pd.Series([1,2,3,4,5])
s2 = pd.Series([10,20,30,40,50])
s1+s2
```




    0    11
    1    22
    2    33
    3    44
    4    55
    dtype: int64




```python
s2-s1
```




    0     9
    1    18
    2    27
    3    36
    4    45
    dtype: int64




```python
s1*s2
```




    0     10
    1     40
    2     90
    3    160
    4    250
    dtype: int64




```python
s2/s1
```




    0    10.0
    1    10.0
    2    10.0
    3    10.0
    4    10.0
    dtype: float64




```python
s3 = pd.Series([1,2,3,4,5,6])
s4 = pd.Series([10,20,30,40,50])
s3+s4
```




    0    11.0
    1    22.0
    2    33.0
    3    44.0
    4    55.0
    5     NaN
    dtype: float64




```python
s4-s3
```




    0     9.0
    1    18.0
    2    27.0
    3    36.0
    4    45.0
    5     NaN
    dtype: float64




```python
s3*s4
```




    0     10.0
    1     40.0
    2     90.0
    3    160.0
    4    250.0
    5      NaN
    dtype: float64




```python
s4/s3
```




    0    10.0
    1    10.0
    2    10.0
    3    10.0
    4    10.0
    5     NaN
    dtype: float64




```python
table_data1 = {'A':[1,2,3,4,5],'B':[10,20,30,40,50],'C':[100,200,300,400,500]}
table_data1
```




    {'A': [1, 2, 3, 4, 5],
     'B': [10, 20, 30, 40, 50],
     'C': [100, 200, 300, 400, 500]}




```python
df1 = pd.DataFrame(table_data1)
df1
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>10</td>
      <td>100</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>20</td>
      <td>200</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>30</td>
      <td>300</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>40</td>
      <td>400</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>50</td>
      <td>500</td>
    </tr>
  </tbody>
</table>
</div>




```python
table_data2 = {'A':[6,7,8],'B':[60,70,80],'C':[600,700,800]}
table_data2
```




    {'A': [6, 7, 8], 'B': [60, 70, 80], 'C': [600, 700, 800]}




```python
df2 = pd.DataFrame(table_data2)
df2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>6</td>
      <td>60</td>
      <td>600</td>
    </tr>
    <tr>
      <th>1</th>
      <td>7</td>
      <td>70</td>
      <td>700</td>
    </tr>
    <tr>
      <th>2</th>
      <td>8</td>
      <td>80</td>
      <td>800</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1+df2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>7.0</td>
      <td>70.0</td>
      <td>700.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>9.0</td>
      <td>90.0</td>
      <td>900.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>11.0</td>
      <td>110.0</td>
      <td>1100.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



* pandas에는 데이터 통계 분석을 위한 다양한 메서드가 있어 데이터의 총합, 평균, 표준편차 등을 구할 수 있음

|메서드|설명|메서드|설명|
|------|------|------|------|
|`sum()`|총합|`mean()`|평균|
|`std()`|표준편차|`var()`|분산|
|`min()`|최솟값|`max()`|최댓값|
|`cumsum()`|원소의 누적 합|`cumprod()`|원소의 누적 곱|


*`describe()` : 평균, 표준편차, 최댓값, 최솟값 등을 한 번에 구할 수 있음


```python
table_data3 = {'봄':[256.5,264.3,215.9,223.2,312.8],'여름':[770.6,567.5,599.8,387.1,446.2],'가을':[363.5,231.2,293.1,247.7,381.6],'겨울':[139.3,59.9,76.9,109.1,108.1]}
table_data3
```




    {'봄': [256.5, 264.3, 215.9, 223.2, 312.8],
     '여름': [770.6, 567.5, 599.8, 387.1, 446.2],
     '가을': [363.5, 231.2, 293.1, 247.7, 381.6],
     '겨울': [139.3, 59.9, 76.9, 109.1, 108.1]}




```python
df3 = pd.DataFrame(table_data3, index=[2012,2013,2014,2015,2016])
df3
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>봄</th>
      <th>여름</th>
      <th>가을</th>
      <th>겨울</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2012</th>
      <td>256.5</td>
      <td>770.6</td>
      <td>363.5</td>
      <td>139.3</td>
    </tr>
    <tr>
      <th>2013</th>
      <td>264.3</td>
      <td>567.5</td>
      <td>231.2</td>
      <td>59.9</td>
    </tr>
    <tr>
      <th>2014</th>
      <td>215.9</td>
      <td>599.8</td>
      <td>293.1</td>
      <td>76.9</td>
    </tr>
    <tr>
      <th>2015</th>
      <td>223.2</td>
      <td>387.1</td>
      <td>247.7</td>
      <td>109.1</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>312.8</td>
      <td>446.2</td>
      <td>381.6</td>
      <td>108.1</td>
    </tr>
  </tbody>
</table>
</div>




```python
df3.mean()
```




    봄     254.54
    여름    554.24
    가을    303.42
    겨울     98.66
    dtype: float64




```python
df3.std()
```




    봄      38.628267
    여름    148.888895
    가을     67.358496
    겨울     30.925523
    dtype: float64




```python
df3.std(axis=1)
```




    2012    274.472128
    2013    211.128782
    2014    221.150739
    2015    114.166760
    2016    146.548658
    dtype: float64




```python
df3.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>봄</th>
      <th>여름</th>
      <th>가을</th>
      <th>겨울</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>5.000000</td>
      <td>5.000000</td>
      <td>5.000000</td>
      <td>5.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>254.540000</td>
      <td>554.240000</td>
      <td>303.420000</td>
      <td>98.660000</td>
    </tr>
    <tr>
      <th>std</th>
      <td>38.628267</td>
      <td>148.888895</td>
      <td>67.358496</td>
      <td>30.925523</td>
    </tr>
    <tr>
      <th>min</th>
      <td>215.900000</td>
      <td>387.100000</td>
      <td>231.200000</td>
      <td>59.900000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>223.200000</td>
      <td>446.200000</td>
      <td>247.700000</td>
      <td>76.900000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>256.500000</td>
      <td>567.500000</td>
      <td>293.100000</td>
      <td>108.100000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>264.300000</td>
      <td>599.800000</td>
      <td>363.500000</td>
      <td>109.100000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>312.800000</td>
      <td>770.600000</td>
      <td>381.600000</td>
      <td>139.300000</td>
    </tr>
  </tbody>
</table>
</div>


