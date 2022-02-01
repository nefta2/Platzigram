"""Posts views."""

# Django
from turtle import width
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Utilities
from datetime import datetime

posts = [
    {
        'title': 'Sancocho de Patio',
        'user': {
            'name': 'Dundunsua',
            'picture': 'https://i.postimg.cc/TwXCrM7k/49906995-355460195005805-3926332708066558657-n1-1.jpg',
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Barranquilla_-_Sancocho_de_mondongo.jpg/800px-Barranquilla_-_Sancocho_de_mondongo.jpg',
    },
    {
        'title': 'Uñas de curundú',
        'user': {
            'name': 'Roxana',
            'picture': 'https://i.postimg.cc/fbYvWqzY/aohqw-ssmk9.jpg',
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://www.tuenlinea.com/wp-content/uploads/2018/08/Nail-Art-inspirado-chicas-s%C3%BAper-feministas.jpg',
    },
    {
        'title': 'Mi rosa',
        'user': {
            'name': 'Nito Cortizo',
            'picture': 'https://i.postimg.cc/Fs2cfbnp/avoth-5ymg5.jpg',
        }, 
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://live.staticflickr.com/43/107602069_0d6211e5f1_c.jpg',
    },
]



@login_required
def list_posts(request):
    """List existing posts."""
    return render(request, 'posts/feed.html', {'posts': posts})
