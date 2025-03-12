#!/usr/bin/python3
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout
from kivy.network.urlrequest import UrlRequest
import scapy
import time
from io import BytesIO
from lxml import etree
from queue import Queue
import sys
import threading
import requests
import scrapy
import logging
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import argparse
from concurrent.futures import ThreadPoolExecutor
import subprocess
import csv
from pprint import pprint
import random
from kivy.clock import Clock
from kivy.properties import ObjectProperty, NumericProperty

Builder.load_string('''
#:import Factory kivy.factory.Factory
#:import SwapTransition kivy.uix.screenmanager.SwapTransition
<MainMenu>:
    FloatLayout:
        canvas.before:
            Color:
                rgba: 0.235, 0.271, 0.302, 1
            Rectangle:
                pos: self.pos
                size: self.size
        BoxLayout:
            orientation: 'vertical'
            rows: 4
            Label:
                size_hint: 1,0.12
                text: "Secrete_service"
                text_size: self.size
                halign: 'left'
                valign: 'middle'
                font_size: 32
                color: [0.114,0.18,0.224,1]
                
            StackLayout:
                size_hint: 1,0.10
                orientation: 'lr-tb'
                #Menu layout
                Button:
                    id: arp
                    text: "Arper"
                    size_hint: 0.166,1
                    on_press: spaceholder.add_widget(Factory.ArpSpoof())
                #Asset Assignment System
                Button:
                    id:fp 
                    text: "FingerPrint"
                    size_hint: 0.166,1
                    on_press: spaceholder.add_widget(Factory.FingerPrint())

                #Asset Assignment System
                Button:
                    id:bf 
                    text: "BruteForce"
                    size_hint: 0.166,1
                    on_press: spaceholder.add_widget(Factory.BruteForce())
                #Review and Revise System
                Button:
                    id: prx
                    text: "Proxy"
                    size_hint: 0.166,1
                    on_press: spaceholder.add_widget(Factory.Proxy())
                #Administrative System
                Button:
                    id: ps
                    text: "PortScan"
                    size_hint: 0.166,1
                    on_press: spaceholder.add_widget(Factory.PortScan())
                #Analytics and Reporting System
                Button:
                    id: spd
                    text: "Spider"
                    size_hint: 0.166,1
                    on_press: spaceholder.add_widget(Factory.Spider())
                #Http-repeater
                Button:
                    id: rpt
                    text: "Repeater"
                    size_hint: 0.166,1
                    on_press: spaceholder.add_widget(Factory.HttpRepeater())

                #Analytics and Reporting System
                Button:
                    id: snf
                    text: "Sniffer"
                    size_hint: 0.166,1
                    on_press: spaceholder.add_widget(Factory.Sniffer())

                #Analytics and Reporting System
                Button:
                    id: vs
                    text: "VulnScan"
                    size_hint: 0.166,1
                    on_press: spaceholder.add_widget(Factory.VulnScanner())
                
                #Analytics and Reporting System
                Button:
                    id: hscr
                    text: "HashTool"
                    size_hint: 0.166,1
                    on_press: spaceholder.add_widget(Factory.HashCracker())

                #Analytics and Reporting System
                Button:
                    id: tcd
                    text: "Decoder"
                    size_hint: 0.166,1
                    on_press: spaceholder.add_widget(Factory.Decoder())

                #Analytics and Reporting System
                Button:
                    id: fpt
                    text: "FootPrint"
                    size_hint: 0.166,1
                    on_press: spaceholder.add_widget(Factory.FootPrint())
                    
            Label:
                canvas.before:
                    Color:
                        rgba: 0.259, 0.643, 0.937, 1
                    Rectangle:
                        pos: self.pos
                        size: self.size
                size_hint: 1,0.005
                
            Widget:
                id: spaceholder

<ArpSpoof>:
    id: arp
    orientation: 'lr-tb'
    #Asset Details
    Label:
        BoxLayout:
            orientation: 'vertical'
            Label:
                text: "Enter subject ip: "
            TextInput:
                id: as1count
            Label:
                text: "Enter server: "
            TextInput:
                id: as2count

<BruteForce>
    id: bf
    orientation: 'lr-tb'
    #Asset Details
    Label:
        BoxLayout:
            orientation: 'vertical'
            Label:
                text: "Enter subject ip: "
            TextInput:
                id: as3count

<FingerPrint>
    id: fp
    orientation: 'lr-tb'
    #Asset Details
    Label:
        BoxLayout:
            orientation: 'vertical'
            Label:
                text: "Enter subject ip: "
            TextInput:
                id: as4count

<Proxy>
    id: prx
    orientation: 'lr-tb'
    #Asset Details
    Label:
        BoxLayout:
            orientation: 'vertical'
            Label:
                text: "Enter subject ip: "
            TextInput:
                id: as5count

<PortScan>
    id: ps
    orientation: 'lr-tb'
    #Asset Details
    Label:
        BoxLayout:
            orientation: 'vertical'
            Label:
                text: "Enter subject ip: "
            TextInput:
                id: as6count

<Spider>
    id: spd
    orientation: 'lr-tb'
    #Asset Details
    Label:
        BoxLayout:
            orientation: 'vertical'
            Label:
                text: "Enter subject ip: "
            TextInput:
                id: as7count

<HttpRepeater>
    id: rpt
    orientation: 'lr-tb'
    #Asset Details
    Label:
        BoxLayout:
            orientation: 'vertical'
            Label:
                text: "Enter subject ip: "
            TextInput:
                id: as8count

<Sniffer>
    id: snf
    orientation: 'lr-tb'
    #Asset Details
    Label:
        BoxLayout:
            orientation: 'vertical'
            Label:
                text: "Enter subject ip: "
            TextInput:
                id: as9count

<VulnScanner>
    id: vs
    orientation: 'lr-tb'
    #Asset Details
    Label:
        BoxLayout:
            orientation: 'vertical'
            Label:
                text: "Enter subject ip: "
            TextInput:
                id: as10count

<HashCracker>
    id: hscr
    orientation: 'lr-tb'
    #Asset Details
    Label:
        BoxLayout:
            orientation: 'vertical'
            Label:
                text: "Enter subject ip: "
            TextInput:
                id: as11count

<Decoder>
    id: tcd
    orientation: 'lr-tb'
    #Asset Details
    Label:
        BoxLayout:
            orientation: 'vertical'
            Label:
                text: "Enter subject ip: "
            TextInput:
                id: as12count

<FootPrint>
    id: fpt
    orientation: 'lr-tb'
    #Asset Details
    Label:
        BoxLayout:
            orientation: 'vertical'
            Label:
                text: "Enter subject ip: "
            TextInput:
                id: as13count

<BruteForce>
    id: pos
    orientation: 'lr-tb'
    #Asset Details
    Label:
        BoxLayout:
            orientation: 'vertical'
            Label:
                text: "Enter subject ip: "
            TextInput:
                id: as14count
                
''')

