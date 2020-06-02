#!usr/bin/env python3
#JobsFinder
#Version 0.1
#Author: Ruslan Shakirov
#https://github.com/ruslanski/JobsFinder
#Start Date: 06/01/2020

from tkinter import *
from tkinter import ttk
import tkinter.messagebox as tm
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox, Label, Button, FALSE, Tk, Entry
import tkinter
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import pyautogui as pag
import time
import sys
import os.path
import os

class JobSeekerBot(Tk):
    def __init__(self,master):
        self.master=master
        self.logo()
        self.background()
        #self.GetCredentials()

    def logo(self):
        """
        Method creates Tabs and Buttons inside main Window Frame.
        """
        #Set frame size and style for Top Logo.
        Tops=Frame(root)
        Tops.pack(side=TOP)
        #Set attributes of Top Logo.
        lblInfo=Label(root, font=('arial',20,'bold'), text="Job Finder",fg="Steel blue",bg="white smoke")
        #Place Top Logo.
        lblInfo.pack(fill=BOTH, expand=1)
        tblInfo = Label(root, font=('arial', 13, 'bold'),fg="Steel Blue",bg="white smoke",height=1)
        tblInfo.pack(fill=BOTH, expand=1)
        def tick():
            """
            Method gets local PC time and updates every 200 miliseconds.
            Time is placed on logo frame to indicate state of script as running.
            If time stops, it means script has crashed.
            """
            #Gets current local time from the PC.
            time2 = time.strftime('%H:%M:%S')
            #Calls itself every 200 milliseconds to update time.
            tblInfo.config(text=time2)
            tblInfo.after(200, tick)
        tick()
        
    def background(self):
         """
         Method creates Tabs and Buttons inside main frame.
         """
         tab1 = Frame(note, bg="steel blue", padx=40)
         tab1.configure(width=300, height=350)

         tab2 = Frame(note, bg="steel blue", padx=40)
         tab2.configure(width=300, height=410)

         tab3 = Frame(note, bg="steel blue", padx=40)
         tab3.configure(width=300, height=410)

         note.add(tab1, text = "     Glassdoor     ")
         note.add(tab2, text = "     Indeed     ")
         note.add(tab3, text = "     Linkedin     ")
         note.pack()

         #Glassdoor
         btn1=Button(tab1,padx=41,bd=2,fg="black",font=('arial',9,'bold'),text="Options",bg="light cyan", command=lambda: JobSeekerBot.Options("Glassdoor"))
         btn1.place(x=30,y=20)
         btn2=Button(tab1,padx=36,bd=2,fg="black",font=('arial',9,'bold'),text="Find Jobs",bg="light cyan", command=lambda: Glassdoor())
         btn2.place(x=30,y=60)


         #Indeed
         btn1=Button(tab2,padx=41,bd=2,fg="black",font=('arial',9,'bold'),text="Options",bg="light cyan", command=lambda: JobSeekerBot.Options("Indeed"))
         btn1.place(x=30,y=20)
         btn2=Button(tab2,padx=36,bd=2,fg="black",font=('arial',9,'bold'),text="Find Jobs",bg="light cyan", command=lambda: Indeed())
         btn2.place(x=30,y=60)

         #Linkedin
         btn1=Button(tab3,padx=41,bd=2,fg="black",font=('arial',9,'bold'),text="Options",bg="light cyan", command=lambda: JobSeekerBot.Options("Linkedin"))
         btn1.place(x=30,y=20)
         btn2=Button(tab3,padx=36,bd=2,fg="black",font=('arial',9,'bold'),text="Find Jobs",bg="light cyan", command=lambda: Linkedin())
         btn2.place(x=30,y=60)

         
    

        #else:
                     #warning = pag.alert(text='Username or password fields cannot be blank.', title='Login Failed', button='OK')

    def GetCredentials(platform):
            
        if path.exists("credentials.txt"):
            warning = pag.alert(text='I saved your password last time', title='Password saved', button='OK')
            pass
        else:
            GetCredentials = Tk()
            #Login window size.
            GetCredentials.geometry("220x100")
            #Login window title.
            GetCredentials.title("Login")
            # Gets requested values of height and width.
            windowWidth = GetCredentials.winfo_reqwidth()
            windowHeight = GetCredentials.winfo_reqheight()
            # Gets both half screen width/height and window width/height.
            positionRight = int(GetCredentials.winfo_screenwidth()/3 - windowWidth/2)
            positionDown = int(GetCredentials.winfo_screenheight()/3 - windowHeight/2)
            # Positions main window frame in the center of screen.
            GetCredentials.geometry("+{}+{}".format(positionRight, positionDown))
            def auth(user,password,platform):
                global linkedin_credentials
                global indeed_credentials
                global glassdoor_credentials
                    
                linkedin_credentials = []
                indeed_credentials = []
                glassdoor_credentials = []

                if platform == "Indeed":
                    indeed_credentials.append(user)
                    indeed_credentials.append(password)
                    print(indeed_credentials)
                    
                if platform == "Glassdoor":
                    glassdoor_credentials.append(user)
                    glassdoor_credentials.append(password)
                    print(glassdoor_credentials)
                    
                messagebox.showinfo("Data received", "Click on Find Jobs button.")
                GetCredentials.destroy()
            
            #Fields for username and password.
            Label(GetCredentials ,text="Email").grid(row=0,column=0)
            Label(GetCredentials,text="Password").grid(row=1,column=0)

            a = Entry(GetCredentials)
            b = Entry(GetCredentials,show="*")

            #Place username and password.
            a.grid(row=0,column=1,sticky="e")
            #Set cursor focus to username.
            a.focus_set()
            b.grid(row=1,column=1,sticky="e")
            #Keep me signed in checkbox.
            checkbox = Checkbutton(GetCredentials,text="Keep me logged in")
            checkbox.grid(row=2,column=1)
            #Login Button use a lambda to get Username and Password when button is pressed
            login_button = Button(GetCredentials, text="Login",command=lambda :
                                auth(a.get(), b.get(),platform))
            login_button.grid(row=3,column=1)
            #Click button by pressing enter key.
            #loginbutton.bind('<Return>',auth)
            GetCredentials.mainloop()

    def Options(platform):
            Options = Tk()
            #Login window size.
            Options.geometry("220x100")
            #Login window title.
            Options.title("Options")
            # Gets requested values of height and width.
            windowWidth = Options.winfo_reqwidth()
            windowHeight = Options.winfo_reqheight()
            # Gets both half screen width/height and window width/height.
            positionRight = int(Options.winfo_screenwidth()/3 - windowWidth/2)
            positionDown = int(Options.winfo_screenheight()/3 - windowHeight/2)
            # Positions main window frame in the center of screen.
            Options.geometry("+{}+{}".format(positionRight, positionDown))

            def Save(job_type,location,platform):
                global linkedin_options
                global indeed_options
                global glassdoor_options
                    
                linkedin_options = []
                indeed_options = []
                glassdoor_options = []

                if platform == "Indeed":
                    indeed_options.append(job_type)
                    indeed_options.append(location)
                    print(indeed_options)
                    
                if platform == "Glassdoor":
                    glassdoor_options.append(job_type)
                    glassdoor_options.append(location)
                    print(glassdoor_options)
                    
                if platform == "Linkedin":
                    linkedin_options.append(job_type)
                    linkedin_options.append(location)
                    print(linkedin_options)
                    
                messagebox.showinfo("Sucess", "Job Title and Location saved. Click on Find Jobs.")
                Options.destroy()
            
            #Fields for username and password.
            Label(Options ,text="Job Title").grid(row=0,column=0)
            Label(Options,text="Location").grid(row=1,column=0)

            a = Entry(Options)
            b = Entry(Options)

            #Place username and password.
            a.grid(row=0,column=1,sticky="e")
            #Set cursor focus to username.
            a.focus_set()
            b.grid(row=1,column=1,sticky="e")
            #Keep me signed in checkbox.
            checkbox = Checkbutton(Options,text="Save options")
            checkbox.grid(row=2,column=1)
            #Login Button use a lambda to get Username and Password when button is pressed
            options_button = Button(Options, text="Apply",command=lambda :
                                Save(a.get(), b.get(),platform))
            options_button.grid(row=3,column=1)
            #Click button by pressing enter key.
            #loginbutton.bind('<Return>',auth)
            Options.mainloop()
                 
