from django.contrib import admin
from pills.models import Pills, Plans, Medical,Schedule 
# Register your models here.
admin.site.register(Pills)
admin.site.register(Schedule)
admin.site.register(Plans)
admin.site.register(Medical)
