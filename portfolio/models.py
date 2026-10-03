from django.db import models


class TechStack(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    project_name = models.CharField(max_length=100)
    description = models.TextField()

    tech_stack = models.ForeignKey(
        TechStack,
        on_delete=models.CASCADE,
        related_name='projects'
    )

    project_link = models.URLField()

    def __str__(self):
        return self.project_name


class PersonalInformation(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    summary = models.TextField()
    contact_number = models.CharField(max_length=20)
    address = models.TextField()
    personal_email = models.EmailField()
    facebook = models.URLField(max_length=200)
    github = models.URLField(max_length=200)
    instagram = models.URLField(max_length=200)
    linkedin = models.URLField(max_length=200)
    student_email = models.EmailField()
    profile_picture = models.ImageField(
        upload_to='profile_pictures/',
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Education(models.Model):
    school_name = models.CharField(max_length=150)
    degree = models.CharField(max_length=150)
    year = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return f"{self.school_name} - {self.degree}"


class Skill(models.Model):
    skill_name = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=100)

    def __str__(self):
        return self.skill_name


class Testimony(models.Model):
    full_name = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.full_name


class Inquiry(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()
    message = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"