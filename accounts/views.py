from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout

def login_view(request):

    next_url = request.GET.get('next')

    if request.method == 'POST':
        login_form = AuthenticationForm(request, data=request.POST)

        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            if next_url:
                return redirect(next_url)
            else:
                return redirect("home")
    else:
        login_form = AuthenticationForm()

    return render(request, 'login.html', {'login_form': login_form})

def logout_view(request):
    logout(request)
    return redirect('accounts:login_form')