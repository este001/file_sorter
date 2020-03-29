from appJar import gui
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os


def config_reader():
    with open("config.txt", "r", encoding="utf-8") as read_config:
        config = read_config.readlines()
        return config


def config_update(update):
    open("config.txt", "w").close()
    with open("config.txt", "a+") as update_config:
        for item in update:
            update_config.write(item+"\n")


def read_default_folder():
    default = [d.rstrip('\n') for d in config_reader()[1:3]]
    return default


def read_extension():
    file_extension = [fe.rstrip('\n') for fe in config_reader()[4:]]
    return file_extension

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):

        for filename in os.listdir(app.getEntry('FolderToTrack')):
            src = app.getEntry('FolderToTrack') + "/" + filename
            try:
                if src.endswith(app.getOptionBox("extentionBox")):
                    new_destionation = app.getEntry('DestinationFolder') + "/" + filename
                    os.rename(src, new_destionation)
            except FileExistsError:
                os.remove('/Users/estef/Downloads/'+filename)


def button(press):
    my_button_dict = {'Start': start, 'Close': close,"Open Destination Folder": open_dest_folder, "Open Track Folder": open_track_folder}
    for k, v in my_button_dict.items():
        if k == press:
            v()


def observers():
    try:
        event_handler = MyHandler()
        observer.schedule(event_handler, app.getEntry('FolderToTrack'), recursive=True)
        observer.start()
    except (RuntimeError,FileNotFoundError) as error:
        app.hideLabel("loadinglbl")
        app.errorBox("obs", error)


def start():
    try:
        app.thread(observers)
        app.setStatusbar("Tracking Folder..")
        app.setStatusbarBg("green")
    except FileNotFoundError:
        app.errorBox("file404", "You have to select 2 folders")


def close():
    try:
        observer.stop()
        observer.join()
        app.stop()
    except RuntimeError:
        app.stop()


def open_dest_folder():
    os.startfile(app.getEntry("DestinationFolder"))


def open_track_folder():
    os.startfile(app.getEntry("FolderToTrack"))


def save_default_folder():
   if app.getCheckBox("defaultbox"):
       app.setCheckBoxText("defaultbox","Saved!")
       orig = config_reader()
       orig[1] = app.getEntry("FolderToTrack")
       orig[2] = app.getEntry("DestinationFolder")
       updated = [o.rstrip("\n") for o in orig]
       config_update(updated)
   else:
       app.setCheckBoxText("defaultbox", "Set as default Folder")


observer = Observer()

app = gui("File")
app.setResizable(False)

app.startLabelFrame("File Sorter")
app.setPadding(0,10)
app.setSticky("nn")
app.addNamedCheckBox("Set as default Folder", "defaultbox", 0)
app.setCheckBoxChangeFunction("defaultbox", save_default_folder)
app.setSticky('ne')
app.addOptionBox("extentionBox", read_extension(), 0)
app.setSticky('ww')
app.addLabel("lbl1", "Folder to track", 0)
app.setSticky("ww")
app.addButton("Open Track Folder", button,1)
app.setInPadding(100,0)
app.addDirectoryEntry("FolderToTrack")
app.setEntry("FolderToTrack", read_default_folder()[0])

app.addStatusbar("Status")
app.setStatusbar("Not tracking folder..")

app.setInPadding(0,0)
app.setSticky("ww")
app.addLabel("lbl2", "File Destination")
app.addButton("Open Destination Folder", button,4)
app.setInPadding(100,0)
app.addDirectoryEntry("DestinationFolder")
app.setEntry("DestinationFolder", read_default_folder()[1])

# TODO Add option to open destination/tracked folder


app.setSticky("ss")
app.addButtons(['Start', 'Close'], button)
app.stopLabelFrame()
app.go()