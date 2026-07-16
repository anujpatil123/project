print("✅ views.py loaded!")

'''from django.shortcuts import render
from .forms import PromptForm
from .ai_engine import generate_response

def home(request):
    form = PromptForm()
    response = ""
    if request.method == 'POST':
        form = PromptForm(request.POST)
        if form.is_valid():
            user_prompt = form.cleaned_data['prompt']
            response = generate_response(user_prompt)
            return render(request, 'builder/output.html', {'response': response})
    return render(request, 'builder/input.html', {'form': form})
'''
print("✅ views.py loaded!")

'''from django.shortcuts import render
from .forms import PromptForm
import json
from .ai_engine import generate_response


def home(request):
    form = PromptForm()
    quiz = []
    topic = ""
    
    if request.method == 'POST':
        form = PromptForm(request.POST)
        if form.is_valid():
            topic = form.cleaned_data['prompt']
            try:
                raw_response = generate_response(topic)

                # Remove Markdown formatting if present
                if raw_response.startswith("```json") or raw_response.startswith("```"):
                    raw_response = raw_response.replace("```json", "").replace("```", "").strip()

                quiz = json.loads(raw_response)
            except Exception as e:
                quiz = [{
                    "question": "Error loading quiz",
                    "options": {},
                    "answer": "N/A",
                    "explanation": str(e)
                }]
    
            return render(request, 'builder/output.html', {'quiz': response, 'user_prompt': user_prompt})

    
    return render(request, 'builder/input.html', {'form': form})'''
'''from django.shortcuts import render
from .forms import PromptForm, ContentForm
from .ai_engine import generate_response  # uses your ai_engine.py
from .utils import extract_text_from_pdf

def home(request):
    form = PromptForm()
    quiz = []
    topic = ""

    if request.method == 'POST':
        form = PromptForm(request.POST)
        if form.is_valid():
            topic = form.cleaned_data['prompt']  # we call it "topic" here
            quiz = generate_response(topic)      # this returns a list of MCQs

            return render(request, 'builder/output.html', {
                'quiz': quiz,
                'topic': topic
            })

    return render(request, 'builder/input.html', {'form': form})'''
'''def home(request):
    prompt_form = PromptForm()
    content_form = ContentForm()
    quiz = []
    topic = ""

    if request.method == "POST":
        prompt_form = PromptForm(request.POST)
        content_form = ContentForm(request.POST, request.FILES)

        if prompt_form.is_valid() and prompt_form.cleaned_data.get("prompt"):
            topic = prompt_form.cleaned_data['prompt']
            quiz = generate_response(topic)

        elif content_form.is_valid():
            user_text = content_form.cleaned_data['text']
            pdf_file = request.FILES.get('pdf')
            content = user_text or (extract_text_from_pdf(pdf_file) if pdf_file else "")
            quiz = generate_response(content)

    return render(request, "builder/output.html", {
        "prompt_form": prompt_form,
        "content_form": content_form,
        "quiz": quiz,
        "topic": topic
    })
def home(request):
    quiz = []
    topic = ""

    if request.method == 'POST':
        if 'prompt' in request.POST:
            form = PromptForm(request.POST)
            if form.is_valid():
                topic = form.cleaned_data['prompt']
                quiz = generate_response(topic)
                return render(request, 'builder/output.html', {'quiz': quiz, 'topic': topic})
        else:
            form = ContentForm(request.POST, request.FILES)
            if form.is_valid():
                user_text = form.cleaned_data['text']
                pdf_file = request.FILES.get('pdf')
                content = user_text or (extract_text_from_pdf(pdf_file) if pdf_file else "")
                quiz = generate_response(content)
                return render(request, 'builder/output.html', {'quiz': quiz, 'topic': 'Uploaded Content'})

    return render(request, 'builder/input.html', {'form': PromptForm(), 'form2': ContentForm()})'''
