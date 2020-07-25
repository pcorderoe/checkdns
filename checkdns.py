import socket
import dns.resolver
import os
import time
import datetime
import sys


def check_dns(argv):
    if(len(argv) == 3):
        url = str(argv[1])
        reg = (argv[2])

        if(url != '' and reg != ''):
            os.system('clear')

            old_dns = 'mail.tecnigen.cl.'

            not_changed = True
            while not_changed:
                try:
                    for rdata in dns.resolver.query(url, reg):
                        if(str(rdata.exchange) != old_dns):
                            os.system(
                                "spd-say 'El registro MX finalmente ha cambiado.'")
                            print(str(datetime.datetime.now(
                            ))+" -- The MX registers of the domain scoped has finally changed ("+str(rdata.exchange)+")")
                            not_changed = False
                        else:
                            print(str(datetime.datetime.now()) +
                                  ' -- Not yet: ' + str(rdata.exchange))
                except:
                    print(str(datetime.datetime.now()) +
                          ' -- No DNS info available')
                if(not_changed):
                    time.sleep(5)

        else:
            print('usage: checkdns [url] [dnsType(MX,CNAME,A,TXT)]')
    else:
        print('usage: checkdns [url] [dnsType(MX,CNAME,A,TXT)]')


if __name__ == "__main__":
    check_dns(sys.argv)
