from django.shortcuts import render, get_object_or_404
from .models import Beach
# Create your views here.
def beaches(request):
    beaches = Beach.objects.all()
    context = {
        'beaches': beaches
    }
    return render(request, 'beaches/beach_listings.html', context)

def beach(request, beach_id):
    beach_object = get_object_or_404(Beach, pk=beach_id)
    context = {
        'beach': beach_object
    }
    return render(request, 'beaches/beach.html', context)