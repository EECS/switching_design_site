from django.shortcuts import render

# Create your views here.
def index(request):
    # Render the HTML template index.html with the data in the context variable
    show_testimonials = False
    trial_length = 14
    header_title = "Design Electronics"
    tag_break_lines = range(10)

    return render(
        request,
        'index.html',
        context={'header_title': header_title,
                'show_testimonials': show_testimonials,
                'trial_length':trial_length,
                'tag_break_lines': tag_break_lines}
    )