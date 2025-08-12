from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate , login , logout
from django.urls import reverse 
import ticketSales.views
from django.conf import settings



def LoginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request , user)
            if request.GET.get('next'):
                return HttpResponseRedirect(request.GET.get('next'))
            
            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
        else:
            context = {'error' : 'نام کاربری یا رمز عبور اشتباه است.'}
            return render(request , 'account/login.html', context )
        
    return render(request , 'account/login.html')



def LogoutView(request):
    if request.user.is_authenticated:
        logout(request)
    return HttpResponseRedirect(reverse(ticketSales.views.ConcertListView))



def ProfileView(request):
    if request.user.is_authenticated:
        profile = request.user.profilemodel
        return render(request, 'account/profile.html', {'profile': profile})
    return HttpResponseRedirect(reverse('account:login'))

