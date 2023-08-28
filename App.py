from tkinter import *
import pyqrcode
import png
from PIL import ImageTk,Image
root=Tk()
root.title("QRCode Generator")
canvas=Canvas(root,width=400,height=500)
canvas.pack()

def generateQRCode():#ดึงname,linkมาสร้างQRCode
    name = name_entry.get()
    link = link_entry.get()
    file_name = name+".png"
    #สร้างQRCode
    url=pyqrcode.create(link)
    url.png(file_name,scale=5)
    #แสดงภาพ QRCode
    image = ImageTk.PhotoImage(Image.open(file_name))
    imang_label=Label(image=image)
    imang_label.image=image
    canvas.create_window(200,370,window=imang_label)
#ชื่อโปรแกรม
app_label=Label(root,text="QRCode Generator",font=('arial',20,'bold'),bg="pink")
canvas.create_window(200,50,window=app_label)

#ระบุชื่อพร้อมลิงค์ --> QRCode
name_label=Label(root,text="ชื่อคิวอาร์โค้ด")
canvas.create_window(200,100,window=name_label)

link_label=Label(root,text="URL")
canvas.create_window(200,160,window=link_label)

#สร้าง TextBox
name_entry=Entry(root)
canvas.create_window(200,130,window=name_entry)

link_entry=Entry(root)
canvas.create_window(200,180,window=link_entry)

#Button สร้าง QRCode
button=Button(text="สร้างQRCode",command=generateQRCode)
canvas.create_window(200,230,window=button)
root.mainloop()