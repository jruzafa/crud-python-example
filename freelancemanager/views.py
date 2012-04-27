# Create your views here.
from django.template import Context, loader
from django.http import HttpResponse,Http404
from freelancemanager.models import Work

from django.shortcuts import render_to_response, get_object_or_404

def index(request):
	# all_works = Work.objects.all()
	# t = loader.get_template('works/index.html')
	# c = Context({
	# 	'all_works': all_works,
	# })

	# #return HttpResponse("Hello, world. You're at the work view")
	# return HttpResponse(t.render(c))
	all_works = Work.objects.all()
	return render_to_response('works/index.html', {'all_works': all_works})

def detail(request, work_id):
	# return HttpResponse("You're looking at the results of work %s." % work_id)

	# try:
	# 	w = Work.objects.get(pk=work_id)
	# except Work.DoesNotExist:
	# 	raise Http404
	# return render_to_response('works/detail.html',{'work': w})	

	w = get_object_or_404(Work, pk=work_id)
	return render_to_response('works/detail.html', {'work': w})

def customer(request, customer_id):
	return HttpResponse("You're looking at the results of customer %s." % customer_id)