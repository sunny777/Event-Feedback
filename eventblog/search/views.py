import re
from django.http import HttpResponse
from django.template import RequestContext, loader
from event.models import *
from blog.models import *
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import itertools

def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    ''' Splits the query string in invidual keywords, getting rid of unecessary spaces
        and grouping quoted words together.
        Example:

        >>> normalize_query('  some random  words "with   quotes  " and   spaces')
        ['some', 'random', 'words', 'with quotes', 'and', 'spaces']

    '''
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)]

def get_query(query_string, search_fields):
    ''' Returns a query, that is a combination of Q objects. That combination
        aims to search keywords within a model by testing the given search fields.

    '''
    query = None # Query to search for every search term
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None # Query to search for a given term in each field
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query

@login_required(login_url='/account/login')
def search(request):
        template = loader.get_template('search.html')
        query_string = ''
        found_entries = None
        if ('q' in request.GET) and request.GET['q'].strip():
            query_string = request.GET['q']

            entry_query1 = get_query(query_string, ['id', 'event_name', ])
            entry_query2 = get_query(query_string, ['id', 'blog_title', ])

            found_entries1 = Event.objects.filter(entry_query1).order_by('-event_date')
            found_entries2 = Blog.objects.filter(entry_query2).order_by('-created_time')
            if len(found_entries1) > 0 and len(found_entries2)> 0:
               found_entries = itertools.chain(found_entries1, found_entries2)
            elif len(found_entries1) == 0:
               found_entries = found_entries2
            elif len(found_entries2) == 0:
               found_entries = found_entries1
        context = RequestContext(request, {
            'template_name': 'search.html',
            'query_string': query_string,
            'found_entries': found_entries,
            'success_url': '/thanks/',
        })
        return HttpResponse(template.render(context))