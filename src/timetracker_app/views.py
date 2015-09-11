from django.contrib import messages
from .models import Player, RecordTime, CheckPoint
from django.shortcuts import render
import time

from .forms import AddTimeForm


def welcome(request):
    title = "Scavenger Run | TimeTracker"
    cps = CheckPoint.objects.all()
    context = {
        "title": title,
        "cps" : cps
    }
    return render(request, "welcome.html", context)


def cp(request, cpid, template_name):
    title = "ScavengerRunApp - CP%s" % cpid
    head = "Check Point %s" % cpid

    form = AddTimeForm()

    if request.method == "POST":
        form = AddTimeForm(request.POST)

        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Record guardado exitosamente.')

            form = AddTimeForm()
    else:
        pass

    context = {
        "title": title,
        "head": head,
        "form": form,
        "cpid": cpid
    }
    return render(request, template_name, context)


def reports(request, template_name):
    player = Player.objects.all()
    print player

    context = {
        "player": player
    }
    return render(request, template_name, context)


def playertimedetails(request, mprid, template_name):
    detail_records = RecordTime.objects.filter(mprid= mprid).order_by('check_in_time')

    time1 = None
    i = 0
    details_table= []
    for dr in detail_records:
        if i == 0:
            time1 = dr.check_in_time
            details_table.append({'diff':None,'check_in_time':dr.check_in_time,'place_name':dr.place_name})
            i += 1
        else :
            details_table.append({'diff':dr.check_in_time - time1,'check_in_time':dr.check_in_time,'place_name':dr.place_name})
            time1 = dr.check_in_time
            i += 1
    context = {
        "details": details_table,
        "mprid" : mprid
    }
    return render(request, template_name, context)
