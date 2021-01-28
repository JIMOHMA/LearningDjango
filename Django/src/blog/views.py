from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from django.views.generic import(
	CreateView,
	DetailView,
	ListView,
	UpdateView,
	DeleteView
	)
# Import of Article model class
from .models import Article
from .forms import ArticleModelForm

# Create your views here.
class ArticleListView(ListView):
	template_name = 'blog/article_list.html'
	queryset = Article.objects.all()

class ArticleDetailView(DetailView):
	template_name = 'blog/article_detail.html'
	# this is used when we use pk in our urls path
	# queryset = Article.objects.all()

	# this is used when we use id instead of primary key (pk)
	# in our urls path 
	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Article, id=id_)

class ArticleCreateView(CreateView):
	template_name = 'blog/article_create.html'
	form_class = ArticleModelForm
	queryset = Article.objects.all()

	def form_valid(self, form):
		print(form.cleaned_data)
		return super().form_valid(form)


class ArticleUpdateView(UpdateView):
	template_name = 'blog/article_create.html'
	form_class = ArticleModelForm
	queryset = Article.objects.all()

	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Article, id=id_)

	def form_valid(self, form):
		print(form.cleaned_data)
		return super().form_valid(form)


class ArticleDeleteView(DeleteView):
	template_name = 'blog/article_delete.html'
	# this is used when we use pk in our urls path
	# queryset = Article.objects.all()

	# this is used when we use id instead of primary key (pk)
	# in our urls path 
	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Article, id=id_)

	# When we delete, we don't have access to the url of the object 
	# deleted anymore. This function allows us to reverse back to a url that's still available
	# which is the list of the remaining article in our blog
	def get_success_url(self):
		return reverse('blog:article-list')