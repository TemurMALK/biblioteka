from django.db import models

class Student(models.Model):
    ism = models.CharField(max_length=30)
    st_raqam = models.CharField(max_length=30, unique=True)
    guruh = models.CharField(max_length=30)
    bitiruvchi = models.BooleanField(default=False)
    kitob_soni = models.PositiveSmallIntegerField(default=0)
    def __str__(self):
        return f"{self.ism}"
class Muallif(models.Model):
    JINS = [
        ("Erkak","Erkak"),
        ("Ayol","Ayol")
    ]
    ism = models.CharField(max_length=30)
    jins = models.CharField(max_length=30, blank = True, choices=JINS)
    tirik = models.BooleanField()
    tugilgan_yil= models.DateField(null=True,blank=True)
    kitoblar_soni = models.PositiveSmallIntegerField()
    def __str__(self):
        return f"{self.ism},{self.tugilgan_yil}"

class Kitob(models.Model):
    JANR=[
        ("Hujjatli","Hujjatli"),
        ("Detektiv", "Detektiv"),
        ("Sayohat", "Sayohat"),
        ("Ilmiy", "Ilmiy"),
    ]
    nom = models.CharField(max_length=30)
    sahifa = models.PositiveSmallIntegerField()
    muallif = models.ForeignKey(Muallif,on_delete=models.CASCADE)
    janr = models.CharField(max_length=30, blank=True,choices=JANR)
    def __str__(self):
        return f"{self.nom},{self.sahifa}"

class Record(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    kitob = models.ForeignKey(Kitob,on_delete=models.CASCADE)
    ol_sana = models.DateTimeField(auto_now_add=True)
    qaytarilgan_sana = models.DateField(null=True, blank=True)
    def __str__(self):
        return f"{self.student}"


