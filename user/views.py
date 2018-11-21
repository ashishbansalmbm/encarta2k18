from django.shortcuts import render, redirect
from user.forms import RegistrationForm, CreateProfileForm
from user.models import Event, Participation


def homepage(request):
    all_events = Event.objects.all()
    return render(request, 'homepage.html', {'all_events': all_events})

def detail(request, id):
    event = Event.objects.get(pk=id)
    return render(request, 'event_detail.html', {'event': event})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'homepage.html')
        return render(request, 'registration_form.html', {'form': form})

    else:
        form = RegistrationForm()
        return render(request, 'registration_form.html', {'form': form})


def profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user_id = request.user.id
            user.encarta_id = 'EN-V21.0-' + str(user.user_id)
            form.save()
            id = request.user
            event = Event.objects.all()
            return render(request, 'event.html', {'user': id,'event': event})
        else:
            id = request.POST.getlist('event')
            b = request.user.id
            idw = request.user
            event = Event.objects.raw(
                "select * from user_event where id not in ( select event_id from user_participation where user_id = %s)",
                [idw.id])
            event2 = Event.objects.raw(
                "select * from user_event where id in ( select event_id from user_participation where user_id = %s and verified = 0)",
                [idw.id])
            event3 = Participation.objects.filter(user_id=idw.id, verified=True)

            for i in id:
                participant = Participation(user_id=b, event_id=i)
                participant.save()
            return render(request, 'event.html', {'user': idw, 'event': event, 'event2': event2, 'event3': event3})



    else:
        try:
            if request.user.profile:
                id = request.user
                event = Event.objects.raw("select * from user_event where id not in ( select event_id from user_participation where user_id = %s)",[id.id])
                event2 = Event.objects.raw(
                    "select * from user_event where id in ( select event_id from user_participation where user_id = %s and verified = 0)",
                    [id.id])
                event3 = Participation.objects.filter(user_id=id.id,verified=True)
                return render(request, 'event.html', {'user': id, 'event': event, 'event2': event2, 'event3': event3})
        except:
            form = CreateProfileForm()
            return render(request, 'profile.html', {'form': form})