class Indeed:

    def __init__(self):
        self.login()
        
    def login(self):
        os.startfile("C:\Program Files (x86)\BraveSoftware\Brave-Browser\Application\Brave.exe")
        time.sleep(2)
        pag.typewrite("indeed.com")
        pag.press("enter")
        time.sleep(3)
        pag.typewrite(indeed_options[0])
        pag.press("tab")
        pag.typewrite(indeed_options[1])
        pag.press("tab")
        pag.press("enter")
        time.sleep(3)
        
class Glassdoor:

    def __init__(self):
        self.login()
        
    def login(self):
        os.startfile("C:\Program Files (x86)\BraveSoftware\Brave-Browser\Application\Brave.exe")
        time.sleep(2)
        pag.typewrite("https://www.glassdoor.com/Job/jobs.htm")
        pag.press("enter")
        time.sleep(6)
        pag.hotkey('ctrl', 'f')
        pag.typewrite('Job Title')
        time.sleep(2)
        pag.press("tab")
        pag.press("tab")
        pag.press("tab")
        pag.press("enter")
        pag.press("tab")
        pag.press("tab")
        pag.typewrite(glassdoor_options[1])
        pag.hotkey('shift', 'tab')
        pag.hotkey('shift', 'tab')
        pag.typewrite(glassdoor_options[0])
        pag.press("tab")
        pag.press("tab")
        pag.press("tab")
        pag.press("enter")
        time.sleep(3)                
        
class Linkedin:

    def __init__(self):
        self.login()
        
    def login(self):
        os.startfile("C:\Program Files (x86)\BraveSoftware\Brave-Browser\Application\Brave.exe")
        time.sleep(2)
        pag.typewrite("https://www.linkedin.com/jobs/")
        pag.press("enter")
        time.sleep(6)
        pag.hotkey('ctrl', 'f')
        pag.typewrite('Search by')
        time.sleep(2)
        pag.press("tab")
        pag.press("tab")
        pag.press("tab")
        pag.press("enter")
        pag.press("tab")
        pag.typewrite(linkedin_options[1])
        pag.hotkey('shift', 'tab')
        pag.typewrite(linkedin_options[0])
        pag.press("tab")
        pag.press("tab")
        pag.press("enter")
        time.sleep(3)                   
        

if __name__ == '__main__':
    root = Tk()
    #Title of main window frame.
    root.title("Job Finder")
    #Size of main window frame.
    root.geometry("300x380+0+0")
    # Gets requested values of height and width.
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()
    # Gets both half screen width/height and window width/height
    positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
    # Positions main window frame in the center of screen.
    root.geometry("+{}+{}".format(positionRight, positionDown))
    #Sets icon for main window frame.
    #root.iconbitmap(r'logo.ico')
    #Attach tabs to main window frame.
    note = ttk.Notebook(root)
    #Fixed size of main window frame.
    root.resizable(width=False, height=False)
    app = JobSeekerBot(root)
    root.mainloop()
