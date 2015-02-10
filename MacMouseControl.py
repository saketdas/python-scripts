from Quartz.CoreGraphics import CGEventCreateMouseEvent
from Quartz.CoreGraphics import CGEventPost
from Quartz.CoreGraphics import kCGEventMouseMoved
from Quartz.CoreGraphics import kCGEventLeftMouseDown
from Quartz.CoreGraphics import kCGEventLeftMouseDown
from Quartz.CoreGraphics import kCGEventLeftMouseUp
from Quartz.CoreGraphics import kCGMouseButtonLeft
from Quartz.CoreGraphics import kCGHIDEventTap

import time

def mouseEvent(type, posx, posy):
  theEvent = CGEventCreateMouseEvent(
      None, 
      type, 
      (posx,posy), 
      kCGMouseButtonLeft)
  CGEventPost(kCGHIDEventTap, theEvent)

def mousemove(posx,posy):
  mouseEvent(kCGEventMouseMoved, posx,posy);

def mouseclick(posx,posy):
  mouseEvent(kCGEventMouseMoved, posx,posy);
  mouseEvent(kCGEventLeftMouseDown, posx,posy);
  mouseEvent(kCGEventLeftMouseUp, posx,posy);

time.sleep(5)

counter = 100;
while counter > 0 :
  mouseclick(585,150)
  time.sleep(0.1)
  counter -= 1
  print "Clicks remaining %d" % counter

