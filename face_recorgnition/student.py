from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk   
from tkinter import messagebox

 



class Student:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recogniton System")
        


        #===========vardiable================
        self.var_dep=StringVar()
        self.var_year=StringVar()
        self.var_course=StringVar()
        self.var_sem=StringVar()
        self.var_id=StringVar()
        self.var_acd_year=StringVar()
        self.var_name=StringVar()
        self.var_div=StringVar()
        self.var_roll_no=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_address=StringVar()
        self.var_phone_no=StringVar()


        #first_img
        img=Image.open(r"C:\Users\Kamal Kumar\OneDrive\Desktop\face_recorgnition\collage pics\logo.jpg")
        img=img.resize((998, 133), Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage (img)

        f_lbl=Label(self.root, image=self.photoimg)
        f_lbl.place(x=150, y=0,width=998,height=133)

        title_lbl=Label( text="STUDENT DETAILS",font=("logan",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0, y=133,width=1330,height=45)

        #left lable frame
        Left_frame=LabelFrame(bd=2,relief=RIDGE,text="student details",bg="white",font=("logan",12,"bold"))
        Left_frame.place(x=10,y=180,width=630,height=500)

        #current course  frame
        current_cours_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="current cours information",bg="white",font=("logan",12,"bold"))
        current_cours_frame.place(x=15,y=10,width=600,height=115)

        #Department
        dep_lable=Label(current_cours_frame,text="Department",bg="white",font=("logan",12,"bold"))
        dep_lable.grid(row=0,column=0,padx=10)      

        dep_combo=ttk.Combobox(current_cours_frame,textvariable=self.var_dep,font=("logan",12,"bold"),width=15,state="read only") 
        dep_combo["values"]=("select department","Computer","IT","Civil","Mech",)
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
 

        #year
        year_lable=Label(current_cours_frame,text="year",bg="white",font=("logan",12,"bold"))
        year_lable.grid(row=0,column=2,padx=10)      

        year_combo=ttk.Combobox(current_cours_frame,textvariable=self.var_year,font=("logan",12,"bold"),width=15,state="read only") 
        year_combo["values"]=("select year","First year","Second year","third year","final year",)
        year_combo.current(0)
        year_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)


        #course
        course_lable=Label(current_cours_frame,text="Course",bg="white",font=("logan",12,"bold"))
        course_lable.grid(row=1,column=0,padx=10)      

        course_combo=ttk.Combobox(current_cours_frame,textvariable=self.var_course,font=("logan",12,"bold"),width=15,state="read only") 
        course_combo["values"]=("select course","B.tech","M.tech","BBA","MBA",)
        course_combo.current(0)
        course_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)


        #Semister
        semister_lable=Label(current_cours_frame,text="semister",bg="white",font=("logan",12,"bold"))
        semister_lable.grid(row=1,column=2,padx=10)      

        semister_combo=ttk.Combobox(current_cours_frame,textvariable=self.var_sem,font=("logan",12,"bold"),width=15,state="read only") 
        semister_combo["values"]=("select semister","Ist sem","IInd sem",)
        semister_combo.current(0)
        semister_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)


        #class sudent information frame
        class_student_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="class students information",bg="white",font=("logan",12,"bold"))
        class_student_frame.place(x=15,y=125,width=600,height=350)
     
        #StudentID 1
        studentsID_lable=Label(class_student_frame,text="studentsID:",bg="white",font=("logan",12,"bold"))
        studentsID_lable.grid(row=0,column=0,padx=10,pady=10) 

        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_id,width=15,font=("logan",12,"bold"))     
        studentID_entry.grid(row=0,column=1,sticky=W)


        #Section 2
        academic_year_lable=Label(class_student_frame,text="academic year:",bg="white",font=("logan",12,"bold"))
        academic_year_lable.grid(row=0,column=2,padx=10,pady=10) 

        academic_year_entry=ttk.Entry(class_student_frame,textvariable=self.var_acd_year,width=15,font=("logan",12,"bold"))     
        academic_year_entry.grid(row=0,column=3,sticky=W)


        #StudentName 3
        studentName_lable=Label(class_student_frame,text="studentName:",bg="white",font=("logan",12,"bold"))
        studentName_lable.grid(row=1,column=0,padx=10,pady=10) 

        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_name,width=15,font=("logan",12,"bold"))     
        studentName_entry.grid(row=1,column=1,sticky=W)


        #Class Division 4
        class_division_lable=Label(class_student_frame,text="classdivision:",bg="white",font=("logan",12,"bold"))
        class_division_lable.grid(row=1,column=2,padx=10,pady=10) 

        class_division_entry=ttk.Entry(class_student_frame,textvariable=self.var_div,width=15,font=("logan",12,"bold"))     
        class_division_entry.grid(row=1,column=3,sticky=W)


        #Roll no 5
        Roll_no_lable=Label(class_student_frame,text="Roll no:",bg="white",font=("logan",12,"bold"))
        Roll_no_lable.grid(row=2,column=0,padx=10,pady=10) 

        Roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll_no,width=15,font=("logan",12,"bold"))     
        Roll_no_entry.grid(row=2,column=1,sticky=W)


        #Gender 6 
        Gender_lable=Label(class_student_frame,text="Gender:",bg="white",font=("logan",12,"bold"))
        Gender_lable.grid(row=2,column=2,padx=10,pady=10) 

        Gender_entry=ttk.Entry(class_student_frame,textvariable=self.var_gender,width=15,font=("logan",12,"bold"))     
        Gender_entry.grid(row=2,column=3,sticky=W)


        #DOB 7
        DOB_lable=Label(class_student_frame,text="DOB:",bg="white",font=("logan",12,"bold"))
        DOB_lable.grid(row=3,column=0,padx=10,pady=10) 

        DOB_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=15,font=("logan",12,"bold"))     
        DOB_entry.grid(row=3,column=1,sticky=W)


        #Email 8
        Email_lable=Label(class_student_frame,text="Email:",bg="white",font=("logan",12,"bold"))
        Email_lable.grid(row=3,column=2,padx=10,pady=10) 

        Email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=15,font=("logan",12,"bold"))     
        Email_entry.grid(row=3,column=3,sticky=W)


        #Address 9
        Address_lable=Label(class_student_frame,text="Address:",bg="white",font=("logan",12,"bold"))
        Address_lable.grid(row=4,column=0,padx=10,pady=10) 

        Address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=15,font=("logan",12,"bold"))     
        Address_entry.grid(row=4,column=1,sticky=W)


        #Phone No 10
        Phone_No_lable=Label(class_student_frame,text="Phone No:",bg="white",font=("logan",12,"bold"))
        Phone_No_lable.grid(row=4,column=2,padx=10,pady=10) 

        Phone_No_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone_no,width=15,font=("logan",12,"bold"))     
        Phone_No_entry.grid(row=4,column=3,sticky=W)



        #radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="take photo sample",value="yes")
        radiobtn1.grid(row=5,column=0)

        self.var_radio2=StringVar()
        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio2,text="no photo sample",value="no")
        radiobtn2.grid(row=5,column=1)
        

        #buttons frame 1   
        btn_frame=LabelFrame(class_student_frame,bd=2,relief=RIDGE,bg="white",font=("logan",12,"bold"))
        btn_frame.place(x=2,y=250,width=590,height=37)

        # button 1
        Save_bth=Button(btn_frame,text="Save",command=self.add_data,width=13,font=("logan",12,"bold"),bg="blue",fg="white")
        Save_bth.grid(row=0,column=1)
     
        # button 2
        Update_bth=Button(btn_frame,text="Update",width=14,font=("logan",12,"bold"),bg="blue",fg="white")
        Update_bth.grid(row=0,column=2)

        # button 3
        Delete_bth=Button(btn_frame,text="Delete",width=14,font=("logan",12,"bold"),bg="blue",fg="white")
        Delete_bth.grid(row=0,column=3)

        # button 4
        Reset_bth=Button(btn_frame,text="Reset",width=14,font=("logan",12,"bold"),bg="blue",fg="white")
        Reset_bth.grid(row=0,column=4)


        #buttons frame 2
        btn_frame1=LabelFrame(class_student_frame,bd=2,relief=RIDGE,bg="white",font=("logan",12,"bold"))
        btn_frame1.place(x=2,y=285,width=590,height=37)

        # button 1
        Take_photo_bth=Button(btn_frame1,text="Take a photo sample",width=28,font=("logan",12,"bold"),bg="blue",fg="white")
        Take_photo_bth.grid(row=0,column=1)

        # button 2
        Update_photo_bth=Button(btn_frame1,text="Update photo sample",width=29,font=("logan",12,"bold"),bg="blue",fg="white")
        Update_photo_bth.grid(row=0,column=2)
    

        #right lable frame
        Right_frame=LabelFrame(bd=2,relief=RIDGE,text="student details",bg="white",font=("logan",12,"bold"))
        Right_frame.place(x=650,y=180,width=610,height=500)

        #=======Search System==========


        #Search System frame
        Search_system_frame=LabelFrame(Right_frame,bd=2,relief=RIDGE,text="Search System",bg="white",font=("logan",12,"bold"))
        Search_system_frame.place(x=10,y=10,width=590,height=70)
 
 
        #search
        Search_by_lable=Label(Search_system_frame,text="Search By:",bg="yellow",font=("logan",12,"bold"))
        Search_by_lable.grid(row=0,column=0,padx=10,pady=10) 

        search_combo=ttk.Combobox(Search_system_frame,font=("logan",12,"bold"),width=12,state="read only") 
        search_combo["values"]=("select ","Roll no","Phone no","StudentID")
        search_combo.current(0)
        search_combo.grid(row=0,column=2,padx=2,pady=10,sticky=W)


        search_entry=ttk.Entry(Search_system_frame,width=15,font=("logan",12,"bold"))     
        search_entry.grid(row=0,column=3,sticky=W)

        Search_bth=Button(Search_system_frame,text="Search",width=8,font=("logan",12,"bold"),bg="blue",fg="white")
        Search_bth.grid(row=0,column=4,padx=3)

        Show_all_bth=Button(Search_system_frame,text="Show all",width=8,font=("logan",12,"bold"),bg="blue",fg="white")
        Show_all_bth.grid(row=0,column=5,padx=3)


        #=========table frame=============
        table_frame=LabelFrame(Right_frame,bd=2,relief=RIDGE,bg="white",font=("logan",12,"bold"))
        table_frame.place(x=10,y=90,width=590,height=385)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","year","course","sem","id","acd year","name","div","roll no","gender","dob","email","address","phone no","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("sem",text="Semister")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("acd year",text="Academic Year")
        self.student_table.heading("name",text="name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll no",text="Roll no")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("phone no",text="Phone no")
        self.student_table.heading("photo",text="Photo")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100) 
        self.student_table.column("year", width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("acd year",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("roll no", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("phone no", width=100)
        self.student_table.column("photo",width=150)

        self.student_table.pack(fill=BOTH,expand=1)

#===============function declaration============================
    def add_data(self):
        if self.var_dep.get()=="select departmant" or self.var_name.get()=="name" or self.var_id.get()=="":
           messagebox.showerror("error","all detail are required to be filled",parent=self.root)
        else:
            pass
       





        
        
if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
    