from django.contrib import admin

# Register your models here.

from .models import Post, User
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    pass

class UserAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(User, UserAdmin)