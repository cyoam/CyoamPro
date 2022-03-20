from django.shortcuts import render
from .forms import ContactForm

# Create your views here.

# Home Page View


def index(request):
    return render(request, 'index-helena.html')

# Works Page View


def works(request):
    return render(request, 'helena-work.html')

# Contact Page View


def contact(request):
    context = {}
    form = ContactForm(request.POST or None)
    context['form'] = form
    if request.GET:
        return render(request, 'helena-404.html')

    return render(request, 'helena-contact.html', context)

# Home Page View


def pricing(request):
    return render(request, 'helena-pricing.html')

# Home Page View


def about(request):
    return render(request, 'helena-about.html')

# Home Page View


def services(request):
    return render(request, 'helena-services.html')

# Home Page View


def blog(request):
    return render(request, 'helena-news.html')

# Home Page View


def blogDetails(request):
    return render(request, 'helena-news-details.html')

# Home Page View


def career(request):
    return render(request, 'helena-career.html')

# Home Page View


def team(request):
    return render(request, 'helena-team.html')

