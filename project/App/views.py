from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


# Create your views here.
def index(request):

    return render(
        request,
        "App/index.html",  # Relative path from the 'templates' folder to the template file
        {
            'title' : "Start Page",
            'message' : "Choose Encryption or Decryption",
            'encryptionButton' : "Encryption",
            'decryptionButton' : "Decryption" 
            
        }
    )