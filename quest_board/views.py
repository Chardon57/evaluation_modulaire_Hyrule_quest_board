from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from django.http import HttpResponse
from .models import Quest, Places

# Create your views here.
def quest_list(request):
    current_selected = request.GET.get("selected","").strip()
    print(current_selected)
    quests = Quest.objects.all()

    if current_selected:
        filter_pattern = (current_selected == "finished")
        quests = quests.filter(is_completed=filter_pattern)
        
    context = {
        "quests": quests,
        "current_selected": current_selected
    }

    return render(request, "quest_board/quest_list.html", context)

def quest_detail(request, slug:str):
    quest = get_object_or_404(Quest, slug=slug)
    context = {
        "quest": quest
    }

    return render(request, "quest_board/quest_detail.html", context)

def places_list(request):
    places = Places.objects.annotate(nb_quests = Count("quests"))
    context = {
        'places': places
    }
    return render(request, "quest_board/places_list.html", context)

def place_detail(request, slug:str):
    place = get_object_or_404(Places, slug=slug)
    quests = place.quests.all()
    context = {
        'place': place,
        'quests': quests
    }
    return render(request, "quest_board/place_detail.html", context)