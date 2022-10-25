from turtle import home

from kutbxonachi.views import *
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('home/', home),
    path('dost/', dost),
    path('doc/', doc),
    path('studentlar/', student),
    path('studentlar/<int:son>/', student_edit),
    path('mualliflar/<int:son>/', muallif_edit),
    path('kitoblar/', hamma_kitoblar),
    path('kitoblar/<int:son>/', kitob_edit),
    path('mualliflar/', muallif),
    path('student/<int:son>/', bitta_student),
    path('student_ochir/<int:t_id>/', student_ochir),
    path('muallif_ochir/<int:t_id>/', muallif_ochir),
    path('recordlar/', hamma_recordlar),
    path('all_students/', all_students),
    path('all_record', all_record),
    path('kitoblar/', hamma_kitoblar),
    path('kitob/<int:son>/', bitta_kitob),
    path('kitob_ochir/<int:k_id>/', kitob_ochir),
    path('register/', register),
    path('', loginView, name="login"),
    path('logout/', logoutView, name="logout"),
]
