from django.shortcuts import render, get_list_or_404
from quest_board.models import Quest

# Create your views here.
def home(request):
    available_quest_count = get_list_or_404(Quest, is_completed=False).__len__()
    finished_quest_count = get_list_or_404(Quest, is_completed=True).__len__()
    quest_count = get_list_or_404(Quest).__len__()
    context = {
        "nb_available_quest": available_quest_count,
        "nb_finished_quest": finished_quest_count,
        "nb_quests": quest_count
    }
    return render(request, "pages/homepage.html", context)