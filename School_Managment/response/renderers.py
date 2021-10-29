from rest_framework.renderers import JSONRenderer


class CustomJSONRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        if not data is None and 'meta' in data and data['meta']['status'] is False:
            response_data = {
                'data': None,
                'meta': data['meta']
            }
        elif renderer_context['response'].status_code not in range(200, 300):
            response_data = {
                'data': None,
                'meta': {
                    'message': 'Error',
                    'errors': [data],
                    'status': False
                }
            }
        else:
            response_data = {
                'data': data,
                'meta': {
                    'message': '',
                    'errors': [],
                    'status': True
                }
            }

        # getattr(renderer_context.get('view', ).get_serializer().Meta, 'resource_name', 'objects')

        # call super to render the response
        response = super(CustomJSONRenderer, self).render(response_data, accepted_media_type, renderer_context)

        return response
