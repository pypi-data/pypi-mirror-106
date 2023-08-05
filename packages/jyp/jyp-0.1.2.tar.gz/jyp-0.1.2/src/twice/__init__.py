from .fetching import fetch
from .processing import process
from .sending import send

def communicate():
    """
    Send a text message containing all information relevant to
    Korean to Canadian currency exchange rates and trends.
    """
    response = fetch()
    process(response)
    send(response)
