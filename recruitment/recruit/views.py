# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render_to_response
# Create your views here.
from forms import RecruitmentForm
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseServerError, HttpResponseForbidden

def recruitment_form(request):
	print 'sdfsdf'
	if request.method=='POST':
		form = RecruitmentForm(request.POST)
		if form.is_valid():
			form.save()
			return render(request, "completed.html")
	else:
		form=RecruitmentForm()

	return render(request, 'recruitment_form.html', {'form':form})