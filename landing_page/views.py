from django.shortcuts import render
import math, re, numexpr
from .models import ConverterEquation

def js_math(transfer_function):
    num_points = 500

    start_frequency = 1 #Hz
    end_frequency = 11 #kHz
    step_size = int(((end_frequency*1000)-start_frequency)/num_points)

    bode_x_range = [step for step in range(start_frequency, end_frequency*1000, step_size)]

    #Define circuit parameters to graph
    vals = {"R1": '100', "R2":'10000'}
    #Replace symbols with values defined in vals dictionary
    for k, v in vals.items():
        #Find key and only the key. Example, finds R1 and not R11 by separating on the non-word boundary.
        transfer_function = re.sub(r"\b"+k+r"\b", v, transfer_function)

    print(transfer_function)
    print(numexpr.evaluate(transfer_function))

    for f in bode_x_range:
        pass

    return bode_x_range

# Create your views here.
def index(request):
    #####################################
    #Index.html parameters
    #####################################
    show_testimonials = False
    paid_site = False
    trial_length = 14
    header_title = "Design Electronics"
    tag_break_lines = range(10)

    show_power_electronics = True
    show_ana_electronics = False
    show_dig_electronics = True

    #####################################
    #Circuit Parameters
    #####################################
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

    #####################################
    #Model Parameters
    #####################################
    modelQuery = ConverterEquation.objects.filter(name="Landing Page Example")

    if len(modelQuery) > 0:
        input_output_transfer = modelQuery[0].input_output_transfer
        input_impedance = modelQuery[0].input_impedance
        output_impedance = modelQuery[0].output_impedance
        duty_output_transfer = modelQuery[0].duty_output_transfer
        print(input_impedance)

    bode_x_range = js_math(input_output_transfer)

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
                'capacitance':capacitance,
                'bode_x_range': bode_x_range}
    )