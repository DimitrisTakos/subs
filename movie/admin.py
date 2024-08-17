from django.contrib import admin
from .models import Post
from .models import Cheatsheet
from .models import Old

# Register your models here.

admin.site.register(Post)
admin.site.register(Cheatsheet)
admin.site.register(Old)
