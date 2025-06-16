import datetime


def current_year(request):
    """
    Context processor to add the current year to the template context.
    This allows templates to display the current year dynamically.
    """
    return {"current_year": datetime.date.today().year}
