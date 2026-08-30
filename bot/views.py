from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from ollama import chat, ChatResponse

def bot_view(request):

    conversation = request.session.get('conversation', [])
    conversation = [m for m in conversation if m['role'] != 'system']

    return render(request, 'bot/conversation.html', {'conversation':conversation})

def bot_action(request):
    conversation = request.session.get('conversation')
    if not conversation:
        conversation = [{
            "role": "system",
            "content": "Tu es un bot spécialisé dans le monde de Zelda. Tu t'appelles ZeldaBot. Tu dois répondre à l'utilisateur sur le ton d'un sage issu de l'univers de Zelda mais en restant toujours FRIENDLY. Ta réponse devra être en texte brut, sans AUCUN formatage.    Si la question ne concerne pas l'univers de Zelda, réponds UNIQUEMENT par une phrase de refus dans le ton d'un sage d'Hyrule (par exemple : 'Cette question s'égare hors des terres que je connais, voyageur.'). Ne traite JAMAIS le fond de la question dans ce cas, même partiellement."
        }]

    user_request = request.POST.get("prompt", "").strip()
    if not user_request:
        return redirect("bot:view")

    user_prompt = {
        "role": "user",
        "content": user_request
    }

    conversation.append(user_prompt)

    response: ChatResponse = chat(
        model='gemma3:4b',
        messages=conversation
    )

    request.session['conversation'] = conversation + [{ "role": "assistant", "content": response.message.content}]

    return redirect("bot:view")