import sys
from django.shortcuts import render, redirect
from engine_app.forms import FeedbackForm, ContactForm
from engine_app.models import Feedback, Project, Contact, ProjectGallery


def index_page(request):
    feedbacks = Feedback.objects.all()
    return render(request, "index.html", {"feedbacks": feedbacks})


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
    project_images = ProjectGallery.objects.filter(project=id)
    return render(request, "project-details.html",
                  {"project": project, "project_gallery": project_images})


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


def submit_user_contact_details(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        print(f"Form is valid = {form.is_valid()}")
        if form.is_valid():
            try:
                form.save()
                return redirect('/contact/')
            except Exception as e:
                print(f'System Exception Information = {sys.exc_info()}')
                print(f'Exception = {e}')
        else:
            print(f"Form Error = {form.errors}")

    else:
        form = Contact()

    return render(request, 'contact.html', {'form': form})
