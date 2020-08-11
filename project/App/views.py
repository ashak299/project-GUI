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
            'decryptionButton' : "Decryption", 
            'extensionMessage' : "Files to be encrypted must have extension: .txt, .docx and decryption requires files with extension: .enc",
            
        }
    )

def EncryptPage(request):
    return render(
        request,
        "App/EncryptPage.html",
        {
            'title' : "Encrypt Page",
            'chooseFile' : "Encryption",
            'extensionMessage' : "Files to be encrypted must have extension: .txt, .docx"
        }
    )

def DecryptPage(request):
    return render(
        request,
        "App/DecryptPage.html",
        {
            'title' : "Decrypt Page",
            'head' : "Decryption",
            'extensionMessage' : "Files to be decrypted must have extension: .enc"
        }
    )