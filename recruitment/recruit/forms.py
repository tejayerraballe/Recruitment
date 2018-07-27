from django import forms
from recruit.models import Recruit

class RecruitmentForm(forms.ModelForm):
		# TRUE_FALSE_CHOICES = (
		#   (True, 'Accept'),
		#   (False, 'Reject')
		# )
		# application_status = forms.ChoiceField(choices = TRUE_FALSE_CHOICES, label="Application Status", 
  #                             initial='', widget=forms.Select(), required=True)
		# def save(self, commit=True):
		#     application_status = self.cleaned_data.get('application_status', None)
		#     return super(RecruitmentForm, self).save(commit=commit)
		class Meta:
		  model = Recruit
		  widgets = {'application_status': forms.HiddenInput()}
		  fields = '__all__'