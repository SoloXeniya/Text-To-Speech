from django.contrib import admin
from .models import Text_to_speech
from django.utils.safestring import mark_safe

@admin.register(Text_to_speech)
class Text_to_speechAdmin(admin.ModelAdmin):
    list_display = ["id", "file_name", "text", "audio_player", "created_at"]
    search_fields = ["text", "file_name"]
    list_filter = ["created_at"]
    date_hierarchy = "created_at"
    ordering = ["-created_at"]
    
    fieldsets = (
        (None, {"fields": ("text", "file_name")}),
        ("Важные даты", {"fields": ("created_at",)}),
    )


    readonly_fields = ("created_at",)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ("file_name") + self.readonly_fields
        return self.readonly_fields
    
    
    def audio_player(self, obj):
        # Возвращаем аудио-тег для проигрывания звука
        return mark_safe(f'<audio controls><source src="{obj.path_file.url}" type="audio/wav"></audio>')
    
    audio_player.short_description = 'Audio Player'






