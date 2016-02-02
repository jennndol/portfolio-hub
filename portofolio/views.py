from django.shortcuts import render
from portofolio.models import Portofolio

def portofolios(request):
	portofolios = Portofolio.objects.all()
	return render(request, 'portofolio/index.html', {'portofolios': portofolios})