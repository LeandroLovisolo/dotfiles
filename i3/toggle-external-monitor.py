#!/usr/bin/env python2

LAPTOP_DISPLAY = 'LVDS-1'
EXTERNAL_DISPLAY = 'VGA-1'
TMP_FILE = '~/.i3/.external-monitor-active'

import os
from subprocess import call

TMP_FILE = os.path.expanduser(TMP_FILE)

def turn_on():
  call(['xrandr', '--output', EXTERNAL_DISPLAY, '--auto',
  # call(['xrandr', '--output', EXTERNAL_DISPLAY, '--mode', '1680x1050',
        '--right-of', LAPTOP_DISPLAY])

def turn_off():
  call(['xrandr', '--output', EXTERNAL_DISPLAY, '--off'])

if os.path.isfile(TMP_FILE):
  turn_off()
  os.remove(TMP_FILE)
else:
  turn_on()
  f = open(TMP_FILE, 'w')
  f.close()
