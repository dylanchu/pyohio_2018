#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class WindowMain:
	
	def __init__(self):

		# Get GUI from Glade file
		self.builder = Gtk.Builder()
		self.builder.add_from_file("gui1.glade")
		
		# Display main window
		self.windowMain = self.builder.get_object("windowMain")		
		self.windowMain.show()	

	def main(self):
		Gtk.main()	
		

if __name__ == "__main__":

	application = WindowMain()
	application.main()
