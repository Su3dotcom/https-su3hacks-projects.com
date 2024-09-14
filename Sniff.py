#!/usr/bin/python3
import socket
import os 
host = input("Enter host/ip to sniff:")

def main():
    #Create a raw socket bin to public interface
    if os.name == 'nt':
        socket_protocol = socket.IPPROTO_IP
    else:
        socket_protocol = IPPROTO_ICMP
        sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)
        sniffer.bind((host, 0))
            #include ip header on the capture
        sniffer.setsockopt(socket.IPPROTO_IP, socket.HDRINCL, 1)
        if os == 'nt':
            sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
            # read one packet
            print(sniffer.recv_from(65565))
            #if its windows,turn off promiscous mode
            if os.name == 'nt':
                sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
                print('\nUser interrupted.')
                if hosts_up:
                    print(f'\n\nSummary: Hosts up on {SUBNET}')
                    for host in sorted(hosts_up):
                        print(f'{host}')
                        print('')
                        sys.exit()

            if __name__ == '__main__':
                main()