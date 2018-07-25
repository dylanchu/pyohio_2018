#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import GObject 

import os
import random

class WindowMain:

	def __init__(self):

		# Get GUI from Glade file
		self.builder = Gtk.Builder()
		self.builder.add_from_file("gui6.glade")
		self.builder.connect_signals(self)		
		
		# Display main window
		self.windowMain = self.builder.get_object("window_main")		
		self.windowMain.show()	
		
		# Get list of files in image directory
		img_dir = "img"
		self.img_files = os.listdir(img_dir)
		
		# Display image
		self.imageMain = self.builder.get_object("image_main")
		img_file = "img/kg.jpg"
		self.imageMain.set_from_file(img_file)
		self.imageMain.show()		

		# Setup status bar
		self.statusBar = self.builder.get_object("bar_status")
		self.context_id = self.statusBar.get_context_id("status")
		self.status_count = 0	
		
		# Update status bar
		status_text = "File: " + img_file		
		self.statusBar.push(self.context_id, status_text)		
		
		# Start timer
		timer_interval = 3
		GObject.timeout_add_seconds(timer_interval, self.on_handle_timer)
		
	def on_window_main_destroy(self, widget, data=None):
		print("on_window_main_destory")
		Gtk.main_quit()
		
	def on_file_quit_activate(self, widget, data=None):
		print("on_file_quit")
		self.windowMain.destroy()
		
	def on_handle_timer(self):
		# Display image
		img_file = "img/" + random.choice(self.img_files)
		self.imageMain.set_from_file(img_file)
		self.imageMain.show()	
		
		# Update status bar
		self.statusBar.pop(self.context_id)
		status_text = "File: " + img_file		
		self.statusBar.push(self.context_id, status_text)			
		return True
			
	def main(self):
		Gtk.main()	

if __name__ == "__main__":

	application = WindowMain()
	application.main()
