from django.test import TestCase


    
# class TextToSpeechView(BaseTextToSpeechView, generics.ListCreateAPIView):
#     def user_text(self,file_name, text, *args, **kwargs):
#         march = re.search(r'[\u0400-\u04ff]|[\u0500-\u052f]', text)
#         lang ='ru' if march else 'en'
#         tts = gTTS(text=text, lang=lang) 
#         voice_bytes = io.BytesIO()
#         tts.write_to_fp(voice_bytes)  
#         voice_bytes.seek(0)
        
#         voice_path = f"voice/{file_name}.wav"
#         with open(voice_path, 'wb') as f:
#             f.write(voice_bytes.read())
            
#         return voice_path
    
#     def post(self, request, *args, **kwargs):
#         text = request.data.get('text')
#         file_name = request.data.get('file_name')
#         try:
#             self.validate_request_data(text, file_name)
#         except ValidationError as e:
#             return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             voice_path = self.user_text(file_name, text)
#             request.data['path_voice'] = voice_path 
            
#             return super().post(request, *args, **kwargs)

# class TextToSpeechDetailView(BaseTextToSpeechView, generics.RetrieveUpdateDestroyAPIView):
    
#     def update_voice(self, file_name, text):
#         voice_path = self.user_text(file_name, text)
#         self.get_object().path_voice = voice_path
#         self.get_object().save()
    
#     def put(self, request, *args, **kwargs):
#         text = request.data.get('text')
#         file_name = request.data.get('file_name')
#         try:
#             self.validate_request_data(text, file_name)
#         except ValidationError as e:
#             return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)
#         # if self.get_object().created_at is not None:
#         #     raise MethodNotAllowed("PUT")
        
#         responce = super().put(request, *args, **kwargs)
#         self.update_voice(file_name, text)
#         return responce
