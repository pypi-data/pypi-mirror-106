import json

from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.decorators.csrf import csrf_exempt

from .functions import get_payeer_api
from .exceptions import PayeerValidationError, AlreadyPaid


@method_decorator(csrf_exempt, name="dispatch")
class NotifyView(generic.View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return HttpResponse("JSON decode error", status=400)
        api = get_payeer_api()
        try:
            result = api.notify(data)
        except PayeerValidationError as exc:
            return HttpResponse(f"{exc.order_id}|error")
        except AlreadyPaid as exc:
            return HttpResponse(f"{exc.order_id}|success")

        result.payment.accept()
        return HttpResponse(f"{result.raw_order_id}|success")
