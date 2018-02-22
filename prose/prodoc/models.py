from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models

class Prodoc(models.Model):
	title = models.CharField(max_length=250)
	content = models.CharField(max_length=1000000)
	cover = models.CharField(max_length=1000)

	def get_absolute_url(self):
		return reverse('prodoc:detail', kwargs={'pk':self.pk})

	def __str__(self):
		return self.title

		