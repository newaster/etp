from django.contrib import admin
from .models import User_addon,user_approval,fault,site,ticket,zones,etpflow,UserProfile



admin.site.register(User_addon)

admin.site.register(user_approval)

admin.site.register(fault)

admin.site.register(ticket)

admin.site.register(zones)

admin.site.register(etpflow)

admin.site.register(UserProfile)


class SiteAdmin(admin.ModelAdmin):
    search_fields = ['smno'] 
    list_display = ['name', 'smno', 'city', 'status', 'dnt', 'ud']


admin.site.register(site,SiteAdmin)



