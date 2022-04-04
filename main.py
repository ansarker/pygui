from tkinter import *
from tkinterdnd2 import *
import os
from shutil import copy
from PIL import Image, ImageTk


master = TkinterDnD.Tk()
master.title('Image cleaning')
main_dirs = ['cloth', 'image', 'test']

default_img_1 = 'cloth.jpg'
default_img_2 = 'image.jpg'
default_img_3 = 'test.jpg'

global cloth_count_start
cloth_count_start = 1
global image_count_start
image_count_start = 1
global test_count_start
test_count_start = 1

def doSomething():
    path = path_entry.get()
    for dir in main_dirs:
        if os.path.exists(os.path.join(path, dir)):
            print('Directory exists! Skipping...')
        else:
            os.makedirs(os.path.join(path, dir))
            print(f'Directory created! {os.path.join(path, dir)}')

def img_resize(src):
    img = Image.open(src)
    width, height = img.size
    aspect_ratio = int(width // 140)
    height = int(height // aspect_ratio)
    return ImageTk.PhotoImage(img.resize((140, height)))

def drop1(event):
    global cloth_count_start
    dest = os.path.join(path_entry.get(), 'cloth', f'000000{cloth_count_start}.jpg')
    copy(event.data, dest)
    print(f'INFO: copied to {dest}')
    de = img_resize(event.data)
    photo_label1.configure(image=de)
    photo_label1.image = de
    cloth_count_start += 1

def drop2(event):
    global image_count_start
    dest = os.path.join(path_entry.get(), 'image', f'000000{image_count_start}.jpg')
    copy(event.data, dest)
    print(f'INFO: copied to {dest}')
    de = img_resize(event.data)
    photo_label2.configure(image=de)
    photo_label2.image = de
    image_count_start += 1

def drop3(event):
    global test_count_start
    dest = os.path.join(path_entry.get(), 'test', f'000000{test_count_start}.jpg')
    copy(event.data, dest)
    print(f'INFO: copied to {dest}')
    de = img_resize(event.data)
    photo_label3.configure(image=de)
    photo_label3.image = de
    test_count_start += 1
    
path_label = Label(master, text='Path to save', fg='black')
path_entry = Entry(master)
# name_label = Label(master, text='Name start from', fg='black')
# name_entry = Entry(master)
B1 = Button(master, text ="OK", command=doSomething)

path_label.grid(row=0,column=0, sticky=W, padx=10)
path_entry.grid(row=1, column=0, sticky=W, padx=10)
# name_label.grid(row=2,column=0, sticky=W, padx=10)
# name_entry.grid(row=3,column=0, sticky=W, padx=10)
B1.grid(row=4,column=0, sticky=W, padx=10)

Label(master, text="cloth").grid(row=5, column=0, padx=10)
Label(master, text="image").grid(row=5, column=1, padx=10)
Label(master, text="test").grid(row=5, column=2, padx=10)

img1 = img_resize(default_img_1)
img2 = img_resize(default_img_2)
img3 = img_resize(default_img_3)

photo_label1 = Label(image=img1)
photo_label2 = Label(image=img2)
photo_label3 = Label(image=img3)

photo_label1.drop_target_register(DND_FILES)
photo_label1.dnd_bind('<<Drop>>', drop1)

photo_label2.drop_target_register(DND_FILES)
photo_label2.dnd_bind('<<Drop>>', drop2)

photo_label3.drop_target_register(DND_FILES)
photo_label3.dnd_bind('<<Drop>>', drop3)

photo_label1.grid(row=6, column=0, padx=10, pady=5)
photo_label2.grid(row=6, column=1, padx=10, pady=5)
photo_label3.grid(row=6, column=2, padx=10, pady=5)

mainloop()