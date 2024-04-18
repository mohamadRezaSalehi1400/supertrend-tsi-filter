# supertrend and tsi filter

در این جا ما با استفاده از 2 اندیکاتور supertrend و tsi موقعیت های مناسب برای خرید یا فروش را پیدا می کنیم.
هنگامی که یک موقعیت خرید یا فروش پیدا شود، یک اعلام صوتی پخش و پیغام متناسب در cmd چاپ خواهد شد.

## سیگنال خرید:
در کندل قبل خط tsi زیر خط signal باشد،
و در کندل بعد خط tsi با اختلاف 5، بالای خط سیگنال باشد 
همچنین رنگ خط supertrend سبز باشد.

## سیگنال فروش:
در کندل قبل خط tsi بالای خط signal باشد،
و در کندل بعد خط tsi با اختلاف 5، زیر خط سیگنال باشد 
همچنین رنگ خط supertrend قرمز باشد.

**توجه:**
این استراتژی برای بازاری که روند دارد مناسب است و در بازار رنج سیگنال اشتباه می دهد.

## ورودی ها:
1- ابتدا نام نماد را وارد کرده و enter بزنید.
2-  در ورودی بعدی timeframe را وارد کنید و emter بزنید.
مثلا برای timeframe 5 دقیقه، M5  و برای 1 ساعت، H1 را وارد کنید.
3-  در این مرحله باید 5 عدد را که 3 عدد اول مربوط به تنظیمات tsi و 2 عدد آخر آن مربوط به تنظیمات supertrend است را به این ترتیب وارد کنید:
عدد اول: slow period for tsi
عدد دوم: fast period for tsi
عدد سوم: signal for tsi
عدد چهارم: ATR period for supertrend
عدد پنجم: ATR multiplier for supertrend
مثلا :
3 7 4 10 3
و سپس enter
**تذکر:**
اگر بدون وارد کردن هیچ عددی، enter بزنید،
به صورت پیش فرض، اعداد 13 25 5 10 3 اعمال خواهد شد.

### تذکر بسیار مهم:
این برنامه داده های خود را از طریق metatrader5 دریافت می کند.
بنابر این هنگام  اجرای برنامه، باید metatrader5 را با یک حساب فعال روی سیستم خود داشته باشید.

# supertrend and tsi filter

Here we use 2 supertrend and tsi indicators to find suitable positions for buying or selling.
When a buy or sell position is found, an audio announcement will be played and the corresponding message will be printed in cmd.

## Buy signal:
In the previous candle, the tsi line should be below the signal line.
And in the next candle, the tsi line should be above the signal line with a difference of 5
Also, the color of the supertrend line should be green.

## Sell ​​signal:
In the previous candle, the tsi line should be above the signal line.
And in the next candle, the tsi line should be below the signal line with a difference of 5
Also, the color of the supertrend line should be red.

**Attention:**
This strategy is suitable for trending market and gives wrong signal in range market.

## Inputs:
1- First, enter the name of the symbol and press enter.
2- In the next entry, enter the timeframe and press enter.
For example, enter M5 for 5 minutes timeframe and H1 for 1 hour.
3- In this step, you have to enter 5 numbers, the first 3 numbers are related to tsi settings and the last 2 numbers are related to supertrend settings as follows:
First number: slow period for tsi
The second number: fast period for tsi
The third number: signal for tsi
The fourth number: ATR period for supertrend
The fifth number: ATR multiplier for supertrend
For example :
3 7 4 10 3
and then press enter
**note:**
If you press enter without entering any number,
By default, the numbers 13 25 5 10 3 will be applied.

### Very important note:
The program receives its data through metatrader5.
Therefore, when running the program, you must have metatrader5 with an active account on your system.
