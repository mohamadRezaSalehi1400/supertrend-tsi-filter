# برای نصب این کتابخانه توصیه می شود از کد زیر استفاده کنید:
# pip install playsound==1.2.2
from playsound import playsound

def sound(soundAddress):
	try:
		playsound(soundAddress)
	except:
		pass
