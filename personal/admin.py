from django.contrib import admin
from personal.models.project import Project
from personal.models.module import Module


class ProjectAdmin(admin.ModelAdmin):
    list_display = ["name","describe","status","create_time"]
    # 搜索栏
    search_fields = ['name']
    list_filter = ['status']
# Register your models here.


class ModuleAdmin(admin.ModelAdmin):
    list_display = ["name","describe","project","create_time"]
    search_fields = ['name']
    list_filter = ['project']
# Register your models here.
admin.site.register(Project,ProjectAdmin)
admin.site.register(Module,ModuleAdmin)
