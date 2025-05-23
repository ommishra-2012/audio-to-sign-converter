import os
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
import json

# 👇 This is the missing view
def index(request):
    return render(request, 'converter/index.html')

def get_signs(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        text = data.get('text', '').lower().strip()
        sign_folder = os.path.join(settings.STATICFILES_DIRS[0], 'converter/signs')
        output = []

        sentence_path = os.path.join(sign_folder, f"{text}.gif")
        if os.path.exists(sentence_path):
            output.append([f"converter/signs/{text}.gif"])
        else:
            words = text.split()
            for word in words:
                word_path = os.path.join(sign_folder, f"{word}.gif")
                if os.path.exists(word_path):
                    output.append([f"converter/signs/{word}.gif"])
                else:
                    letter_images = []
                    for letter in word:
                        letter_path = os.path.join(sign_folder, 'letters', f"{letter}.gif")
                        if os.path.exists(letter_path):
                            letter_images.append(f"converter/signs/letters/{letter}.gif")
                    if letter_images:
                        output.append(letter_images)

        return JsonResponse({'output': output})
    return JsonResponse({'error': 'Invalid request method.'}, status=400)
