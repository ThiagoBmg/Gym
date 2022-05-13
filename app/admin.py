from pyexpat import model
import nested_admin
from django.contrib import admin

from .models import Machine, Set, Rep, Workout   
# Register your models here.

class RepInLine(nested_admin.NestedTabularInline,):
    model = Rep
    #classes = ['collapse']
    extra = 0

    fieldsets = (
        (
            None,{
                "description":None,
                "fields":("weight","qtd")
            }
        ),
    )

class MachineAdmin(admin.ModelAdmin):
    list_display = ['name','gp_foco']

class SetAdmin(nested_admin.NestedModelAdmin, admin.ModelAdmin):
    list_display = ['machine','created_date',]
    inlines = [RepInLine]

    fieldsets = (
        (
            "INFORMAÇÕES",{
                "description":None,
                "fields":("machine",)
            }
        ),
    )

class RepAdmin(admin.ModelAdmin):
    list_display = ['set','weight','created_date', ]

class WorkoutAdmin(admin.ModelAdmin):
    list_display = ['created_date',]

admin.site.register(Machine,MachineAdmin)
admin.site.register(Set,SetAdmin)
admin.site.register(Rep,RepAdmin)
admin.site.register(Workout,WorkoutAdmin)

