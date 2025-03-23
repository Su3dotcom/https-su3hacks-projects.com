#!/usr/bin/python3
from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
import kivy
from kivy.uix.label import Label
from kivy.uix.button import Button
from wifidroid.wifi import WifiManager

text = 'Test'
try:
    wifi = WifiManager()
    wifi.startScan()
    wifi.EnabledWifi(True)
    for i in range(wifi.scanResults.size()):
        ssid = [wifi.ScanResults.get(i).SSID]
        bssid = [wifi.ScanResults.get(i).BSSID]
        levell = [wifi.ScanResults.get(i).level]
        text += ssid[0] + " " + bssid[0] + " " + str(levell[0])
except Exception as e:
    print("Something went wrong", e)

try:
    wifi.ConnectWifiWpa("WifiName", "WifiPassword")
except:
    pass

#wifi ConnectWifiPublic("WifiName")

class Interface(FloatLayout):
    output = StringProperty()
    input = StringProperty()

    def get_ssid(self):
        self.ssid = self.ids.input_value.text  #store input in a variable

class AndroWifiApp(App):
    def build(self):
        return Interface()

if __name__ == '__main__':
    print("Ezase-Ntumbane")
AndroWifiApp().run()
