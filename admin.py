from django.contrib import admin
from .models import Categoria, Produto # O ponto antes de models é essencial!

admin.site.register(Categoria)
admin.site.register(Produto)