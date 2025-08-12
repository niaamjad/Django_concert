from django.urls import path
from .views import ConcertListView , LocationListView , ConcertdetailView , TimeListView , TicketListView 


urlpatterns = [
    path('concerts/', ConcertListView),
    path('locations/' , LocationListView),
    path('concerts/<int:concert_id>/', ConcertdetailView),
    path('times/', TimeListView),
    path('tickets/' , TicketListView)
]