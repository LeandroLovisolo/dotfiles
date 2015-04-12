#!/usr/bin/env python2

TMP_FILE = '~/.i3/.external-monitor-active'

import os
from subprocess import call

TMP_FILE = os.path.expanduser(TMP_FILE)

def turn_on():
  call(['xrandr', '--output', 'VGA-0', '--mode', '1280x1024',
        '--right-of', 'LVDS'])

def turn_off():
  call(['xrandr', '--output', 'VGA-0', '--off'])

if os.path.isfile(TMP_FILE):
  turn_off()
  os.remove(TMP_FILE)
else:
  turn_on()
  f = open(TMP_FILE, 'w')
  f.close()
