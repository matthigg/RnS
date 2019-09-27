from django.forms import CheckboxInput, ModelForm, TextInput, Textarea
from . import models

# This is a hack to get rid of the defalt label_suffix=":"
# https://www.caktusgroup.com/blog/2018/06/18/make-all-your-django-forms-better/
class BaseForm(ModelForm):
  def __init__(self, *args, **kwargs):
    kwargs.setdefault('label_suffix', '')  
    super(BaseForm, self).__init__(*args, **kwargs)
ModelForm = BaseForm

class CreateContactForm(ModelForm):
  class Meta:
    model = models.ContactForm
    fields = [
      'name',
      'email',
      'phone',
      'number_of_stories',
      'type_of_exterior',
      'fence_cleaning',
      'surface_cleaning',
      'soft_wash',
      'outdoor_stain_removal',
      'deck_cleaning',
      'message',
    ]
    widgets = {
      'name': TextInput(attrs={'placeholder': 'name', 'aria-required': 'true'}),
      'email': TextInput(attrs={'placeholder': 'email', 'aria-required': 'true'}),
      'phone': TextInput(attrs={'placeholder': 'phone'}),
      'fence_cleaning': CheckboxInput(attrs={'class': 'test'}),
      'surface_cleaning': CheckboxInput(attrs={'class': 'test'}),
      'soft_wash': CheckboxInput(attrs={'class': 'test'}),
      'outdoor_stain_removal': CheckboxInput(attrs={'class': 'test'}),
      'deck_cleaning': CheckboxInput(attrs={'class': 'test'}),
      'message': Textarea(attrs={'placeholder': 'message', 'aria-required': 'true'}),
    }