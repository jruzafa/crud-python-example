from freelancemanager.models import User,Customer,Work
from django.contrib import admin


class UserAdmin(admin.ModelAdmin):
    # ...
    list_display = ('name','email')

class CustomerAdmin(admin.ModelAdmin):
    # ...
    list_display = ('name','website')
   

class WorkAdmin(admin.ModelAdmin):
    # ...
    list_display = ('name','customer','paid')

admin.site.register(Customer, CustomerAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Work, WorkAdmin)