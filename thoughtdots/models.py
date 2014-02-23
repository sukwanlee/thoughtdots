from django.db import models

import numpy as np
import pandas
from loadnames import gather

class Data_Point(models.Model):
	year = models.IntegerField(blank = True)
	value = models.DecimalField(blank = True,decimal_places=5, max_digits=10)

	class Meta:
		ordering = ['year']

class Country(models.Model):
	name = models.CharField(max_length=100, blank=True)
	short_name = models.CharField(max_length=3, blank=True)
	longitude = models.DecimalField(blank=True, decimal_places=5, max_digits=10)
	latitude = models.DecimalField(blank=True,decimal_places=5, max_digits=10)
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
		df = gather("NGDP") #fuxin's data frame method
		super(Data_Set, self).save(*args, **kwargs)
		df = gather ("NGDP")
		times = df.columns
		ind = df.index
		for i in range(0,len(times)):
			vals = times[i].split(",")
			country = vals[0]
			shortname = vals[1]
			longi = (float(vals[2])+100)/2
			lati = (float(vals[3])+100)/2
			# print country + "+" + shortname + "+" + longitude + "+" + latitude
			c = Country(name=country, short_name = shortname, longitude = longi-20, latitude = lati-20)
			c.save()
			for k in range(0, len(ind)):
				time = ind[k].year
				vall = df.iloc[k,i]
				if (np.isnan(vall)):
					c.data.create(year=time, value = 0.0)
				else:
					c.data.create(year=time, value=vall)

			self.country.add(c)
