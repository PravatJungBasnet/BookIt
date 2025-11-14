from rest_framework.renderers import JSONRenderer


class CustomJSONRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        if isinstance(data, dict) and not any(
            key in data for key in ["data", "errors", "field_errors"]
        ):
            return {"data": data}
        return super().render(data, accepted_media_type, renderer_context)
