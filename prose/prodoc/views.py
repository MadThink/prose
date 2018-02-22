
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Prodoc

class IndexView(generic.ListView):
	template_name = "prodoc/index.html"
	context_object_name = "all_prose"

	def get_queryset(self):
		return Prodoc.objects.all()

class DetailView(generic.DetailView):
	model = Prodoc
	template_name = "prodoc/detail.html"