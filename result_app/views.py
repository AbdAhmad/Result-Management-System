from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Subject, Student, Marks 
from .forms import StudForm, MarkForm
from django.contrib import messages

def sub(request):
    if request.method == 'POST':
        subname = request.POST.get('subname')
        subcode = request.POST.get('subcode').upper()
        maxmarks = request.POST.get('maxmarks')
        course = request.POST.get('course')
        branch = request.POST.get('branch').upper()
        sem = request.POST.get('sem')
        subject = Subject(Subject_Name = subname, Subject_Code = subcode, Max_Marks = maxmarks, Course = course, Branch = branch, Semester = sem)
        subject.save()
        return redirect('/')
    else:
        return render(request, 'AddSubject.html')

def stud(request):
    if request.method == 'POST':
        form = StudForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/stud')
        else:
            return redirect('/stud')
    else:
        form = StudForm()
        return render(request, 'AddStud.html',{'form':form})

def marks(request):
    if request.method == 'POST':
        roll = request.POST.get('roll')
        subcode = Subject.objects.get(id=request.POST.get('subcode'))                 
        form = MarkForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.roll = roll
            post.subjectcode = subcode
            post.save()
            return redirect('/search')
        else:     
            std = Student.objects.get(studroll=roll)
            return render(request,'AddMark.html',{'std':std,'form':form})
    else:
        return redirect('/search')

def search(request):
    if request.method=='POST':
        studroll = request.POST.get('studroll')
        std = Student.objects.get(studroll=studroll)
        form = MarkForm()
        return render(request,'AddMark.html',{'std':std,'form':form})
    else:
        return render(request,'search.html')

def login(request):
    if request.method=='POST':
        studroll = request.POST.get('studroll')
        std = Student.objects.get(studroll=studroll)
        marks = Marks.objects.all()
        form = marks.filter(roll=studroll)
        return render(request, 'oneview3.html',{'form': form, 'std':std})
    else:
        return render(request,'login.html')


