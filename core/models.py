from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
import datetime


# Create your models here.
class Brand(models.Model):
    PO = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='po')
    scrum_master = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                     related_name='scrum_master')

    name = models.CharField(max_length=128, null=True, blank=True)
    logo = models.FileField(upload_to='brnad_logos', null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

    def get_current_objective(self):
        curr = datetime.date.today()
        quarter = Quarter.objects.get(start_date__lt=curr, end_date__gt=curr)
        objective = Objective.objects.filter(Quarter=quarter, Brand=self).first()
        return objective

    def get_current_sub_objective(self):
        curr = datetime.date.today()
        sprint = Sprint.objects.get(Brand=self, start_date__lt=curr, end_date__gt=curr)
        sub_objective = SubObjective.objects.filter(Sprint=sprint).first()
        return sub_objective



class Quarter(models.Model):
    name = models.CharField(max_length=12, null=True, blank=True)

    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


class Sprint(models.Model):
    Quarter = models.ForeignKey(Quarter, on_delete=models.CASCADE, related_name='sprint', null=True, blank=True)
    Brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='brand_sprint', null=True, blank=True)

    name = models.CharField(max_length=128, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.name} {self.start_date} - {self.end_date} '


class Objective(models.Model):
    Brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='brand_objective', null=True, blank=True)
    Quarter = models.ForeignKey(Quarter, on_delete=models.CASCADE, related_name='quarter_objective', null=True,
                                blank=True)

    objective = models.CharField(max_length=512, null=True, blank=True)
    completion = models.IntegerField(validators=[MinValueValidator(0)])

    def __str__(self):
        return f'{self.objective}'


class SubObjective(models.Model):
    Objective_fk = models.ForeignKey(Objective, on_delete=models.CASCADE, related_name='sub_objective',
                                     null=True, blank=True)
    Sprint = models.ForeignKey(Sprint, on_delete=models.CASCADE, related_name='sprint_sub', null=True,
                               blank=True)

    objective = models.CharField(max_length=512, null=True, blank=True)
    completion = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return f'{self.objective}'