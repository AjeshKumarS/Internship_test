from django.shortcuts import render
import os
from django.core.files.storage import FileSystemStorage


def home(request):
	args = {
		'uploaded_file_url': None,
		'error': None
	}
	if request.method == 'POST' and request.FILES['myfile']:
		myfile = request.FILES['myfile']
		if myfile.name.endswith('.py') or myfile.name.endswith('.sh'):
			fs = FileSystemStorage()
			filename = fs.save(myfile.name, myfile)
			uploaded_file_url = fs.url(filename)
			args['uploaded_file_url'] = uploaded_file_url
		else:
			args['error'] = "invalid file type"
	return render(request, 'test2/test2.html', args)


def get_output(request):
	file_name = request.POST['file']
	if file_name.endswith('.py'):
		os.system('python .'+file_name+' > output.txt')
	else:
		os.system('chmod +x .' + file_name)
		os.system('.'+file_name + ' > output.txt')
	file = open('output.txt', 'r')
	args = {
		'content': file.read()
	}
	return render(request, 'test2/output.html', args)
