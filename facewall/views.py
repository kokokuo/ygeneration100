from django.shortcuts import render

# Create your views here.
# Upload video
def index(request):
	return render(request, 'facewall/index.html', {})
