import tkinter
import mysql.connector
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Treeview
from tkinter import messagebox
from PIL import Image, ImageTk


db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="bmh204"
)
mycursor = db.cursor()


def login():

    if Eku.get() == "" or Esif.get() == "":
        messagebox.showerror("Hata", "Kullanıcı Veya Şifrenizi Kontrol Ediniz")
    else:
        try:
            mycursor.execute("select * from Maykod where tc ='%s' and sifre = %s " % (Eku.get(), Esif.get()))
            row = mycursor.fetchone()

            if row == None:
                messagebox.showerror("Hata", "Kullanıcı Veya Şifrenizi Kontrol Ediniz")
            else:
                formgiris.destroy()
                giris()

        except EXCEPTION as es:
            messagebox.showerror("Hata", f"Kullanıcı Veya Şifrenizi Kontrol Ediniz:{str(es)}")
    db.commit()


def giris():
    anasayfa()


def admin():
    def admingir():
        if aku.get() == "" or asif.get() == "":
            messagebox.showerror("Hata", "Kullanıcı Veya Şifrenizi Kontrol Ediniz")
        elif aku.get() != "a" or asif.get() != "1":
            messagebox.showerror("Hata", "Kullanıcı Veya Şifrenizi Kontrol Ediniz")
        else:
            Login()
            admin.destroy()

    admin = Toplevel()
    admin.title("Yetkili  Formu")
    admin.geometry('600x400')

    my_picet = Image.open("adminbg.jpg")
    resized = my_picet.resize((600, 400), Image.ANTIALIAS)
    new_picet = ImageTk.PhotoImage(resized)
    my_laben = Label(admin, image=new_picet)
    my_laben.place(x=0, y=0)

    frame1 = Frame(admin, bg="#e53c09")
    frame1.place(relx=0.2, rely=0.15, relwidth=0.6, relheight=0.2)
    cv = Canvas(admin, bg='white', width=420, height=200)
    cv.place(x=100, y=100)
    yetki = Label(admin, text="Admin Panel Login", fg="black", bg="#e53c09", font="Times 18 italic").place(x=130, y=65)
    aku = Label(admin, text="Kullanıcı Adı:", fg="black", bg="white", font="Times 22 italic").place(x=150, y=100)
    aku = Entry(admin, bd=1, width=25)
    aku.place(x=150, y=150)
    asif = Label(admin, text="Şifre :", fg="black", bg="white", font="Times 22 italic").place(x=150, y=190)
    asif = Entry(admin, bd=1, width=25)
    asif.place(x=150, y=250)
    Kaydet = Button(admin, text="Giriş Yap", fg="Blue", bg="white", font="Times 22 italic", command=admingir)
    Kaydet.place(x=180, y=280)
    admin.mainloop()


