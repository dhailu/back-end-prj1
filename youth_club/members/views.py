
from django.http import HttpResponse
from django.template import loader
from .models import Member

## Note about the view 
# The members view does the following:
# Creates a mymembers object with all the values of the Member model.
# Loads the all_members.html template.
# Creates an object containing the mymembers object.
# Sends the object to the template.
# Outputs the HTML that is rendered by the template.

## First version
# def members(request):
#   template = loader.get_template('myfirst.html')
#   return HttpResponse(template.render())

## Second version
def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
