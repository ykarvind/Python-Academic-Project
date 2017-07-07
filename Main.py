'''
Created on Jun 1, 2017

@author: macbookpro
'''

from TourGui import TourGui
from tkinter import Tk

def main():
    
    root=Tk()
    root.title('Tour')
    TourGui(root)
    root.mainloop()

if __name__=='__main__': main()