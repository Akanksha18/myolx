from django.contrib import admin
from models import UserDetail, ItemDetail, ItemUpload

class ItemUploadInline(admin.StackedInline):
    model = ItemUpload
    extra = 3

class ItemUploadAdmin(admin.ModelAdmin):
    fieldsets = ('user','category')
    # fieldsets = [
    #     (None,               {'fields': ['user']}),
    #     ('Date information', {'fields': ['category'], 'classes': ['collapse']}),
    # ]
    # inlines = [ItemUploadInline]
admin.site.register(UserDetail)
admin.site.register(ItemDetail)
admin.site.register(ItemUpload)