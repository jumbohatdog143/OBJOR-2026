from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect

from .models import (
    Project,
    TechStack,
    PersonalInformation,
    Education,
    Skill,
    Inquiry,
    Testimony,
)

from .forms import (
    ProjectForm,
    TechStackForm,
    InquiryForm,
    TestimonyForm,
)


# =========================
# PUBLIC PORTFOLIO
# =========================

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


def project_list(request):
    projects = Project.objects.all()

    return render(request, "projects.html", {
        "projects": projects,
    })


def project_detail(request, id):
    project = Project.objects.get(id=id)

    return render(request, "project_detail.html", {
        "project": project,
    })


def personal_information(request):
    info = PersonalInformation.objects.first()

    return render(request, "personal_information.html", {
        "info": info,
    })


# =========================
# CONTACT / INQUIRY
# =========================

def inquiry(request):
    if request.method == "POST":
        form = InquiryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("home")

    else:
        form = InquiryForm()

    return render(request, "inquiry_form.html", {
        "form": form,
    })


# =========================
# TESTIMONIES
# =========================

def testimony_list(request):
    testimonies = Testimony.objects.all()

    return render(request, "testimony_list.html", {
        "testimonies": testimonies,
    })


def add_testimony(request):
    if request.method == "POST":
        form = TestimonyForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("testimony_list")

    else:
        form = TestimonyForm()

    return render(request, "testimony_form.html", {
        "form": form,
    })


def testimony_detail(request, id):
    testimony = Testimony.objects.get(id=id)

    return render(request, "testimony_detail.html", {
        "testimony": testimony,
    })


# =========================
# ADMIN AUTHENTICATION
# =========================

def admin_check(user):
    return user.is_authenticated and user.is_superuser


def admin_login(request):

    # If already logged in as admin, go directly to dashboard
    if request.user.is_authenticated and request.user.is_superuser:
        return redirect("dashboard")

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        # Only superusers are allowed to log in
        if user is not None and user.is_superuser:
            login(request, user)
            return redirect("dashboard")

        return render(request, "admin_login.html", {
            "error": "Invalid admin credentials."
        })

    return render(request, "admin_login.html")


@user_passes_test(admin_check, login_url="/admin-login/")
def admin_logout(request):
    logout(request)

    return redirect("admin_login")


# =========================
# ADMIN DASHBOARD
# =========================

@user_passes_test(admin_check, login_url="/admin-login/")
def dashboard(request):

    # ForeignKey uses select_related()
    projects = Project.objects.select_related("tech_stack").all()

    # TechStack -> Projects uses the related_name "projects"
    tech_stacks = TechStack.objects.prefetch_related("projects").all()

    return render(request, "dashboard.html", {
        "projects": projects,
        "tech_stacks": tech_stacks,
    })


# =========================
# CREATE PROJECT
# =========================

@user_passes_test(admin_check, login_url="/admin-login/")
def add_project(request):

    if request.method == "POST":

        form = ProjectForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("dashboard")

    else:
        form = ProjectForm()

    return render(request, "project_form.html", {
        "form": form,
    })


# =========================
# CREATE TECH STACK
# =========================

@user_passes_test(admin_check, login_url="/admin-login/")
def add_tech_stack(request):

    if request.method == "POST":

        form = TechStackForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("dashboard")

    else:
        form = TechStackForm()

    return render(request, "tech_stack_form.html", {
        "form": form,
    })


# =========================
# CUSTOM ERROR PAGES
# =========================

def custom_404(request, exception):
    return render(request, "404.html", status=404)


def custom_500(request):
    return render(request, "500.html", status=500)