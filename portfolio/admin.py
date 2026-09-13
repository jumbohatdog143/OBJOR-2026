from django.contrib import admin
from .models import Project, PersonalInformation, Education, Skill,Testimony, Inquiry 


admin.site.register(Project)
admin.site.register(PersonalInformation)
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(Testimony)
admin.site.register(Inquiry)