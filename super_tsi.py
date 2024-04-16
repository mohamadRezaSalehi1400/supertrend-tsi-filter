import pandas as pd
import pandas_ta as ta
from mt_data import get_data, time_frame, sym_info
from check_timeframe import check_current_tf_per_second
import time
from sound import sound


def direction(x):
    if x == -1 : return 'red'
    if x == 1 : return 'green'

def SUPER(df, symbol, periods):
    p = sym_info(symbol)['digits']
    ln = int(periods.split(' ')[3])
    mp = float(periods.split(' ')[4])
    super = ta.supertrend(df.high, df.low, df.close, length= ln, multiplier= mp)
    dir_col = 'SUPERTd_{}_{}'.format(ln, mp)
    super['color'] =super[dir_col].apply(direction)
    #super = super.rename(columns={'SUPERT_10_3.0': 'super'})
    super_col = 'SUPERT_{}_{}'.format(ln, mp)
    super['super'] = round(super[super_col], p)
    super = super[['super', 'color']]
    
    #df = pd.concat([df, super], axis=1)
    #return df
    return super


def TSI(df, periods):
    fast = int(periods.split(' ')[0])
    slow = int(periods.split(' ')[1])
    sig = int(periods.split(' ')[2])
    tsi = ta.tsi(df.close, fast=fast, slow= slow, signal= sig)
    #tsi = tsi.rename(columns={'TSI_13_25_13': 'power', 'TSIs_13_25_13': 'signal'})
    power_col ='TSI_{}_{}_{}'.format(fast, slow, sig)
    signal_col ='TSIs_{}_{}_{}'.format(fast, slow, sig)
    tsi['power'] = round(tsi[power_col], 2)
    tsi['signal'] = round(tsi[signal_col], 2)
    tsi = tsi[['power', 'signal']]
    #df = pd.concat([df, tsi], axis=1)
    #return df
    return tsi

symbol = input('(XAUUSD_i)')
tf = input('(M5)')
periods = input('(3 7 4 10 2.5)')
sound("./sound/Windows Default.wav")

while True:
    time.sleep(1)
    if check_current_tf_per_second(tf):
        time.sleep(4)
        df = get_data(symbol, time_frame(tf), 100)
        tsi = TSI(df, periods)
        super = SUPER(df, symbol, periods)
        if tsi.power[97] > tsi.signal[97] and tsi.power[98] < tsi.signal[98] and super.color[98] == 'red' :
            print('موقعیت فروش در ', symbol)
            sound("./sound/notification.wav")
        if tsi.power[97] < tsi.signal[97] and tsi.power[98] > tsi.signal[98] and super.color[98] == 'green' :
            print('موقعیت خرید در ', symbol)
            sound("./sound/notification.wav")


'''
if __name__=='__main__':
    df = get_data('XAUUSD_i', time_frame('H1'), 110)
    periods = input('inter periods')
    tsi = TSI(df, periods)
    print(tsi)
    if not tsi is None : tsi.to_excel('tsi_test.xlsx', index=False)    
    '''