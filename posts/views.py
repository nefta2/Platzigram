"""Posts views."""

# Django
from django.shortcuts import render

# Utilities
from datetime import datetime

posts = [
    {
        'title': 'Sancocho de Patio',
        'user': {
            'name': 'Dundunsua',
            'picture': 'https://s2.aconvert.com/convert/p3r68-cdx67/t2xyi-rdja1.jpg',
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Barranquilla_-_Sancocho_de_mondongo.jpg/800px-Barranquilla_-_Sancocho_de_mondongo.jpg',
    },
    {
        'title': 'Uñas de curundú',
        'user': {
            'name': 'Roxana',
            'picture': 'https://s2.aconvert.com/convert/p3r68-cdx67/tpqzr-ahug1.jpg',
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://www.tuenlinea.com/wp-content/uploads/2018/08/Nail-Art-inspirado-chicas-s%C3%BAper-feministas.jpg',
    },
    {
        'title': 'Mi rosa',
        'user': {
            'name': 'Nito Cortizo',
            'picture': 'https://s2.aconvert.com/convert/p3r68-cdx67/tao3b-3bcw4.jpg',
        }, 
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://live.staticflickr.com/43/107602069_0d6211e5f1_c.jpg',
    },
]




def list_posts(request):
    """List existing posts."""
    return render(request, 'feed.html', {'posts': posts})
