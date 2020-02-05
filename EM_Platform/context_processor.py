from django.conf import settings as original_settings

def settings(request):
    return {'settings':original_settings}

def user_name(request):
    return {'user_name':request.session.get('user_name')}