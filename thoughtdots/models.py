from django.db import models

import numpy, pandas

class Data_Point(models.Model):
	year = models.IntegerField(blank = True)
	value = models.IntegerField(blank = True)

class Country(models.Model):
	name = models.CharField(max_length=30, blank=True)
	short_name = models.CharField(max_length=3, blank=True)
	longitude = models.IntegerField(blank=True)
	latitude = models.IntegerField(blank=True)
	data = models.ManyToManyField(Data_Point, null=True)

	class Meta:
		ordering = ['name']

	def __unicode__(self):
		return self.name

class Data_Set(models.Model):
	name = models.CharField(max_length=30, blank=True)
	country = models.ManyToManyField(Country, null=True, blank=True, related_name='countries')
	data_type = models.CharField(max_length=300, blank=True)

	def __unicode__(self):
		return self.name

	def save(self, *args, **kwargs):
		# frame_data = fuxin_method(self.data_type)
		super(Data_Set, self).save(*args, **kwargs)
		my_list = ["a","b","c","d","e"]
		for element in my_list:
			c = Country(name=element, short_name="ab", longitude=1, latitude=1)
			c.save()
			for element in my_list:
				c.data.create(year=2013, value=10000)

			self.country.add(c)