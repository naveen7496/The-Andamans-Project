from django.shortcuts import render, get_object_or_404
from .models import Tribe


# Create your views here.
def tribes(request):
    tribes = Tribe.objects.all()
    context = {
        'tribes': tribes
    }
    return render(request, 'tribes/tribe_listings.html', context)


def tribe(request, tribe_id):
    tribe_object = get_object_or_404(Tribe, pk=tribe_id)
    context = {
        'tribe': tribe_object
    }
    return render(request, 'tribes/tribe.html', context)
