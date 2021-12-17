from core.models import Quarter
from datetime import date

def check_date():
    current_date = date
    first_of_year = date(date.today().year, 1, 1)
    if current_date == first_of_year:
        Quarter.objects.create(start_date=date.year-1-1, end_date=date.year-3-31)
    else:
        return False