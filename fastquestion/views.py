from django.shortcuts import render

# Create your views here.
# Fast Question Wall
def index(request):
	fast_ques_faces = []
	for num in range(1, 6):
		fast_ques_faces.append('images/fast_question/face' + str(num) + '.png')
	context = {
		'fast_ques_faces': fast_ques_faces,
		'questions_video': [
			'https://www.youtube.com/watch?v=H_SiWTFmp0E&index=35&list=PL3Nh-KZ3bVowVPaVHwl5ZRiWrYZhfvYA5',
			'https://www.youtube.com/watch?v=h8lt8NmPm4A&list=PL3Nh-KZ3bVowVPaVHwl5ZRiWrYZhfvYA5&index=36',
		]
	}
	return render(request, 'fastquestion/index.html', context)