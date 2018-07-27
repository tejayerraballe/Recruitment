# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from recruit.models import Recruit
from recruit.forms import RecruitmentForm

class RecruitAdmin(admin.ModelAdmin):
    model=Recruit
    list_display = ['name', 'technologies', 'application_status']

    # fieldsets = (
    #     (None, {
    #         'fields': ('name', 'email', 'years_of_experience', 'technologies', 'current_organisation', 'current_CTC', 'expected_CTC', 'notice_period', 'description', 'application_status'),
    #     }),
    # )

admin.site.register(Recruit, RecruitAdmin)