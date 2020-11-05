from django.http import HttpResponse
from django.shortcuts import render

def home(request):
	return render(request, 'home.html')


def reverse(request):
	user_text = request.GET['usertext']
	reversed_text = user_text[::-1]
	

	splited_string = user_text.split()
	words_number = len(splited_string)
	# print(count)

	# print(user_text)	
	return render(request, 'reverse.html', {'usertext':user_text, 
		'reversedtext':reversed_text,'wordsnumber':words_number})