def anasayfa():
    ana = Tk()
    ana.title('MAYKOD ANASAYFA')
    ana.geometry('1550x900')

    def yonetim():
        top = Toplevel()
        top.geometry('1000x1000')
        top.title('Yönetim Ekibi')
        top.iconbitmap("maykod.ico")
        cmy = Canvas(top, width=1000, height=1000)
        L1 = Label(top, text="YÖNETİM EKİBİ", bg="#00bcdd", font="Times 45 ").place(x=150, y=40)
        img = PhotoImage(file="ybg.png")
        my_image = cmy.create_image(0, 0, anchor=NW, image=img)

        cmy.create_rectangle(1550, 120, 0, 20, fill='#00bcdd')
        cmy.pack()

        photo12 = PhotoImage(file='maykod.png')
        photoRezised12 = photo12.subsample(2, 2)
        cmy.create_image(75, 100, image=photoRezised12)

        photo22 = PhotoImage(file='mşü1.png')
        photoRezised22 = photo22.subsample(2, 2)
        cmy.create_image(900, 100, image=photoRezised22)

        frame1 = Frame(top, bg="#1608d6")
        frame1.place(relx=0.35, rely=0.1, relwidth=0.25, relheight=0.18)

        frame2 = Frame(top, bg="#1608d6")
        frame2.place(relx=0.15, rely=0.3, relwidth=0.18, relheight=0.18)

        frame3 = Frame(top, bg="#1608d6")
        frame3.place(relx=0.55, rely=0.3, relwidth=0.18, relheight=0.18)

        frame4 = Frame(top, bg="#1608d6")
        frame4.place(relx=0.15, rely=0.55, relwidth=0.18, relheight=0.18)

        frame5 = Frame(top, bg="#1608d6")
        frame5.place(relx=0.55, rely=0.55, relwidth=0.18, relheight=0.18)

        frame6 = Frame(top, bg="#1608d6")
        frame6.place(relx=0.05, rely=0.75, relwidth=0.18, relheight=0.18)

        frame7 = Frame(top, bg="#1608d6")
        frame7.place(relx=0.35, rely=0.75, relwidth=0.18, relheight=0.18)

        frame8 = Frame(top, bg="#1608d6")
        frame8.place(relx=0.65, rely=0.75, relwidth=0.18, relheight=0.18)

        photo = PhotoImage(frame1, file='pp.png')
        photoRezised = photo.subsample(4, 4)
        cmy.create_image(480, 250, image=photoRezised)
        lbl=Label(top,text="Mehmet Can ARSLAN \n MAYKOD Başkanı", font="Comic 13 italic")
        lbl.place(x=370, y=320)

        photo2 = PhotoImage(frame2, file='esra.png')
        photoRezised2 = photo2.subsample(2, 2)
        cmy.create_image(250, 450, image=photoRezised2)
        lbl = Label(top, text="Esra YILDIRIM \n MAYKOD Başkan Yardımcısı", font="Comic 13 italic")
        lbl.place(x=140, y=505)

        photo3 = PhotoImage(frame3, file='Volkan.png')
        photoRezised3 = photo3.subsample(2, 2)
        cmy.create_image(700, 450, image=photoRezised3)
        lbl = Label(top, text="Volkan AKGÖL \n MAYKOD Başkan Yardımcısı", font="Comic 13 italic")
        lbl.place(x=590, y=505)

        photo4 = PhotoImage(frame4, file='merve.png')
        photoRezised4 = photo4.subsample(2, 2)
        cmy.create_image(250, 650, image=photoRezised4)
        lbl = Label(top, text="Merve OT \n MAYKOD Yazman", font="Comic 13 italic")
        lbl.place(x=140, y=705)

        photo5 = PhotoImage(frame5, file='beyda.png')
        photoRezised5= photo5.subsample(3, 3)
        cmy.create_image(700, 650, image=photoRezised5)
        lbl = Label(top, text="Beyda ÇETİN \n MAYKOD Sayman", font="Comic 13 italic")
        lbl.place(x=590, y=705)

        photo6 = PhotoImage(frame6, file='alper.png')
        photoRezised6 = photo6.subsample(2, 2)
        cmy.create_image(150, 850, image=photoRezised6)
        lbl = Label(top, text="Alper KOÇAK \n Kurucu Üye", font="Comic 13 italic")
        lbl.place(x=80, y=905)

        photo7 = PhotoImage(frame7, file='neşe.png')
        photoRezised7 = photo7.subsample(2, 2)
        cmy.create_image(460, 850, image=photoRezised7)
        lbl = Label(top, text="Neşe VUROL \n MAYKOD Sekteteri", font="Comic 13 italic")
        lbl.place(x=350, y=905)

        photo8 = PhotoImage(frame8, file='eda.png')
        photoRezised8 = photo8.subsample(2, 2)
        cmy.create_image(830, 850, image=photoRezised8)
        lbl = Label(top, text="Edanur TAŞÇI \n Denetleme Kurul Üyesi", font="Comic 13 italic")
        lbl.place(x=720, y=905)


        top.mainloop()

    def iletisim():
        ilet = Toplevel()
        ilet.geometry('1000x900')
        ilet.title('Yönetim Ekibi')
        ilet.iconbitmap("maykod.ico")

        cv = Canvas(ilet, bg='white', width=10000, height=10000)
        cv.pack()
        cv.create_rectangle(1550, 120, 0, 20, fill='#00bcdd')

        img = PhotoImage(file="ana.png")
        my_image = cv.create_image(0, 0, anchor=NW, image=img)

        photo7 = PhotoImage(file='mşü1.png')
        photoRezised7 = photo7.subsample(2, 2)
        cv.create_image(900, 100, image=photoRezised7)

        photo = PhotoImage(file='mail.png')
        photoRezised = photo.subsample(3, 3)
        cv.create_image(65, 400, image=photoRezised)

        photo6 = PhotoImage(file='maykod.png')
        photoRezised6 = photo6.subsample(2, 2)
        cv.create_image(75, 100, image=photoRezised6)

        photo5 = PhotoImage(file='okul.png')
        photoRezised5 = photo5.subsample(6, 6)
        cv.create_image(65, 500, image=photoRezised5)

        photo2 = PhotoImage(file="twiter.png")
        photoRezised2 = photo2.subsample(12, 12)
        cv.create_image(65, 720, image=photoRezised2)

        photo3 = PhotoImage(file="insta.png")
        photoRezised3 = photo3.subsample(12, 12)
        cv.create_image(65, 632, image=photoRezised3)

        photo4 = PhotoImage(file="tel.png")
        photoRezised4 = photo4.subsample(5, 5)
        cv.create_image(65, 825, image=photoRezised4)

        frame1 = Frame(ilet, bg="#1608d6")
        frame1.place(relx=0.07, rely=0.2, relwidth=0.8, relheight=0.05)

        L1 = Label(ilet,  text="İLETİŞİM", bg="white", font="Times 45 ").place(x=150, y=40)
        Lf1 = Label(ilet, text="MUŞ ALPARSLAN ÜNİVERSİTESİ YAZILIM KULÜBÜ", bg="#1608d6", fg="white", font="Comic 20 italic").place(x=145, y=180)
        Lf2 = Label(ilet, text="E-MAİL Adresi:", bg="#0d0075", fg="white",font="Comic 20 italic").place(x=150, y=380)
        Lf2yan = Label(ilet, text="maykod@alparslan.edu.tr", bg="#0d0075",fg="white", font="Comic 20 italic").place(x=600, y=380)
        Lf3 = Label(ilet, text="Muş Alparslan Üniversitesi", bg="#0d0075",fg="white", font="Comic 20 italic").place(x=150, y=450)
        Lf3yan = Label(ilet, text="https://www.alparslan.edu.tr/tr", bg="#0d0075",fg="white",  font="Comic 20 italic").place(x=600, y=450)
        Lbu = Label(ilet, text="Bize Ulaşın", bg="#0d0075",fg="white", font="Times 30 italic").place(x=150, y=500)

        Lf4 = Label(ilet, text="Instagram adresimiz:", bg="#0d0075", fg="white",font="Comic 20 italic").place(x=150, y=600)
        Lf4yan = Label(ilet, text="maykodmsu", bg="#0d0075",  fg="white",font="Comic 20 italic").place(x=600, y=600)

        Lf5 = Label(ilet, text="twitter adresimiz:", bg="#0d0075", fg="white",font="Comic 20 italic").place(x=150, y=700)
        Lf5yan = Label(ilet, text="@MaykodMSU", bg="#0d0075", fg="white",font="Comic 20 italic").place(x=600, y=700)

        Lf6 = Label(ilet, text="Yönetici tel:", bg="#0d0075", fg="white",font="Comic 20 italic").place(x=150, y=800)
        Lf6yan = Label(ilet, text="0 (545) 720 28 66", fg="white",bg="#0d0075", font="Comic 20 italic").place(x=600, y=800)






        ilet.mainloop()

    def hakkında():
        root = Toplevel()
        root.geometry("1100x1000")
        mycanvas = Canvas(root, bg="white", width=1100, height=1000)
        mycanvas.create_rectangle(1550, 120, 0, 0, fill='#00bcdd')
        mlabel = Label(mycanvas, text="KULÜP FAALİYETLERİMİZ", bg="#00bcdd", font="Times 35 ").place(x=150, y=40)
        mycanvas.pack()

        photo1 = PhotoImage(file='maykod.png')
        photoRezised1 = photo1.subsample(2, 2)
        mycanvas.create_image(75, 100, image=photoRezised1)

        photo2 = PhotoImage(file='mşü1.png')
        photoRezised2 = photo2.subsample(2, 2)
        mycanvas.create_image(1000, 100, image=photoRezised2)

        root.mainloop()

    canvas = Canvas(ana, width=1550, height=900)
    image = ImageTk.PhotoImage(Image.open("ana.png"))
    canvas.create_image(0, 0, anchor=NW, image=image)
    canvas.pack()
    canvas.create_rectangle(1550, 120, 0, 20, fill='#00bcdd')

    my_picet = Image.open("mşü.png")
    resized = my_picet.resize((1349, 124), Image.ANTIALIAS)
    new_picet = ImageTk.PhotoImage(resized)
    my_laben = Label(image=new_picet)
    my_laben.place(x=100, y=750)

    AnaSayfa = Button(ana, text="Anasayfa", bg='#00bcdd', borderwidth='0', fg='#00007f', font="Times 20 italic")
    AnaSayfa.place(x=320, y=50)
    Kulup = Button(ana, text="Kulüp", bg='#00bcdd', borderwidth='0', fg='#00007f', font="Times 20 italic", command=hakkında)
    Kulup.place(x=500, y=50)
    yonet = Button(ana, text="Yönetim", bg='#00bcdd', borderwidth='0', fg='#00007f', font="Times 20 italic", command=yonetim)
    yonet.place(x=650, y=50)
    foto = Button(ana, text="Fotoğraf Galerisi", bg='#00bcdd', borderwidth='0', fg='#00007f', font="Times 20 italic")
    foto.place(x=800, y=50)
    iletisim = Button(ana, text="İletişim", bg='#00bcdd', borderwidth='0', fg='#00007f', font="Times 20 italic", command=iletisim)
    iletisim.place(x=1050, y=50)
    my_pice = Image.open("maykod.png")
    resized = my_pice.resize((130, 130), Image.ANTIALIAS)
    new_pice = ImageTk.PhotoImage(resized)
    my_laben = Label(image=new_pice)
    my_laben.place(x=50, y=50)

    my_pic = Image.open("mşü2.png")
    resized = my_pic.resize((130, 130), Image.ANTIALIAS)
    new_pic = ImageTk.PhotoImage(resized)
    my_labe = Label(image=new_pic)
    my_labe.place(x=1370, y=50)

    my_picen = Image.open("admin.png")
    resized = my_picen.resize((90, 60), Image.ANTIALIAS)
    new_picen = ImageTk.PhotoImage(resized)
    Admin = Button(image=new_picen, text="Giriş", fg="red", borderwidth='0', bg='#00007f', command=admin, font="arial 25")
    Admin.place(x=1225, y=40)

    my_ana = Image.open("s1.png")
    resizedana = my_ana.resize((1124, 400), Image.ANTIALIAS)
    new_picana = ImageTk.PhotoImage(resizedana)
    my_labeana = Label(image=new_picana)
    my_labeana.place(x=250, y=250)




    def icice():
        messagebox.showinfo("aliş")

    menu = Menu(ana)
    ana.config(menu=menu)

    def quit():
        ana.destroy()
    subMenu = Menu(menu)

    menu.add_cascade(label="File", font="Times 20", menu=subMenu)
    subMenu.add_command(label="Admin", font="Times 13", command=admin)
    subMenu.add_command(label="Destek", font="Times 13", command=icice)
    subMenu.add_separator()
    subMenu.add_command(label="EXIT", font="Times 13", command=quit)
    ana.mainloop()


