from django.shortcuts import render
from .models import ConverterEquation

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

    input_voltage = 24
    output_voltage = 5
    output_current = 3
    q1_on_res = 25 #milliOhms
    d1_on_volt = 0.7
    inductor_res = 5 #milliohms
    capacitor_res = 10 #milliohms
    inductance = 10 #microhenries
    capacitance = 100 #microfarads
    load_res = 1.67 #ohms

    #Get model parameters
    test = ConverterEquation.objects.filter(name="Landing Page Example")

    if len(test) > 0:
        print(test[0].input_output_transfer)

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
                'show_dig_electronics':show_dig_electronics,
                'input_voltage':input_voltage,
                'output_voltage':output_voltage,
                'output_current':output_current,
                'q1_on_res':q1_on_res,
                'd1_on_volt':d1_on_volt,
                'inductor_res':inductor_res,
                'capacitor_res':capacitor_res,
                'inductance':inductance,
                'capacitance':capacitance}
    )