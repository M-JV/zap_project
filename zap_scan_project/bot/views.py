from django.shortcuts import render,reverse
from .models import ChatBot
from django.http import HttpResponseRedirect, JsonResponse
from embedchain import App
import os


config = {
  'llm': {
    'provider': 'google',
    'config': {
      'model': 'gemini-1.5-pro-latest',
      'top_p': 0.5,
      'temperature': 0.64
    }
  },
  'embedder': {
    'provider': 'google',
    'config': {
      'model': 'models/embedding-001',
      'task_type': 'retrieval_document'
    }
  }
}



os.environ["GOOGLE_API_KEY"]="AIzaSyAdu6M5CTz6cDeLOvUTEJNp3n9atrG2bDU"
app=App.from_config(config=config)

def ask(request):
    if request.method == "POST":
        text = request.POST.get("text")
        app.add('zap_scan_project/csv_output/scan_results.csv',data_type='csv')
        app.add('http://127.0.0.1:8000/report/',data_type='web_page')
        response = app.query(text)
        
        # Extract necessary data from response
        if isinstance(response, str):
            response_data = {"text": response}
        else:
            response_data = {"text": response.text}

        return JsonResponse({"data": response_data})
    else:
        return HttpResponseRedirect(reverse("chat"))


def chat(request):
    chats = ChatBot.objects.all()
    return render(request, "chatbot.html", {"chats": chats})

app.reset() 

