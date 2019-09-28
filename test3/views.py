from django.shortcuts import render


def home(request):
	args = {
		'os': request.user_agent.os.family
	}
	os = request.user_agent.os.family.lower()
	if 'ubuntu' in os:
		args['extn'] = 'test.deb'
	elif 'linux' in os:
		args['extn'] = 'test.deb'
	elif 'debian' in os:
		args['extn'] = 'test.deb'
	elif 'fedora' in os:
		args['extn'] = 'test.deb'
	elif 'manjaro' in os:
		args['extn'] = 'test.deb'
	elif 'windows' in os:
		args['extn'] = 'test.exe'
	elif 'mac' in os:
		args['extn'] = 'test.dmg'
	elif 'android' in os:
		args['extn'] = 'test.apk'
	elif 'ios' in os:
		args['extn'] = 'test.ipa'
	else:
		args['extn'] = 'test.exe'

	return render(request, "test3/test3.html", args)
