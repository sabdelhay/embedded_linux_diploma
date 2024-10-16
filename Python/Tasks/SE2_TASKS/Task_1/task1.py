#!/usr/bin/python3
import webbrowser

websites = {'facebook':"facebook.com", 'x':"x.com", 'reddit':"reddit.com", 'instagram':"instagram.com"}

def open_link(link):
    return webbrowser.get('firefox').open(link)
    