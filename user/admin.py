from django.contrib import admin

# Register your models here.
from user.models import Profile, Event, Participation


admin.site.register(Event)


class ParticipationAdmin(admin.ModelAdmin):
    list_display = ['name', 'en', 'event', 'cost', 'verified']
    list_editable = ['verified']
    list_filter = ['verified', 'event', 'user__first_name']
    search_fields = ['user__first_name', 'user__profile__encarta_id']

    def name(self, obj):
        return obj.user.first_name + ' ' + obj.user.last_name

    def en(self,obj):
        return obj.user.profile.encarta_id

    def cost(self,obj):
        return obj.event.cost

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'mobile', 'current_year_of_study', 'encarta_id']
    search_fields = ['encarta_id']

    def name(self, obj):
        return obj.user.first_name + ' ' + obj.user.last_name

admin.site.register(Participation, ParticipationAdmin)
admin.site.register(Profile, ProfileAdmin)