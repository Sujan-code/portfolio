from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(service)
admin.site.register(blog)
admin.site.register(contact)
admin.site.register(work)
admin.site.register(education)
admin.site.register(experience)
