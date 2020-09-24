from datetime import datetime,timedelta
end = str((datetime.strptime(str(datetime.now().strftime('%Y-%m-%d')),'%Y-%m-%d') + timedelta(days=35)).strftime('%Y-%m-%d'))
f = open('time/time.txt', 'w')
f.write(end)
f.close() 
y = [line.strip() for line in open('time/time.txt','r')][0]
print( str(datetime.strptime(y,'%Y-%m-%d') - datetime.now()).split('days')[0] + "days" + ' [' + y + ']')
