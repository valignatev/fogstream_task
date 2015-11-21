from django.contrib import admin

from .models import Feedback


class FeedbackAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return False


admin.site.register(Feedback, FeedbackAdmin)
