"""Posts views."""

# Django
from django.http import HttpResponse

# Utilities
from datetime import datetime

posts = [
    {
        'name': 'Mont Blac',
        'user': 'Yesica Cortes',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/id/237/200/200',
    },
    {
        'name': 'Cocina',
        'user': 'Sancocho',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/id/1025/200/300',
    },
    {
        'name': 'Pajaros',
        'user': 'Pescuezo Pelao',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/id/1024/200/200',
    }
]




def list_posts(request):
    """List existing posts."""
    content= []
    for post in posts:
        content.append("""
        <p><strong>{name}</strong></p>
        <p><small>{user} - <i> {timestamp}</i></small></p>
        <figure><img src="{picture}"/></figure>
        """.format(**post))
    return HttpResponse('<br>'.join(content))
