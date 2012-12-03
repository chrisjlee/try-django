from django.shortcuts import render_to_response
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    return render_to_response('current_datetime.html', {'current_date': now})
def hello(request):
    return HttpResponse("Hello world")
def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    assert False
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)
#def hours_ahead(request, offset):
#    try:
#        offset = int(offset)
#    except ValueError:
#        raise Http404()
#    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
#    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
#    return HttpResponse(html)
def chapter_request(request):
    current_chapter = 'Chapter 4'
    url = 'http://www.djangobook.com/en/2.0/chapter04.html'
    html = "<html><body>Current Chapter is: <a href='%s'><b>%s</b></a>.</body></html>" % (url, current_chapter)
    return HttpResponse(html)