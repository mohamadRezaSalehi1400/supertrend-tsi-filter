import MetaTrader5 as mt
import pandas as pd
from datetime import datetime
from persiantools.jdatetime import JalaliDateTime
#from nvdll import speak

def jalal(x, correction):
    return JalaliDateTime.to_jalali(datetime.fromtimestamp(x -correction))

def dir_indic(x):
    if x == 0: return 'flat'
    elif x > 0: return 'صعودی'
    elif x < 0: return 'نزولی'

def sym_list():
    '''
    این تابع بسته به این که دفعه آخر از مفید تریدر یا متا تریدر استفاده کرده باشیم،
    لیست نماد های بازار ایران یا فارکس را خروجی میدهد 
    '''
    try:
        #if not mt.initialize() : return
        mt.initialize()
    except:
        #speak('به meta trader متصل نیست ')
        return
    lst=[]
    symbols=mt.symbols_get()

    for s in symbols:  
        name=s.name
        if name.split(' ')[-1] == 'CFD' : continue
        lst+=[name]
    lst.sort()
    mt.shutdown()
    return lst

def sym_info(symbol):
    '''
    تابعی برای گرفتن مشخصات یک نماد
    '''
    #if not mt.initialize() : return
    try:
        mt.initialize()
    except:
        #speak('برنامه به meta trader متصل نیست ')
        return
    info=mt.symbols_get(symbol)[0]
    mt.shutdown()
    return {'name': info.name, 'path': info.path, 'description': info.description, 'digits': info.digits}

def pip(df, symbol):
    p = sym_info(symbol)['digits']
    if p == 5:
        return round(df['atr'] *10000,1)
    elif p == 3:
        return round(df['atr'] *100, 1)
    elif p == 2:
        return round(df['atr'], 1)
    else:
        return df['atr']

def time_frame(tf):
    '''
    جهت دریافت تایم فریم از این تابع کنک می گیریم
    '''
    if tf == 'M1': return mt.TIMEFRAME_M1
    if tf == 'M2': return mt.TIMEFRAME_M2
    if tf == 'M5': return mt.TIMEFRAME_M5
    elif tf == 'M10': return mt.TIMEFRAME_M10
    elif tf == 'M15': return mt.TIMEFRAME_M15
    elif tf == 'M30': return mt.TIMEFRAME_M30
    elif tf == 'H1': return mt.TIMEFRAME_H1
    elif tf == 'H4': return mt.TIMEFRAME_H4
    elif tf == 'H8': return mt.TIMEFRAME_H8
    elif tf == 'D1': return mt.TIMEFRAME_D1
    elif tf == 'W1': return mt.TIMEFRAME_W1
    elif tf == 'MN1': return mt.TIMEFRAME_MN1
    else:
        return 0

def get_data(sym_name, timeFrame, number_of_cdl):
    '''
    3 ورودی تابع شامل نام نماد و تایم فریم که همان خروجی تابع tTimeFrame است 
    و تعداد کندل می باشد.
    خروجی هم تایم فریم با سر ستون های:
    Time Open High Low Close
    می باشد.
    '''
    #if not mt.initialize() : return
    try:
        mt.initialize()
    except:
        speak('برنامه به متاتریدر متصل نیست ')
        return
    rates=mt.copy_rates_from_pos(sym_name, timeFrame, 0, number_of_cdl)
    if rates is None : return
    df=pd.DataFrame(rates)
    c = 12600
    df['j_time'] = df['time'].apply(func= jalal, correction= c)
    df['time']=pd.to_datetime(df['time'], unit='s')
    #تغییر ایندکس به تایم
    #df.set_index(df['time'], inplace=True)

    df['atr'] = (df['high'].rolling(33).sum() - df['low'].rolling(33).sum() ) / 33

    df['tenkan'] = (df['high'].rolling(9).max() +df['low'].rolling(9).min())/2
    df['kijun'] = (df['high'].rolling(26).max() +df['low'].rolling(26).min())/2
    df['spanA'] = ((df['tenkan'] +df['kijun'])/2 ).shift(26)
    df['spanB'] = ((df['high'].rolling(52).max() +df['low'].rolling(52).min())/2 ).shift(26)
    
    #تغییر نام ستون ها
    df = df.rename(columns={'real_volume': 'volume'})

    #df['atr pip'] = df.apply( func= pip, symbol= sym_name, axis=1)
    mt.shutdown()
    #print(df)
    return df

def get_data_from_date(sym_name, timeFrame, from_date):
    '''
    3 ورودی تابع شامل نام نماد و تایم فریم که همان خروجی تابع tTimeFrame است 
    و زمانی را که از آن تاریخ داده میخواهیم می باشد.
    خروجی هم تایم فریم با سر ستون های:
    Time Open High Low Close volume
    می باشد.
    '''
    #if not mt.initialize() : return
    try:
        mt.initialize()
    except:
        return
    rates=mt.copy_rates_range(sym_name, timeFrame, from_date, datetime.now())
    if rates is None : return
    df=pd.DataFrame(rates)
    df['time']=pd.to_datetime(df['time'], unit='s')
    df.set_index(df['time'], inplace=True)
    #تغییر نام ستون ها
    df = df.rename(columns={'tick_volume': 'volume'})
    # حذف ستون های اضافی
    df = df[[ 'time', 'open', 'high', 'low', 'close', 'volume']]
    mt.shutdown()
    return df



if __name__=='__main__':
    #symbol = sym_list()
    #print(symbol)
    df = get_data('XAUUSD', time_frame('D1'), 100)
    print(df)
    #print(sym_info('EURUSD')['digits'])
    #from_date =datetime(2022, 1, 1)
    #print(get_data_from_date('EURUSD', time_frame('H1'), from_date))
    if not df is None : df.to_excel('data_test.xlsx', index=False)    