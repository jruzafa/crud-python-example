# Create your views here.
from django.http import HttpResponse


def index(request):
	return HttpResponse("Hello, world. You're at the work view")

def detail(request, work_id):
	return HttpResponse("You're looking at the results of work %s." % work_id)

def customer(request, customer_id):
	return HttpResponse("You're looking at the results of customer %s." % customer_id)