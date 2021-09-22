from django.contrib import admin
from .models import *
from embed_video.admin import AdminVideoMixin
# Register your models here.
admin.site.register(User)
admin.site.register(Image)

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Nuggets, MyModelAdmin)
admin.site.register(Dancehall, MyModelAdmin)
admin.site.register(Hangout, MyModelAdmin)
admin.site.register(Amapiano, MyModelAdmin)
admin.site.register(Afrobeat, MyModelAdmin)
admin.site.register(Hiphop, MyModelAdmin)
admin.site.register(Reels, MyModelAdmin)




