from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    
    # Add context in the view to render
    context = {
        "name": "Sanu",
        "age": 40 
    }

    # Render view with html template
    return render(request, "second_page.html", context)