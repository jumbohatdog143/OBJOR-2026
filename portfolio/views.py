from django.shortcuts import render, redirect
from .models import (
    Project,
    PersonalInformation,
    Education,
    Skill,
    Inquiry,
    Testimony
)
from .forms import (
    ProjectForm,
    InquiryForm,
    TestimonyForm
)


# -------------------------
# HOME PAGE
# -------------------------
def home(request):
    projects = Project.objects.all()
    info = PersonalInformation.objects.first()
    educations = Education.objects.all()
    skills = Skill.objects.all()

    return render(request, "index.html", {
        "projects": projects,
        "info": info,
        "educations": educations,
        "skills": skills,
    })


# -------------------------
# PROJECT LIST VIEW
# -------------------------
def project_list(request):
    projects = Project.objects.all()

    return render(request, "projects.html", {
        "projects": projects
    })


# -------------------------
# PROJECT DETAIL VIEW
# -------------------------
def project_detail(request, id):
    project = Project.objects.get(id=id)

    return render(request, "project_detail.html", {
        "project": project
    })


# -------------------------
# ADD PROJECT (FORM VIEW)
# -------------------------
def add_project(request):

    if request.method == "POST":
        form = ProjectForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("projects")

    else:
        form = ProjectForm()

    return render(request, "project_form.html", {
        "form": form
    })


# -------------------------
# PERSONAL INFORMATION
# -------------------------
def personal_information(request):
    info = PersonalInformation.objects.first()

    return render(request, "personal_information.html", {
        "info": info
    })


# -------------------------
# CONTACT / INQUIRY FORM
# -------------------------
def inquiry(request):

    if request.method == "POST":
        form = InquiryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("home")

    else:
        form = InquiryForm()

    return render(request, "inquiry_form.html", {
        "form": form
    })


# -------------------------
# TESTIMONY LIST VIEW
# -------------------------
def testimony_list(request):
    testimonies = Testimony.objects.all()

    return render(request, "testimony_list.html", {
        "testimonies": testimonies
    })


# -------------------------
# ADD TESTIMONY (FORM VIEW)
# -------------------------
def add_testimony(request):

    if request.method == "POST":
        form = TestimonyForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("testimony_list")

    else:
        form = TestimonyForm()

    return render(request, "testimony_form.html", {
        "form": form
    })


# -------------------------
# TESTIMONY DETAIL VIEW
# -------------------------
def testimony_detail(request, id):
    testimony = Testimony.objects.get(id=id)

    return render(request, "testimony_detail.html", {
        "testimony": testimony
    })


# -------------------------
# CUSTOM ERROR PAGES
# -------------------------
def custom_404(request, exception):
    return render(request, "404.html", status=404)


def custom_500(request):
    return render(request, "500.html", status=500)