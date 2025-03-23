import requests
import scrapy
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time
import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout

#Define the Crawler Function:
visited = set()
        
def crawl(url, base_url):
    if url not in visited:
        visited.add(url)
        global response
        response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        for link in soup.find_all('a'):
            href = link.get('href')
            #create logfile for saving results in a file
            logfile_name = "f spidering_logs.txt"
            #now open logfile for writing
            with open(logfile_name, 'w') as logfile:
                if href:
                    full_url = urljoin(base_url, href)
                    print(full_url)
                    time.sleep(1) # Delay to avoid server overload/crash
                    crawl(full_url, base_url)
                    full_url_decode = full_url.decode() #Decode full url response to logfile
                    methods = ["Get", "Post"]
                    for i in methods:
                        if i in full_url_decode:
                            return full_url_decode
                            base_url_decode = base_url.decode() #Decode base url response
                            for k in methods:
                                if k in base_url_decode:
                                    return base_url_decode


if __name__ == "__main__":
#Start crawling URL:
    print("Ezase-Ntumbane")
    start_url = input("[*] Please enter the target-url: ")
    crawl(start_url, start_url)
