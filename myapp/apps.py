from django.apps import AppConfig



# class MyappConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'myapp'

from django.apps import AppConfig
class AppConfig(AppConfig):
      name = 'myapp'
      #Add this
      verbose_name = "Student APP"