#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, random, time, threading, Queue, subprocess, re, os  

from math import *
  
from numpy import array, append
import gtk
import glib
 
R = 400
 
degrees = pi/180
rotationMatrix = array([[1.,0,0], [0,1,0], [0,0,1]])
def rotate(rotationMatrix, angle, (axis1, axis2)):
    p, q = sin(angle), cos(angle)
    m = array([[1.,0,0], [0,1,0], [0,0,1]])
    m[axis1][axis1] = q
    m[axis1][axis2] = p
    m[axis2][axis1] = -p
    m[axis2][axis2] = q
    return rotationMatrix.dot(m)
 
rotate.xy = (0, 1)
rotate.yz = (1, 2)
rotate.xz = (0, 2)
print rotationMatrix
rotationMatrix = rotate(rotationMatrix, 30*degrees, rotate.xy)
print rotationMatrix
rotationMatrix = rotate(rotationMatrix, 60*degrees, rotate.yz)
print rotationMatrix
 
def pointRad(parallel, longitude, points):
    x = cos(parallel * degrees) * cos(longitude * degrees)
    y = sin(parallel * degrees)
    z = cos(parallel * degrees) * sin(longitude * degrees)
    if points is None:
        return array([[ x, y, z ]])
    else:
        return append(points, [[ x, y, z ]], axis=0)
 
def drawPoints(points):
  for x, y, z in points.dot(rotationMatrix):
    if z >= 0:
      point(int(x * R/2 + R/2), int(y * R/2 + R/2))
 
def grid1(points):
  for parallel in range(-90, 90, 15):
    for degree in range(0, 360, 3):
      points = pointRad(parallel, degree, points)
  for longitude in range(0, 360, 15):
    for degree in range(-90, 90, 3):
      points = pointRad(degree, longitude, points)
  return points
 
def grid2(points):
  for parallel in range(-90, 90, 5):
    for longitude in range(0, 360, 5):
      points = pointRad(parallel, longitude, points)
  return points
 
def scatter1(points):
  for i in range(3000):
    points = pointRad(
      random.random() * 180 - 90,
      random.random() * 360,
      points)
  return points
 
def scatter2(points):
  for i in range(3000):
    # inverse of the stem function of distribution (inv(stem(cos))):
    parallel = asin(random.random() * 2 - 1) / degrees
    longitude = random.random() * 360 - 180
    #if (floor(longitude/20) + floor(parallel/20)) % 2:
    #  continue
    points = pointRad(parallel, longitude, points)
  return points
 
pointsLists = []
pointsLists.append(grid1(None))
pointsLists.append(grid2(None))
pointsLists.append(scatter1(None))
pointsLists.append(scatter2(None))
 
class PyApp(gtk.Window):
  def __init__(self):
    super(PyApp, self).__init__()
    self.set_title("ball")
    self.resize(R + 40, R + 40)
    self.set_position(gtk.WIN_POS_CENTER)
    self.connect("destroy", gtk.main_quit)
    self.canvas = gtk.DrawingArea()
    self.canvas.connect("expose_event", self.expose)
    self.canvas.connect("motion_notify_event", self.motion)
    self.canvas.connect("enter_notify_event", self.enter)
    self.canvas.connect("leave_notify_event", self.leave)
    self.canvas.connect("button_press_event", self.click)
    self.canvas.set_events(
        gtk.gdk.POINTER_MOTION_MASK |
        gtk.gdk.ENTER_NOTIFY_MASK |
        gtk.gdk.LEAVE_NOTIFY_MASK |
        gtk.gdk.BUTTON_PRESS_MASK)
    self.lastX = self.lastY = None
    self.add(self.canvas)
    glib.timeout_add(20, self.onTimer)
    self.show_all()
    self.xyd = 0.0
    self.yzd = 0.0
    self.xzd = 0.0
 
  def onTimer(self):
    global rotationMatrix
    rotationMatrix = rotate(rotationMatrix, self.xyd, rotate.xy)
    rotationMatrix = rotate(rotationMatrix, self.yzd, rotate.yz)
    rotationMatrix = rotate(rotationMatrix, self.xzd, rotate.xz)
    self.xyd = (self.xyd * 999 + random.random()-0.5) / 1000
    self.yzd = (self.yzd * 999 + random.random()-0.5) / 1000
    self.xzd = (self.xzd * 999 + random.random()-0.5) / 1000
    self.canvas.queue_draw()
    return True
 
  def expose(self, widget, event):
    cr = widget.window.cairo_create()
    cr.set_source_rgb(0, 0, 0)
    cr.paint()
    rotatedPoints = pointsLists[0].dot(rotationMatrix)
    for x, y, z in rotatedPoints:
      if z < 0:
        cr.set_source_rgb(0.7 * -z, 0.0, 0.0)
        cr.rectangle(int(x * R/2 + R/2+20), int(y * R/2 + R/2+20), 1, 1)
        cr.fill()
    for x, y, z in rotatedPoints:
      if z >= 0:
        cr.set_source_rgb(z, z, z)
        cr.rectangle(int(x * R/2 + R/2+20), int(y * R/2 + R/2+20), 1, 1)
        cr.fill()
 
  def motion(self, widget, event):
    if self.lastX is not None:  # motion
      dx = self.lastX - event.x
      dy = self.lastY - event.y
      #print dx, dy
      self.xzd += dx / 10000.0
      self.yzd += dy / 10000.0
    self.lastX, self.lastY = event.x, event.y
 
  def enter(self, widget, event):
    self.lastX, self.lastY = event.x, event.y
 
  def leave(self, widget, event):
    self.lastX = self.lastY = None
 
  def click(self, widget, event):
    pointsLists.append(pointsLists.pop(0))
 
PyApp()
gtk.main()

