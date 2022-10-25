from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User

def asosiy(request):
    return render(request, 'asosiy.html')

def dost(request):
    return render(request, 'dostlarim.html')

def doc(sorov):
    return render(sorov,'doc.html', {"names":["Ali","Gulom","Vali"]})

def student(a):
    if a.method =='POST':
        # Student.objects.create(
        #     ism=a.POST.get("i"),
        #     st_raqam=a.POST.get("st"),
        #     guruh=a.POST.get("g"),
        #     kitob_soni=a.POST.get("k"),
        # )
        forma = StudentForm(a.POST)
        if forma.is_valid():
            Student.objects.create(
                ism = forma.cleaned_data.get("ism"), #1 models 2 form
                st_raqam = forma.cleaned_data.get("st_raqam"),
                guruh = forma.cleaned_data.get("gr"),
                bitiruvchi = forma.cleaned_data.get("bitiruvchi"),
                kitob_soni = forma.cleaned_data.get("k_s"),
            )
        return redirect('/studentlar/')
    qidiruv_sozi = a.GET.get("soz")
    if qidiruv_sozi is None:
        st = Student.objects.all()
    else:
        st = Student.objects.filter(ism__contains=qidiruv_sozi) | Student.objects.filter(guruh__contains=qidiruv_sozi)
    data ={
        "talabalar":st,
        "forma":StudentForm()
    }
    return render(a,'student.html', data)

def muallif(mul):
    if mul.method =='POST':
        # if mul.POST.get('b') == 'on':
        #     t_m =True
        # else:
        #     t_m =False
        # Muallif.objects.create(
        #     ism=mul.POST.get("i_m"),
        #     jins=mul.POST.get("j_m"),
        #     tirik=t_m,
        #     kitoblar_soni=mul.POST.get("kt_m"),
        #     tugilgan_yil=mul.POST.get("ty_m"),
        # )

        forma = MuallifForm(mul.POST)
        if forma.is_valid():
            Muallif.objects.create(
                ism = forma.cleaned_data.get("ism"), #1 models 2 form
                jins = forma.cleaned_data.get("jins"),
                tirik = forma.cleaned_data.get("tirik"),
                tugilgan_yil = forma.cleaned_data.get("tugilgan_yil"),
                kitoblar_soni = forma.cleaned_data.get("kitoblar_soni"),
            )
        return redirect('/mualliflar/')
    qidiruv_sozi = mul.GET.get("soz")
    if qidiruv_sozi is None:
        ml = Muallif.objects.all()
    else:
        ml = Muallif.objects.filter(ism__contains=qidiruv_sozi)
    data ={
        "mualliflar":ml,
        "forma": MuallifForm()
    }
    return render(mul,'muallif.html', data)

def muallif_ochir(mul,mul_id):
    Muallif.objects.filter(id=mul_id).delete()
    return redirect('/mualliflar/')


def bitta_student(request, son):
    data ={
        "talaba":Student.objects.get(id=son)
    }
    return render(request, "studentchoose.html", data)




def student_ochir(request,t_id):
    Student.objects.filter(id=t_id).delete()
    return redirect('/studentlar/')
def all_students(request):
    st=Student.objects.all()
    data={"studentlar":st}
    return render(request,"all_students.html",data)



def all_record(request):
    st=Record.objects.all()
    data={"recordlar":st}
    return render(request,"all_record.html",data)
