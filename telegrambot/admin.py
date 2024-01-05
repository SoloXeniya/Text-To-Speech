from django.contrib import admin
from .models import TelegramUser, TryTransform
# Register your models here.
from django.utils.safestring import mark_safe


@admin.register(TelegramUser)
class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ["get_formatted_info", "user_id", "username", "created_at"]
    search_fields = ["user_id", "username", "first_name", "last_name"]
    ordering = ["-created_at"]
    
    def get_formatted_info(self, obj):
        info = (
            f"<div style='background-color: #f8f9fa; padding: 10px; border-radius: 5px; "
            f"box-shadow: 0 0 30px rgba(0, 0, 0, 0.1);'>"
        )
        info += f"<strong style='color: #00ff00;'>ID:</strong> {obj.user_id}<br>"
        info += f"<strong style='color: #00ff00;'>Username:</strong> {obj.username}<br>"
        info += f"<strong style='color: #00ff00;'>First Name:</strong> {obj.first_name}<br>"
        info += f"<strong style='color: #00ff00;'>Last Name:</strong> {obj.last_name}<br>"
        info += f"<strong style='color: #00ff00;'>Is Bot:</strong> {obj.is_bot}<br>"
        info += f"<strong style='color: #00ff00;'>Language Code:</strong> {obj.language_code}<br>"
        info += f"<strong style='color: #00ff00;'>Created At:</strong> {obj.created_at}<br>"
        info += "</div>"

        return mark_safe(info)

    get_formatted_info.short_description = 'User Info'
    
    
@admin.register(TryTransform)
class TryTransformAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'count')
    search_fields = ('tuser__user_id', 'tuser__username', 'tuser__first_name', 'tuser__last_name')
    list_filter = ('count',)
    list_per_page = 20
    ordering = ['-tuser__created_at']
    
    def user_name(self, obj):
        return obj.tuser.get_name()

    user_name.short_description = 'Пользователь'
    user_name.admin_order_field = 'tuser__username'

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('tuser')

admin.site.site_header = "Администрирование преобразований текста"
admin.site.site_title = "Администрирование преобразований текста"
admin.site.index_title = "Добро пожаловать в администрирование преобразований текста"