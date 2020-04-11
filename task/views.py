from rest_framework.decorators import api_view
from rest_framework.response import Response

from .tasks import generate_power, is_prime


@api_view(["POST"])
def get_prime(request):
    number = request.data

    result = is_prime.delay(number["n"])

    return Response()


@api_view(["POST"])
def get_power(request):

    number = request.data

    result = generate_power.delay(number["n"])

    return Response()
