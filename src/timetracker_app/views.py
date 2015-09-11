from django.contrib import messages
from django.shortcuts import render

from .forms import AddTimeForm


def welcome(request):
    title = "Scavenger Run | TimeTracker"
    context = {
        "title": title
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
    return render(request, template_name, {})
