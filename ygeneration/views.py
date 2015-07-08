from django.shortcuts import render

# Create your views here.
def home(request):
	# activity images
	fast_ques_photo = []
	for num in range(1, 7):
		fast_ques_photo.append('images/face_question/photo' + str(num) + '.JPG')

	context = {
		'fast_ques_photo': fast_ques_photo,
	}
	return render(request, 'home.html', context)

def activity_intro(request):
	return render(request, 'activity_intro.html', {})


def team_intro(request):
	return render(request, 'team_intro.html', {})