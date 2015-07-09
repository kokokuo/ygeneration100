from django.contrib import admin
from .forms import OnlineQuestionForm
from .models import OnlineQuestion

# Register your models here.
class OnlineQuestionAdmin(admin.ModelAdmin):
	# Display in Admin
	list_display = ["__unicode__", "timestamp", "updated"]
	# Edit Model field (by Form)
	form = OnlineQuestionForm

	# class Meta:
	# 	model = OnlineQuestion

# reigster model and set the Admin custom by second args
admin.site.register(OnlineQuestion, OnlineQuestionAdmin)