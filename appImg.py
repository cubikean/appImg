import tkinter
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
import os
import subprocess

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
    uniformize = uniformize_var.get()
    try:
        width = int(width_entry.get()) if uniformize else None
        height = int(height_entry.get()) if uniformize else None
    except ValueError:
        messagebox.showerror("Erreur", "Largeur et hauteur doivent être des entiers.")
        return

    if not img_folder:
        messagebox.showerror("Error","Must have an image folder")
        return
    if not result_folder:
        messagebox.showerror("Error","Must have a result folder")
        return
    if (jpg and webp) or (jpg and png) or (png and webp):
        messagebox.showerror('Error', "Must have 0 or 1 checkbox checked")
        return
    compress_img(images=collect_img(img_folder),destination=result_folder,new_size_ratio=ratio,quality=quality,width=width,height=height,uniformize=uniformize,to_jpg=jpg,to_webp=webp,to_png=png)

    # # Si webp est sélectionné, lancer la conversion avif
    # if webp:
    #     try:
    #         cmd = [
    #             'npx', 'avif',
    #             '--input=images/ToConvert/*.webp',
    #             '--output=output',
    #             '--effort=9',
    #             '--lossless=false',
    #             '--quality=40',
    #             '--overwrite=true'
    #         ]
    #         result = subprocess.run(
    #             'cd "C:/Users/Beekom/Desktop/dev/DEV/avif/" && ' + ' '.join(cmd),
    #             shell=True,
    #             capture_output=True,
    #             text=True
    #         )
    #         if result.returncode == 0:
    #             messagebox.showinfo("Succès", f"Conversion AVIF terminée.\\n{result.stdout}")
    #         else:
    #             messagebox.showerror("Erreur AVIF", f"Erreur : {result.stderr}")
    #     except Exception as e:
    #         messagebox.showerror("Erreur lors de la conversion AVIF", str(e))

# Fonction pour lancer la conversion AVIF uniquement
def convert_avif_only():
    import subprocess
    try:
        result_folder = result_folder_entry.get()
        cmd = [
            'npx', 'avif',
            '--input=images/ToConvert/*.webp',
            '--output=output',
            '--effort=9',
            '--lossless=false',
            '--quality=40',
            '--overwrite=true'
        ]
        subprocess.run(
            'cd "C:/Users/Beekom/Desktop/dev/DEV/avif/" && ' + ' '.join(cmd),
            shell=True,
            check=True
        )
        messagebox.showinfo("Succès", "Conversion AVIF terminée.")
    except Exception as e:
        messagebox.showerror("Erreur lors de la conversion AVIF", str(e))

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
img_folder_entry.insert(0, r"C:\Users\Beekom\Desktop\dev\DEV\avif\images\ToConvert")

result_folder_button = tkinter.Button(folders_frame,text='Destination Folder',command=result_folder)
result_folder_button.grid(row=0,column=1)
result_folder_entry = tkinter.Entry(folders_frame)
result_folder_entry.grid(row=1, column=1)
result_folder_entry.insert(0, r"C:\Users\Beekom\Desktop\dev\DEV\avif\images\ToConvert")



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

# Uniformisation de la taille
uniformize_var = tkinter.BooleanVar(value=False)
uniformize_checkbox = ttk.Checkbutton(option_frame, text="Uniformiser la taille (16/9)", variable=uniformize_var, onvalue=True, offvalue=False)
uniformize_checkbox.grid(row=2, column=0, padx=20, pady=10)

width_label = tkinter.Label(option_frame, text='Largeur cible')
width_label.grid(row=0, column=2, padx=20, pady=10)
width_entry = tkinter.Entry(option_frame, width=6)
width_entry.grid(row=1, column=2, padx=20, pady=10)
width_entry.insert(0, "1920")

height_label = tkinter.Label(option_frame, text='Hauteur cible')
height_label.grid(row=0, column=3, padx=20, pady=10)
height_entry = tkinter.Entry(option_frame, width=6)
height_entry.grid(row=1, column=3, padx=20, pady=10)
height_entry.insert(0, "1080")

#button
convert_button = tkinter.Button(window, text='Create The Survey',command=convert)
convert_button.grid(row=3,column=0,padx=20,pady=10)

# Nouveau bouton pour lancer la conversion AVIF
convert_avif_button = tkinter.Button(window, text='Convertir en AVIF', command=convert_avif_only)
convert_avif_button.grid(row=3, column=1, padx=20, pady=10)

window.minsize(window.winfo_width(), window.winfo_height())
x_cordinate = int((window.winfo_screenwidth() / 2) - (window.winfo_width() / 2))
y_cordinate = int((window.winfo_screenheight() / 2) - (window.winfo_height() / 2))
window.geometry("+{}+{}".format(x_cordinate, y_cordinate-20))
window.mainloop()
