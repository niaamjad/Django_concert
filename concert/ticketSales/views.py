from django.shortcuts import render
from .models import concertmodel , locationmodel , timemodel
from django.contrib.auth.decorators import login_required



@login_required
def ConcertListView(request):
    conserts = concertmodel.objects.all()
    return render(request, 'ticketSales\concertlist.html', {'conserts': conserts ,'concerts_count' : conserts.count()})



@login_required
def LocationListView(request):
    locations = locationmodel.objects.all()
    return render(request, 'ticketSales\locationlist.html', {'locationlist': locations})
    



@login_required
def ConcertdetailView(request, concert_id):
    concert = concertmodel.objects.get(id=concert_id)
    return render(request, 'ticketSales\concertdetail.html', {'concert': concert})
 



@login_required
def TimeListView(request):
    times = timemodel.objects.all()
    return render(request, 'ticketSales\timelist.html', {'times': times})
    
    

@login_required
def profileView(request):
        profile = request.user.profilemodel
        return render(request, 'ticketSales\profile.html', {'profile': profile})

    
@login_required
def TicketListView(request):
    tickets = request.user.ticketmodel_set.all()
    return render(request, 'ticketSales\ticketlist.html', {'tickets': tickets})
   

 



