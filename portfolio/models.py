from django.db import models

class Project(models.Model):
    project_name = models.CharField(max_length=100)
    description = models.TextField()
    tech_stack = models.CharField(max_length=200)
    project_link = models.URLField(blank=True)

    def __str__(self):
        return self.project_name

class PersonalInformation(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    summary = models.TextField()

    contact_number = models.CharField(max_length=20)
    student_email = models.EmailField()
    personal_email = models.EmailField()

    address = models.TextField()

    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)

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
    description = models.TextField(blank=True)

    def __str__(self):
        return self.school_name

class Skill(models.Model):
    skill_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=100, default="fas fa-code")

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