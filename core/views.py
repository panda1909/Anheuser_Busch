import datetime

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import get_object_or_404, get_list_or_404
from core.models import *
from core.forms import *
import datetime
import random


# Create your views here.


@login_required()
def home(request):
    brands = Brand.objects.all()
    labels = []
    data = []
    colour = ["red", "blue", "green", "yellow", "purple", "orange", "black"]
    rand_colours = [random.choice(colour) for i in range(brands.count())]
    for x in brands:
        labels.append(x.name)
        if x.get_current_objective():
            data.append(x.get_current_objective().completion)
        else:
            data.append(0)
    context = {
        'obj': brands,
        'label': labels,
        'data': data,
        'colors': rand_colours
    }
    return render(request, 'core/index.html', context)


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
            return redirect('core:home')
    else:
        form = BrandFrom()

    return render(request, 'core/create_brand.html', {'form': form})


def view_brand(request, pk):
    obj = get_object_or_404(Brand, id=pk)
    curr = datetime.date.today()
    quarter = get_object_or_404(Quarter, start_date__lt=curr, end_date__gt=curr)
    objectives = Objective.objects.filter(Brand=obj, Quarter=quarter)
    sub_objectives = SubObjective.objects.filter(Objective_fk__in=objectives)
    sprints = Sprint.objects.filter(Quarter=quarter, SubObjective__in=sub_objectives)

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
                return redirect(f'core:brand-detail', pk=obj.pk)
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
            return redirect('core:home')
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
            return redirect('core:home')
    else:
        form = ObjectiveFrom(instance=obj)

    return render(request, 'core/update_objective.html', {'form': form})


@login_required()
def add_sprint(request):
    if request.method == 'POST':
        form = SprintForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:home')
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
            return redirect('core:home')
    else:
        form = SprintForm(instance=obj)

    return render(request, 'core/update_sprint.html', {'form': form})


@login_required()
def add_sub_objective(request):
    if request.method == 'POST':
        form = SubObjectiveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:home')
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
            return redirect('core:home')
    else:
        form = SubObjectiveForm(instance=obj)

    return render(request, 'core/update_sub-objective.html', {'form': form})
