from django.contrib import messages
from .models import Player, RecordTime, CheckPoint
from django.shortcuts import render
from django.db.models import Sum

from .forms import AddTimeForm


def welcome(request):
    title = "Scavenger Run | TimeTracker"
    cps = CheckPoint.objects.all()
    context = {
        "title": title,
        "cps": cps
    }
    return render(request, "welcome.html", context)


def cp(request, cpid, template_name):
    title = "ScavengerRunApp - CP%s" % cpid
    head = "Check Point %s" % cpid

    form = AddTimeForm()

    if request.method == "POST":
        form = AddTimeForm(request.POST)

        if form.is_valid():
            player = Player.objects.get(pk=form.cleaned_data['player'])
            previous_record = player.get_last_checkpoint()
            current_record = form.save()
            if previous_record:
                current_record.duration = current_record.check_in_time-previous_record.check_in_time
                current_record.save()

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

    player_total_time = Player.objects.annotate(total_time=Sum('record_time__duration')).order_by('-total_time')

    context = {
        "player_total_time": player_total_time

    }
    return render(request, template_name, context)


def playertimedetails(request, player, template_name):
    detail_records = RecordTime.objects.filter(player=player).order_by('check_in_time')

    context = {
        "details": detail_records,
        "player": player
    }
    return render(request, template_name, context)
