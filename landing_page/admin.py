from django.contrib import admin
from .models import landing_page_header
from .models import landing_page_home
from .models import landing_page_content

# Register your models here.
admin.site.register(landing_page_header)
admin.site.register(landing_page_home)
admin.site.register(landing_page_content)
