def index(request):
	'''index'''
	return HttpResponse('index')
def login(request):
	'''login'''
	return redirect(request, '')
