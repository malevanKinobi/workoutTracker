from django.shortcuts import render

from training.models import TrainingProgram


# Create your views here.
def training_program(request):
    programs = TrainingProgram.objects.all()
    return render(request, 'training/training_program/programs.html', {"programs": programs})

def training_program_details(request, id):
    program = TrainingProgram.objects.get(id=id)
    return render(request, 'training/training_program/program.html', {"program": program})