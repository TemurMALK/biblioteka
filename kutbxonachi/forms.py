from django import forms
from .models import *
class StudentForm(forms.Form):
    ism = forms.CharField()
    st_raqam = forms.CharField(label = "Student raqami")
    gr = forms.CharField()
    bitiruvchi = forms.BooleanField(required=False)
    k_s = forms.IntegerField(max_value=5, min_value=0, label="Kitoblar soni")

class MuallifForm(forms.Form):
    ism = forms.CharField(label = "Ism")
    jins = forms.ChoiceField(label="Jins",choices=(("Ayol","Ayol"),("Erkak","Erkak")))
    tirik = forms.BooleanField(required=False)
    tugilgan_yil = forms.DateField(label="tugilgan yil")
    kitoblar_soni = forms.IntegerField(label="Kitob soni")

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = '__all__'


class KitobForm(forms.ModelForm):
    class Meta:
        model = Kitob
        fields = '__all__'