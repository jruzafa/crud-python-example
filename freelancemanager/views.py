# Create your views here.
from django.template import Context, loader
from django.http import HttpResponse
from freelancemanager.models import Work

def index(request):
	all_works = Work.objects.all()
	t = loader.get_template('works/index.html')
	c = Context({
		'all_works': all_works,
	})

	#return HttpResponse("Hello, world. You're at the work view")
	return HttpResponse(t.render(c))

def detail(request, work_id):
	return HttpResponse("You're looking at the results of work %s." % work_id)

def customer(request, customer_id):
	return HttpResponse("You're looking at the results of customer %s." % customer_id)