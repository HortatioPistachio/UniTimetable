from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('complete/',views.complete, name='complete'),
    path('timetable/',views.timetable_gone,name='timetable'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('error/', views.error,name='error'),
    path('faq/', views.faq ,name='faq'),
    path('project-<name>/', views.projectDetail,name="projectDetail"),
    path('timetable/<name>.ics',views.iCalLink, name='iCal-Calendar'),
    path('iCalComplete/<code>', views.iCal_complete, name="iCal_complete"),
    path('overuseError/', views.overuseError, name='overuseError'),
    path('timetableGoogle/', views.googleTimetable, name='timtableGoogle'),
    path('timetableiCal/', views.iCalTimetable, name='timtableiCal'),
    path('timetable_legacy/', views.timetable, name='timetable_legacy')

    
]


