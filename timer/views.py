import json
from django.shortcuts import get_object_or_404, render, reverse
from django.http import HttpResponseRedirect, Http404, HttpResponse 
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from timer.models import Activity
from timer.forms import ActivityForm





def index(request):
    if request.user.is_authenticated:
        
        activities = Activity.objects.filter(owner=request.user).order_by('-activity_time')[:]     
   
        context = {'activities':activities}
        return render(request, 'timer/index.html', context) 
    return render(request, 'timer/index.html') 

@login_required   
def activities(request):
    
    activities = Activity.objects.filter(owner=request.user).order_by('-activity_time')[:]
    context = {'activities':activities}
    return render(request, 'timer/activities.html', context)

@login_required
def activity_detail(request, activity_id):
    activity = Activity.objects.get(pk=activity_id)
    activityTimeList = activity.activity_time.split(":")
    if (activityTimeList[0] == ""):
        activityHoursStr = "0"
        activityHoursInt = 0  
    else:
        activityHoursStr = activityTimeList[0] 
   
    
    if activity.owner != request.user:
        raise Http404
    
    if (len(activity.activity_time) != 14):
        pass
        
        
    activities = Activity.objects.filter(owner=request.user).order_by('-activity_time')[:]
    if (len(activities) >= 1):
        firstActivity = activities[0]
        
    else:
        raise Http404
    
    
    
    hourList = []
    for x in range(100):
        hourList.append(x)  
        
    minList = []
    for x in range(60):
        minList.append(x)  
        
    context = {
        'activity' : activity, 
        'activities' : activities, 
        'hourList' : hourList, 
        'minList' : minList, 
        'activityHoursStr' : activityHoursStr, 
        'activityLevel' : activity.activity_level,
        'firstActivity' : firstActivity
               }
    return render(request, 'timer/activity_detail.html', context)


@login_required
def update_stopwatch(request):
    """
    incorporates ajax. every 4-5 seconds sends updates
    on new activity_time to be stored while the user
    is using the stopwatch in activity_detail
    """
    updateString = request.body.decode("utf-8")
    updateStringList = updateString.split('$$TEXT$$')
    time = updateStringList[0]
    activity = Activity.objects.get(pk=int(updateStringList[1]))
    
    if activity.owner != request.user:
        raise Http404  
    
    activity.activity_time = time
    activity.save()
    return HttpResponse("")

@login_required 
def editActivityTitle(request):
    updateTitle = request.body.decode("utf-8")
    updateTitleList = updateTitle.split('$$TEXT$$')
    activity = Activity.objects.get(pk=int(updateTitleList[1]))
    
    if activity.owner != request.user:
        raise Http404   
    
    activity.activity_title = updateTitleList[0]
    activity.save()
    return HttpResponse("")


@login_required
def insertTime(request):

    #timeInsert = request.body.decode("utf-8")
    data = json.loads(request.body)
    activity = Activity.objects.get(pk=data['acitivityID'])
    hoursAdd = int(data['hours'])
    minutesAdd = int(data['minutes'])
    
    # get hours and minutes of activity before we add new hours and minutes
    activityTimeList = activity.activity_time.split(":")
    activityHours = int(activityTimeList[0])
    activityMins = int(activityTimeList[1])
    activitySecs = (activityTimeList[2])
    
    if (activityMins + minutesAdd >= 60):
        activityHours += 1
        activityHours += hoursAdd
        
        tempMins = (activityMins + minutesAdd) - 60
        activityMins = tempMins
    else:
        activityHours += hoursAdd
        activityMins += minutesAdd      
        
    activityHours = str(activityHours)
    while (len(activityHours) < 4):
        activityHours = '0' + activityHours
    
    activityMins = str(activityMins)
    while (len(activityMins) < 2):
        activityMins = '0' + activityMins
        
    
    timeSave = activityHours + ":" + activityMins + ":" + activitySecs
    activity.activity_time = timeSave
    activity.save()
    return HttpResponse("")
    
    
def deleteActivity(request):
    data = json.loads(request.body)
    activity = Activity.objects.get(pk=data['acitivityID'])
    activity.delete()
    return HttpResponseRedirect(reverse('timer:activities'))   
    
    
@login_required 
def new_activity(request):
    """Add a new activity"""
    if request.method != 'POST': 
        #No data submitted, create a blank form
        form = ActivityForm()   
    else:
        #POST data submitted; process data
        form = ActivityForm(request.POST, request.FILES)  
        if form.is_valid():   
            new_activity = form.save(commit=False)
            new_activity.owner = request.user
        try:
            activity = Activity.objects.get(activity_title=new_activity.activity_title)
            msgText =  "You already have an activity called " + new_activity.activity_title + "!"
            messages.info(request, msgText)
            return HttpResponseRedirect(reverse('timer:new_activity'))             
        except:
            pass 
            new_activity.save()
            return HttpResponseRedirect(reverse('timer:activities'))   
        
    context = {'form': form}   
    return render(request, 'timer/new_activity.html', context)


@login_required
def autoSave(request):
    activityInfo = json.loads(request.body)
    activity = Activity.objects.get(pk=activityInfo['activityID'])    
    activity.activity_time = activityInfo['currentTime']
    activity.activity_level = activityInfo['newLvl']
    activity.save()
    return HttpResponse("")


    
    