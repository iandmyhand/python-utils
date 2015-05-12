##-*- coding: utf-8 -*- 
#!/usr/bin/python
'''
This app can test TCP protocol only, because client can\'t test UDP protocol.

usage:
        $ python checkHostIsAccessble.py -f <filename>

Each Host and Port will must be separated by colon(:).
Each address must be separated by new line.
        e.g.:   127.0.0.1:80
                127.0.0.2:443
'''

import sys, getopt, socket
import os.path

options = {
        'timeout' : 5,
        'sample-filename' : 'host-list-sample.txt',
        'bcolors' : {
                'HEADER' : '\033[95m',
                'OKBLUE' : '\033[94m',
                'OKGREEN' : '\033[92m',
                'WARNING' : '\033[93m',
                'FAIL' : '\033[91m',
                'ENDC' : '\033[0m',
                'BOLD' : '\033[1m',
                'UNDERLINE' : '\033[4m',
        }
}

def main(argv):
        file_name = options['sample-filename']
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
                if 'comment' in address:
                        print unicode('\n' + address['comment'])
                else:
                        print 'checking ' + address['host'] + ':' + address['port'] + ' ...'
                        printResult(address, isHostAccessible(address['host'], address['port']))

def usage():
        print 'This app can test TCP protocol only, because client can\'t test UDP protocol.'
        print ''
        print 'usage:'
        print '\t$ python checkHostIsAccessble.py -f <filename>'
        print ''
        print 'Refer ' + options['sample-filename'] + ' file.:'
        print '\tEach Host and Port will must be separated by colon(:).'
        print '\tEach address must be separated by new line(' + os.pathsep + ').'
        print '\t\te.g.:\t127.0.0.1:80'
        print '\t\t\t127.0.0.2:443'
        sys.exit(0)

def getAddressList(file_name):
        print 'read file: ' + file_name

        try:
                if os.path.isfile(file_name):
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
                        # Print comment.
                        if line.startswith( '#' ):
                                address_list.append({'comment':line})
                                continue
                        tmp_arr = line.split(':')
                        if len(tmp_arr) is 2:
                                address_list.append({'host':tmp_arr[0], 'port':tmp_arr[1], 'protocol':'TCP'})
                        elif len(tmp_arr) is 3:
                                address_list.append({'host':tmp_arr[0], 'port':tmp_arr[1], 'protocol':tmp_arr[2]})
                        else:
                                print '\tAddress must be "HOST:PORT", but [' + line + '] is not.'
                                print '\t\te.g.: 127.0.0.1:80'
                                sys.exit(2)

        except Exception as e:
                print e

        finally:
                file.close()

        return address_list

def isHostAccessible(host, port):
        result = False
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(options['timeout'])
        try:
                sock.connect((host, int(port)))
                sock.shutdown(socket.SHUT_RDWR)
                result = True
        except Exception as e:
                try:
                        errno, errtxt = e
                except ValueError:
                        print e
                else:
                        if errno == 107:
                                result = True
                        else:
                                print 'errno: ' + str(errno)
                                print 'errtxt: ' + errtxt
        finally:
                sock.close()
        return result

def printResult(address, result):
        if sys.platform == 'win32':
                if result:
                        print address['host'] + ':' + address['port'] + ' is accessible.'
                else:
                        print '!!!!!!!!!! ' + address['host'] + ':' + address['port'] + ' is not accessible. !!!!!!!!!!'
        else:
                if result:
                        print options['bcolors']['OKBLUE'] + address['host'] + ':' + address['port'] + ' is accessible.' + options['bcolors']['ENDC']
                else:
                        print options['bcolors']['BOLD'] + options['bcolors']['FAIL'] + address['host'] + ':' + address['port'] + ' is not accessible.' + options['bcolors']['ENDC']

if __name__ == '__main__':
        reload(sys)
        sys.setdefaultencoding('utf-8')
        main(sys.argv[1:])