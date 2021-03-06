from django.urls import path
from django.utils.translation import gettext_lazy as _
from . import views


app_name = 'timer'
urlpatterns = [
    path('', views.index, name='index'),
    path('activities/', views.activities, name='activities'),
    path('activities/new_activity/', views.new_activity, name='new_activity'),
    path('activities/deleteActivity/', views.deleteActivity, name='deleteActivity'),
    path('activities/update_stopwatch/', views.update_stopwatch, name="update_stopwatch"),
    path('activities/editActivityTitle/', views.editActivityTitle, name="editActivityTitle"),
    path('activities/insertTime/', views.insertTime, name="insertTime"),
    path('activities/activity/<int:activity_id>/', views.activity_detail, name='activity_detail'),
    path('activities/autoSave/', views.autoSave, name='autoSave'),
    

]