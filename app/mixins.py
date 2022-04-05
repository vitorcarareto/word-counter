from django.http import JsonResponse
from http import HTTPStatus


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


class AjaxFormMixin(object):
    def form_invalid(self, form):
        response = super().form_invalid(form)

        if is_ajax(self.request):
            return JsonResponse(form.errors, status=HTTPStatus.BAD_REQUEST)
        else:
            return response

    def get_result(self, form, **kwargs):
        return {}

    def form_valid(self, form):
        response = super().form_valid(form)

        if is_ajax(self.request):
            result_dict = {}
            try:
                result_dict = self.get_result(form)
                return JsonResponse(result_dict, status=HTTPStatus.OK)
            except Exception as e:
                result_dict["message"] = f"{e}"
                return JsonResponse(result_dict, status=HTTPStatus.INTERNAL_SERVER_ERROR)

        return response
