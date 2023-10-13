from django.shortcuts import render

from text_to_html_generator.html_generator.forms import GeneratorForm


def converter_view(request):
    form = GeneratorForm()
    context = {
        "form": form
    }

    return render(request, 'html_generator_page.html', context)