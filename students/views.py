from django.shortcuts import render, redirect
from .models import StudentsInfo
from .forms import studentForm
from django.contrib import messages

# Create your views here.
def student_list(request):
    students = StudentsInfo.objects.all()  

    return render(request, 'student_list.html', {'students': students})


def add_student(request):
    if request.method == 'POST':
        form = studentForm(request.POST)
        if form.is_valid():
            form.save() 
            messages.success(request, "Successfully Student Information Added")
            return redirect('student_list')
        else:
            return render(request, 'add_student.html', {'form': form})
    else:
        form = studentForm()  
        return render(request, 'add_student.html', {'form': form})


def update(request, roll):
    student = StudentsInfo.objects.get(id=roll)  

    if request.method == "POST":
        form = studentForm(request.POST, instance=student)  
        if form.is_valid():
            form.save()  
            messages.success(request, "Successfully Student Information Updated")
            return redirect('student_list')
        else:
            return render(request, 'add_student.html', {'form': form})
    else:
        form = studentForm(instance=student)  
        return render(request, 'add_student.html', {'form': form})


def delete(request, roll):
    student = StudentsInfo.objects.get(id=roll)  

    if student:
        student.delete() 
        messages.success(request, "Successfully Student Information Deleted")
    return redirect('student_list')
