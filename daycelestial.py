# -*- coding: cp1252 -*-

from Tkinter import *
import ephem
import celnav


class MyApp:
    def __init__(self, parent):
        self.myContainer1 = Frame(parent)
        self.myContainer1["bd"] = 5
        self.myContainer1["relief"] = "ridge"
        self.myContainer1.grid(sticky=W+E+N+S)

        self.myContainer2 = Frame(parent)
        self.myContainer2["bd"] = 5
        self.myContainer2["relief"] = "ridge"
        self.myContainer2.grid(sticky=W+E+N+S)


        self.myContainer3 = Frame(parent)
        self.myContainer3["bd"] = 5
        self.myContainer3["relief"] = "ridge"
        self.myContainer3.grid(sticky=W+E+N+S)



        self.label1 = Label(self.myContainer1,font=("Times", "12", "bold"))
        self.label1["text"] = "DR pos:"     
        self.label1.grid(row=0, column=0, sticky=W)
    
        self.label2 = Label(self.myContainer1)
        self.label2["text"] = "lon:"    
        self.label2.grid(sticky=E,row=1, column=0 )

        self.entry_drlon = Entry ( self.myContainer1, width=3)
        self.entry_drlon.grid(row=1, column=2, padx=5, sticky=E+W)
        
        self.label3 = Label(self.myContainer1)
        self.label3["text"] = "lat:"    
        self.label3.grid(sticky=E,row=1, column=3 )

        self.entry_drlat = Entry ( self.myContainer1, width=3)
        self.entry_drlat.grid(row=1, column=4, padx=5, sticky=E+W)

    


        self.label4 = Label(self.myContainer1)
        self.label4["text"] = "speed kn:"   
        self.label4.grid(row=2, column=0, sticky=W)

        self.entry_speed = Entry ( self.myContainer1, width=3 )
        self.entry_speed.grid(row=2, column=2, padx=5, sticky=E+W)

        self.label5 = Label(self.myContainer1)
        self.label5["text"] = "hdg:"    
        self.label5.grid(sticky=E,row=2, column=3 )

        self.entry_hdg = Entry ( self.myContainer1, width=3 )
        self.entry_hdg.grid(row=2, column=4, padx=5, sticky=E+W)

        self.diplabel = Label(self.myContainer1)
        self.diplabel["text"] = "elev.(m):"    
        self.diplabel.grid(sticky=E,row=2, column=5 )

        self.entry_elev = Entry ( self.myContainer1, width=3 )
        self.entry_elev.grid(row=2, column=6, padx=5, sticky=E+W)


        

        self.label6 = Label(self.myContainer2,font=("Times", "12", "bold"))
        self.label6["text"] = "Sights:"     
        self.label6.grid(row=2, column=0, sticky=W)



 ## Sight 1
        self.targetVar1 = StringVar()
        self.targetVar1.set("target")
        self.mb1 =Menubutton( self.myContainer2, text="target", textvariable=self.targetVar1, relief=RAISED )
        self.mb1.grid(row=3, column=0, pady=3)
        self.mb1.menu  =  Menu ( self.mb1, tearoff=0 )
        self.mb1["menu"]  =  self.mb1.menu
        self.mb1.menu.add_radiobutton ( label="Sun LL", variable=self.targetVar1, value="sunll" )
        self.mb1.menu.add_radiobutton ( label="Sun UL", variable=self.targetVar1, value="sunul" )
        self.mb1.menu.add_radiobutton ( label="Moon LL", variable=self.targetVar1, value="moonll" ) 
        self.mb1.menu.add_radiobutton ( label="Moon UL", variable=self.targetVar1, value="moonul" )
        self.mb1.menu.add_radiobutton ( label="Venus", variable=self.targetVar1, value="venus" )

        self.label7 = Label(self.myContainer2)
        self.label7["text"] = "Hs deg:"     
        self.label7.grid(sticky=E,row=3, column=1 )

        self.entry_hs1d = Entry ( self.myContainer2, width=3 )
        self.entry_hs1d.grid(row=3, column=2, padx=5, sticky=E+W)

        self.label8 = Label(self.myContainer2)
        self.label8["text"] = "min:"    
        self.label8.grid(sticky=E,row=3, column=3 )

        self.entry_hs1m = Entry ( self.myContainer2, width=3 )
        self.entry_hs1m.grid(row=3, column=4, padx=5, sticky=E+W)

        self.label9 = Label(self.myContainer2)
        self.label9["text"] = "time:"   
        self.label9.grid(sticky=E,row=3, column=5 )

        self.time1Var = StringVar()
        self.entry_t1 = Entry ( self.myContainer2, width=19, textvariable = self.time1Var )
        self.entry_t1.grid(row=3, column=6, padx=5, sticky=E+W)
        self.time1Var.set(str(ephem.now()))


        def settime1():
            self.time1Var.set(str(ephem.now()))

        def showHc1():
            self.hc1 = celnav.Sight(int(self.entry_drlon.get()), int(self.entry_drlat.get()), self.targetVar1.get(), time=self.entry_t1.get())
            self.hclabel = Label(self.myContainer2)
            self.hclabel["text"] = "Hc: %s Az: %s"  %(self.hc1.getalt(), self.hc1.getaz())
            self.hclabel.grid(sticky=E,row=3, column=9 )
            
        self.nowbutton1 = Button(self.myContainer2, text="Now", command=settime1) 
        self.nowbutton1.grid(row=3, column=7, pady=3)

        self.hcbutton1 = Button(self.myContainer2, text="Hc", command=showHc1) 
        self.hcbutton1.grid(row=3, column=8, pady=3)


        def settime2():
            self.time2Var.set(str(ephem.now()))

        def showHc2():
            self.hc2 = celnav.Sight(int(self.entry_drlon.get()), int(self.entry_drlat.get()), self.targetVar2.get(), time=self.entry_t2.get())
            self.hclabel = Label(self.myContainer2)
            self.hclabel["text"] = "Hc: %s Az: %s"  %(self.hc2.getalt(), self.hc2.getaz())
            self.hclabel.grid(sticky=E,row=4, column=9 )
            
        self.nowbutton2 = Button(self.myContainer2, text="Now", command=settime2) 
        self.nowbutton2.grid(row=4, column=7, pady=3)

        self.hcbutton2 = Button(self.myContainer2, text="Hc", command=showHc2) 
        self.hcbutton2.grid(row=4, column=8, pady=3)


