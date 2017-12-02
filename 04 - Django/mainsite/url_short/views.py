import uuid
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import URLItem


#  function to render initial page
def index(request):

    return render(request, 'url_short/index.html')


# function to take URL, check if URL already exists in DB. if it does, get code from DB and create example link and
# render new page. if it doesn't, create a code for that page (slicing first 6 chars of UUID), save it to DB, create
# an example link and render a new page with that link
def saveurl(request):

    url_string = request.POST['url_string']

    # can't figure out how to do try, except with a model query
    #
    # try:
    #     URLItem.objects.filter(url_string__isnull=url_string == False)
    #
    # except URLItem.DoesNotExist:
    #     code = str(uuid.uuid4())[:6]
    #     url_item = URLItem(url_string=url_string, code=code)
    #     url_item.save()
    #
    # else:
    #     code = URLItem.objects.get(url_string=url_string)
    #     code = code.code

    code = str(uuid.uuid4())[:6]
    url_item = URLItem(url_string=url_string, code=code)
    url_item.save()
    new_url = str('http://' + request.get_host() + '/url_short/redirect/' + code)
    context = {'new_url': new_url}
    return render(request, 'url_short/saveurl.html', context)


# get url key from incoming url, find object in DB with key, get URL from object and redirect to that URL
def redirect(request, url_key):
    redirect_url = URLItem.objects.get(code=url_key)
    redirect_url = redirect_url.url_string
    return HttpResponseRedirect(redirect_url)
