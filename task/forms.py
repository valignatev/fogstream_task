from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm

from .models import Feedback


class AuthFormCustomLabel(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(AuthFormCustomLabel, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Логин'


class FeedbackForm(ModelForm):

    class Meta:
        model = Feedback
        exclude = ('user', )

