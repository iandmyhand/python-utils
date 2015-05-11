#!/usr/bin/python

import sys, getopt, socket
import os.path

class bcolors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'

def main(argv):
        file_name = 'ip-list-sample.txt'
        try:
                opts, args = getopt.getopt(argv, 'hf:', ['help', 'file='])
        except getopt.GetoptError:
                usage()
                sys.exit(2)
        for opt, arg in opts:
                if opt in ('-h', '--help'):
                        usage()
                        sys.exit(0)
                elif opt in ('-f', '--file'):
                        file_name = arg
                else:
                        usage()
                        sys.exit(0)

        address_list = getAddressList(file_name)
        for address in address_list:
                print 'checking ' + address['ip'] + ':' + address['port'] + ' ...'
                printResult(address, isIpAccessible(address['ip'], address['port']))

def usage():
        print 'usage:'
        print '\t$ python checkIpIsAccessble.py -f <filename>'
        print '\t\tEach IP and Port will must be separated by colon(:).'
        print '\t\tEach address will must be separated by new line(' + os.pathsep + ').'
        sys.exit()

def getAddressList(file_name):
        print 'read file: ' + file_name
        if(os.path.isfile(file_name)):
                file = open(file_name, 'r')
        else:
                print 'Cannot open file: ' + file_name
                sys.exit(2)

        address_list = []

        while 1:
                line = file.readline()
                if not line:
                        break
                line = str(line.rstrip('\n').rstrip('\r').strip())

                # Continue to read next line if line is empty.
                if not line:
                        continue
                # Print commnet.
                if line.startswith( '#' ):
                        print line
                        continue
                tmp_arr = line.split(':')
                if len(tmp_arr) == 2:
                        address_list.append({'ip':tmp_arr[0], 'port':tmp_arr[1]})
                else:
                        print 'IP address must be "IP:PORT", but [' + line + '] is not.'
                        print 'e.g. 127.0.0.1:80'
                        sys.exit(2)

        file.close()
        return address_list

def isIpAccessible(ip, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
                sock.connect((ip, int(port)))
                sock.shutdown(socket.SHUT_RDWR)
                sock.close()
                return True
        except:
                return False

def printResult(address, result):
        if sys.platform == 'win32':
                if result:
                        print address['ip'] + ':' + address['port'] + ' is accessible.'
                else:
                        print '!!!!!!!!!! ' + address['ip'] + ':' + address['port'] + ' is not accessible. !!!!!!!!!!'
        else:
                if result:
                        print bcolors.OKBLUE + address['ip'] + ':' + address['port'] + ' is accessible.' + bcolors.ENDC
                else:
                        print bcolors.BOLD + bcolors.FAIL + address['ip'] + ':' + address['port'] + ' is not accessible.' + bcolors.ENDC

if __name__ == '__main__':
        main(sys.argv[1:])