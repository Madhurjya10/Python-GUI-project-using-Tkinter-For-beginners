from tkinter import *
from datetime import datetime
import pytz,pyttsx3,cv2, wikipedia,webbrowser
from pygame import*
from tkinter.ttk import Notebook, Style
from tkinter import Tk, filedialog,messagebox
from PIL import Image, ImageTk

Black="#000000"
fBlack=fblack="#1B1B1B"
Cyan="CYAN"
LARGE_FONT_STYLE = ("Arial", 26)
SMALL_FONT_STYLE = ("Arial", 16)
DIGITS_FONT_STYLE = ("Arial", 24)

muted = False

class MainWindow():

    def __init__(self):
        self.App = Tk()
        self.App.geometry("1600x900+170+50")
        self.App.title("Matrix v1.0 - Project XI-A")
        self.App.iconbitmap("Icons and Images\Ypf-Transformers-Network-connections.ico")
        self.App.resizable(False,False)
        self.App.config(background = Black)
        self.Display_Tabs = self.Tabs()
        self.Display_Labels = self.Labels()        
        self.Display_Frames = self.Frames()
        self.Display_About = self.Labels_2()
        self.Display_Buttons = self.Butttons_On_Tab1()
        self.Display_Buttons = self.Butttons_On_Tab2()
        self.Display_Buttons = self.Butttons_On_Tab3()
        self.Display_Buttons = self.Butttons_On_Tab4()
        self.Display_Buttons = self.Butttons_On_Tab5()
        self.Display_Entries = self.Entry_Tabs()
        self.Display_time_date = self.update_clock()
        self.Display_Logos = self.Images_on_Tabs()
        self.Display_Text_Box = self.add_textbox()
        self.run_Calculator = self.init_Calculator()
        self.App.mainloop()

    def Frames(self):
        self.Line_Frame_1=Frame(self.App, height = 2 , width=1600, bg= Cyan, relief = FLAT)
        self.Line_Frame_1.place(x=0   , y=29)
        self.Line_Frame_2=Frame(self.App, height = 2 , width=1600, bg= Cyan, relief = FLAT)
        self.Line_Frame_2.place(x=0   , y=53)
        self.Line_Frame_3=Frame(self.App, height = 22, width=1600, bg=Black, relief = FLAT)
        self.Line_Frame_3.place(x=672 , y=31)
        self.Line_Frame_4=Frame(self.App, height = 26, width=2   , bg= Cyan, relief = FLAT)
        self.Line_Frame_4.place(x=1528, y=29)
        self.Line_Frame_5=Frame(self.App, height = 26, width=2   , bg= Cyan, relief = FLAT)
        self.Line_Frame_5.place(x=1448, y=29)

        self.Transport_BTN_Frame_1=Frame(self.tab1,height=60, width=799 ,bg =Cyan)
        self.Transport_BTN_Frame_1.place(x=395 , y=790)
        self.Transport_BTN_Frame_2=Frame(self.tab2,height=60, width=799 ,bg =Cyan)
        self.Transport_BTN_Frame_2.place(x=395 , y=790)
        self.Transport_BTN_Frame_3=Frame(self.tab3,height=60, width=799 ,bg =Cyan)
        self.Transport_BTN_Frame_3.place(x=395 , y=790)
        self.Transport_BTN_Frame_4=Frame(self.tab4,height=60, width=799 ,bg =Cyan)
        self.Transport_BTN_Frame_4.place(x=395 , y=790)
        self.Transport_BTN_Frame_5=Frame(self.tab5,height=60, width=799 ,bg =Cyan)
        self.Transport_BTN_Frame_5.place(x=395 , y=790)

        self.Music_Section_Frame=Frame(self.tab1,height=50, width=150 ,bg =Cyan)
        self.Music_Section_Frame.place(x=1480, y=804)
        self.Refernce_Section = Frame(self.tab1,height=70, width=108 ,bg=Cyan)
        self.Refernce_Section.place(x=0 , y=775)

        self.IMG_Frame_tab3=Frame(self.tab3,height=188, width=485 ,bg =Cyan)
        self.IMG_Frame_tab3.place(x=1050, y=20)
        self.IMG_Frame_tab4=Frame(self.tab4,height=345, width=330 ,bg =Cyan)
        self.IMG_Frame_tab4.place(x=1188, y=78)
        self.IMG_Frame_tab5=Frame(self.tab5,height=350, width=320 ,bg =Cyan)
        self.IMG_Frame_tab5.place(x=1198, y=78)

        self.IMG_Frame_tab4_Back=Frame(self.tab4,height=340, width=325 ,bg=Black)
        self.IMG_Frame_tab4_Back.place(x=1191, y=80)
        self.IMG_Frame_tab5_Back=Frame(self.tab5,height=345, width=315 ,bg=Black)
        self.IMG_Frame_tab5_Back.place(x=1200, y=80)

        self.Image_Frame_Base=Frame(self.tab2,height=657, width=1168 ,bg =Cyan)
        self.Image_Frame_Base.place(x=140 , y=80)

        self.Image_Frame_Back = Frame(self.tab2,height=657, width=1168 ,bg =Cyan)
        self.Image_Frame_Back.place(x=140 , y=80)

        self.Image_Frame_Bac=Frame(self.Image_Frame_Back,height=653, width=1164 ,bg= Black)
        self.Image_Frame_Bac.place(x=2,y=2)

        self.Image_Frame = Frame(self.Image_Frame_Bac,height=653, width=1164 ,bg=Black)
        self.Image_Frame.place(x=-1, y=-1)
 
        self.Pattern_Frame_Bas=Frame(self.tab3,height=130,width=1350,bg=Cyan)
        self.Pattern_Frame_Bas.place(x=146,y=296)
        self.Pattern_Frame_Ba=Frame(self.tab3,height=126,width=1345,bg=Black)
        self.Pattern_Frame_Ba.place(x=148,y=298)
        self.Pattern_Frame_Base=Frame(self.tab3,height=122,width=1343,bg=Black)
        self.Pattern_Frame_Base.place(x=150,y=300)
        self.Pattern_Frame=Frame(self.Pattern_Frame_Base,height=100,width=36,bg=Black)
        self.Pattern_Frame.pack(pady=12)  

        self.Calc_Frame_Base=Frame(self.tab5, height= 660, width=408, bg=Cyan, relief = FLAT)
        self.Calc_Frame_Base.place(x=598,y=98)
        self.Calc_Frame = Frame(self.tab5,width=800, height=700, bg =Black)
        self.Calc_Frame.place(x=600, y=100) 

        self.Button_Base_1=Frame(self.tab2, height= 37, width=108, bg= Cyan, relief = FLAT)
        self.Button_Base_1.place(x=1398, y=100)
        self.Button_Base_2=Frame(self.tab2, height= 37, width=108, bg= Cyan, relief = FLAT)
        self.Button_Base_2.place(x=1398, y=198)
        
        self.Button_Base_3=Frame(self.tab3, height= 37, width=77, bg= Cyan, relief = FLAT)
        self.Button_Base_3.place(x=798, y=120)

        self.Button_Base_4=Frame(self.tab4, height= 30, width=71, bg= Cyan, relief = FLAT)
        self.Button_Base_4.place(x=798, y=148)
        self.Button_Base_5=Frame(self.tab4, height= 30, width=71, bg= Cyan, relief = FLAT)
        self.Button_Base_5.place(x=898, y=148)

        self.Button_Base_6=Frame(self.tab3, height=35, width=64, bg= Cyan, relief = FLAT)
        self.Button_Base_6.place(x=898, y=120)

        self.Wiki_TextBox_Base=Frame(self.tab4, height=558, width=558, bg= Cyan, relief = FLAT)
        self.Wiki_TextBox_Base.place(x=178, y=198)

        self.Instruction_Frame1=Frame(self.tab2, height=238, width=169, bg= Cyan, relief = FLAT)
        self.Instruction_Frame1.place(x=1370, y=398)
        self.Instruction_Frame2=Frame(self.tab3, height=105, width=810, bg= Cyan, relief = FLAT)
        self.Instruction_Frame2.place(x=146, y=500)
        self.Instruction_Frame3=Frame(self.tab4, height=105, width=495, bg= Cyan, relief = FLAT)
        self.Instruction_Frame3.place(x=948, y=550)
        self.Instruction_Frame4=Frame(self.tab5, height=105, width=251, bg= Cyan, relief = FLAT)
        self.Instruction_Frame4.place(x=150, y=150) 

    def Labels(self):
        self.Heading_App= Label(text='MATRIX', bg=Black, fg=Cyan, font="helvetica 15")
        self.Heading_App.pack()

        self.Heading_Tab1= Label(self.tab2,text='Image to Pencil Sketch', bg=Black, fg=Cyan, font="helvetica 25",pady=10)
        self.Heading_Tab1.pack()

        self.Heading_Tab2= Label(self.tab3,text='Text in Pattern', bg=Black, fg=Cyan, font="helvetica 25",pady=10)
        self.Heading_Tab2.pack()

        self.Heading_Tab3= Label(self.tab4,text='  Wikipedia\nThe free Encyclopaedia', bg=Black, fg=Cyan, font="helvetica 25",pady=10)
        self.Heading_Tab3.pack()

        self.Heading_Tab4= Label(self.tab5,text='Calculator', bg=Black, fg=Cyan, font="helvetica 25",pady=10)
        self.Heading_Tab4.pack()

    def Labels_2(self):
        self.About_tab2 = Label(self.Instruction_Frame1, text="      Instructions\n\n In the first step \n Select An Image,\n It can be either in \n jpg or png format. \n\n Second, click on \n 'Convert' Button to \n convert it to \n Pencil Sketch", 
        bg=Black, fg=Cyan, font="helvetica 13",justify="left",padx=10, pady=10)
        self.About_tab2.place(x=2,y=2)

        self.About_tab2 = Label(self.Instruction_Frame2, text="\t\tInstructions\n\nEnter The String to convert it '$' symbol pattern, Try not to enter more than 20 characters (space included), \nThen Click on 'Pattern' Button (Don't click Enter)", 
        bg=Black, fg=Cyan, font="helvetica 13",justify="left",padx=10, pady=10)
        self.About_tab2.place(x=2,y=2)

        self.About_tab2 = Label(self.Instruction_Frame3, text="\t\t   Instructions\n\nEnter specifically about which you want to search in Wikipedia. \nThen click on 'Search' Button (don't click Enter) to search",
        bg=Black, fg=Cyan, font="helvetica 13", justify="left",padx=10, pady=10)
        self.About_tab2.place(x=2,y=2)

        self.About_tab2 = Label(self.Instruction_Frame4, text="\tInstructions\n\nDon't enter any number more  \nthan 15 digits", bg=Black, fg=Cyan, font="helvetica 13", justify="left",padx=10, pady=10)
        self.About_tab2.place(x=2,y=2)

    def Entry_Tabs(self):
        self.Pattern_Entry = Entry(self.tab3,width=50, font="helvetica 15")
        self.Pattern_Entry.place(x=150, y=120)

        self.Wikipedia_Entry = Text(self.tab4, width=50, height=1, font="helvetica 15")
        self.Wikipedia_Entry.place(x=180, y=150)

    def Tabs(self):
        self.All_tabs=Notebook(self.App)
        self.tab1=Frame(self.All_tabs, bg=Black, height=900, width=1600)
        self.tab2=Frame(self.All_tabs, bg=Black, height=900, width=1600)
        self.tab3=Frame(self.All_tabs, bg=Black, height=900, width=1600)
        self.tab4=Frame(self.All_tabs, bg=Black, height=900, width=1602)
        self.tab5=Frame(self.All_tabs, bg=Black, height=900, width=1602)
        self.All_tabs.add(self.tab1, text="Home")
        self.All_tabs.add(self.tab2,text="Image to Sketch")
        self.All_tabs.add(self.tab3,text="Print in Pattern")
        self.All_tabs.add(self.tab4,text="Wikipedia")
        self.All_tabs.add(self.tab5,text="Calculator")
        self.All_tabs.place(x=-1, y=31)
        style = Style()
        style.theme_create( "MyStyle", parent="alt", 
        settings={"TNotebook.Tab": {"configure": {"padding": [35, 2] },}})
        style.theme_use("MyStyle")
        style.configure('TNotebook.Tab', background=fblack, foreground=Cyan)

    def Images_on_Tabs(self):
        self.PIP_IMG_init = Image.open("Icons and Images\Print In Pattern.png")
        self.PIP_IMG_int = self.PIP_IMG_init.resize((600,229), Image.ANTIALIAS)
        self.PIP_IMG = ImageTk.PhotoImage(self.PIP_IMG_init)

        self.Wikipedia_IMG_init = Image.open("Icons and Images\Wikipedia logo.png")
        self.Wikipedia_IMG_int = self.Wikipedia_IMG_init.resize((300,275), Image.ANTIALIAS)
        self.Wikipedia_IMG = ImageTk.PhotoImage(self.Wikipedia_IMG_int)

        self.Calc_IMG_init = Image.open('Icons and Images\Windows-10-Calculator-Fluent-Icon-Big-256.png')
        self.Calc_IMG_int = self.Calc_IMG_init.resize((300,275), Image.ANTIALIAS)
        self.Calc_IMG = ImageTk.PhotoImage(self.Calc_IMG_int)

        self.Jarvis=Image.open("Icons and Images\Main home image.png")
        self.Main_Img=ImageTk.PhotoImage(self.Jarvis)
        self.jarvis_Img=Label(self.tab1, image=self.Main_Img, bg=Black)
        self.jarvis_Img.place(x=100,y=2)

        self.PIP_IMG_Label = Label(self.tab3,image=self.PIP_IMG,fg=Cyan,bg=Black)
        self.PIP_IMG_Label.place(x=1052 , y=22)

        self.Wiki_IMG_Label = Label(self.tab4,image=self.Wikipedia_IMG,fg=Cyan,bg=Black)
        self.Wiki_IMG_Label.place(x=1199 , y=110)

        self.Calc_IMG_Label = Label(self.tab5, image=self.Calc_IMG, bg=Black)
        self.Calc_IMG_Label.place(x=1202 , y=110)

    def Butttons_On_Tab1(self):
        self.Transport_BTN_1=Button(self.tab1,text="Image to Sketch", bg=Black, fg=Cyan, font="helvetica 18", command=lambda: self.All_tabs.select(1), relief=FLAT)
        self.Transport_BTN_1.place(x=398,y=795)
        self.Transport_BTN_2=Button(self.tab1,text="Print in Pattern", bg=Black, fg=Cyan, font="helvetica 18", command=lambda: self.All_tabs.select(2), relief=FLAT, padx=7)
        self.Transport_BTN_2.place(x=598,y=795)
        self.Transport_BTN_3=Button(self.tab1, text="Wikipedia", bg=Black, fg=Cyan, font="helvetica 18", command=lambda: self.All_tabs.select(3), relief=FLAT, padx=36)
        self.Transport_BTN_3.place(x=797,y=795)
        self.Transport_BTN_4=Button(self.tab1, text="Calculator", bg=Black,fg=Cyan,font="helvetica 18",command=lambda: self.All_tabs.select(4), relief=FLAT, padx=33)
        self.Transport_BTN_4.place(x=997,y=795)
        
        self.Refernce_BTN = Button(self.tab1,text="Refernces", font=15,bg=Black,fg=Cyan,command=self.go_to_ref, padx=10)
        self.Refernce_BTN.place(x=2, y=777)
        self.Souce_Code_BTN=Button(self.tab1,text="Source code", font=15,bg=Black,fg=Cyan,command=self.go_to_yt)
        self.Souce_Code_BTN.place(x=2, y=812)

        self.Music_Brwose_BTN=Button(self.tab1, height=1, width=3, text="Browse", bg="black",font=15,fg=Cyan,padx = 19,pady = 4 ,borderwidth=2,command=self.Play_Music, relief=FLAT)
        self.Music_Brwose_BTN.place(x=1482, y=806)

        self.mutePhoto = PhotoImage(file='Icons and Images\mute.png'  )
        self.volumePhoto = PhotoImage(file='Icons and Images\Volume.png')

        self.Mute_BTN = Button(self.tab1, image=self.volumePhoto, bg=Black, command=self.Mute_Music, relief=FLAT)
        self.Mute_BTN.place(x=1559, y=806)

    def Butttons_On_Tab2(self):
        self.Transport_BTN_5=Button(self.tab2, text="Home", bg=Black,fg=Cyan,font="helvetica 18",command=lambda: self.All_tabs.select(0), relief=FLAT,padx=56)
        self.Transport_BTN_5.place(x=398,y=795)
        self.Transport_BTN_6=Button(self.tab2, text="Print in Pattern", bg=Black, fg=Cyan, font="helvetica 18", command=lambda: self.All_tabs.select(2), relief=FLAT, padx=7)
        self.Transport_BTN_6.place(x=598,y=795)
        self.Transport_BTN_7=Button(self.tab2, text="Wikipedia", bg=Black, fg=Cyan, font="helvetica 18", command=lambda: self.All_tabs.select(3), relief=FLAT, padx=36)
        self.Transport_BTN_7.place(x=797,y=795)
        self.Transport_BTN_8=Button(self.tab2, text="Calculator", bg=Black,fg=Cyan,font="helvetica 18",command=lambda: self.All_tabs.select(4), relief=FLAT, padx=33)
        self.Transport_BTN_8.place(x=997,y=795)

        self.Browse_IMG_BTN=Button(self.tab2, text="Browse Img", bg =Black,font=15,padx=5,fg = Cyan,command=self.Browse_img)
        self.Browse_IMG_BTN.place(x=1400, y=102)
        self.Convert_IMG_BTN=Button(self.tab2, text="Convert", bg =Black,font=15,padx=19,fg = Cyan,command=self.Img_to_Pencil_Sketch)
        self.Convert_IMG_BTN.place(x=1400, y=200)                             

    def Butttons_On_Tab3(self):
        self.Transport_BTN_9=Button(self.tab3, text="Home", bg=Black,fg=Cyan,font="helvetica 18",command=lambda: self.All_tabs.select(0), relief=FLAT,padx=56)
        self.Transport_BTN_9.place(x=398,y=795)
        self.Transport_BTN_10=Button(self.tab3, text="Image to Sketch", bg=Black, fg=Cyan, font="helvetica 18", command=lambda: self.All_tabs.select(1), relief=FLAT)
        self.Transport_BTN_10.place(x=598,y=795)
        self.Transport_BTN_11=Button(self.tab3, text="Wikipedia", bg=Black, fg=Cyan, font="helvetica 18", command=lambda: self.All_tabs.select(3), relief=FLAT, padx=36)
        self.Transport_BTN_11.place(x=797,y=795)
        self.Transport_BTN_12=Button(self.tab3, text="Calculator", bg=Black,fg=Cyan,font="helvetica 18",command=lambda: self.All_tabs.select(4), relief=FLAT, padx=33)
        self.Transport_BTN_12.place(x=997,y=795)
        
        self.Print_in_Pattern_BTN= Button(self.tab3, text="Pattern", bg =Black,font=15,padx=5,fg = Cyan,command=self.Print_in_Pattern)
        self.Print_in_Pattern_BTN.place(x=800, y=122)

        self.PIP_Clear_BTN= Button(self.tab3, text="Clear", bg =Black,font=15,padx=5,fg = Cyan,command=self.PIP_Clear)
        self.PIP_Clear_BTN.place(x=900, y=122)

    def Butttons_On_Tab4(self):
        self.Transport_BTN_13=Button(self.tab4, text="Home", bg=Black,fg=Cyan,font="helvetica 18",command=lambda: self.All_tabs.select(0), relief=FLAT,padx=56)
        self.Transport_BTN_13.place(x=398,y=795)
        self.Transport_BTN_14=Button(self.tab4, text="Image to Sketch", bg=Black, fg=Cyan, font="helvetica 18", command=lambda: self.All_tabs.select(1), relief=FLAT)
        self.Transport_BTN_14.place(x=598,y=795)
        self.Transport_BTN_15=Button(self.tab4, text="Print in Pattern", bg=Black, fg=Cyan, font="helvetica 18", command=lambda: self.All_tabs.select(2), relief=FLAT, padx=7)
        self.Transport_BTN_15.place(x=797,y=795)
        self.Transport_BTN_16=Button(self.tab4, text="Calculator", bg=Black,fg=Cyan,font="helvetica 18",command=lambda: self.All_tabs.select(4), relief=FLAT, padx=33)
        self.Transport_BTN_16.place(x=997,y=795)

        self.Wikipedia_Search_BTN= Button( self.tab4, text="Search", width = 5, bg=Black, fg = Cyan,command=self.Wikipedia_Search,borderwidth=2, padx=12 , relief=FLAT)
        self.Wikipedia_Search_BTN.place(x=800, y=150)

        self.Clear_Search_BTN=Button(self.tab4, text="Clear", width = 5, bg=Black, fg = Cyan,command=self.Clear_Wiki,borderwidth=2, padx=12 , relief=FLAT)
        self.Clear_Search_BTN.place(x=900, y=150)                                                                       

    def Butttons_On_Tab5(self):
        self.Transport_BTN_17=Button(self.tab5, text="Home", bg=Black,fg=Cyan,font="helvetica 18",command=lambda: self.All_tabs.select(0), relief=FLAT,padx=56)
        self.Transport_BTN_17.place(x=398,y=795)
        self.Transport_BTN_18=Button(self.tab5, text="Image to Sketch", bg=Black, fg=Cyan, font="helvetica 18",command=lambda: self.All_tabs.select(1), relief=FLAT)
        self.Transport_BTN_18.place(x=598,y=795)
        self.Transport_BTN_19=Button(self.tab5, text="Print in Pattern", bg=Black, fg=Cyan, font="helvetica 18",command=lambda: self.All_tabs.select(2), relief=FLAT, padx=7)
        self.Transport_BTN_19.place(x=797,y=795)
        self.Transport_BTN_20=Button(self.tab5, text="Wikipedia", bg=Black, fg=Cyan, font="helvetica 18", command=lambda: self.All_tabs.select(3), relief=FLAT, padx=36)
        self.Transport_BTN_20.place(x=997,y=795)

    def update_clock(self):
        self.IST = pytz.timezone('Asia/Kolkata')
        self.label_date_now = Button(self.App,text="Current Date",command=self.Wish_me,bg = "black", fg=Cyan, borderwidth=0)
        self.label_date_now.place( x = 1455 , y = 31 )
        self.label_time_now = Button(self.App,text="Current Time",bg="black",command=self.Wish_me,fg=Cyan, padx=8, borderwidth=0)
        self.label_time_now.place( x = 1530, y = 31)       
        self.raw_TS = datetime.now(self.IST)
        self.date_now = self.raw_TS.strftime("%d %b %Y")
        self.time_now = self.raw_TS.strftime("%H:%M %p")
        self.formatted_now = self.raw_TS.strftime("%d-%m-%Y")
        self.label_date_now.config(text = self.date_now)
        self.label_time_now.config(text = self.time_now)
        self.label_time_now.after(1000, self.update_clock)        
        return self.formatted_now

    def Browse_img(self):
        for Img in self.Image_Frame.winfo_children():
            Img.destroy()
        self.filepath= filedialog.askopenfilename(title="Choose a file",filetypes=[("jpg file","*.jpg"),("png file","*.png")])
        try:
            self.temporary = Image.open(self.filepath)
            self.width, self.height = int(self.temporary.size[0]), int(self.temporary.size[1])
            if self.width>1168 or self.height>657:
                if self.width > self.height:
                    self.height = int(1168/self.width*self.height)
                    self.width = 1168
                elif self.height > self.width:
                    self.width = int(657/self.height*self.width)
                    self.height = 657
                else:
                    self.width, self.height = 657,657
            else:
                pass
            self.resize = self.temporary.resize((self.width,self.height), Image.ANTIALIAS) #Width, Height
            self.Garrentee = ImageTk.PhotoImage(self.resize)
            self.Browse_img_label = Label(self.Image_Frame,image=self.Garrentee,fg=Cyan,bg=Black)
            self.Browse_img_label.pack()
        except Exception as e:
            messagebox.showerror("Error", "You have not selected an Image file to convert, \nPlease Select an Image")
            return    
        return

    def Img_to_Pencil_Sketch(self):
        try:
            img=cv2.imread(self.filepath)
            gf=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            inv=cv2.bitwise_not(gf)
            blur=cv2.GaussianBlur(inv,(41,41),0)
            invb=cv2.bitwise_not(blur)
            self.sketch=cv2.divide(gf,invb,scale=240.0)   
            cv2.imwrite('Output.png', self.sketch)       
            resizeimg=cv2.resize(self.sketch,(self.width,self.height))
            cv2.imshow('Output.png',resizeimg)
            cv2.waitKey(0)
        except Exception as e:
            messagebox.showerror("Error", "You have not selected an Image file to convert, \nPlease Select an Image")
            self.Browse_img()
            return   
        return

    def Print_in_Pattern(self):
            self.Sp_Count = 0
            for widgets in self.Pattern_Frame.winfo_children():
                widgets.destroy()
            self.f=self.Pattern_Entry.get()
            self.Pattern_Entry.delete(0, END)
            try:
                for I in self.f :
                    if I=='a'or I=='A' :
                        self.A=Label(self.Pattern_Frame,text='   $ $    \n $      $  \n $ $ $ $  \n $       $  \n $       $  ',font="50",padx=1, pady=2, bg="black", fg="#15F4EE")
                        self.A.pack(side=LEFT,anchor="nw")
                    elif I=='b'or I=='B':
                        self.B=Label(self.Pattern_Frame,text=' $ $ $ $   \n $         $  \n $ $ $ $   \n $         $  \n $ $ $ $   ',font="50",padx=1, pady=2, bg="black", fg="#15F4EE")
                        self.B.pack(side=LEFT,anchor="nw")
                    elif I=='c'or I=='C':
                        self.C=Label(self.Pattern_Frame,text=' $ $ $ $ \n$          \n$          \n$          \n $ $ $ $ ',font="50",padx=1, pady=2, bg="black", fg="#15F4EE")
                        self.C.pack(side=LEFT,anchor="nw")
                    elif I=='d' or I=='D':
                        self.D=Label(self.Pattern_Frame,text=' $ $ $ $    \n $        $   \n $         $  \n $        $   \n $ $ $ $    ',font="50",padx=1, pady=2, bg="black", fg="#15F4EE")
                        self.D.pack(side=LEFT,anchor="nw")
                    elif I=='e' or I=='E':
                        self.E=Label(self.Pattern_Frame,text=' $ $ $ $  \n$           \n $ $ $ $  \n$           \n $ $ $ $  ',font="50",padx=1, pady=2, bg="black", fg="#15F4EE")
                        self.E.pack(side=LEFT,anchor="nw")
                    elif I=='f' or I=='F':
                        self.F=Label(self.Pattern_Frame,text=' $ $ $ $ \n $          \n $ $ $    \n $          \n $          ',font="50",padx=1, pady=2, bg="black", fg="#15F4EE")
                        self.F.pack(side=LEFT,anchor="nw")
                    elif I=='g' or I=='G':
                        self.G=Label(self.Pattern_Frame,text=' $ $ $ $   \n $           \n $    $ $   \n $        $  \n $ $ $ $   ',font="50",padx=1, pady=2, bg="black", fg="#15F4EE")
                        self.G.pack(side=LEFT,anchor="nw")
                    elif I=='h' or I=='H':
                        self.H=Label(self.Pattern_Frame,text=' $        $  \n $        $  \n$ $ $ $ \n $        $  \n $        $  ',font="50",padx=1, pady=2, bg="black", fg="#15F4EE")
                        self.H.pack(side=LEFT,anchor="nw")
                    elif I=='i' or I=='I':
                        self.I=Label(self.Pattern_Frame,text='$ $ $ $  \n   $     \n   $     \n   $     \n$ $ $ $  ',font="50",padx=1, pady=2, bg="black", fg="#15F4EE")
                        self.I.pack(side=LEFT,anchor="nw")
                    elif I=='j' or I=='J':
                        self.J=Label(self.Pattern_Frame,text='$ $ $ $ $  \n    $      \n    $      \n$    $       \n$ $ $       ',font="50",padx=1, pady=2, bg="black", fg="#15F4EE")
                        self.J.pack(side=LEFT,anchor="nw")
                    elif I=='k' or I=='K':
                        self.K=Label(self.Pattern_Frame,text='$     $  \n$   $    \n$ $      \n$   $    \n$     $  ',font="50",padx=1, pady=2, bg="black", fg="#15F4EE")
                        self.K.pack(side=LEFT,anchor="nw")
                    elif I=='l' or I=='L':
                        self.L=Label(self.Pattern_Frame,text='$ $        \n$          \n$          \n$          \n$ $ $ $  ',font="50",padx=1, pady=2, bg="black", fg="#15F4EE")
                        self.L.pack(side=LEFT,anchor="nw")
                    elif I=='m' or I=='M':
                        self.M=Label(self.Pattern_Frame,text=' $         $  \n $ $   $ $  \n $   $$  $  \n $          $  \n $          $  ',font="50",padx=1, pady=2, bg="black", fg="#15F4EE")
                        self.M.pack(side=LEFT,anchor="nw")
                    elif I=='n' or I=='N':
                        self.N=Label(self.Pattern_Frame,text='$       $ \n$ $    $ \n$  $   $ \n$    $ $ \n$       $ ',font="50",padx=1, pady=2, bg="black", fg="#15F4EE")
                        self.N.pack(side=LEFT,anchor="nw")
                    elif I=='o' or I=='O':
                        self.O=Label(self.Pattern_Frame,text=' $ $ $   \n$       $  \n$ $ $ $  \n$       $  \n $ $ $   ',font="50",padx=1, pady=2, bg="black", fg="#15F4EE")
                        self.O.pack(side=LEFT,anchor="nw")
                    elif I=='p' or I=='P':
                        self.P=Label(self.Pattern_Frame,text='$ $ $    \n$      $  \n$ $ $    \n$         \n$         ',font="50",padx=1, pady=2, bg="black", fg="#15F4EE")
                        self.P.pack(side=LEFT,anchor="nw")
                    elif I=='q' or I=='Q':
                        self.Q=Label(self.Pattern_Frame,text='    $  $ 	 \n$ $    $     \n$  $   $     \n$    $ $     \n  $ $  $ $   ',font="50",padx=1, pady=2, bg="black", fg="#15F4EE")
                        self.Q.pack(side=LEFT,anchor="nw")
                    elif I=='r' or I=='R':
                        self.R=Label(self.Pattern_Frame,text='$ $ $ $   \n$        $  \n$ $ $ $   \n$     $     \n$       $   ',font="50",padx=1, pady=2, bg="black", fg="#15F4EE")
                        self.R.pack(side=LEFT,anchor="nw")
                    elif I=='s' or I=='S':
                        self.S=Label(self.Pattern_Frame,text='$ $ $ $  \n$           \n$ $ $ $  \n         $  \n$ $ $ $  ',font="50",padx=1, pady=2, bg="black", fg="#15F4EE")
                        self.S.pack(side=LEFT,anchor="nw")
                    elif I=='t' or I=='T':
                        self.T=Label(self.Pattern_Frame,text='$ $ $ $ $  \n    $      \n    $      \n    $      \n   $ $     ',font="50",padx=1, pady=2, bg="black", fg="#15F4EE")
                        self.T.pack(side=LEFT,anchor="nw")
                    elif I=='u' or I=='U':
                        self.U=Label(self.Pattern_Frame,text='$       $  \n$       $  \n$       $  \n$       $  \n$ $ $ $  ',font="50",padx=1, pady=2, bg="black", fg="#15F4EE")
                        self.U.pack(side=LEFT,anchor="nw")
                    elif I=='v' or I=='V':
                        self.V=Label(self.Pattern_Frame,text='$        $  \n $      $   \n  $    $    \n   $  $     \n    $$      ',font="50",padx=1, pady=2, bg="black", fg="#15F4EE")
                        self.V.pack(side=LEFT,anchor="nw")
                    elif I=='w' or I=='W':
                        self.W=Label(self.Pattern_Frame,text='$          $  \n$          $  \n$   $$   $  \n$ $    $ $  \n$           $  ',font="50",padx=1, pady=2, bg="black", fg="#15F4EE")
                        self.W.pack(side=LEFT,anchor="nw")
                    elif I=='x' or I=='X':
                        self.X=Label(self.Pattern_Frame,text='$        $  \n  $    $    \n    $$      \n  $    $    \n$        $  ',font="50",padx=1, pady=2, bg="black", fg="#15F4EE")
                        self.X.pack(side=LEFT,anchor="nw")
                    elif I=='y' or I=='Y':
                        self.Y=Label(self.Pattern_Frame,text='$      $  \n $    $   \n   $$     \n   $      \n $        ',font="50",padx=1, pady=2, bg="black", fg="#15F4EE")
                        self.Y.pack(side=LEFT,anchor="nw")
                    elif I=='z' or I=='Z':
                        self.Z=Label(self.Pattern_Frame,text='$ $ $ $  \n     $   \n   $     \n $       \n$ $ $ $  ',font="50",padx=1, pady=2, bg="black", fg="#15F4EE")
                        self.Z.pack(side=LEFT,anchor="nw")
                    elif I==' ':
                        self._=Label(self.Pattern_Frame,text='     \n     \n     \n     \n     ',font="50",padx=1, pady=2, bg="black", fg="#15F4EE")
                        self._.pack(side=LEFT,anchor="nw")
                    elif I=='1':
                        self._1=Label(self.Pattern_Frame,text='    $       \n  $ $        \n    $       \n    $       \n $ $ $ $    ',font="50",padx=1, pady=2, bg="black", fg="#15F4EE")
                        self._1.pack(side=LEFT,anchor="nw")    
                    elif I=='2':
                        self._2=Label(self.Pattern_Frame,text='  $ $ $     \n$       $    \n    $      \n $         \n$ $ $ $    ',font="50",padx=1, pady=2, bg="black", fg="#15F4EE")
                        self._2.pack(side=LEFT,anchor="nw")
                    elif I=='3':
                        self._3=Label(self.Pattern_Frame,text='$ $ $ $    \n         $    \n   $ $ $    \n         $    \n$ $ $ $    ',font="50",padx=1, pady=2, bg="black", fg="#15F4EE")
                        self._3.pack(side=LEFT,anchor="nw")
                    elif I=='4':
                        self._4=Label(self.Pattern_Frame,text='$       $    \n$       $    \n$ $ $ $    \n         $    \n         $    ',font="50",padx=1, pady=2, bg="black", fg="#15F4EE")
                        self._4.pack(side=LEFT,anchor="nw")
                    elif I=='5':
                        self._5=Label(self.Pattern_Frame,text='$ $ $ $    \n$            \n$ $ $      \n        $    \n$ $ $      ',font="50",padx=1, pady=2, bg="black", fg="#15F4EE")
                        self._5.pack(side=LEFT,anchor="nw")
                    elif I=='6':
                        self._6=Label(self.Pattern_Frame,text='$ $ $ $    \n$             \n$ $ $ $    \n$       $    \n$ $ $ $    ',font="50",padx=1, pady=2, bg="black", fg="#15F4EE")
                        self._6.pack(side=LEFT,anchor="nw")
                    elif I=='7':    
                        self._7=Label(self.Pattern_Frame,text='$ $ $ $    \n      $     \n  $ $      \n  $        \n$          ',font="50",padx=1, pady=2, bg="black", fg="#15F4EE")
                        self._7.pack(side=LEFT,anchor="nw")
                    elif I=='8':    
                        self._8=Label(self.Pattern_Frame,text='$ $ $ $    \n$       $    \n$ $ $ $    \n$       $    \n$ $ $ $    ',font="50",padx=1, pady=2, bg="black", fg="#15F4EE")
                        self._8.pack(side=LEFT,anchor="nw")
                    elif I=='9':
                        self._9=Label(self.Pattern_Frame,text='$ $ $ $    \n$       $    \n$ $ $ $    \n         $    \n         $    ',font="50",padx=1, pady=2, bg="black", fg="#15F4EE")
                        self._9.pack(side=LEFT,anchor="nw")
                    elif I=='0':
                        self._0=Label(self.Pattern_Frame,text='$ $ $ $    \n$       $    \n$       $    \n$       $    \n$ $ $ $    ',font="50",padx=1, pady=2, bg="black", fg="#15F4EE")
                        self._0.pack(side=LEFT,anchor="nw")    
                    else:
                        self.Sp_Count +=1
            except Exception as e:
                messagebox.showerror("Unexpected error", "There is an unexpected error occured")
                return
            if self.Sp_Count>=1:
                messagebox.showinfo("Character unsupport", "Special characters are not supported") 
                   
            return

    def PIP_Clear(self):
        for widgets in self.Pattern_Frame.winfo_children():
            widgets.destroy()

    def Wikipedia_Search(self):
        if self.Wikipedia_Entry.get(1.0, END):
            try:         
                results = wikipedia.summary(self.Wikipedia_Entry.get(1.0, END), sentences=15)
            except Exception as e:
                messagebox.showinfo("Results not found",f"Wikipedia is not showing result about {self.Wikipedia_Entry.get(1.0, END)}\nPlease Enter correctly about which you want to search")     
                return
        else:
            messagebox.showinfo("Search is empty",f"Please Enter about which you want to search")     
            return
        self.Wiki_text_box.insert(1.0,results )
        self.Wiki_text_box.tag_configure("left", justify="left")
        self.Wiki_text_box.tag_add("left", 1.0, "end")
        
    def add_textbox(self):
        self.Wiki_text_box = Text(self.tab4, height=25, width=50, bg=Black, fg=Cyan, font="helvetica 14")
        self.Wiki_text_box.place(x=180, y=200)

    def Clear_Wiki(self):
        self.Wiki_text_box.delete(1.0, END)

    def go_to_yt(self):
            webbrowser.open("https://github.com/Madhurjya10/Python-GUI-project-using-Tkinter-For-beginners")

    def go_to_ref(self):
            webbrowser.open_new_tab("https://www.youtube.com/c/Codemycom")
            webbrowser.open_new_tab("https://youtube.com/playlist?list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV")
            webbrowser.open("https://www.youtube.com/c/CodeWithHarry")

    def Play_Music(self):
        mixer.init()
        self.Music_Filepath=filedialog.askopenfilename(title="Choose a file",filetypes=[("wav file","*.wav"),("mp3 file","*.mp3")])
        try:
            mixer.music.load(self.Music_Filepath)
            mixer.music.set_volume(0.4)
            mixer.music.play(-1)		
        except Exception as e:
            messagebox.showerror("Error", "You have not selected the audio file for backgroung music,\nPlease Select the Audio file")
            return
        return
    
    def Mute_Music(self):
        global muted
        if muted:  # Unmute the music
            mixer.music.set_volume(0.4)
            self.Mute_BTN.configure(image=self.volumePhoto)
            muted = FALSE
        else: 
            mixer.music.set_volume(0)
            self.Mute_BTN.configure(image=self.mutePhoto)
            muted = TRUE       
        return

    def Wish_me(self):
        self.hour = int(self.raw_TS.strftime("%H"))
        if self.hour>=0 and self.hour<12:
            self.Speak("Good Morning guys!")

        elif self.hour>=12 and self.hour<18:
            self.Speak("Good Afternoon guys!")   

        else:
            self.Speak("Good Evening guys!")
        self.Speak(f"Today is {self.date_now} and time is {self.time_now}")  

    def Speak(self, audio):
        self.Engine = pyttsx3.init()
        Rate=self.Engine.setProperty("rate",150)
        voice=self.Engine.getProperty("voices")
        self.Engine.say(audio)
        self.Engine.runAndWait()

    def init_Calculator(self):
        self.total_expression = ""
        self.current_expression = ""
        self.display_frame = self.create_display_frame()

        self.total_label, self.label = self.create_display_labels()

        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.': (4, 1)
        }
        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
        self.buttons_frame = self.create_buttons_frame()

        self.buttons_frame.rowconfigure(0, weight=1)
        for x in range(1, 5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)
        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()
        self.bind_keys()

    def bind_keys(self):
        self.Calc_Frame.bind("<Return>", lambda event: self.evaluate())
        for key in self.digits:
            self.Calc_Frame.bind(str(key), lambda event, digit=key: self.add_to_expression(digit))

        for key in self.operations:
            self.Calc_Frame.bind(key, lambda event, operator=key: self.append_operator(operator))

    def create_special_buttons(self):
        self.create_clear_button()
        self.create_equals_button()
        self.create_square_button()
        self.create_sqrt_button()

    def create_display_labels(self):
        total_label = Label(self.display_frame, text=self.total_expression,height=2,anchor=E, bg=Black,
                               fg=Cyan, padx=24, font=SMALL_FONT_STYLE)
        total_label.pack(expand=False, fill='both')

        label = Label(self.display_frame, text=self.current_expression,height=3,anchor=E, bg=Black,
                         fg=Cyan, padx=24, font=LARGE_FONT_STYLE)
        label.pack(expand=False, fill='both')

        return total_label, label

    def create_display_frame(self):
        frame = Frame(self.Calc_Frame, height=221, bg=Black)
        frame.pack(expand=False, fill="both")
        return frame

    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_label()

    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = Button(self.buttons_frame, text=str(digit), bg=Black,height=2,width=5 ,fg=Cyan, font=DIGITS_FONT_STYLE,
                               borderwidth=0, command=lambda x=digit: self.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1])

    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_total_label()
        self.update_label()

    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = Button(self.buttons_frame, text=symbol, bg=Black, fg=Cyan, font=DIGITS_FONT_STYLE,height=2,width=5 ,
                               borderwidth=0, command=lambda x=operator: self.append_operator(x))
            button.grid(row=i, column=4)
            i += 1

    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_label()
        self.update_total_label()

    def create_clear_button(self):
        button = Button(self.buttons_frame, text="C", bg=Black, fg=Cyan, font=DIGITS_FONT_STYLE,height=2,width=5,
                           borderwidth=0, command=self.clear)
        button.grid(row=0, column=1)

    def square(self):
        self.current_expression = str(eval(f"{self.current_expression}**2"))
        self.update_label()

    def create_square_button(self):
        button = Button(self.buttons_frame, text="x\u00b2", bg=Black, fg=Cyan, font=DIGITS_FONT_STYLE,height=2,width=5,
                           borderwidth=0, command=self.square)
        button.grid(row=0, column=2)

    def sqrt(self):
        self.current_expression = str(eval(f"{self.current_expression}**0.5"))
        self.update_label()

    def create_sqrt_button(self):
        button = Button(self.buttons_frame, text="\u221ax", bg=Black, fg=Cyan, font=DIGITS_FONT_STYLE,height=2,width=5,
                           borderwidth=0, command=self.sqrt)
        button.grid(row=0, column=3)

    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_total_label()
        try:
            self.current_expression = str(eval(self.total_expression))

            self.total_expression = ""
        except Exception as e:
            self.current_expression = "Error"
        finally:
            self.update_label()

    def create_equals_button(self):
        button = Button(self.buttons_frame, text="=", bg=Black, fg=Cyan,padx=4,font=DIGITS_FONT_STYLE,height=2,width=10,
                           borderwidth=0, command=self.evaluate)
        button.grid(row=4, column=3, columnspan=2)

    def create_buttons_frame(self):
        frame = Frame(self.Calc_Frame)
        frame.pack(expand=False, fill="both")
        return frame

    def update_total_label(self):
        expression = self.total_expression
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f' {symbol} ')
        self.total_label.config(text=expression)

    def update_label(self):
        self.label.config(text=self.current_expression[:15])

if __name__ == "__main__":
    calc = MainWindow()