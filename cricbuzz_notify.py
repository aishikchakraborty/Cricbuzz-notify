import requests
import xml.dom.minidom
import urllib2
from bs4 import BeautifulSoup
from time import sleep
import os

def notify(title, subtitle, message):
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    os.system('terminal-notifier {}'.format(' '.join([m, t, s])))
    return 0;

def func():
	url = "http://synd.cricbuzz.com/j2me/1.0/livematches.xml"
	f = urllib2.urlopen(url)
	doc = xml.dom.minidom.parse(f)
	node = doc.documentElement
	matches = node.getElementsByTagName("match")
	match = matches[0]
	mchdesc = match.getAttribute("mchDesc")
	try:
		team = match.getElementsByTagName("btTm")
		tm = team[0].getAttribute("sName")
		team1 = match.getElementsByTagName("blgTm")
		tm1 = team1[0].getAttribute("sName")
		innings = match.getElementsByTagName("Inngs")
		runs = innings[0].getAttribute("r")
		runs1 = innings[1].getAttribute("r")
		wkts = innings[0].getAttribute("wkts")
		wkts1 = innings[1].getAttribute("wkts")
		s = tm + " " + runs + "/" + wkts + " vs " + tm1 + " " + runs1 + "/" + wkts1
		notify(title    = 'A Real Notification',
        		subtitle = 'with python',
       			message  = s)

	except Exception:
		print ""
	return 0;

def main():
	while True:
		func()
		sleep(10)
	return 0;
if __name__ == "__main__":
	main()
