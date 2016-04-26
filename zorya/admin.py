# coding=utf-8

from .models import  Constellations as Constelation
from .models import StellarObject, Catalogues, Objects_list, ObjectPhotos, BugTracker, ContactApplet, ReletedType
from django.conf import settings
from django.contrib import admin

#TODO Cały admin do przepisania
class ConstelationInline(admin.StackedInline):
    model = StellarObject
    extra = 0


class AdminConst(admin.ModelAdmin):
    list_display = ['abbreviation',
                    'constellation',
                    'other_abbreviation',
                    'genitive',
                    'family',
                    'origin',
                    'meaning',
                    'brightest_star',
                    'pk'
    ]

    verbos_name_plural = 'Constelations'

    inlines = [
        ConstelationInline
    ]
class ImageInline(admin.StackedInline):
    model = ObjectPhotos
    extra = 0

class AdminNGC(admin.ModelAdmin):
    list_display = ["unique_name",
                    "type", "type_shortcut", "classe",
                    "rightAsc", "declination", "constelation",
                    "magnitudo", "dimAxb", "description",
                    "id1", "id2", "id3", "notes"]
    search_fields = ["unique_name", "description",
                     "id1", "id2", "id3"]

    inlines = [ImageInline]

class ObjectsInline(admin.TabularInline):
    readonly_fields = ['selflink',]
    model = Objects_list
    verbose_name = ''
    raw_id_fields = ("single_object",)
    extra = 1
class AdminPhoto(admin.ModelAdmin):
    list_display = ['normal']
    search_fields = ['name', 'photo', 'photo_thumbnail', 'photo_url']


#class AdminCatalogue(admin.ModelAdmin):
# wy
#    class Media:
#        static_url = getattr(settings,  'STATIC_URL', '/static/')
#        js = [ static_url+'/admin/js/custom_inlines.js', ]
#        inlines = [
#                    ObjectsInline
#                ]


#Catalogues_filtered = Catalogues.objects.exclude(pk=1)

#And then include it in a admin declaration
admin.site.register(ObjectPhotos, AdminPhoto)
admin.site.register(BugTracker)
admin.site.register(ContactApplet)
admin.site.register(StellarObject, AdminNGC)
admin.site.register(Constelation, AdminConst)
admin.site.register(Catalogues, admin.ModelAdmin)
admin.site.register(ReletedType)
