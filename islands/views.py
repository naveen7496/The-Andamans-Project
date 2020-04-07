from django.shortcuts import render, get_object_or_404
from .models import Island


# Create your views here.
def islandsListings(request):
    islands = Island.objects.all()
    # print(islands)
    context = {
        'islands': islands
    }
    return render(request, 'islands/island_listings.html', context)


def island(request, island_id):
    print("#########################",island_id)
    island_object = get_object_or_404(Island, pk=island_id)
    context = {
        'island': island_object
    }
    return render(request, 'islands/island.html', context)
