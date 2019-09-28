from django.shortcuts import render


def home(request):
	args = {}
	return render(request, 'test2/test2.html', args)
