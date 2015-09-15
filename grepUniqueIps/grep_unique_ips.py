##-*- coding: utf-8 -*- 
#!/usr/bin/python

import sys, getopt
import os.path
import re


options = {
	'sample-filename-prefix' : 'not_verify_ips_1509',
	'sample-filename-suffix' : '.txt',
	'sample-filename-list' : list(('01','02','03'))
}


def main(argv):
	filename_prefix = options['sample-filename-prefix']
	filename_suffix = options['sample-filename-suffix']
	filename_list = options['sample-filename-list']
	try:
		opts, args = getopt.getopt(argv, 'hf:p:s:', ['help', 'filename-list', 'filename-prefix=', 'filename-suffix='])
	except getopt.GetoptError as err:
		print 'Couldn\'t parse the options!!'
		print str(err)
		sys.exit(2)
	for opt, arg in opts:
		if opt in ('-h', '--help'):
			printUsageAndExit()
		elif opt in ('-f', '--filename-list'):
			if arg:
				filename_list = arg.split(',')
			else:
				printUsageAndExit()
		elif opt in ('-p', '--filename-prefix'):
			if arg:
				filename_prefix = arg
			else:
				printUsageAndExit()
		elif opt in ('-s', '--filename-suffix'):
			if arg:
				filename_suffix = arg
			else:
				printUsageAndExit()
		else:
			printUsageAndExit()
	unique_ips = grepUniqueIps(filename_prefix, filename_suffix, filename_list)
	printResult(unique_ips)
	createResultFile(filename_prefix, filename_suffix, unique_ips)


def printUsageAndExit():
	usage()
	sys.exit(0)


def usage():
	print 'This script finds the unique IPs in the given text files.'
	print ''
	print 'usage:'
	print '$ python grep_unique_ips.py -p <filename-prefix> -s <filename-suffix> -f <filename-list>'
	print ''
	print 'e.g.:'
	print '$ pythond gerp_unique_ips.py -p unregistered-ips-201509 -s .txt -f 01,02,03'
	print 'Then this script finds the unique IPs in below files.'
	print '\tunregistered-ips-20150901.txt'
	print '\tunregistered-ips-20150902.txt'
	print '\tunregistered-ips-20150903.txt'
	sys.exit(0)


def grepUniqueIps(filename_prefix, filename_suffix, filename_list):
	unique_ips = list()
	for filename in filename_list:
		file_fullname = filename_prefix + filename + filename_suffix
		print 'Search not verified IPs in this file: ' + file_fullname
		try:
			with open(file_fullname, 'r') as infile:
				while 1:
					line = infile.readline() 
					if not line:
						break
					ips = re.findall(r'(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})$', line.strip())
					if ips is not None and len(ips) is not 0:
						for ip in ips:
							if ip not in unique_ips:
								unique_ips.extend(ips)
		except IOError as e:
			print "I/O error({0}): {1}".format(e.errno, e.strerror)
			exit(2)
	print "\n"
	unique_ips.sort()
	return unique_ips


def printResult(unique_ips):
	print "\n"
	for ip in unique_ips:
		print ip
	print "\n"


def createResultFile(filename_prefix, filename_suffix, unique_ips):
	try:
		file_fullname = filename_prefix + filename_suffix
		with open(file_fullname, 'a') as outfile:
			outfile.seek(0)
			outfile.truncate()
			for ip in unique_ips:
				outfile.write(ip)
				outfile.write("\n")
			print "\n"
			print "Result file: " + file_fullname
			print "\n"
	except IOError as e:
		print "I/O error({0}): {1}".format(e.errno, e.strerror)
		exit(2)


if __name__ == '__main__':
	reload(sys)
	sys.setdefaultencoding('utf-8')
	main(sys.argv[1:])