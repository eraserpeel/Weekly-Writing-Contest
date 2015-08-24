from django.shortcuts import render_to_response
from django.template import RequestContext
from allauth.socialaccount.models import SocialAccount

# Create your views here.
def home(request):
	if request.user.is_authenticated():
		return render_to_response('main/main_logged_in.html',  context_instance=RequestContext(request))
	else:
		return render_to_response('main/main_not_logged_in.html',  context_instance=RequestContext(request))

def view_profile(request):
	return render_to_response('profile/view_profile.html', context_instance=RequestContext(request))

