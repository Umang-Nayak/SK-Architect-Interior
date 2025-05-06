import sys
from django.shortcuts import render, redirect
from engine_app.forms import FeedbackForm
from engine_app.models import Feedback, Project


def index_page(request):
    return render(request, "index.html")


def about_us_page(request):
    feedbacks = Feedback.objects.all()
    return render(request, "about.html", {"feedbacks": feedbacks})


def service_page(request):
    return render(request, "services.html")


def project_page(request):
    all_projects = Project.objects.all()
    return render(request, "projects.html", {"projects": all_projects})


def project_detail_page(request, id):
    project = Project.objects.filter(id=id).first()
    return render(request, "project-details.html", {"project": project})


def contact_page(request):
    return render(request, "contact.html")


def submit_user_feedback(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        print(f"Form is valid = {form.is_valid()}")
        if form.is_valid():
            try:
                form.save()
                return redirect('/about-us')
            except Exception as e:
                print(f'System Exception Information = {sys.exc_info()}')
                print(f'Exception = {e}')
        else:
            print(f"Form Error = {form.errors}")

    else:
        form = Feedback()

    return render(request, 'about.html', {'form': form})
