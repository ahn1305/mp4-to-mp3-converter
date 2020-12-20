# Importing necessary packages 
import tkinter as tk 
from pathlib import Path
import os
from tkinter import *
from tkinter import messagebox, filedialog 
#--------------------------------------------------------------------------------------------------------------------------------

root = tk.Tk()

#--------------------------------------------------------------------------------------------------------------------------------

   
# Setting the title, background color  
# and size of the tkinter window and  
# disabling the resizing property 
root.geometry("600x120") 
root.resizable(False, False) 
root.title("Mp4-to-Mp3 Converter") 
root.config(background="#000000") 

#--------------------------------------------------------------------------------------------------------------------------------
#Functions(Browse and Convert)

def Browse(): 
    # Presenting user with a pop-up for 
    # directory selection. initialdir  
    # argument is optional Retrieving the 
    # user-input destination directory and 
    # storing it in video_Directory
    video_Directory = filedialog.askopenfilename(initialdir = "/",title = "Select a File", filetypes = (("Video files",  "*.mp4*"), ("all files","*.*"))) 
   
    # Displaying the directory in the directory 
    # textbox 
    video_loc.set(video_Directory) 

def Convert():

	if len(video_loc.get()) == 0:
		tk.messagebox.showerror("Error","Select a file to convert")
	else:

	    location = video_loc.get()

	    loca = Path(location)
	    
	    h = loca.name

	    t = location.replace(h,'')

	    original_location = t+'"'+h+'"'

	    converted_h = '"'+h+'"'

	    location_final = loca.name+".mp3"

	    saved_destination = "converted_files/"+converted_h.replace('.mp4',".mp3")

	    conversion = f"ffmpeg -i {original_location} {saved_destination}" 

	    os.system(conversion)

	    tk.messagebox.showinfo("Conversion successful",f"File saved as\n\n{location_final.replace('.mp4','')}\n\n In {saved_destination}")

	    root.video_entry.delete(first=0,last=100)

#--------------------------------------------------------------------------------------------------------------------------------			   
#vars
video_loc = StringVar()
destination_path = StringVar()

#Labels
video_location = Label(root,text="VideoLocation :",bg="#E8D579").grid(row=1,column=0,pady=5,padx=5)

#Entry
root.video_entry = Entry(root,width=40,textvariable=video_loc)
root.video_entry.grid(row=1,column=1,pady=5,padx=5) 

#Buttons
browse_B = Button(root,text="Browse",command=Browse, width=10,bg="#05E8E0").grid(row=1,column=2,pady=1,padx=1)
Convert_B = Button(root, text="Convert",command=Convert,width=20,bg="#05E8E0").grid(row=3,column=1,pady=3,padx=3) 

root.mainloop()
#--------------------------------------------------------------------------------------------------------------------------------
