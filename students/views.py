from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm

def student_list(request):
    # Retrieve all students from the database
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

def student_add(request):
    # Handle adding a new student
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()  # Save the student data
            return redirect('student_list')  # Redirect to the list view
    else:
        form = StudentForm()  # Show an empty form for GET requests
    return render(request, 'students/student_form.html', {'form': form})

def student_delete(request, pk):
    # Handle deleting a student by primary key
    student = Student.objects.get(pk=pk)
    student.delete()  # Delete the student record from the database
    return redirect('student_list')  # Redirect to the list view
