from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("Billing Management system")
#Sroot.geometry("1280*720")
#bg_color="#209290"

#====================variable==============================================================
Bread=IntVar()
Wine=IntVar()
Cake=IntVar()
Ice_Cream=IntVar()
total=IntVar()

cd=StringVar()
cw=StringVar()
cr=StringVar()
cm=StringVar()
total_cost=StringVar()

#==================================functions=======================================================
def Total():
    if Bread.get()==0 and Wine.get()==0 and Cake.get()==0 and Ice_Cream.get()==0:
        messagebox.showerror("error","please select number of quantity")
    else:
            b=Bread.get()
            w=Wine.get()
            r=Cake.get()
            m=Ice_Cream.get()
            t=float(b*1.89+w*8.99+r*2.18+m*4.50)
            total.set(b+w+r+m)
            total_cost.set("$"+str(round(t,2)))

            cd.set("$"+str(round(b*1.89,2)))
            cw.set("$"+str(round(w*8.99,2)))
            cr.set("$"+str(round(r*2.18,2)))
            cm.set("$"+str(round(m*4.50,2)))
def receipt():
    textarea.delete(1.0,END)
    textarea.insert(END,'Items\tNumber of Items\tCost of Items')
    textarea.insert(END,f'\n\nBread\t\t{Bread.get()}\t {cd.get()}')
    textarea.insert(END,f'\n\nWine\t\t{Wine.get()}\t {cw.get()}')
    textarea.insert(END,f'\n\nCake\t\t{Cake.get()}\t {cr.get()}')
    textarea.insert(END,f'\n\nIce Cream\t\t{Ice_Cream.get()}\t {cm.get()}')
    textarea.insert(END,f'\n\n==================================')
    textarea.insert(END,f'\n\nTotal price\t\t{total.get()}\t {total_cost.get()}')
    textarea.insert(END,f'\n==================================')

title=Label(root,text="Billing Management System",bg="#209290",fg="white",font=("times new romman",35,"bold"),relief=GROOVE,bd=12)
title.pack(fill=X)
#==================================product details=========================================================================================
F1=LabelFrame(root,text="Product Details",font=("times new romman",18,"bold"),fg="gold",bg="#209290",relief=RIDGE,bd=15)
F1.place(x=5,y=90,width=800,height=500)
#=========================headings==========================================================================================================
itm=Label(F1,text="Items",font=("Helvetic",25,"bold","underline"),fg="black")
itm.grid(row=0,column=0,padx=20,pady=15)

n=Label(F1,text="Number of items",font=("Helvetic",25,"bold","underline"),fg="black")
n.grid(row=0,column=1,padx=20,pady=15)

cost=Label(F1,text=" Cost of items",font=("Helvetic",25,"bold","underline"),fg="black")
cost.grid(row=0,column=2,padx=20,pady=15)

#================product===================
bread=Label(F1,text="Bread",font=("times new romman",20,"bold"),fg="black",bg="#209290")
bread.grid(row=1,column=0,padx=20,pady=15)

b_txt=Entry(F1,font="arial 15 bold",relief=SUNKEN,bd=7,justify=CENTER,textvariable=Bread)
b_txt.grid(row=1,column=1,padx=20,pady=15)

cb_txt=Entry(F1,font="arial 15 bold",relief=SUNKEN,bd=7,justify=CENTER,textvariable=cd)
cb_txt.grid(row=1,column=2,padx=20,pady=15)

wine=Label(F1,text="Wine",font=("times new romman",20,"bold"),fg="black",bg="#209290")
wine.grid(row=2,column=0,padx=20,pady=15)


db_txt=Entry(F1,font="arial 15 bold",relief=SUNKEN,bd=7,justify=CENTER,textvariable=Wine)
db_txt.grid(row=2,column=1,padx=20,pady=15)

lb_txt=Entry(F1,font="arial 15 bold",relief=SUNKEN,bd=7,justify=CENTER,textvariable=cw)
lb_txt.grid(row=2,column=2,padx=20,pady=15)

cake=Label(F1,text="Cake",font=("times new romman",20,"bold"),fg="black",bg="#209290")
cake.grid(row=3,column=0,padx=20,pady=15)


db_txt=Entry(F1,font="arial 15 bold",relief=SUNKEN,bd=7,justify=CENTER,textvariable=Cake)
db_txt.grid(row=3,column=1,padx=20,pady=15)

lb_txt=Entry(F1,font="arial 15 bold",relief=SUNKEN,bd=7,justify=CENTER,textvariable=cr)
lb_txt.grid(row=3,column=2,padx=20,pady=15)

ice_cream=Label(F1,text="Ice Cream",font=("times new romman",20,"bold"),fg="black",bg="#209290")
ice_cream.grid(row=4,column=0,padx=20,pady=15)


db_txt=Entry(F1,font="arial 15 bold",relief=SUNKEN,bd=7,justify=CENTER,textvariable=Ice_Cream)
db_txt.grid(row=4,column=1,padx=20,pady=15)

lb_txt=Entry(F1,font="arial 15 bold",relief=SUNKEN,bd=7,justify=CENTER,textvariable=cm)
lb_txt.grid(row=4,column=2,padx=20,pady=15)

t=Label(F1,text="Total price",font=("times new romman",20,"bold"),fg="black",bg="#209290")
t.grid(row=6,column=0,padx=20,pady=15)

db_txt=Entry(F1,font="arial 15 bold",relief=SUNKEN,bd=7,justify=CENTER,textvariable=total)
db_txt.grid(row=6,column=1,padx=20,pady=15)

lb_txt=Entry(F1,font="arial 15 bold",relief=SUNKEN,bd=7,justify=CENTER,textvariable=total_cost)
lb_txt.grid(row=6,column=2,padx=20,pady=15)



#==============billing area================================================================================

F2=Frame(root,relief=GROOVE,bd=10)
F2.place(x=820,y=90,width=430,height=500)
bill_title=Label(F2,text="receipt",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
scroll=Scrollbar(F2,orient=VERTICAL)
scroll.pack(side=RIGHT,fill=Y)
textarea=Text(F2,font="arial 15 bold",yscrollcommand=scroll.set)
textarea.pack(fill=BOTH)
scroll.config(command=textarea.yview)
#===================BUTTON======================================================================================

F3=Frame(root,relief=GROOVE,bd=10)
F3.place(x=5,y=590,width=1270,height=120)
btn1=Button(F3,text="Total",font="arial 25 bold",bg="yellow",fg="crimson",padx=5,pady=5,width=10,command=Total)
btn1.grid(row=0,column=0,padx=10,pady=10)

btn2=Button(F3,text="Receipt",font="arial 25 bold",bg="yellow",fg="crimson",padx=5,pady=5,width=10)
btn2.grid(row=0,column=1,padx=10,pady=10)

btn3=Button(F3,text="Print",font="arial 25 bold",bg="yellow",fg="crimson",padx=5,pady=5,width=10)
btn3.grid(row=0,column=2,padx=10,pady=10)


btn4=Button(F3,text="Reset",font="arial 25 bold",bg="yellow",fg="crimson",padx=5,pady=5,width=10)
btn4.grid(row=0,column=3,padx=10,pady=10)


btn5=Button(F3,text="Exit",font="arial 25 bold",bg="yellow",fg="crimson",padx=5,pady=5,width=10)
btn5.grid(row=0,column=4,padx=10,pady=10)

root.mainloop()
