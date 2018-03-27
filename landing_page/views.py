from django.shortcuts import render

# Create your views here.
def index(request):
    # Render the HTML template index.html with the data in the context variable
    show_testimonials = False
    paid_site = False
    trial_length = 14
    header_title = "Design Electronics"
    tag_break_lines = range(10)

    show_power_electronics = True
    show_ana_electronics = False
    show_dig_electronics = True

    return render(
        request,
        'index.html',
        context={'header_title': header_title,
                'show_testimonials': show_testimonials,
                'trial_length':trial_length,
                'tag_break_lines': tag_break_lines,
                'paid_site':paid_site,
                'show_power_electronics':show_power_electronics,
                'show_ana_electronics':show_ana_electronics,
                'show_dig_electronics':show_dig_electronics}
    )