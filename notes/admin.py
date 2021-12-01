from django.contrib import admin
from notes.models import Note

# Register your models here.
class NoteModelAdmin(admin.ModelAdmin):
    def has_add_permission(self, request,obj= None):
        return False

    def has_delete_permission(self, request,obj= None):
        return False

    def has_module_permission(self, request,obj= None):
        return False


admin.site.register(Note,NoteModelAdmin)
