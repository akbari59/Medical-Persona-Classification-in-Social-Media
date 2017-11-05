import datetime
import time
def timediff(prev,now='Sat Nov 04 14:23:30 +0000 2017'):
	ts=time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(prev,'%a %b %d %H:%M:%S +0000 %Y'))
	tt=time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(now,'%a %b %d %H:%M:%S +0000 %Y'))
	start=datetime.datetime.strptime(tt, '%Y-%m-%d %H:%M:%S')
	end=datetime.datetime.strptime(ts, '%Y-%m-%d %H:%M:%S')
	return abs((end-start).total_seconds())

