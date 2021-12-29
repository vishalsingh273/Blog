from django.contrib import admin
from home.models import Home
# Register your models here.



class HomeAdmin(admin.ModelAdmin):
    class Media:
        css={
            "all":("css/main.css",)
}
js=("js/blog.js",)

admin.site.register(Home,HomeAdmin)