import datetime

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import get_object_or_404, get_list_or_404
from core.models import *
from core.forms import *
import datetime


# Create your views here.


def superuser_test(user):
    return user.is_superuser


@login_required()
def home(request):
    brands = Brand.objects.all()
    return render(request, 'core/index.html', {'obj': brands})


def brands(request):
    brands = Brand.objects.all()
    return render(request, 'core/brands.html', {'brands': brands})

'''
Brand CRUD operations
'''


@user_passes_test(lambda u: u.is_superuser)
def create_brand(request):
    if request.method == 'POST':
        form = BrandFrom(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = BrandFrom()

    return render(request, 'core/create_brand.html', {'form': form})


def view_brand(request, pk):
    obj = get_object_or_404(Brand, id=pk)
    curr = datetime.date.today()
    quarter = Quarter.objects.get(start_date__lt=curr, end_date__gt=curr)
    objectives = Objective.objects.filter(Brand=obj, Quarter=quarter)
    sprints = Sprint.objects.filter(Quarter=quarter)
    sub_objectives = SubObjective.objects.filter(Objective_fk__in=objectives, Sprint__in=sprints)

    context = {
        'obj': obj,
        'quarter': quarter,
        'objectives': objectives,
        'sprints': sprints,
        'sub_objectives': sub_objectives,
    }

    return render(request, 'core/brand-detail.html', context)


@user_passes_test(lambda u: u.is_superuser)
def delete_brand(request, pk):
    obj = get_object_or_404(Brand, id=pk)
    obj.delete()
    return redirect('core:home')


@login_required()
def update_brand(request, pk):
    obj = get_object_or_404(Brand, id=pk)

    if request.user.id == obj.PO.id or request.user.id == obj.scrum_master.id:
        if request.method == 'POST':
            form = BrandFrom(request.POST, instance=obj)
            if form.is_valid():
                form.save()
        else:
            form = BrandFrom(instance=obj)
    else:
        return redirect('core:home')


    context = {
        'form': form,
    }
    return render(request, 'core/update-brand.html', context)


'''
Objective CRUD operations
'''


@login_required()
@user_passes_test(lambda u: u.is_superuser)
def add_objective(request):
    if request.method == 'POST':
        form = ObjectiveFrom(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ObjectiveFrom

    return render(request, 'core/add_objective.html', {'form': form})

@login_required()
def update_objective(request, pk):
    obj = get_object_or_404(Objective, id=pk)
    if request.method == 'POST':
        form = ObjectiveFrom(request.POST, instance=obj)
        if form.is_valid():
            form.save()
    else:
        form = ObjectiveFrom(instance=obj)

    return render(request, 'core/update_objective.html', {'form': form})


@login_required()
def add_sprint(request):
    if request.method == 'POST':
        form = SprintForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SprintForm

    return render(request, 'core/add_sprint.html', {'form': form})


@login_required()
def update_sprint(request, pk):
    obj = get_object_or_404(Sprint, id=pk)
    if request.method == 'POST':
        form = SprintForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
    else:
        form = SprintForm(instance=obj)

    return render(request, 'core/update_sprint.html', {'form': form})


@login_required()
def add_sub_objective(request):
    if request.method == 'POST':
        form = SubObjectiveForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SubObjectiveForm

    return render(request, 'core/add_subobjective.html', {'form': form})

@login_required()
def update_sub_objective(request, pk):
    obj = get_object_or_404(SubObjective, id=pk)
    if request.method == 'POST':
        form = SubObjectiveForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
    else:
        form = SubObjectiveForm(instance=obj)

    return render(request, 'core/update_sub-objective.html', {'form': form})