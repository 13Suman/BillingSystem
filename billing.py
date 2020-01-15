from tkinter import*
import math,random
class billing_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing System")
        bg_color = "#b23884"
        title = Label(self.root,text="Billing System", bd=12,relief=GROOVE, bg=bg_color,fg="white", font=("times new roman",30,"bold"), pady=2).pack(fill=X)

        ##############Variables#############

           #########Cosmetics#########
        self.soap=IntVar()
        self.lotion=IntVar()
        self.shampoo=IntVar()
        self.gel=IntVar()
        self.perfume=IntVar()
        self.sunscreen=IntVar()
          #########Grocery###########
        self.dal=IntVar()
        self.rice=IntVar()
        self.namkeen=IntVar()
        self.biscuit=IntVar()
        self.maggi=IntVar()
        self.chocolate=IntVar()
          ##########Dresses###########
        self.top=IntVar()
        self.jeans=IntVar()
        self.ctop=IntVar()
        self.saree=IntVar()
        self.kurti=IntVar()
        self.culottes=IntVar()
          #########Product price & tax variables##########
        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.dress_price=StringVar()

        self.cosmetic_tax=StringVar()
        self.grocery_tax=StringVar()
        self.dress_tax=StringVar()

        self.c_name=StringVar()
        self.c_phone=StringVar()
        x=random.randint(1000,9999)
        self.bill_no=StringVar()
        self.bill_no.set(str(x))
        self.search_bill=StringVar()

         ######Customer Details######
        F1 = LabelFrame(self.root,text="Customer Details",bd=10, relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)

        custname_lbl = Label(F1,text="Customer Name",bg=bg_color,fg="white", font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        custname_txt = Entry(F1,width=20,textvariable=self.c_name, font="arial 15",bd=7,relief=SUNKEN).grid(row=0, column=1, padx=10, pady=5)

        custphone_lbl = Label(F1, text="Phone No.", bg=bg_color, fg="white",font=("times new roman", 18, "bold")).grid(row=0, column=2, padx=20, pady=5)
        custphone_txt = Entry(F1, width=20,textvariable= self.c_phone, font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=3, padx=10, pady=5)

        custbill_lbl = Label(F1, text="Bill Number", bg=bg_color, fg="white",font=("times new roman", 18, "bold")).grid(row=0, column=4, padx=20, pady=5)
        custbill_txt = Entry(F1, width=20,textvariable= self.search_bill, font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=5, padx=10, pady=5)

        bill_btn = Button(F1, text="Search", width=10, bd=7, font="arial 12 bold").grid(row=0, column=6, padx=10, pady=10)

        ##########Cosmetics Frame###########
        F2 = LabelFrame(self.root, text="Cosmetics", bd=10, relief=GROOVE, font=("times new roman", 15, "bold"),fg="gold", bg=bg_color)
        F2.place(x=5, y=180, width=325, height=380)

        bath_label = Label(F2, text="Bath Soap", font=("times new roman", 16, "bold"),bg=bg_color, fg="light green").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        bath_txt = Entry(F2, width=10,textvariable= self.soap, font=("times new roman", 16, "bold"),bd=5, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        lotion_label = Label(F2, text="Lotion", font=("times new roman", 16, "bold"), bg=bg_color,fg="light green").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        lotion_txt = Entry(F2, width=10,textvariable= self.lotion, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1,padx=10, pady=10)

        shampoo_label = Label(F2, text="Shampoo", font=("times new roman", 16, "bold"), bg=bg_color,fg="light green").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        shampoo_txt = Entry(F2, width=10,textvariable= self.shampoo, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1,padx=10, pady=10)

        perfume_label = Label(F2, text="Perfume", font=("times new roman", 16, "bold"), bg=bg_color,fg="light green").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        perfume_txt = Entry(F2, width=10,textvariable=self.perfume, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=1,padx=10, pady=10)

        hair_gel_label = Label(F2, text="Hair Gel", font=("times new roman", 16, "bold"), bg=bg_color, fg="light green").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        hair_gel_txt = Entry(F2, width=10,textvariable=self.gel, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=1,padx=10, pady=10)

        sunscreen_label = Label(F2, text="Sunscreen", font=("times new roman", 16, "bold"), bg=bg_color,fg="light green").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        sunscreen_txt = Entry(F2, width=10,textvariable=self.sunscreen, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1,padx=10, pady=10)

        ##########Grocery Frame###########
        F3 = LabelFrame(self.root, text="Grocery", bd=10, relief=GROOVE, font=("times new roman", 15, "bold"),fg="gold", bg=bg_color)
        F3.place(x=340, y=180, width=325, height=380)

        daal_label = Label(F3, text="Daal", font=("times new roman", 16, "bold"), bg=bg_color,fg="light green").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        daal_txt = Entry(F3, width=10,textvariable= self.dal, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1,padx=10, pady=10)

        rice_label = Label(F3, text="Rice", font=("times new roman", 16, "bold"), bg=bg_color,fg="light green").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        rice_txt = Entry(F3, width=10,textvariable=self.rice, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        namkeen_label = Label(F3, text="Namkeen", font=("times new roman", 16, "bold"), bg=bg_color,fg="light green").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        namkeen_txt = Entry(F3, width=10,textvariable=self.namkeen, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2,column=1, padx=10,pady=10)

        biscuits_label = Label(F3, text="Biscuits", font=("times new roman", 16, "bold"), bg=bg_color,fg="light green").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        biscuits_txt = Entry(F3, width=10,textvariable=self.biscuit, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3,  column=1, padx=10,pady=10)

        maggi_label = Label(F3, text="Maggi", font=("times new roman", 16, "bold"), bg=bg_color,fg="light green").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        maggi_gel_txt = Entry(F3, width=10,textvariable=self.maggi, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        chocolates_label = Label(F3, text="Chocolates", font=("times new roman", 16, "bold"), bg=bg_color,fg="light green").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        chocolates_txt = Entry(F3, width=10,textvariable=self.chocolate, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        ##########Dresses Frame###########
        F4 = LabelFrame(self.root, text="Dresses", bd=10, relief=GROOVE, font=("times new roman", 15, "bold"),fg="gold", bg=bg_color)
        F4.place(x=670, y=180, width=325, height=380)

        top_label = Label(F4, text="Top", font=("times new roman", 16, "bold"), bg=bg_color, fg="light green").grid( row=0, column=0, padx=10, pady=10, sticky="w")
        top_txt = Entry(F4, width=10,textvariable=self.top, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1,padx=10, pady=10)

        jeans_label = Label(F4, text="Jeans", font=("times new roman", 16, "bold"), bg=bg_color, fg="light green").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        jeans_txt = Entry(F4, width=10,textvariable=self.jeans, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1,padx=10, pady=10)

        croptop_label = Label(F4, text="Crop Top", font=("times new roman", 16, "bold"), bg=bg_color, fg="light green").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        croptop_txt = Entry(F4, width=10,textvariable=self.ctop, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2,column=1,padx=10, pady=10)

        saree_label = Label(F4, text="Saree", font=("times new roman", 16, "bold"), bg=bg_color,fg="light green").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        saree_txt = Entry(F4, width=10,textvariable=self.saree, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        kurti_label = Label(F4, text="kurti", font=("times new roman", 16, "bold"), bg=bg_color, fg="light green").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        kurti_gel_txt = Entry(F4, width=10,textvariable=self.kurti, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        culottes_label = Label(F4, text="Culottes", font=("times new roman", 16, "bold"), bg=bg_color,fg="light green").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        culottes_txt = Entry(F4, width=10,textvariable=self.culottes, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1,padx=10,pady=10)

        ############Billing Corner############
        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=1005, y=180, width=350, height=380)
        bill_title = Label(F5,text="Bill Corner", font="arial 15 bold", bd=7, relief=GROOVE).pack(fill=X)
        scroll_y = Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        ###############Button Frame##################
        F6 = LabelFrame(self.root, text="Billing Menu", bd=10, relief=GROOVE, font=("times new roman", 15, "bold"), fg="gold", bg=bg_color)
        F6.place(x=0, y=560, relwidth=1, height=140)

        s1_lbl=Label(F6,text="Total Cosmetic Amount",bg=bg_color, fg="white",font=("times new roman", 14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        s1_txt=Entry(F6, width=18,textvariable=self.cosmetic_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=0,column=1, padx=1, pady=1)

        s2_lbl = Label(F6, text="Total Grocery Amount", bg=bg_color, fg="white",font=("times new roman", 14, "bold")).grid(row=1, column=0, padx=20, pady=1, sticky="w")
        s2_txt = Entry(F6, width=18,textvariable=self.grocery_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=1, column=1, padx=1, pady=1)

        s3_lbl = Label(F6, text="Total Dress Amount", bg=bg_color, fg="white",font=("times new roman", 14, "bold")).grid(row=2, column=0, padx=20, pady=1, sticky="w")
        s3_txt = Entry(F6, width=18,textvariable=self.dress_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=2, column=1, padx=1, pady=1)

        s4_lbl = Label(F6, text="Cosmetic Tax", bg=bg_color, fg="white",font=("times new roman", 14, "bold")).grid(row=0, column=2, padx=20, pady=1, sticky="w")
        s4_txt = Entry(F6, width=18,textvariable=self.cosmetic_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=0, column=3, padx=1, pady=1)

        s5_lbl = Label(F6, text="Grocery Tax", bg=bg_color, fg="white",font=("times new roman", 14, "bold")).grid(row=1, column=2, padx=20, pady=1, sticky="w")
        s5_txt = Entry(F6, width=18,textvariable=self.grocery_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=1, column=3, padx=1, pady=1)

        s6_lbl = Label(F6, text="Dresses Tax", bg=bg_color, fg="white",font=("times new roman", 14, "bold")).grid(row=2, column=2, padx=20, pady=1, sticky="w")
        s6_txt = Entry(F6, width=18,textvariable=self.dress_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=2, column=3, padx=1, pady=1)

        btn_F=Frame(F6,bd=7,relief=GROOVE,)
        btn_F.place(x=750,width=580,height=105)

        total_btn = Button(btn_F,command=self.total,text="Total",  bg="cadetblue",fg="white",  bd=2, pady=15,  width=10,font="arial 12 bold").grid(row=0,column=0,padx=5,pady=5)
        gen_Bill_btn = Button(btn_F,command=self.bill_area, text="Generate Bill", bg="cadetblue", fg="white", bd=2, pady=20, width=15,font="arial 12 bold").grid(row=0, column=1, padx=5, pady=10)
        clear_btn = Button(btn_F, text="Clear", bg="cadetblue", fg="white", bd=2, pady=15, width=10,font="arial 12 bold").grid(row=0, column=2, padx=5, pady=5)
        exit_btn = Button(btn_F, text="Exit", bg="cadetblue", fg="white", bd=2, pady=15, width=10,font="arial 12 bold").grid(row=0, column=3, padx=5, pady=5)
        self.welcome_bill()

    def total(self):
        self.cs_soap=self.soap.get()*20
        self.cs_gel=self.gel.get()*90
        self.cs_shampoo=self.shampoo.get()*100
        self.cs_perfume=self.perfume.get()*110
        self.cs_lotion= self.lotion.get()*60
        self.cs_sunscreen=self.sunscreen.get()*120

        self.total_cosmetic_price=float(
                                    self.cs_soap+
                                    self.cs_gel+
                                    self.cs_shampoo+
                                    self.cs_perfume+
                                    self.cs_lotion+
                                    self.cs_sunscreen
                                       )
        self.cosmetic_price.set("Rs. " +str(self.total_cosmetic_price))
        self.cosmetic_tax.set("Rs. " +str(round((self.total_cosmetic_price*0.05),2)))

        self.gr_daal=self.dal.get() * 20
        self.gr_rice =self.rice.get() * 100
        self.gr_namkeen =self.namkeen.get() * 90
        self.gr_biscuit =self.biscuit.get() * 110
        self.gr_maggi =self.maggi.get() * 60
        self.gr_chocolate =self.chocolate.get() * 120

        self.total_grocery_price = float(
                                     self.gr_daal+
                                     self.gr_rice+
                                     self.gr_namkeen+
                                     self.gr_biscuit+
                                     self.gr_maggi+
                                     self.gr_chocolate
                                        )
        self.grocery_price.set("Rs. " +str(self.total_grocery_price))
        self.grocery_tax.set("Rs. " + str(round((self.total_grocery_price * 0.1), 2)))

        self.dr_top=self.top.get() * 200
        self.dr_jeans =self.jeans.get() * 1000
        self.dr_ctop =self.ctop.get() * 190
        self.dr_culottes =self.culottes.get() * 520
        self.dr_saree =self.saree.get() * 1110
        self.dr_kurti =self.kurti.get() * 560

        self.total_dress_price = float(
                                    self.dr_top+
                                    self.dr_jeans+
                                    self.dr_ctop+
                                    self.dr_culottes+
                                    self.dr_saree+
                                    self.dr_kurti
                                      )
        self.dress_price.set("Rs. " +str(self.total_dress_price))
        self.dress_tax.set("Rs. " + str(round((self.total_dress_price * 0.05), 2)))

    def welcome_bill(self):
        a = (self.bill_no.get())
        b = (self.c_name.get())
        c = (self.c_phone.get())
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\t     Welcome \n")
        self.txtarea.insert(END, "\n Bill Number : {}".format(a))
        self.txtarea.insert(END, "\n Customer Name: {}".format(b))
        self.txtarea.insert(END, "\n Customer Phone: {}".format(c))
        self.txtarea.insert(END, "\n ******************************************")
        self.txtarea.insert(END, "\n Products\t\tQty\t\tPrice ")
        self.txtarea.insert(END, "\n ******************************************")
    def bill_area(self):
        d=(self.soap.get())
        self.welcome_bill()
        if self.soap.get()!=0:
             self.txtarea.insert(END, "\n Bath Soap\t\t{}".format(d))
root = Tk()
obj = billing_App(root)
root.mainloop()



