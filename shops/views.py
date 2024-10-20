from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import ShopsForm

# Markup Values

html_values = {
  "google_form_link": "https://docs.google.com/forms/d/e/1FAIpQLSeop8N4cvcL6Dj09266ZGXQxBdkdTjhHCM4WqZ3WXfHPhTR7g/viewform",
"pure_css_cdn":"https://cdn.jsdelivr.net/npm/purecss@3.0.0/build/pure-min.css","list_link": "https://docs.google.com/spreadsheets/d/1x1DgKM5yyP03AdZXcHDuDZowOHTIMt0-xnx3Cm2Wa0Y/edit?usp=sharing"}

seo_values = {
  "meta_description": "Explore Maryland's family-owned businesses. Add your favorites, join our Think-Tank for updates, suggest features, and support local shopping!", "meta_keywords": "Maryland local businesses, family-owned shops, Maryland shopping, support local, weekend shopping, holiday shopping, small businesses, community shops, Maryland Think-Tank, local gems"
}

all_values = {**seo_values, **html_values}

# Views

def home(request):
  return render(request, "myfirst.html", all_values)  

def add_shop(request):
  if request.method == 'POST':
    form = ShopsForm
    if form.is_valid():
      form.save()
      return redirect('shop_list')
  
  else:
    form = ShopsForm

  
  return render(request, 'shops/add_shop.html', {'form': form})

