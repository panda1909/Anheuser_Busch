from core.models import Quarter
import datetime


def check_date():
    current_date = datetime.date.today()
    first_of_year = datetime.date(datetime.date.today().year, 1, 1)
    if current_date == first_of_year:
        Quarter.objects.create(name='Q1', start_date=datetime.date(current_date.year, 1, 1),
                               end_date=datetime.date(current_date.year, 3, 31))
        Quarter.objects.create(name='Q2', start_date=datetime.date(current_date.year, 4, 1),
                               end_date=datetime.date(current_date.year, 6, 30))
        Quarter.objects.create(name='Q3', start_date=datetime.date(current_date.year, 7, 1),
                               end_date=datetime.date(current_date.year, 9, 30))
        Quarter.objects.create(name='Q4', start_date=datetime.date(current_date.year, 10, 1),
                               end_date=datetime.date(current_date.year, 12, 31))
    else:
        pass