formgiris = Tk()
formgiris.title('MAYKOD')
formgiris.geometry('1600x650')
formgiris.iconbitmap('maykod.ico')
canvas = Canvas(formgiris, width=5000, height=5000, bg="white")
canvas.pack()
frame_orta=Frame(formgiris, bg="yellow")
frame_orta.place(relx=0.427, rely=0, relwidth=0.005, relheight=1)
my_picet = Image.open("yen3.jpg")
resized = my_picet.resize((900, 650), Image.ANTIALIAS)
new_picet = ImageTk.PhotoImage(resized)
my_laben = Label(image=new_picet)
my_laben.place(x=690, y=0)



def kayitolma():

    kayitol = Toplevel()
    kayitol.title("Kayıt Olma Formu")
    kayitol.geometry('1600x566')

    canvasa = Canvas(kayitol, width=5000, height=5000, bg="white")
    canvasa.pack()
    img = PhotoImage(file="yen3.png")
    my_image = canvasa.create_image(0, 0, anchor=NW, image=img)

    frame_orta = Frame(kayitol, bg="yellow")
    frame_orta.place(relx=0.485, rely=0, relwidth=0.005, relheight=1)

    formgiris.withdraw()
    def kaydet():
        if (etck.get() == "" or esifre.get() == "" or eadi.get() == "" or esoyadi.get() == "" or eemail.get() == "" or eil.get() == "" or eilce.get() == "" or ebolum.get() == ""):
            messagebox.showerror("Hata", "Lütfen Bütün Alanları Doldurun")
        else:
            try:
                mycursor.execute("INSERT INTO Maykod (tc,sifre,adi,soyadi,email,il,ilce,bolum) VALUES " \
                                 "('%s','%s','%s','%s','%s','%s','%s','%s')" % (
                                    etck.get(), esifre.get(), eadi.get(), esoyadi.get(), eemail.get(), eil.get(),
                                    eilce.get(), ebolum.get()))

                messagebox.showinfo("Durum", "Kaydınız Başarıyla Tamamlanmıştır")
                formgiris.deiconify()
                kayitol.destroy()
                db.commit()
            except EXCEPTION as es:
                messagebox.showerror("Hata", f"Boş alanları kontrol ediniz:{str(es)}")


    def geri():
        formgiris.deiconify()
        kayitol.destroy()

    tck = Label(kayitol, text=" Kullanıcı Adı:", fg="black", bg="white", font="Times 20 italic").place(x=1000, y=80)
    etck = Entry(kayitol, bd=1, width=25)
    etck.place(x=1280, y=80)

    lsifre = Label(kayitol, text="Şifre :", fg="black", bg="white", font="Times 20 italic").place(x=1090, y=120)
    esifre = Entry(kayitol, bd=1, width=25)
    esifre.place(x=1280, y=120)

    ladi = Label(kayitol, text="Adı :", fg="black", bg="white", font="Times 20 italic").place(x=1100, y=160)
    eadi = Entry(kayitol, bd=1, width=25)
    eadi.place(x=1280, y=160)

    lsoyadi = Label(kayitol, text="Soyadi :", fg="black", bg="white", font="Times 20 italic").place(x=1060, y=200)
    esoyadi = Entry(kayitol, bd=1, width=25)
    esoyadi.place(x=1280, y=200)

    lemail = Label(kayitol, text="Email :", fg="black", bg="white", font="Times 20 italic").place(x=1070, y=240)
    eemail = Entry(kayitol, bd=1, width=25)
    eemail.place(x=1280, y=240)

    lil = Label(kayitol, text="İL :", fg="black", bg="white", font="Times 20 italic").place(x=1070, y=280)
    eil = Entry(kayitol, bd=1, width=25)
    eil.place(x=1280, y=280)

    lilce = Label(kayitol, text="İlçe :", fg="black", bg="white", font="Times 20 italic").place(x=1070, y=320)
    eilce = Entry(kayitol, bd=1, width=25)
    eilce.place(x=1280, y=320)

    lbolum = Label(kayitol, text="Bölüm :", fg="black", bg="white", font="Times 20 italic").place(x=1070, y=360)
    ebolum = Entry(kayitol, bd=1, width=25)
    ebolum.place(x=1280, y=360)

    Kaydet = Button(kayitol, text="Kaydol", fg="black", bg="white", font="Times 20 italic", command=kaydet)
    Kaydet.place(x=1280, y=400)

    geri = Button(kayitol, text="Geri Dön", fg="black", bg="white", font="Times 20 italic", command=geri)
    geri.place(x=1400, y=400)
    kayitol.mainloop()