## Sight 2
        self.targetVar2 = StringVar()
        self.targetVar2.set("target")
        self.mb2 =Menubutton( self.myContainer2, text="target", textvariable=self.targetVar2, relief=RAISED )
        self.mb2.grid(row=4, column=0, pady=3)
        self.mb2.menu  =  Menu ( self.mb2, tearoff=0 )
        self.mb2["menu"]  =  self.mb2.menu
        self.mb2.menu.add_radiobutton ( label="Sun LL", variable=self.targetVar2, value="sunll" )
        self.mb2.menu.add_radiobutton ( label="Sun UL", variable=self.targetVar2, value="sunul" )
        self.mb2.menu.add_radiobutton ( label="Moon LL", variable=self.targetVar2, value="moonll" ) 
        self.mb2.menu.add_radiobutton ( label="Moon UL", variable=self.targetVar2, value="moonul" )
        self.mb2.menu.add_radiobutton ( label="Venus", variable=self.targetVar2, value="venus" )

        self.label10 = Label(self.myContainer2)
        self.label10["text"] = "Hs deg:"    
        self.label10.grid(sticky=E,row=4, column=1 )

        self.entry_hs2d = Entry ( self.myContainer2, width=3 )
        self.entry_hs2d.grid(row=4, column=2, padx=5, sticky=E+W)

        self.label11 = Label(self.myContainer2)
        self.label11["text"] = "min:"   
        self.label11.grid(sticky=E,row=4, column=3 )

        self.entry_hs2m = Entry ( self.myContainer2, width=3 )
        self.entry_hs2m.grid(row=4, column=4, padx=5, sticky=E+W)

        self.label12 = Label(self.myContainer2)
        self.label12["text"] = "time:"      
        self.label12.grid(sticky=E,row=4, column=5 )

        self.time2Var = StringVar()
        self.entry_t2 = Entry ( self.myContainer2, width=3, textvariable = self.time2Var)
        self.entry_t2.grid(row=4, column=6, padx=5, sticky=E+W)

##        def settime2():
##            self.time2Var.set(str(ephem.now()))           
##        self.nowbutton2 = Button(self.myContainer2, text="Now", command=settime2) 
##        self.nowbutton2.grid(row=4, column=7, pady=3)


        
        def comppos():
            drlon = ephem.degrees(self.entry_drlon.get())
            drlat = ephem.degrees(self.entry_drlat.get())
            Hs1 = ephem.degrees(self.entry_hs1d.get())
            Hs2 = ephem.degrees(self.entry_hs2d.get())
            t1 = self.entry_t1.get()
            t2 = self.entry_t2.get()
            elev = float(self.entry_elev.get())
            hdg = ephem.degrees(self.entry_hdg.get())
            speed = float(self.entry_speed.get())
            s1 = celnav.Sight(drlon, drlat, self.targetVar1.get(), Hs1, t1, elev)
            s2 = celnav.Sight(drlon, drlat, self.targetVar2.get(), Hs2, t2, elev)
            fix = celnav.compfix(s1, s2, speed, hdg)                 
            output.set(celnav.formlat(fix[0]) + "   " + celnav.formlon(fix[1]))



        self.button4 = Button(self.myContainer3, text="compute", command=comppos) 
        self.button4.grid(row=1, column=0, pady=3)

        
        output = StringVar()
        self.result = Label(self.myContainer3, textvariable=output)
        self.result.grid(row=1, column=1, columnspan=5)



root = Tk()
myapp = MyApp(root)
root.mainloop()