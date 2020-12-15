from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from django.contrib.auth.forms import UserCreationForm

def home(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Thank you for reaching out. We'll get back soon!")
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'online_profile/home.html', {'form': form})

# def resume(request):
#     return render(request, 'portfolio/home.html', {'title': 'Blog'})
