from django.contrib import admin

# Register your models here.

class ParticipanteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'email']
