import os
import json
import phonenumbers
import colorama
from colorama import Fore 
from phonenumbers import carrier
from phonenumbers import geocoder
from tabulate import tabulate
from urllib.request import urlopen
import sys 
import time 


class NumberAnalyzer(object):
    def __init__(self, number):
        self.number = phonenumbers.parse(number)
        self.url = "https://ipinfo.io/" # basic ip tracer link, but how could it fetch an IP via number? 

    def analyze(self):
        description = geocoder.description_for_number(self.number, "en")
        supplier = carrier.name_for_number(self.number, "en")
        response = urlopen(self.url)
        data = json.load(response)
        return [description, supplier, data]
    
    @property
    def parse_data(self):
        country, supplier, device = self.analyze()
        region = device["region"] # region/ country 
        city = device["city"] # city where sim parsed
        lat, lon = str(device["loc"]).split(",")
        location = f"Latitude: {lat}, Longtitude: {lon}" # longitude and latitude, find a way to return individual rows
        postal = device["postal"] # postal code EX: 34501
        timezone = device["timezone"] # timezone 
        server = device["org"] #ORG NAME
        hostname = device["hostname"] # ISP
        #print(" IP used to connect was ")
        ip = device["ip"] # how would it get this?
        time.sleep(0.1)
        return [["Country  = ", country], ["Region   = ", region], ["City     = ", city], ["Location = ", location], 
                ["Postal   = ", postal], ["Timezone = ", timezone], ["Server   = ", server], ["Hostname = ", hostname], 
                ["Supplier = ", supplier], ["IP       = ", ip]] #info gathered from phone or returnable info 
    
    def __str__(self):
        return str(f"\n{tabulate(self.parse_data)}") # parse the fata- or return the datas via tabed 

if __name__ == "__main__":
    os.system("clear") # win32-64 will use cls since os clear is cls for windows and clear for linux
    print(Fore.RED+" ")
    time.sleep(1)
    print(" [=] Do's and Dont's [=] ")
    time.sleep(0.1)
    print(" [!] Do not use this for illegal use [!]  ")
    time.sleep(0.1)
    print(" [!] Do not run this as root [!] ")
    time.sleep(0.1)
    print(" [!] Do not run this program with proxy chains [!] ")
    print(" waiting 11 seconds to start this program ")
    time.sleep(1)
    time.sleep(10)
    os.system(' clear ')
    print(Fore.BLUE+" ")
    print("[ Ghosted-PH-Tracer - ArK_Angel ]\n")
    number = input("Enter Number: ")
    os.system(' clear ')
    print(" Waiting till script kiddies leave XDDD ")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    analyze = NumberAnalyzer(number)    
    time.sleep(0.1)
    print(" [+] note that the IP IS NOT YOUR TARGETS IT IS THE IPA USED TO CONNECT TO THE WEBSITE ")
    print(analyze)
    time.sleep(5)
    print("+===================+")
    print("+Have a nice one XD +")
    print("+===================+")
    sys.exit()