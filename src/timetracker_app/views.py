from django.contrib import messages
from django.shortcuts import render
import time

from .forms import AddTimeForm


def welcome(request):
    title = "Scavenger Run | TimeTracker"
    context = {
        "title": title
    }
    return render(request, "welcome.html", context)


def cp(request, cpid, ts, template_name):
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
        "cpid": cpid,
        "ts" : int(time.time() * 1000)
    }
    return render(request, template_name, context)


def reports(request, template_name):
    return render(request, template_name, {})


def details(request, template_name):
    return render(request, template_name, {})
