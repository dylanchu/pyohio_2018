#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class WindowMain:

	def __init__(self):

		# Get GUI from Glade file
		self.builder = Gtk.Builder()
		self.builder.add_from_file("gui5.glade")
		self.builder.connect_signals(self)		
		
		# Display main window
		self.windowMain = self.builder.get_object("window_main")		
		self.windowMain.show()	
		
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
		
	def on_window_main_destroy(self, widget, data=None):
		print("on_window_main_destory")
		Gtk.main_quit()
		
	def on_file_quit_activate(self, widget, data=None):
		print("on_file_quit")
		self.windowMain.destroy()
			
	def main(self):
		Gtk.main()	

if __name__ == "__main__":

	application = WindowMain()
	application.main()
