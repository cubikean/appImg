import tkinter
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
import os

from util import collect_img, compress_img

def img_folder():
    img_folder_entry.delete(0,'end')
    img_folder = filedialog.askdirectory(title='Select File')
    img_folder_entry.insert(0,img_folder)
    
def result_folder():
    result_folder_entry.delete(0,'end')
    result_folder = filedialog.askdirectory(title='Select File')
    result_folder_entry.insert(0,result_folder)

def convert():
    img_folder = img_folder_entry.get()
    result_folder = result_folder_entry.get()
    jpg = jpg_var.get()
    webp = webp_var.get()
    png = png_var.get()
    ratio = int(ratio_spinbox.get())/100
    quality = int(quality_spinbox.get())

    if not img_folder:
        messagebox.showerror("Error","Must have an image folder")
    if not result_folder:
        messagebox.showerror("Error","Must have a result folder")
    if (jpg and webp) or (jpg and png) or (png and webp):
        messagebox.showerror('Error', "Must have 0 or 1 checkbox checked")
    
    compress_img(images=collect_img(img_folder),destination=result_folder,new_size_ratio=ratio,quality=quality,to_jpg=jpg,to_webp=webp,to_png=png)


window = tkinter.Tk()
window.title('Image Compressor')

#Frames
frame = tkinter.Frame(window)
frame.grid(row=0,column=0,sticky='nesw')

folders_frame = tkinter.LabelFrame(frame,text="Folders")
folders_frame.grid(row=0,column=0,sticky='news', padx=20,pady=10)

extension_frame = tkinter.LabelFrame(frame,text="Output extension")
extension_frame.grid(row=1,column=0,sticky='news', padx=20,pady=10)

option_frame = tkinter.LabelFrame(frame,text="Options")
option_frame.grid(row=2,column=0,sticky='news', padx=20,pady=10)

#folders_frame
img_folder_button = tkinter.Button(folders_frame,text='Folder To Convert',command=img_folder)
img_folder_button.grid(row=0,column=0)
img_folder_entry = tkinter.Entry(folders_frame)
img_folder_entry.grid(row=1, column=0)

result_folder_button = tkinter.Button(folders_frame,text='Destination Folder',command=result_folder)
result_folder_button.grid(row=0,column=1)
result_folder_entry = tkinter.Entry(folders_frame)
result_folder_entry.grid(row=1, column=1)


#extension_frame
jpg_var = tkinter.BooleanVar(value=False)
jpg_checkbox = ttk.Checkbutton(extension_frame,text="JPG",variable=jpg_var, onvalue=True,offvalue=False)
jpg_checkbox.grid(row=0,column=0, padx=20,pady=10)

webp_var = tkinter.BooleanVar(value=False)
webp_checkbox = ttk.Checkbutton(extension_frame,text="WEBP",variable=webp_var, onvalue=True,offvalue=False)
webp_checkbox.grid(row=0,column=1, padx=20,pady=10)

png_var = tkinter.BooleanVar(value=False)
png_checkbox = ttk.Checkbutton(extension_frame,text="PNG",variable=png_var, onvalue=True,offvalue=False)
png_checkbox.grid(row=0,column=2, padx=20,pady=10)


#option_frame
ratio_label = tkinter.Label(option_frame,text='Ratio %')
ratio_label.grid(row=0,column=0,padx=20,pady=10)
ratio_spinbox = tkinter.Spinbox(option_frame,from_=0,to=100)
ratio_spinbox.grid(row=1,column=0,padx=20,pady=10)
ratio_spinbox.delete(0,'end')
ratio_spinbox.insert(0,90)

quality_label = tkinter.Label(option_frame,text='Quality %')
quality_label.grid(row=0,column=1,padx=20,pady=10)
quality_spinbox = tkinter.Spinbox(option_frame,from_=0,to=100)
quality_spinbox.grid(row=1,column=1,padx=20,pady=10)
quality_spinbox.delete(0,'end')
quality_spinbox.insert(0,75)

#button
convert_button = tkinter.Button(window, text='Create The Survey',command=convert)
convert_button.grid(row=3,column=0,padx=20,pady=10)


window.minsize(window.winfo_width(), window.winfo_height())
x_cordinate = int((window.winfo_screenwidth() / 2) - (window.winfo_width() / 2))
y_cordinate = int((window.winfo_screenheight() / 2) - (window.winfo_height() / 2))
window.geometry("+{}+{}".format(x_cordinate, y_cordinate-20))
window.mainloop()
