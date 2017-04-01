from django.conf.urls import url, include
from runehas import views as runehas_views

urlpatterns = [
    url(r'^$', runehas_views.index, name='index'),
    url(r'^book_hostel/', runehas_views.bookhostel, name='hostelbookingroomsearch'),
    url(r'^allocation_confirmation/', runehas_views.confirmhostelbook, name='hostelbookingconfirmation'),
    url(r'^print_receipt/', runehas_views.printhostelreceipt, name='hostelbookingreceipt'),
]