class MainMenu(Screen):
    pass
class MyScreenManager(ScreenManager):
    pass
class ArpSpoof(Screen):
    container = ObjectProperty(None)
    def on_pre_enter(self):
        Window.size = (800, 600)

    def get_mac(ip):
        mac = self.ids.input_value.text
        arp_request = scapy.ARP(pdst = ip) 
        broadcast = scapy.Ether(dst ="ff:ff:ff:ff:ff:ff") 
        arp_request_broadcast = broadcast / arp_request 
        answered_list = scapy.arp(arp_request_broadcast, timeout = 5, verbose = False)[0] 
        return answered_list[0][1].hwsrc

class FingerPrint(StackLayout):
    fingerprint = ObjectProperty(None)

    def on_pre_enter(self):
        Window.size = (400, 300)

class Proxy(StackLayout):
    pass
class Sniffer(StackLayout):
    pass
class VulnScaner(StackLayout):
    pass

class HttpRepeater(StackLayout):
    pass
class Decoder(StackLayout):
    pass
class HashCracker(StackLayout):
    pass
class FootPrint(StackLayout):
    pass

class MercenaryApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainMenu(name='mainmenu'))
        sm.add_widget(ArpSpoof(name='arpspoof'))
        return sm

if __name__ == '__main__':
    MercenaryApp().run()
