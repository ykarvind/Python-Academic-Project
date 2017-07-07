'''
Created on Jun 1, 2017

@author: macbookpro
'''

from tkinter import Frame, Button, Label, Entry, messagebox,TOP,BOTTOM,END
from Tour import Tour

class TourGui(Frame):
    
    #TourGUI constructor
    def __init__(self,parent):
        Frame.__init__(self,parent)
        frame1=Frame(parent)
        frame1.pack(side=TOP)
        frame2=Frame(parent)
        frame2.pack(side=BOTTOM)
        frame1.config(bg='grey')
        frame2.config(bg='grey')
        self.labelOrigin=Label(frame1,text='Origin', bg='grey')
        self.labelOrigin.pack(side=TOP)
        self.entryOrigin = Entry(frame1, font = ('Helvetica', 18))
        self.entryOrigin.pack(side=TOP)
        self.labelDest=Label(frame1,text='Destination', bg='grey')
        self.labelDest.pack(side=TOP)
        self.entryDest = Entry(frame1, font = ('Helvetica', 18))
        self.entryDest.pack(side=TOP)
        self.labelMode=Label(frame1,text='Mode', bg='grey')
        self.labelMode.pack(side=TOP)
        self.entryMode = Entry(frame1, font = ('Helvetica', 18))
        self.entryMode.pack(side=TOP)
        self.labelDist=Label(frame2,text='Distance (m)', bg='grey')
        self.labelDist.pack(side=TOP)
        self.entryDist=Entry(frame2,font = ('Helvetica', 18))
        self.entryDist.pack(side=TOP)
        self.button=Button(frame2,text='Get Distance',command=self.onClick)
        self.button.pack(side=BOTTOM)
        self.pack()        
        
    def onClick(self):     
        mode=self.entryMode.get()
        if (mode !='') and (mode!='driving') and (mode!='bicycling') and (mode!='walking'):
            messagebox.showinfo('Invalid mode','valid modes are driving,bicycling and walking.')
        else:
            origin = self.entryOrigin.get()
            destination= self.entryDest.get()
            t = Tour(origin,destination)
            try:
                value = t.distance(mode)     
                self.entryDist.configure(state="normal")
                self.entryDist.delete(0, END)
                self.entryDist.insert(END, value)
                self.entryDist.configure(state="disable")     
            except ValueError as e:
                messagebox.showinfo('Error', e)
