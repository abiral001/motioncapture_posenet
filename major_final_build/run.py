from tkinter import *
import os

root = Tk()

def executeLiveVideo():
    os.system('python final.py')

def executeRecordedVideo():
    from tkinter.filedialog import askopenfilename
    filename = askopenfilename(filetypes=(("jpeg files", "*.mp4"), ("all files", "*.*")))
    os.system('python final.py --video {}'.format(filename))

label = Label(root, text = "Motion Capture using Posenet", font = ("Cascadia Code", 20))
createdBy = Label(root, text="Created By: Abiral Pokharel, Eelisha Pathak, Gaurav Regmi, Nidwija Bhatta", font = ("Cascadia Code", 14))
supervisedBy = Label(root, text = "Supervised By: Prof. Dr. Subarna Shakya", font = ("Cascadia Code", 16))
livefeed = Button(root, text = "Use Live Video", width = 50, height = 2, bg = 'yellow', command = executeLiveVideo)
useRecorded = Button(root, text = "Use Video File", width = 50, height = 2, bg = 'yellow', command = executeRecordedVideo)

label.grid(row = 0, column = 1)
createdBy.grid(row = 1, column = 0)
supervisedBy.grid(row = 1, column = 2)

livefeed.grid(row = 2, column = 0)
useRecorded.grid(row = 2, column = 2)

root.mainloop()