from django.shortcuts import render, redirect
from .models import Region, Rating
from django.contrib.auth import login, logout
from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from .forms import LoginForm, RegisterForm


# Create your views here.

def index(request):
    regions = Region.objects.filter(parent=None)
    context = {
        'regions': regions,
        'all_regions': Region.objects.all()
    }
    return render(request, 'app/index.html', context=context)


def region_detail(request, pk):
    selected_region = Region.objects.get(pk=pk)
    regions = Region.objects.filter(parent=None)
    context = {
        'selected_region': selected_region,
        'regions': regions,
        'all_regions': Region.objects.all()
    }
    rating = Rating.objects.filter(post=selected_region, user=request.user.id).first()  # Requestdan foydalanish
    selected_region.user_rating = rating.rating if rating else 0
    return render(request, 'app/index.html', context=context)


def user_login(request):
    """This is for login"""

    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'{user.username.title()}, you have successfully entered the site.')
            return redirect('index')

        if form.errors:
            messages.error(request, "Check that the fields are correct!")

    form = LoginForm()
    context = {
        'form': form,
        'title': 'Sign in'
    }
    return render(request, 'app/login.html', context=context)


def user_logout(request):
    """This is for logout"""

    logout(request)
    messages.warning(request, "You are logged out!")
    return redirect('login')


def user_register(request):
    """This is for sing up"""

    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "You can log in by entering your username and password.")
            return redirect('login')

        if form.errors:
            messages.error(request, "Check that the fields are correct!")

    form = RegisterForm()
    context = {
        'form': form,
        'title': 'Sign up'
    }
    return render(request, 'app/register.html', context=context)


def about_us(request):
    return render(request, 'app/about.html')


def rate(request: HttpRequest, post_id: int, rating: int) -> HttpResponse:
    post = Region.objects.get(id=post_id)
    Rating.objects.filter(post=post, user=request.user).delete()
    post.rating_set.create(user=request.user, rating=rating)
    return region_detail(request, post_id)
