from django.views.generic import View
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.mail import mail_admins

from .forms import FeedbackForm


class LoginRequiredMixin:
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view, login_url='/login')


class FeedbackView(LoginRequiredMixin, View):

    form = FeedbackForm
    template_name = 'feedback.html'

    def get(self, request, *args, **kwargs):
        form = self.form()
        return render(request, self.template_name,
                      context={'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.user = request.user
            form.save()

            email_message = (
                '{user} отправил сообщение: {message}\n'
                'обратный email: {email}'.format(user=message.user.username,
                                                 message=message.message,
                                                 email=message.email)
            )

            mail_admins('Новое сообщение', email_message)
            return HttpResponseRedirect('/')

        return render(request, self.template_name, {'form': form})
