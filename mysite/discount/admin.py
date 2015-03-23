from django.contrib import admin
from discount.models import DiscountInfo, DiscountWeb, DiscountCategory


class DiscountWebAdmin(admin.ModelAdmin):
    list_display = ('name', 'url_')
    list_display_links = ('name',)

    def url_(self, instance):
        return '<a href="%s" target="_blank">%s</a>' % (instance.url, instance.url)
    url_.allow_tags = True

class DiscountInfoAdmin(admin.ModelAdmin):
    # ...
    list_display = ('category', 'name', 'price', 'url_', 'source', 'date', 'was_published_recently')
    list_display_links = ('name', )
    list_filter = ['category__name', 'source__name', 'date']
    search_fields = ['name']

    def url_(self, instance):
        return '<a href="%s" target="_blank">link</a>' % instance.url
    url_.allow_tags = True

admin.site.register(DiscountCategory)
admin.site.register(DiscountWeb, DiscountWebAdmin)
admin.site.register(DiscountInfo, DiscountInfoAdmin)