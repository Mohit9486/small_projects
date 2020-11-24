import tkinter as tk
from PIL import Image,ImageTk
import os
from tkinter import filedialog

#GUI Application window
win = tk.Tk()
win.title("Image to pdf converter")
win.geometry("700x600")
win.iconphoto(False, tk.PhotoImage(file = 'pdf.png'))
win.resizable(0,0)

#Krishna_Image 
can = tk.Canvas(win,bg = "yellow", width = 250,height = 240)
can.grid(row=0,column=0, sticky = tk.N, padx=225,pady = 30)
im = ImageTk.PhotoImage(Image.open('krishna.jpg'))
can.create_image(127,121,image = im)

#welcome image
canv = tk.Canvas(win,bg='yellow', width = 600,height =120)
canv.grid(row=1,column=0,padx=25)
img = ImageTk.PhotoImage(Image.open('welc.png'))
canv.create_image(302,62,image =img)

#functions
def disable(btn):
    btn['state']='disabled'

def enable(btn):
    btn['state'] = 'active'

files = {}
def upload():
    global files
    files['filename'] = filedialog.askopenfilenames(filetypes=[('JPG','*.jpg'),('PNG','*.png'),('JPEG','*.jpeg')],
    initialdir = os.getcwd(), title='Select File/Files')
    if len(files['filename'])!=0:
        enable(down_button)

def save():
    
        l = []
        for file in files['filename']:
            l.append(Image.open(file).convert('RGB'))
        file_name = filedialog.asksaveasfilename(filetypes = [('PDF','*.pdf')], initialdir=os.getcwd(), title='Save File')
        l[0].save(f'{file_name}.pdf', save_all=True, append_images = l[1:])
        disable(down_button)
    

#Upload Butoon
button = tk.Button(win,text="Upload Images",width = 20, height = 1,font = ('arial',14,'bold'),bg='white',fg='blue',command=upload)
button.grid(row=2,column=0,padx=200,pady=20)

#download button
down_button = tk.Button(win,text="Download Pdf",width = 20,height =1,font = ('arial',14,'bold'),bg= 'white',fg='green',command=save)
down_button.grid(row=3,column=0)
disable(down_button)


win.mainloop()