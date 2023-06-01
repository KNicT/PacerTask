#API Endpoint
from django.http import JsonResponse
from api.models import Scores
def get_score(request):
    val = 100
    result = val + 1

    userId = request.GET.get('userId', '')
    Scores.objects.create(userId=userId, score=result)

    response = {'result': result}
    return JsonResponse(response)
