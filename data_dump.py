import psycopg2
from time import gmtime, strftime
import time

conn = psycopg2.connect( "dbname='everify' port = 8080 user='grant'")
conn.autocommit = True
cur = conn.cursor()
conn.commit()

def save(data_storage_1):
	conn.commit()
	a = data_storage_1
	numero = 0
	number = 0
	even = 0 

	if len(a[0]) == 7 :
		maximum_3 = len(a[0]) / 7
		last = 1
	else:
		maximum_1 = len(a[even])/7
		maximum_2 = len(a[even])/7
		
	if not len(a[0]) == 7:
		for numero in range(maximum_1):
			millis = int(round(time.time() * 1000))
			current_milli_time = lambda: int(round(time.time() * 1000))
			number = current_milli_time()
			name = a[even][0].strip()
			city = a[even][3].strip()
			town = a[even][4].strip()
			z_code = a[even][5].strip()
			time.sleep(.5)
			print name, city, town, z_code
			cur.execute("""INSERT INTO company VALUES (%r, %r, %r, %r, %r)"""%(number, name, city, town, z_code))

			del a[even][0]
			del a[even][0]
			del a[even][0]
			del a[even][0]
			del a[even][0]
			del a[even][0]
			del a[even][0]
			
	else:
		if int(last) == 1:
			for numero in range(maximum_3):
				millis = int(round(time.time() * 1000))
				current_milli_time = lambda: int(round(time.time() * 1000))
				number = current_milli_time()
				name = a[0][0].strip()
				city = a[0][3].strip()
				town = a[0][4].strip()
				z_code = a[0][5].strip()
				time.sleep(.5)
				print name, city, town, z_code
				cur.execute("""INSERT INTO company VALUES (%r, %r, %r, %r, %r)"""%(number, name, city, town, z_code))
				
			last = 0	
		else:
			pass
