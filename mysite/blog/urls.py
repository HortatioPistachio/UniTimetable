from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name='index'),
    path('complete/',views.complete, name='complete'),
    path('timetable/',views.timetable,name='timetable'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('error/', views.error,name='error'),
    path('faq/', views.faq ,name='faq'),
]


