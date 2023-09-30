from django.contrib import admin

from .models import Birthday, Tag, Congratulation

# ...и регистрируем её в админке:
admin.site.register(Birthday)
admin.site.register(Tag)
admin.site.register(Congratulation)