def hamma_recordlar(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            Record.objects.create(
                student = Student.objects.get(id=request.POST.get('st')),
                kitob=  Kitob.objects.get(id=request.POST.get('k'))

            )
            # forma = RecordForm(request.POST)
            # if forma.is_valid():
            #     forma.save()
                # s1 = Student.objects.get(id=request.POST.get('st'))
                # s1.kitob_soni += 1
                # s1.save()
            return redirect('/recordlar/')
        data = {
            "records": Record.objects.all(),
            "students": Student.objects.all(),
            "kitobs": Kitob.objects.all(),
            "f":RecordForm(),
        }
        return render(request, 'record.html', data)
    return redirect('/')



def hamma_kitoblar(k):
    if k.user.is_authenticated:
        if k.method == 'POST':
            Kitob.objects.create(
                nom = k.POST.get("n"),
                sahifa = k.POST.get("s"),
                muallif = Muallif.objects.get(id=k.POST.get("m")),
                janr = k.POST.get("j"),
            )
            return redirect('/kitoblar/')
        qidiruv_sozi = k.GET.get("soz")
        if qidiruv_sozi is None:
            ki = Kitob.objects.all()
        else:
            ki = Kitob.objects.filter(nom__contains=qidiruv_sozi)
        data ={
            "kitoblar":ki,
            "mualliflar":Muallif.objects.all(),
        }
        return render(k, "kitob.html", data)
    else:
        return redirect('/')

def hamma_kitoblar(k):
    if k.user.is_authenticated:
        if k.method == 'POST':
            m = k.POST.get("m")
            kf = KitobForm(k.POST)
            if kf.is_valid():
                kf.save()

            return redirect('/kitoblar/')
        soz = k.GET.get("qidirish")
        kf = KitobForm()
        m = Muallif.objects.all()
        if soz == None:
            hammasi = Kitob.objects.all().order_by("nom")
        else:
            hammasi = Kitob.objects.filter(nom=soz)

        return render(k, "kitob.html", {"kitoblar":hammasi, "avtorlar":m, "form":kf})
    else:
        return redirect('/')

def bitta_kitob(kitob, son):
    data = {
        "kitob":Kitob.objects.get(id=son)
    }
    return render(kitob, "kitob.html", data)


def kitob_ochir(request, k_id):
    Kitob.objects.filter(id=k_id).delete()
    return redirect('/kitoblar/')

def student_edit(request, son):
    if request.method == 'POST':
        if request.POST.get('b') == 'on':
            bitiruvchi_st = True
        else:
            bitiruvchi_st = False
        Student.objects.filter(id=son).update(
            ism=request.POST.get("i"),
            st_raqam=request.POST.get("st"),
            guruh=request.POST.get("g"),
            kitob_soni=request.POST.get("k"),
            bitiruvchi = bitiruvchi_st
        )
        return redirect("/studentlar/")
    data = {
        "talaba":Student.objects.get(id=son)
    }
    return render(request, 'student-edit.html', data)

def muallif_edit(request, son):
    if request.method == 'POST':
        if request.POST.get('t') == 'on':
            tirik_m = True
        else:
            tirik_m = False
        Muallif.objects.filter(id=son).update(
            ism=request.POST.get("i"),
            jins=request.POST.get("j"),
            tirik= tirik_m,
            tugilgan_yil=request.POST.get("k"),
            kitoblar_soni =request.POST.get("k_s")
        )
        return redirect("/mualliflar/")
    data = {
        "muallif":Muallif.objects.get(id=son)
    }
    return render(request, 'muallif-edit.html', data)

def kitob_edit(request, son):
    if request.method == 'POST':
        Kitob.objects.filter(id=son).update(
            nom=request.POST.get("n"),
            sahifa=request.POST.get("s"),
            muallif=request.POST.get("m"),
            janr =request.POST.get("j")
        )
        return redirect("/kitoblar/")
    data = {
        "kitob":Kitob.objects.get(id=son)
    }
    return render(request, 'kitob-edit.html', data)

def hamma_recordlar(request):
    if request.method == 'POST':

        Record.objects.create(
            student = Student.objects.get(id=request.POST.get('st')),
            kitob=  Kitob.objects.get(id=request.POST.get('k'))

        )
        # forma = RecordForm(request.POST)
        # if forma.is_valid():
        #     forma.save()
            # s1 = Student.objects.get(id=request.POST.get('st'))
            # s1.kitob_soni += 1
            # s1.save()
        return redirect('/recordlar/')
    data = {
        "records": Record.objects.all(),
        "students": Student.objects.all(),
        "kitobs": Kitob.objects.all(),
        "f":RecordForm(),
    }
    return render(request, 'record.html', data)



def loginView(request):
    if request.method == "POST":
        user = authenticate(username=request.POST.get('l'),
                            password=request.POST.get('p'),)
        if user is None:
            return redirect('/')
        login(request, user)
        return redirect('/kitoblar/')
    return render(request, 'login.html')

def logoutView(request):
    logout(request)
    return redirect('/')

def register(request):
    if request.method=='POST':
        User.objects.create_user(
            username=request.POST.get('l'),
            password=request.POST.get('p')
        )
        return redirect('/')
    return render(request, 'register.html')