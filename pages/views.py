from django.views.generic import TemplateView


class HomePageView(TemplateView):
    # Define the template
    template_name = 'home.html'
