App starts to observe folder ("Folder To Track"), if a new file is moved to that folder the app will check if the file has the same file-type extension as optionbox. If it does, it will move the file (and all other files with same extension) to the destination folder.


Dev note:
It is possible to change Folder to track/ Destionation Folder/ OptionBox once you press the "Start" button.
Only way to stop the thread is to close the app.

BETA

v0.1
	*File Sorter runs from cmd python file_sorter.py
	*Tracked folder, destionation folder and file extension is harded coded into source code

v0.2
	*Added GUI so you can pick folders to track

v0.3
	*Added dropdown box to be able to hard coded file extensions

v0.4
	*Added option to add file extensions and save default folders through a txt file
	 there by creating a config.txt file

v0.5
	*Added button to open folders

v0.6
    *TODO check date modified so newest file gets moved to the directory. Start program > start dowloading > program takes newest pdf file > moves it to destionation.
