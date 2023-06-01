#API Endpoint
from django.http import JsonResponse
from api.models import Scores
import random
def get_score(request):
    val = 0 
    result = random.randint(val, 100)

    userId = request.GET.get('userId', 'test2')
    Scores.objects.create(userId=userId, score=result)

    response = {'result': result}
    return JsonResponse(response)
