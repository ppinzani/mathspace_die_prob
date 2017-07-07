from django.shortcuts import render
import timeit

from .forms import InputForm
from .functions import get_prob_div, get_prob_it, wrapper


# Create your views here.
def home_view(request):
    """
    This is the home view of the project, it shall render the input
    form for the n parameter and display the calculated probability.
    It also calculates the runtime  for various n cases, to make an
    analysys of the impact of n on the runtime
    """
    probability_div = None
    probability_it = None
    time_iter = None
    time_div = None
    time_measure_calls = 10

    if request.POST:
        form = InputForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['n']:
                n = int(form.cleaned_data['n'])
                probability_div = get_prob_div(n)
                probability_it = get_prob_it(n)
                # If the probability is really small display in scientific
                # notation to improve readibility
                if probability_div < 1e-10:
                    probability_div = "{:.22E}".format(probability_div)

                if probability_it < 1e-10:
                    probability_it = "{:.22E}".format(probability_it)

                # Get execution time for the calculations
                wrapped_div = wrapper(get_prob_div, n)
                wrapped_it = wrapper(get_prob_it, n)
                time_div = timeit.timeit(
                    wrapped_div,
                    number=time_measure_calls
                )
                time_iter = timeit.timeit(
                    wrapped_it,
                    number=time_measure_calls
                )
    else:  # If its a GET request
        form = InputForm()

    time_2_div = timeit.timeit(
        wrapper(get_prob_div, 2),
        number=time_measure_calls
    )
    time_10_div = timeit.timeit(
        wrapper(get_prob_div, 10),
        number=time_measure_calls
    )
    time_1000_div = timeit.timeit(
        wrapper(get_prob_div, 1000),
        number=time_measure_calls
    )
    time_2000_div = timeit.timeit(
        wrapper(get_prob_div, 2000),
        number=time_measure_calls
    )

    time_2_it = timeit.timeit(
        wrapper(get_prob_it, 2),
        number=time_measure_calls
    )
    time_10_it = timeit.timeit(
        wrapper(get_prob_it, 10),
        number=time_measure_calls
    )
    time_1000_it = timeit.timeit(
        wrapper(get_prob_it, 1000),
        number=time_measure_calls
    )
    time_2000_it = timeit.timeit(
        wrapper(get_prob_it, 2000),
        number=time_measure_calls
    )

    penalty_div = int(time_1000_div/time_2_div)
    penalty_it = int(time_1000_it/time_2_it)

    variables = {
        'form': form,
        'probability_div': probability_div,
        'probability_it': probability_it,
        'time_div': time_div,
        'time_iter': time_iter,
        'time_calls': time_measure_calls,
        'time_2_div': time_2_div,
        'time_10_div': time_10_div,
        'time_1000_div': time_1000_div,
        'time_2000_div': time_2000_div,
        'time_2_it': time_2_it,
        'time_10_it': time_10_it,
        'time_1000_it': time_1000_it,
        'time_2000_it': time_2000_it,
        'penalty_div': penalty_div,
        'penalty_it': penalty_it,
    }

    template = 'probability/home.html'

    return render(request, template, variables)