def Login():
    def listele():
        liste.delete(*liste.get_children())
        mycursor.execute('select * from Maykod')
        results = mycursor.fetchall()
        for row in results:
            sifre = row[2]
            adi = row[3]
            soyadi = row[4]
            email = row[5]
            il = row[6]
            ilce = row[7]
            bolum = row[8]
            liste.insert("", 0, text=row[0], values=(row[1], sifre, adi, soyadi, email, il, ilce, bolum))

    def ekle():
        mycursor.execute("INSERT INTO Maykod (tc,sifre,adi,soyadi,email,il,ilce,bolum) VALUES "\
                         "('%s','%s','%s','%s','%s','%s','%s','%s')" % (
                         Etc.get(), Esif.get(), Ead.get(), Esad.get(), Email.get(), Eil.get(), Eilce.get(), Ebolum.get()))
        db.commit()
        listele()

    def guncelle():
        mycursor.execute("UPDATE Maykod SET tc='%s',sifre='%s',adi='%s',soyadi='%s',email='%s',il='%s',ilce='%s',bolum='%s'" \
                         " WHERE id='%s'" % (Etc.get(), Esif.get(), Ead.get(), Esad.get(), Email.get(), Eil.get(), Eilce.get(), Ebolum.get(), Eid.get()))
        db.commit()
        listele()

    def sil():
        mycursor.execute("DELETE FROM Maykod  WHERE id=%s " % (Eid.get()))
        db.commit()
        listele()

    def getir(event):
        idno = liste.item(liste.selection()[0])['text']
        mycursor.execute("SELECT * FROM Maykod WHERE id = %s" % (idno))

        results = mycursor.fetchone()
        Eid.delete(0, END)
        Eid.insert(0, results[0])

        Etc.delete(0, END)
        Etc.insert(0, results[1])

        Esif.delete(0, END)
        Esif.insert(0, results[2])

        Ead.delete(0, END)
        Ead.insert(0, results[3])

        Esad.delete(0, END)
        Esad.insert(0, results[4])

        Email.delete(0, END)
        Email.insert(0, results[5])

        Eil.delete(0, END)
        Eil.insert(0, results[6])

        Eilce.delete(0, END)
        Eilce.insert(0, results[7])

        Ebolum.delete(0, END)
        Ebolum.insert(0, results[8])

    def listetikla(event):
        idtext = liste.item(liste.selection()[0])['values'][0]
        tctext = liste.item(liste.selection()[0])['values'][1]
        sifretext = liste.item(liste.selection()[0])['values'][2]
        adtext = liste.item(liste.selection()[0])['values'][3]
        soyadtext = liste.item(liste.selection()[0])['values'][4]
        emailtext = liste.item(liste.selection()[0])['values'][5]
        iltext = liste.item(liste.selection()[0])['values'][6]
        ilcetext = liste.item(liste.selection()[0])['values'][7]
        bolumtext = liste.item(liste.selection()[0])['values'][8]

        Eid.delete(0, END)
        Eid.insert(0, idtext)

        Etc.delete(0, END)
        Etc.insert(0, tctext)

        Esif.delete(0, END)
        Esif.insert(0, sifretext)

        Ead.delete(0, END)
        Ead.insert(0, adtext)

        Esad.delete(0, END)
        Esad.insert(0, soyadtext)

        Email.delete(0, END)
        Email.insert(0, emailtext)

        Eil.delete(0, END)
        Eil.insert(0, iltext)

        Eilce.delete(0, END)
        Eilce.insert(0, ilcetext)

        Ebolum.delete(0, END)
        Ebolum.insert(0, bolumtext)

    form = Toplevel()
    form.title('Maykod')
    form.geometry('1500x800')
    form.configure(background="grey")

    my_pice = Image.open("adminpanel.jpg")
    resizede = my_pice.resize((1300, 650), Image.ANTIALIAS)
    new_pice = ImageTk.PhotoImage(resizede)
    my_laben = Label(form,image=new_pice)
    my_laben.place(x=100, y=50)

    Lid = Label(form, text="ID", bg="#454f50",fg="white", font="Times 15 italic").place(x=1120, y=120)
    Eid = Entry(form, bd=1)
    Eid.place(x=1150, y=150)

    ltc = Label(form, text="TC", bg="#454f50",fg="white", font="Times 15 italic").place(x=1120, y=170)
    Etc = Entry(form, bd=1)
    Etc.place(x=1150, y=200)

    Lad = Label(form, text="ADI", bg="#454f50",fg="white", font="Times 15 italic").place(x=1120, y=220)
    Ead = Entry(form, bd=1)
    Ead.place(x=1150, y=250)

    Lsad = Label(form, text="SOYADI", bg="#454f50",fg="white", font="Times 15 italic").place(x=1120, y=270)
    Esad = Entry(form, bd=1)
    Esad.place(x=1150, y=300)

    Lsif = Label(form, text="ŞİFRE", bg="#454f50", fg="white", font="Times 15 italic").place(x=1120, y=320)
    Esif = Entry(form, bd=1)
    Esif.place(x=1150, y=350)

    Lmail = Label(form, text="E-MAİL", bg="#454f50", fg="white", font="Times 15 italic").place(x=1120, y=370)
    Email = Entry(form, bd=1)
    Email.place(x=1150, y=400)

    Lil = Label(form, text="İL", bg="#454f50", fg="white", font="Times 15 italic").place(x=1120, y=420)
    Eil = Entry(form, bd=1)
    Eil.place(x=1150, y=450)

    Lilce = Label(form, text="İLÇE", bg="#454f50", fg="white",font="Times 15 italic").place(x=1120, y=470)
    Eilce = Entry(form, bd=1)
    Eilce.place(x=1150, y=500)

    lbolum = Label(form, text="BÖLÜM", bg="#454f50", fg="white", font="Times 15 italic").place(x=1120, y=520)
    Ebolum = Entry(form, bd=1)
    Ebolum.place(x=1150, y=550)

    Kaydet = Button(form, text="Kaydet", command=ekle)
    Kaydet.place(x=1100, y=650)

    sil = Button(form, text="Sil", command=sil)
    sil.place(x=1180, y=650)

    guncelle = Button(form, text="Güncelle", command=guncelle)
    guncelle.place(x=1230, y=650)

    liste = Treeview(form, height=10, selectmode="extended")
    liste["columns"] = ('sut1', 'sut2', 'sut3', 'sut4', 'sut5', 'sut6', 'sut7', 'sut8')
    liste.place(x=120, y=100)
    liste.column("#0", width=50)
    liste.heading("#0", text="id",)
    liste.column("sut1", width=100)
    liste.heading("sut1", text="tc")
    liste.column("sut2", width=90)
    liste.heading("sut2", text="sifre")
    liste.column("sut3", width=120)
    liste.heading("sut3", text="adi")
    liste.column("sut4", width=120)
    liste.heading("sut4", text="soyadi")
    liste.column("sut5", width=120)
    liste.heading("sut5", text="email")
    liste.column("sut6", width=90)
    liste.heading("sut6", text="il")
    liste.column("sut7", width=120)
    liste.heading("sut7", text="ilce")
    liste.column("sut8", width=120)
    liste.heading("sut8", text="bolum")
    liste.bind('<ButtonRelease-1>', getir)
    style = ttk.Style()
    style.theme_use("default")
    style.configure("Treeview",
                    background="yellow",
                    foreground="black",
                    fieldbackground="silver"
                    )
    style.map('Treeview',
              background=[('selected', 'blue')])
    listele()
    form.mainloop()


lgir = Label(formgiris, text="MAYKOD", fg="black", bg="white", font="Times 40 italic").place(x=200, y=0)
Lkul = Label(formgiris, text="Kullanıcı Adı:", fg="black", bg="white", font="Times 18 italic").place(x=150, y=180)
Eku = Entry(formgiris, bd=1, width=25)
Eku.place(x=150, y=210)

Lsif = Label(formgiris, text="Şifre :", fg="black", bg="white", font="Times 18 italic").place(x=150, y=250)
Esif = Entry(formgiris, bd=1, width=25)
Esif.place(x=150, y=280)

Kaydet = Button(formgiris, text="Giriş Yap", fg="black", bg="white", font="Times 22 italic", command=login)
Kaydet.place(x=150, y=330)
Kayit = Button(formgiris, text="Kayıt Ol", fg="black", bg="white", font="Times 22 italic", command=kayitolma)
Kayit.place(x=300, y=330)

formgiris.mainloop()