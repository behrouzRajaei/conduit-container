from rest_framework.renderers import JSONRenderer

class ConduitJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, media_type=None, renderer_context=None):
        # اگر هیچ دیتایی نیست
        if data is None:
            return super().render(data, media_type, renderer_context)

        # اگر لیست است (ReturnList یا list)
        if isinstance(data, list):
            return super().render(data, media_type, renderer_context)

        # اگر دیکشنری نیست
        if not isinstance(data, dict):
            return super().render(data, media_type, renderer_context)

        # pagination
        if 'results' in data:
            data = {
                'articles': data['results'],
                'articlesCount': data.get('count', len(data['results']))
            }

        return super().render(data, media_type, renderer_context)
