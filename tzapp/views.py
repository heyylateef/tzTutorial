from django.shortcuts import render, redirect, reverse
from django.views import generic
from .models import Blogpost
from django.contrib import messages
import pytz


def home(request):
    if request.session.get('django_timezone') == None: #If the browser's timezone isn't set, ask user to set timezone
        return render(request, 'tzapp/settimezone.html', {'timezones': pytz.common_timezones})
    else:
        queryset = Blogpost.objects.all()
        return render(request, 'tzapp/home.html', {'post':queryset})

def settimezone(request):
    if request.method == 'POST':
        request.session['django_timezone'] = request.POST['timezone'] #Sets the request session's timezone to the user selected timezone, so all datetime objects will be rendered in the user's desired timezone
        return redirect(reverse("home"))
    else:
        return render(request, 'tzapp/settimezone.html', {'timezones': pytz.common_timezones})
    return render(request, 'tzapp/settimezone.html', {'timezones': pytz.common_timezones})

class PostDetail(generic.DetailView):
    model = Blogpost
    template_name = 'tzapp/post_detail.html'
    