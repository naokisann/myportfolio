from django.contrib import admin
from .models import Blog

# register model to admin site.
# you can edit content of models.

admin.site.register(Blog)
