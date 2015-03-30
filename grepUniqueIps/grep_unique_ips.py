import re

file_name = 'not_verify_ips_1503'
file_extension = 'txt'

dates = list((24,25,26,27,28,29,30))
for date in dates:
	filefullname = file_name + str(date) + '.' + file_extension

	f = open(filefullname, 'r') 
	unique_ips = list()

	while 1:
		line = f.readline() 
		if not line:
			break
		line_arr = line.split(':')
		s = line_arr[len(line_arr) - 1].strip()
		if '.' in s:
			if s not in unique_ips:
				unique_ips.append(s)
		
	f.close()

unique_ips.sort()
for ip in unique_ips:
	print(ip)