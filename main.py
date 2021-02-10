# Irfan-Lateef

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import *

Folder_name = ""
#Function for getting and handling file location
def openlocation():
    global Folder_name
    Folder_name = filedialog.askdirectory()
    if(len(Folder_name) > 1):
        ytderrorlocation.config(text=Folder_name, fg="green")
    else:
        ytderrorlocation.config(text="First Select Directory !!!", fg="red")
# Function to download videos
def downloadvideo():
    choice = ytdchoices.get()
    url = ytdentry.get()
    if(len(url) > 1):
        ytderror.config(text="")
        yt=YouTube(url)
        if(choice == choices[0]):
            if (len(Folder_name) > 1):
                select = yt.streams.filter(progressive=True, file_extension='mp4').first()
                select.download(Folder_name)
                ytderror.config(text="Download Completed")
            else:
                ytderrorlocation.config(text="First Select Directory !!!", fg="red")
        elif(choice == choices[1]):
            if (len(Folder_name) > 1):
                select = yt.streams.filter(progressive=True, file_extension='mp4').last()
                select.download(Folder_name)
                ytderror.config(text="Download Completed")
            else:
                ytderrorlocation.config(text="First Select Directory !!!", fg="red")
        elif(choice == choices[2]):
            if (len(Folder_name) > 1):
                select = yt.streams.filter(only_audio=True).first()
                select.download(Folder_name)
                ytderror.config(text="Download Completed")
            else:
                ytderrorlocation.config(text="First Select Directory !!!", fg="red")
        else:
            ytderror.config(text="Please Select a format to download", fg="red")
    else:
        ytderror.config(text="Please paste valid link", fg="red")
# Executing functions
def details():
    url = ytdentry.get()
    yt = YouTube(url)
    videotitle = yt.title
    titleheading.config(text="Title:")
    titlelabel.config(text=videotitle)
    if(yt.length <= 60):
        videolength = yt.length
        finalvideolength = str(videolength) + " Sec"
    else:
        videolength = round(yt.length/60, 0)
        finalvideolength = str(videolength) + " Min"
    durationheading.config(text="Duration:")
    durationlabel.config(text=finalvideolength)
    videoauthor = yt.author
    authorheading.config(text="Author:")
    authorlabel.config(text=videoauthor)






# From here the GUI (Graphical User Interface) starts.

root = Tk()
root.title("YouTube Video Downloader")
root.geometry("700x500")  # We are setting windows size.
root.columnconfigure(0, weight=1)  # Setting all contents in center
# Setting Link Label
ytdLabel = Label(root, text="Enter the URL of the Video", font=("arial", 15))
ytdLabel.grid()
# Setting the input value box
ytdentervalue = StringVar()
ytdentry = Entry(root, width=50, textvariable=ytdentervalue)
ytdentry.grid()
#Setting the error message
ytderror = Label(root, text="", fg="red", font=("arial", 10))
ytderror.grid()
# Asking for file location Label
savelabel = Label(root, text="Please Select Directory", font=("arial", 15, "bold"))
savelabel.grid()
# Creating a button for user to select directory
saveentry = Button(root, width=10, bg="red", fg="white", text="Choose path", command=openlocation)
saveentry.grid()
#Setting the error message for location
ytderrorlocation = Label(root, text="No Path Selected", fg="red", font=("arial", 10))
ytderrorlocation.grid()
# Setting label for asking download quality
ytdquality = Label(root, text="Select Quality", font=("arial", 15))
ytdquality.grid()
# Giving user an option to select resolution
choices = ["Lowest available quality", "Highest available quality", "Only Audio"]
ytdchoices = ttk.Combobox(root, values=choices)
ytdchoices.grid()
# Creating a button for user to download video
downloadbtn = Button(root, width=10, bg="red", fg="white", text="Download", command=downloadvideo)
downloadbtn.grid()

# Creating a button for user to See video Details
Detailbtn = Button(root, width=10, bg="red", fg="white", text="Details", command=details)
Detailbtn.grid()
# Displaying the Video Details
# Title heading
titleheading = Label(root, text="", font=("arial", 12, "bold"))
titleheading.grid()
# Displaying Title
titlelabel = Label(root, text="", font=("arial", 10))
titlelabel.grid()
# Duration Heading
durationheading = Label(root, text="", font=("arial", 12, "bold"))
durationheading.grid()
# Displaying Duration
durationlabel = Label(root, text="", font=("arial", 10))
durationlabel.grid()
# author Heading
authorheading = Label(root, text="", font=("arial", 12, "bold"))
authorheading.grid()
# Displaying author
authorlabel = Label(root, text="", font=("arial", 10))
authorlabel.grid()


# Developer Label
developerlabel = Label(root, text="Bolean Autocrats", font=("roboto", 15))
developerlabel.grid()


root.mainloop()