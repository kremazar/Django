from django.contrib import admin
from news.models import News,Img,Category

class ImgInline(admin.TabularInline):
    model = Img

class CategoryInline(admin.TabularInline):
    model = Category

class NewsAdmin(admin.ModelAdmin):
    inlines = [
        ImgInline,
        CategoryInline
    ]


admin.site.register(News,NewsAdmin)
admin.site.register(Img)
admin.site.register(Category)