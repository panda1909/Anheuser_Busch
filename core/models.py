from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Brand(models.Model):
    Name = models.CharField(max_length=128, null=True, blank=True)


class Quarter(models.Model):
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)


class Sprint(models.Model):
    quarter = models.ForeignKey(Quarter, on_delete=models.CASCADE, related_name='sprint', null=True, blank=True)

    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)


class Objective(models.Model):
    Brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='brand_objective', null=True, blank=True)
    Quarter = models.ForeignKey(Quarter, on_delete=models.CASCADE, related_name='quarter_objective', null=True,
                                blank=True)

    objective = models.CharField(max_length=512, null=True, blank=True)
    completion = models.IntegerField(validators=[MinValueValidator(0)])


class SubObjective(models.Model):
    objective_fk = models.ForeignKey(Sprint, on_delete=models.CASCADE, related_name='objective_sub_objective',
                                     null=True, blank=True)
    sprint = models.ForeignKey(Sprint, on_delete=models.CASCADE, related_name='sprint_sub_objective', null=True,
                               blank=True)

    objective = models.CharField(max_length=512, null=True, blank=True)
    completion = models.BooleanField(default=False, null=True, blank=True)
