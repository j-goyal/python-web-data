import urllib.request as ur, urllib.parse as up, urllib.error as ue

hand = ur.urlopen('https://myherupa.com/')

for line in hand:
    print(line.decode().strip())
