# python

## shebang:

#!/usr/bin/env python3

## dependances

#$ pip install <package>

## Conditions

"""
Les conditions en Python 3 sont similaires à celles des autres langages de programmation. 
Vous pouvez utiliser les opérateurs de comparaison suivants pour évaluer les expressions booléennes:

== : égal à
!= : différent de
< : inférieur à
> : supérieur à
<= : inférieur ou égal à
>= : supérieur ou égal à

"""

x = 5
if x > 2:
    print("x est plus grand que 2")
else:
    print("x est plus petit ou égal à 2")

## Conditions ternaires

x = 5
y = "plus grand que 2" if x > 2 else "plus petit ou égal à 2"


## Boucles for

for i in range(5):
    print(i)

## Boucles foreach

fruits = ["pomme", "banane", "cerise"]
for fruit in fruits:
    print(fruit)

## linux time:


>>> import time
>>> time.ctime(152546)
'Fri Jan  2 19:22:26 1970'


## base64:


>>> import base64
>>> base64.b64encode(b'test')
'dGVzdA=='


## Hexlify:


>>> import binascii
>>> binascii.hexlify('A')
'41'
>>> binascii.unhexlify('41') 
'A'


## file:


    with open(file, 'r') as f:
        line = f.readline()
        while line:
            if "MAC Address" in line:
                tgt.addmac(line.split(" ")[1].replace(",",""))
            line = f.readline() #ligne suivante
          
            
            
## Process:


    scan = subprocess.Popen(["nmap","-sP",subnet,"-oG", file ], stdout=subprocess.PIPE)
    while scan.poll() is None: #on attend la fin du process
        pass
    if scan.returncode == 0:
        print("[*] scan arp terminé")



## sha256:


import hashlib
def encrypt_string(hash_string):
    sha_signature = hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature

hash_string = 'confidential data'
sha_signature = encrypt_string(hash_string)
print(sha_signature)
# 3fef7ff0fc1660c6bd319b3a8109fcb9f81985eabcbbf8958869ef03d605a9eb


## mini serveur web:
"""
python3 -m http.server
python -m SimpleHTTPServer
"""

## changer le port:
"""
sudo python3 -m http.server 80
"""

## binaire et char:


>>> import binascii
>>> bin(int(binascii.hexlify('Sam & Max'), 16))[2:]
'10100110110000101101101001000000010011000100000010011010110000101111000'
 
# Et l’inverse:


binascii.unhexlify('%x' % int('0b' + '10100110110000101101101001000000010011000100000010011010110000101111000', 2))
'Sam & Max'


## url decode:

import urllib.parse
encodedStr = 'Hell%C3%B6%20W%C3%B6rld%40Python'
urllib.parse.unquote(encodedStr)
'Hellö Wörld@Python'


## url encode:


import urllib.parse
urllib.parse.quote('&')
#'%26'


## http client:


import http.client
conn = http.client.HTTPSConnection('enirdd6d0146.x.pipedream.net')
conn.request("POST", "/", '{ "name": "Princess Leia" }', {'Content-Type': 'application/json'})

"""
h1 = http.client.HTTPConnection('www.python.org')
h2 = http.client.HTTPConnection('www.python.org:80')
h3 = http.client.HTTPConnection('www.python.org', 80)
h4 = http.client.HTTPConnection('www.python.org', 80, timeout=10)
"""

import http.client

connection = http.client.HTTPSConnection("www.journaldev.com")
connection.request("GET", "/")
response = connection.getresponse()
print("Status: {} and reason: {}".format(response.status, response.reason))

connection.close()


## request:

import requests
url = "http://staging-order.mango.htb"
headers = {'Content-type': 'application/x-www-form-urlencoded'}
post_data = "username=admin&password[$regex]=" + payload +".*" + "&login=login"
r = requests.post(url, data=post_data, headers=headers, allow_redirects=False)


## conversion char / Unicode / ascci:

ord('A')
65
chr(65)
'A'

## little indian:

from struct import pack
pack('<I', 0x08048474)


## avoir un shell (ou corriger le shell apres un netcat) 

"""
python -c "import pty;pty.spawn('/bin/bash')"
"""

## divers:

fonction one line: [print(i) for i in range(4)]


>>> import string
>>> string.printable
'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
>>> string.ascii_letters
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
>>> string.digits
'0123456789'

