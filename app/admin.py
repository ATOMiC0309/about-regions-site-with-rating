from django.contrib import admin
from .models import Region
from django.utils.safestring import mark_safe


# Register your models here.
@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'parent', 'population', 'created', 'published', 'get_image')
    list_display_links = ('pk', 'name')
    list_filter = ('parent', 'published')
    list_editable = ('published', )

    def get_image(self, region):
        if region.image:
            url = region.image.url
        else:
            url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSOl5h_VGoxwBVBMyq1Wbl56swafvs_BVibb88UW5JJzg&s"
        return mark_safe(
                f'<a href="{url}"><img src="{url}" alt="Rasm yo`q" width="90px" style="border: 2px solid blue"></a>')

    get_image.short_description = "Rasmi"