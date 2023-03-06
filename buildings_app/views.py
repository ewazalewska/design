from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required

def all_objects(request):
    all_buildings = Project.objects.all()
    return render(request, 'design.html', {"objects" : all_buildings})

@login_required
def new_building(request):
    form_building = ProjectForm(request.POST or None, request.FILES or None)

    if form_building.is_valid():
        form_building.save()
        return redirect(all_objects)

    return render(request, 'building_form.html',
                  {'form': form_building, 'nowy':True})

@login_required
def edit_building(request, id):
    building = get_object_or_404(Project, pk=id)
    form_building = ProjectForm(request.POST or None, request.FILES or None, instance=building)

    if form_building.is_valid():
        form_building.save()
        return redirect(all_objects)

    return render(request, 'building_form.html',
                  {'form': form_building, 'nowy': False})

@login_required
def delete_building(request, id):
    building = get_object_or_404(Project, pk=id)
    if request.method == "POST":
        building.delete()
        return redirect(all_objects)
    return render(request, 'delete_accept.html', {'building': building})
