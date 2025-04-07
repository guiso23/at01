from django.shortcuts import render, get_list_or_404
from .models import Gun

def home(resquest):
 guns = Gun.objects.all()
 return render('home.html',{'guns':guns})

def details(resquest, gun_id):
    gun = get_list_or_404 (Gun, pk= gun_id)
    return render(resquest, 'details.html', {'gun':gun})
