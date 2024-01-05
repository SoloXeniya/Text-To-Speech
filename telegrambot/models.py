from django.db import models

class TelegramUser(models.Model):
    user_id = models.BigIntegerField(unique=True, verbose_name = 'ID пользователя',
                help_text ="Уникальный идентификатор пользователя в  Telegram")
    username = models.CharField(max_length=120, blank=True, null=True, 
                verbose_name = 'username пользователя', help_text = "username пользователя в Telegram")
    first_name = models.CharField(max_length=120, blank=True, null=True,
                verbose_name = 'Имя пользователя', help_text = "Имя пользователя в Telegram")
    last_name = models.CharField(max_length=120, blank=True, null=True,
                verbose_name = 'Фамилия пользователя', help_text = "Фамилия пользователя в Telegram")
    language_code = models.CharField(max_length=120, blank=True, null=True, verbose_name= "Код языка",
                help_text = "Языка пользователя в Telegram")
    is_bot = models.BooleanField(default=False, verbose_name = "Бот", 
                help_text = "Текст, обозначающий является ли пользователем ботом")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = "Дата создания",)
    
    def get_name(self):
        if self.username:
            return self.username
        elif self.first_name:
            return self.first_name
        elif self.last_name:
            return self.last_name
        else:
            return "Пользователь"

    def __str__(self):
        return f"{self.user_id}: {self.get_name()}"
    
    class Meta:
        verbose_name = 'Пользователь Telegram'
        verbose_name_plural = 'Пользователи Telegram'
        ordering = ['-created_at']

class TryTransform(models.Model):
    count = models.IntegerField(default=10, verbose_name = 'Попытки', help_text = "Попытки")
    tuser = models.OneToOneField(TelegramUser, on_delete=models.CASCADE, verbose_name = 'Пользователь')
    
    def __str__(self):
        return f"{self.tuser.get_name()}: {self.count}"
    
    class Meta:
        verbose_name = 'Попыткя преобразования'
        verbose_name_plural = 'Попытки преобразования'