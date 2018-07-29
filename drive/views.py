from pyramid.view import view_config
import pdb
import yaml


@view_config(route_name='index', renderer='templates/index.jinja2')
def my_view(request):
    return {'project': 'drive'}


@view_config(route_name='weakness_index',
             renderer='templates/weakness_index.jinja2')
def weakness_index_view(request):
    doc = yaml_document()
    links = []
    for slug, data in doc.items():
        title = data['title']
        links.append((slug, title))


    return dict(links=links)


@view_config(route_name='weakness_show',
             renderer='templates/weakness_show.jinja2')
def weakness_show_view(request):
    slug = request.matchdict.get('slug')
    if not slug:
        request.response.status_code = 404
    doc = yaml_document()
    weakness = doc.get(slug)
    if not weakness:
        request.response.status_code = 404
    return dict(weakness=weakness)


def yaml_document():
    with open('drive/templates/weaknesses.yml', 'r') as f:
        document = f.read()
    return yaml.load(document)

