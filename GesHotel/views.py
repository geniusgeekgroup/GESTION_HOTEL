from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def acceuil(request):
    """ Accueil de mon app rest erp """

    text = """

           <h1>Bienvenue POLLS </h1>
            <p> SAINT FOUTRIER ONESYME DEVELOPPEUR PYTHON DJANGO ! </p>

       """
    return render(request, "GesHotel/index.html", {})
