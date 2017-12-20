import uuid
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import URLItem
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


#  function to render initial page
def index(request):
    return render(request, 'url_short/index.html')


# function to take URL, check if URL is valid, then check if URL already exists in DB. if it does, get code from
# DB and create example link and render new page. if it doesn't, create a code for that page (slicing first 6 chars
# of UUID), save it to DB, create an example link and render a new page with that link
def saveurl(request):
    url_string = request.POST['url_string']
    try:
        validate = URLValidator()
        validate(url_string)
    except ValidationError:
        message = 'Not a valid URL.'
        context = {'message': message}
        return render(request, 'url_short/error.html', context)
    try:
        URLItem.objects.filter(url_string=url_string).exists()
        code = URLItem.objects.get(url_string=url_string)
        code = code.code
    except URLItem.DoesNotExist:
        code = str(uuid.uuid4())[:6]
        url_item = URLItem(url_string=url_string, code=code)
        url_item.save()
    new_url = str('http://' + request.get_host() + '/url_short/redirect/' + code)
    context = {'new_url': new_url}
    return render(request, 'url_short/saveurl.html', context)


# get url key from incoming url, find object in DB with key, get URL from object and redirect to that URL.
# If key does not exist, redirect to error template
def redirect(request, url_key):
    try:
        redirect_url = URLItem.objects.get(code=url_key)
    except URLItem.DoesNotExist:
        message = 'URL not found...'
        context = {'message': message}
        return render(request, 'url_short/error.html', context)
    redirect_url = redirect_url.url_string
    return HttpResponseRedirect(redirect_url)
