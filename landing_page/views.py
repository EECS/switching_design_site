from django.shortcuts import render
from .models import landing_page_header, landing_page_home

# Create your views here.
def index(request):
    # Render the HTML template index.html with the data in the context variable
    test = landing_page_header.objects.all()

    for o in test:
        print(o.pk)

    return render(
        request,
        'index.html',
        context={'header_title': test[0].name}
    )