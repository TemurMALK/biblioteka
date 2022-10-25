from django.contrib import admin
from .models import *
from django.contrib.admin import ModelAdmin

@admin.register(Muallif)
class MuallifAdmin(ModelAdmin):
    search_fields = ("id", "ism")
    list_filter = ("jins", "tirik")
    list_display = ("id", "ism", "tugilgan_yil", "tirik", "kitoblar_soni",)
    list_display_links = ("ism",)
    list_editable = ("tugilgan_yil", "kitoblar_soni",)
    ordering = ("ism",)

@admin.register(Kitob)
class KitobAdmin(ModelAdmin):
    search_fields = ("nom","janr","id")
    list_filter = ("janr",)
    list_display = ("id","nom","janr","muallif","sahifa")
    list_editable = ("janr", "sahifa",)
    list_display_links = ("id", "nom",)
    autocomplete_fields = ("muallif",)

@admin.register(Student)
class StudentAdmin(ModelAdmin):
    search_fields = ("guruh","id","ism")
    list_filter = ("guruh","bitiruvchi")
    list_display = ("id","ism","guruh","kitob_soni","st_raqam")
    list_editable = ("ism","guruh")
@admin.register(Record)
class RecordAdmin(ModelAdmin):
    search_fields = ("id", "student", "kitob")
    list_filter = ("ol_sana","qaytarilgan_sana")
    list_display = ("id","student", "kitob", "ol_sana", "qaytarilgan_sana")
    list_editable = ("student","kitob","qaytarilgan_sana")



