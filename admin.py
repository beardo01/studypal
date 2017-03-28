from django.contrib import admin

# Register your models here.
from study.models import *

admin.site.register(User)
admin.site.register(Group)
admin.site.register(Chat)
admin.site.register(Message)
admin.site.register(Reply)
admin.site.register(Timeline)
admin.site.register(TimelineItem)
admin.site.register(TimelineItemRepeat)
admin.site.register(Resource)
admin.site.register(ResourceItem)