'''from django.shortcuts import render
from .forms import PromptForm, ContentForm
from .ai_engine import generate_response
from .utils import extract_text_from_pdf
from .models import QuizQuestion  
from django.contrib.auth.decorators import login_required


def home(request):
    quiz = []
    topic = ""

    if request.method == 'POST':
        if 'prompt' in request.POST:
            form = PromptForm(request.POST)
            if form.is_valid():
                topic = form.cleaned_data['prompt']
                quiz = generate_response(topic)

                
                for item in quiz:
                    QuizQuestion.objects.create(
                        topic=topic,
                        question=item['question'],
                        question_type=item['type'],
                        options=item.get('options', None),
                        answer=item['answer'],
                        explanation=item['explanation']
                    )

                return render(request, 'builder/output.html', {'quiz': quiz, 'topic': topic})

        else:
            form = ContentForm(request.POST, request.FILES)
            if form.is_valid():
                user_text = form.cleaned_data['text']
                pdf_file = request.FILES.get('pdf')
                content = user_text or (extract_text_from_pdf(pdf_file) if pdf_file else "")
                topic = "Uploaded Content"
                quiz = generate_response(content)

                
                for item in quiz:
                    QuizQuestion.objects.create(
                        topic=topic,
                        question=item['question'],
                        question_type=item['type'],
                        options=item.get('options', None),
                        answer=item['answer'],
                        explanation=item['explanation']
                    )

                return render(request, 'builder/output.html', {'quiz': quiz, 'topic': topic})

    return render(request, 'builder/input.html', {'form': PromptForm(), 'form2': ContentForm()})'''
 
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import PromptForm, ContentForm
from .ai_engine import generate_response
from .utils import extract_text_from_pdf
from .models import QuizQuestion

def home(request):
    quiz = []
    topic = ""

    if request.method == 'POST':
        if 'prompt' in request.POST:
            form = PromptForm(request.POST)
            if form.is_valid():
                topic = form.cleaned_data['prompt']
                quiz = generate_response(topic)

                for item in quiz:
                    QuizQuestion.objects.create(
                        topic=topic,
                        question=item['question'],
                        question_type=item['type'],
                        options=item.get('options', None),
                        answer=item['answer'],
                        explanation=item['explanation']
                    )

                return render(request, 'builder/output.html', {'quiz': quiz, 'topic': topic})

        else:
            form = ContentForm(request.POST, request.FILES)
            if form.is_valid():
                user_text = form.cleaned_data['text']
                pdf_file = request.FILES.get('pdf')
                content = user_text or (extract_text_from_pdf(pdf_file) if pdf_file else "")
                topic = "Uploaded Content"
                quiz = generate_response(content)

                for item in quiz:
                    QuizQuestion.objects.create(
                        topic=topic,
                        question=item['question'],
                        question_type=item['type'],
                        options=item.get('options', None),
                        answer=item['answer'],
                        explanation=item['explanation']
                    )

                return render(request, 'builder/output.html', {'quiz': quiz, 'topic': topic})

    return render(request, 'builder/input.html', {'form': PromptForm(), 'form2': ContentForm()})
    '''

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import PromptForm, ContentForm
from .ai_engine import generate_response
from .utils import extract_text_from_pdf
from .models import QuizQuestion




@login_required
def home(request):
    quiz = []
    topic = ""

    if request.method == 'POST':
        if 'prompt' in request.POST:
            form = PromptForm(request.POST)
            if form.is_valid():
                topic = form.cleaned_data['prompt']
                quiz = generate_response(topic)

                for item in quiz:
                    QuizQuestion.objects.create(
                        topic=topic,
                        question=item['question'],
                        question_type=item['type'],
                        options=item.get('options', None),
                        answer=item['answer'],
                        explanation=item['explanation']
                    )

                return render(request, 'builder/output.html', {'quiz': quiz, 'topic': topic})

        else:
            form = ContentForm(request.POST, request.FILES)
            if form.is_valid():
                user_text = form.cleaned_data['text']
                pdf_file = request.FILES.get('pdf')
                content = user_text or (extract_text_from_pdf(pdf_file) if pdf_file else "")
                topic = "Uploaded Content"
                quiz = generate_response(content)

                for item in quiz:
                    QuizQuestion.objects.create(
                        topic=topic,
                        question=item['question'],
                        question_type=item['type'],
                        options=item.get('options', None),
                        answer=item['answer'],
                        explanation=item['explanation']
                    )

                return render(request, 'builder/output.html', {'quiz': quiz, 'topic': topic})

    return render(request, 'builder/input.html', {'form': PromptForm(), 'form2': ContentForm()})
'''