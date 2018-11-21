from django.contrib import admin

# Register your models here.
from user.models import Profile, Event, Participation

admin.site.register(Profile)
admin.site.register(Event)


class ParticipationAdmin(admin.ModelAdmin):
    list_display = ['name', 'en', 'event', 'cost', 'verified']
    list_editable = ['verified']
    list_filter = ['user__first_name', 'event']

    def name(self, obj):
        return obj.user.first_name + ' ' + obj.user.last_name

    def en(self,obj):
        return obj.user.profile.encarta_id

    def cost(self,obj):
        return obj.event.cost



admin.site.register(Participation, ParticipationAdmin)