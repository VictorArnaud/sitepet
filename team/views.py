from django.shortcuts import render
from django.views.generic import View, TemplateView
from .models import Team


class TeamView(View):
  template = 'team/team_static.html'

  def get(self, request):
    teacher = Team.objects.get(is_teacher=True)
    team = Team.objects.filter(is_teacher=False)
    context = {'team': team, 'teacher': teacher}
    return render(request, self.template, context)


class HistoricView(TemplateView):
  template_name = 'team/historic.html'