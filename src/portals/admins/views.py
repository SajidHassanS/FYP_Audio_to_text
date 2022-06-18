from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .ai_pythorch import make_prediction_on_file as english_model

from .ai_pythorch_urdu import make_prediction_on_file as urdu_model

# from .ai_tensorflow import make_prediction_on_file


@method_decorator(csrf_exempt, name='dispatch')
class FormView(View):

    def get(self, request):
        return render(request, template_name='admins/dashboard.html')

    def post(self, request):

        try:
            file = request.FILES['file']
        except:
            context = {
                'error': 'File not found!'
            }
            return render(request, 'admins/dashboard.html', context)

        print(request.POST.get('flexRadioDefault'))
        print(file)
        if request.POST.get('flexRadioDefault') == 'urdu':
            transcript = urdu_model(file)
        else:
            transcript = english_model(file)

        context = {
            'data': transcript,
            'error': ''
        }
        return render(request, 'admins/dashboard.html', context)


filepath = "~/audio_wav/"  # Input audio file path
output_filepath = "~/Transcripts/"  # Final transcript path
bucketname = "callsaudiofiles"  # Name of the bucket created in the step before
