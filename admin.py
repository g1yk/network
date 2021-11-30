from django.contrib import admin

# Register your models here.

from .models import Post, Profile, User, Follower, UserFollowing
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    pass

class UserAdmin(admin.ModelAdmin):
    pass

class ProfileAdmin(admin.ModelAdmin):
    pass

class FollowerAdmin(admin.ModelAdmin):
    pass

class UserFollowingAdmin(admin.ModelAdmin):
    pass



admin.site.register(Post, PostAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Follower, FollowerAdmin)
admin.site.register(UserFollowing, UserFollowingAdmin)




