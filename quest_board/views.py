from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Quest, Places

# Create your views here.
def quest_list(request):
    current_selected = request.GET.get("selected","").strip()
    print(current_selected)
    quests = Quest.objects.all()

    if current_selected:
        filter_pattern = (current_selected == "finished")
        print(filter_pattern)
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