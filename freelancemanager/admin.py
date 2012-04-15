from freelancemanager.models import User,Client,Work
from django.contrib import admin

class ClientAdmin(admin.ModelAdmin):
    # ...
    list_display = ('name','email')

class UserAdmin(admin.ModelAdmin):
    # ...
    list_display = ('name','email')

class WorkAdmin(admin.ModelAdmin):
    # ...
    list_display = ('name','client','paid')

admin.site.register(Client, ClientAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Work, WorkAdmin)