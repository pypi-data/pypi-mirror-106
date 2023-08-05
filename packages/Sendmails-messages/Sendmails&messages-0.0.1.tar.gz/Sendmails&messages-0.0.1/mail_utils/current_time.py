import datetime

def current_time():
	now = datetime.datetime.now()
 
	today_date=datetime.date.today() #today's date
	 
	current_dt, current_mn,current_yr = today_date.strftime("%d %m  %y").split()

	return current_dt,current_mn,current_yr
