from datetime import datetime, timedelta

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
# Create your views here.
from django.shortcuts import reverse
from django.views.decorators.http import require_POST

from root.breadcrumb import BreadCrumb
from root.forms import ContactForm
from root.models import FrontDisplayCategory, SubSubscribers
from shop.models import Category, Product, Tag


def index(request):
    current_time = datetime.now()
    # Calculate the start and end times for the range of dates to filter
    start_time = current_time - timedelta(days=3)
    end_time = current_time
    bread_crumb = [
        BreadCrumb("Home", "/", True),
    ]
    nav = {"home": 'active'}
    categories = Category.objects.all()
    featured = Product.objects.all()[:8]
    recent = Product.objects.filter(created__range=(start_time, end_time))
    display: list = FrontDisplayCategory.objects.all()
    sliders = None
    brands = None
    tags = Tag.objects.all()
    if len(tags) > 2:
        tags = tags[:2]
    for obj in display:
        if obj.category_name == "Sliders":
            sliders = get_object_or_404(FrontDisplayCategory, category_name="Sliders").displays.all()
        elif obj.category_name == "Brands":
            brands = get_object_or_404(FrontDisplayCategory, category_name="Brands").displays.all()
    return render(
        request,
        "index-1.html",
        {
            "categories": categories,
            "featured": featured,
            "recent": recent,
            "nav": nav,
            "sliders": sliders,
            "brands": brands,
            'tags': tags,
            "bread_crumb": bread_crumb
        }
    )


@require_POST
def subscribe(request):
    email = request.POST.get("email")
    try:
        SubSubscribers.objects.create(email=email)
        messages.info(request, "Thank you for subscribing")
    except IntegrityError:
        messages.warning(request, "Account is already in our subscription list")

    return redirect('root:index')


def about(request):
    bread_crumb = [
        BreadCrumb("Home", "/"),
        BreadCrumb("About", reverse('root:about'), True),
    ]
    nav = {"about": 'active'}
    return render(request, "about.html", {'nav': nav, "bread_crumb": bread_crumb})


def contact(request):
    bread_crumb = [
        BreadCrumb("Home", "/"),
        BreadCrumb("Contact", reverse('root:contact'), True),
    ]
    nav = {"contact": 'active'}
    form = ContactForm()
    return render(request, "contact.html", {"form": form, 'nav': nav, "bread_crumb": bread_crumb})


@login_required
def dashboard(request):
    # TODO removed for now, to be implemented later
    bread_crumb = [
        BreadCrumb("Home", "/"),
        BreadCrumb("Dashboard", reverse('root:dashboard'), True),
    ]
    nav = {"dashboard": "active"}
    return render(request, "dashboard/dashboard.html", {'nav': nav, "bread_crumb": bread_crumb})
