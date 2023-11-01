from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from django.contrib import admin
from django.utils.html import format_html
from places.models import Place, Image


class ImageInline(SortableInlineAdminMixin, admin.StackedInline):
    model = Image
    fields = ('image', 'get_preview')
    readonly_fields = ('get_preview', )
    extra = 0

    def get_preview(self, obj):
        return format_html(f'<img src="{obj.image.url}" style="max-width:200px; max-height:200px"/>')


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


@admin.register(Image)
class ImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    fields = ('image', 'place', 'get_preview')
    raw_id_fields = ('place', )
    readonly_fields = ('get_preview', )

    def get_preview(self, obj):
        return format_html(f'<img src="{obj.image.url}" style="max-width:200px; max-height:200px"/>')
