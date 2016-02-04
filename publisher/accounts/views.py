from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '회원 가입해주셔서 감사드려요. ;)')
            return redirect(settings.LOGIN_URL)
    else:
        form = UserCreationForm()
    return render(request, 'form.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

