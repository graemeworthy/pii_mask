# Create your views here.
from django.http import HttpResponse

from people.models import Person
from pii_mask.pii_context import show_pii

PII_KEY = "pii"
MASK_VALUE = "hide"
UNMASK_VALUE = "show"


def index(request):
    button_text = "UNMASK"
    button_value = UNMASK_VALUE
    if request.GET.get(PII_KEY) == UNMASK_VALUE:
        button_text = "MASK"
        button_value = MASK_VALUE
        show_pii()

    person_name = Person.objects.first().name
    page = f"""
    <!DOCTYPE html>
    <html>
        <head>
            <meta charset="utf-8">
        </head>
        <body>

            <p>Hello, {person_name}.<p>
            <form method="get">
                <button name="pii" value="{button_value}">
                  {button_text}
                </button>
            </form>
        </body>
    </html>
    """

    return HttpResponse(page)
