from django.db import models
from gtts import gTTS
import io
import re



# Create your models here.
class Text_to_speech(models.Model):
    
    text = models.CharField(max_length=600, verbose_name = 'Текст', help_text= "Введите текст, который хотите преобразовать в текст")
    file_name = models.CharField(max_length=20, verbose_name = 'Название текста')
    
    path_file = models.FileField(upload_to = 'voice/', verbose_name="Ссылка на запись")
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = 'Дата создания')

    
    def save(self, *args, **kwargs):
        language = re.search(r'[\u0400-\u04ff]|[\u0500-\u052f]', self.text)
        lang ='ru' if language else 'en'
        tts = gTTS(text=self.text, lang=lang) 
        voice_bytes = io.BytesIO()
        tts.write_to_fp(voice_bytes)  
        voice_bytes.seek(0)   
    
        self.path_file.name = f"voice/{self.file_name}.wav"   #сохраням и отправляем в базу данных путь
        with open(self.path_file.path, 'wb') as f:
            f.write(voice_bytes.read())
        
        
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.file_name
    
    class Meta:
        verbose_name = 'Текст'
        verbose_name_plural = 'Текста в речь'
    
    
    
    
    
    #   def save(self, *args, **kwargs):
    #     language = re.search(r'[\u0400-\u04ff]|[\u0500-\u052f]', self.text)
    #     lang ='ru' if language else 'en'
    #     tts = gTTS(text=self.text, lang=lang) 
    #     voice_bytes = io.BytesIO()
    #     tts.write_to_fp(voice_bytes)  
    #     voice_bytes.seek(0)
        
    #     voice_path = f"voice/{self.file_name}.wav"
    #     self.path_file = voice_path   #сохраням и отправляем в базу данных путь
    #     with open(voice_path, 'wb') as f:
    #         f.write(voice_bytes.read())