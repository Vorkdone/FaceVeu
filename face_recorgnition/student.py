from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk   


class student:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("student details")


        #first_img
        img=Image.open(r"C:\Users\Kamal Kumar\OneDrive\Desktop\face_recorgnition\collage pics\logo.jpg")
        img=img.resize((998, 133), Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage (img)

        f_lbl=Label(self.root, image=self.photoimg)
        f_lbl.place(x=150, y=0,width=998,height=133)

        title_lbl=Label( text="STUDENT DETAILS",font=("logan",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0, y=133,width=1330,height=45)


        
if __name__ == "__main__":
    root=Tk()
    obj=student(root)
    root.mainloop()