from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk   


class Face_Recognition_System:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recogniton System")
         
        #first_img
        img=Image.open(r"C:\Users\Kamal Kumar\OneDrive\Desktop\face_recorgnition\collage pics\logo.jpg")
        img=img.resize((998, 133), Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage (img)

        f_lbl=Label(self.root, image=self.photoimg)
        f_lbl.place(x=150, y=0,width=998,height=133)

        
        #bg_img
        img2=Image.open(r"C:\Users\Kamal Kumar\OneDrive\Desktop\face_recorgnition\collage pics\logo6.jpg")
        img2=img2.resize((660, 500), Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage (img2)

        bg_img=Label(self.root, image=self.photoimg2)
        bg_img.place(x=0, y=130,width=1330,height=600)

        title_lbl=Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("logan",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0, y=0,width=1330,height=45)

        # student details button 1
        img3=Image.open(r"C:\Users\Kamal Kumar\OneDrive\Desktop\face_recorgnition\collage pics\logo7.WEBP")
        img3=img3.resize((220,220), Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage (img3)

        b1=Button (bg_img, image=self.photoimg3, cursor="hand2")
        b1.place(x=100, y=50,width=200,height=200)

        b1_1=Button (bg_img,text="student details", cursor="hand2",font=("logan",20,"bold"),bg="blue",fg="white")
        b1_1.place(x=100, y=250,width=200,height=40)


        # detector button 2
        img4=Image.open(r"C:\Users\Kamal Kumar\OneDrive\Desktop\face_recorgnition\collage pics\logo8.png")
        img4=img4.resize((220,220), Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage (img4)

        b1=Button (bg_img, image=self.photoimg4, cursor="hand2")
        b1.place(x=500, y=50,width=200,height=200)

        b1_1=Button (bg_img,text="face detector", cursor="hand2",font=("logan",20,"bold"),bg="blue",fg="white")
        b1_1.place(x=500, y=250,width=200,height=40)


        # attendance button 3
        img5=Image.open(r"C:\Users\Kamal Kumar\OneDrive\Desktop\face_recorgnition\collage pics\logo9.png")
        img5=img5.resize((220,220), Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage (img5)

        b1=Button (bg_img, image=self.photoimg5, cursor="hand2")
        b1.place(x=900, y=50,width=200,height=200)

        b1_1=Button (bg_img,text="attendance", cursor="hand2",font=("logan",20,"bold"),bg="blue",fg="white")
        b1_1.place(x=900, y=250,width=200,height=40)


        # train button 4
        img6=Image.open(r"C:\Users\Kamal Kumar\OneDrive\Desktop\face_recorgnition\collage pics\logo10.jpg")
        img6=img6.resize((220,220), Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage (img6)

        b1=Button (bg_img, image=self.photoimg6, cursor="hand2")
        b1.place(x=100, y=300,width=200,height=200)

        b1_1=Button (bg_img,text="Train", cursor="hand2",font=("logan",20,"bold"),bg="blue",fg="white")
        b1_1.place(x=100, y=500,width=200,height=40)


        # photos button 5
        img7=Image.open(r"C:\Users\Kamal Kumar\OneDrive\Desktop\face_recorgnition\collage pics\logo11.jpg")
        img7=img7.resize((220,220), Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage (img7)

        b1=Button (bg_img, image=self.photoimg7, cursor="hand2")
        b1.place(x=500, y=300,width=200,height=200)

        b1_1=Button (bg_img,text="photos", cursor="hand2",font=("logan",20,"bold"),bg="blue",fg="white")
        b1_1.place(x=500, y=500,width=200,height=40)


        # exit button 6
        img8=Image.open(r"C:\Users\Kamal Kumar\OneDrive\Desktop\face_recorgnition\collage pics\logo12.jpg")
        img8=img8.resize((220,220), Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage (img8)

        b1=Button (bg_img, image=self.photoimg8, cursor="hand2")
        b1.place(x=900, y=300,width=200,height=200)

        b1_1=Button (bg_img,text="Exit", cursor="hand2",font=("logan",20,"bold"),bg="blue",fg="white")
        b1_1.place(x=900, y=500,width=200,height=40)





if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()