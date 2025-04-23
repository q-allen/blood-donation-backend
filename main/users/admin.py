from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.models import Group
# Register your models here.
admin.site.site_header = "Blood Donation Admin"
admin.site.site_title = "Blood Donation Admin Portal"
admin.site.index_title = "Welcome to Blood Donation Admin Portal"
admin.site.site_url = "/admin/"  # Redirect to the admin page after login   
admin.site.enable_nav_sidebar = True  # Disable the sidebar for a cleaner look
admin.site.register(CustomUser)  # Register the CustomUser model to the admin site
admin.site.unregister(Group)