from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Quest, Places

# Create your views here.
def quest_list(request):
    quests = Quest.objects.all()
    print(quests)
    places = Places.objects.all()
    context = {
        "quests": quests,
        "places": places
    }

    return render(request, "quest_board/quest_list.html", context)

def quest_detail(request, slug:str):
    quest = get_object_or_404(Quest, slug=slug)

    context = {
        "quest": quest
    }

    render(request, "quest_board/quest_detail.html", context)