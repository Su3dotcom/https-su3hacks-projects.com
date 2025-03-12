#!/usr/bin/python3
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
import requests
import random
import datetime

class ProxyServer(GridLayout):
    def __init__(self, **kwargs):
        super(ProxyServer, self).__init__(**kwargs)

#my proxy-list
proxies = [
  'https'  "198.13.36.75" "443", #US https port:8080
    'https' "182.258.31.42" "443", #Indonesian https port:8888
    'http' "119.206.242.196" "80", #Korean http port:80
    'http' "83.142.225.197" "3128", #UK http port:3128
    'http' "129.226.50.76" "8088", #US http port:8088
    'http' "46.63.71.13" "8080", #Ukrain http port:8080
    'http' "193.59.27.71" "36748", #Polish http port:36748
    #one port short 443
]

last_subnet = ""
dead_proxies = {}
def get_proxy():
    while True:
        for i in range(10): #Ten requests at the time
            ip = random.choice(proxies)
            ip_subnet = ip.split('.')[2]
            if ip_subnet == last_subnet:
                continue
            if ip in dead_proxies:
                if dead_proxies[ip] - datetime.utcnow() > timedelta(seconds=30):
                #proxy has not recovered yet - skip
                    continue
                else:
                    # proxy has recovered - set it free!
                    del dead_proxies[ip]
                    last_subnet = ip_subnet
                    return ip

def scrape(url, retries=0):
#make requests using the selected proxy
        proxy = get_proxy(proxy_list)
        try:
            response = response.get('https://neverssl.com',proxies = proxy)
            #mark dead proxies and retry
            if response.status_code == 200:
                return response
            else:
                dead_proxies[proxy] = datetime.utcnow()
                retries += 1
            if retries > 3:
                raise RetriesExceeded()
            scrape(url, retries = retries)
            print(response.status_code)
        except requests.RequestException as e:
            print(f"Error: {e}")
        
        try:
            if port == 443: #https
                context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
                context.load_cert_chain(certfile='server.crt', keyfile='server.key')
                s = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=webserver)
            else:
                #http
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(10)
                s.connect((webserver, port))
                s.sendall(request)
        except socket.error as e:
                print(f"Socket error: {e}")
        except ssl.SSLError as e:
            print(f"SSL error: {e}")

class SlowAssasinApp(App):
    def build(self):
        return ProxyServer()

if __name__ == '__main__':
    SlowAssasinApp().run()