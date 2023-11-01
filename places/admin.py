from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from django.contrib import admin
from places.models import Place, Image


class ImageInline(SortableInlineAdminMixin, admin.StackedInline):
    model = Image
    fields = ('image', 'get_preview_image')
    readonly_fields = ('get_preview_image', )
    extra = 0


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


@admin.register(Image)
class ImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    fields = ('image', 'place', 'get_preview_image')
    raw_id_fields = ('place', )
    readonly_fields = ('get_preview_image', )

