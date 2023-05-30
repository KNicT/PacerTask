#API Endpoint
from django.http import JsonResponse
from api.models import Scores
def get_score(request):
    if request.method == 'POST':
        userId = request.POST.get('userId', '')
        score = request.POST.get('score', '')
        #static request to add a value to the key userId
        # userId = request.GET.get('userId', 'JARSO')

        # score = 100
        result = int(score) + 1
        Scores.objects.create(userId=userId, score = result)

        response = {'result' : result}
        return JsonResponse(response, safe=False)
    else:
        return JsonResponse({'message': 'Invalid Request Method'})