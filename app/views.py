from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from .forms import SymptomSelectionForm
from sklearn.tree import DecisionTreeClassifier
import joblib
import numpy as np
# Create your views here.
def index(request) :
    return render(request, 'app/index.html')

def about(request) :
    return render(request, 'app/about.html')

@login_required
def contact(request):
    if request.method == "POST":
       name =request.POST['name']
       email =request.POST['email']
       message =request.POST['message']

       send_mail(

            name,
            email,
            message,
            ['fakemail@email.com'],

       )
       
       return render (request, 'app/contact.html',{'name': name})
      
    else:    
       return render (request, 'app/contact.html')


@login_required
def prediction(request):
    model = joblib.load('app/success.joblib')

    if request.method == 'POST':
        form = SymptomSelectionForm(request.POST)
        if form.is_valid():
            selected_symptoms = form.cleaned_data['symptoms']

            # Convert the selected symptoms into a one-hot encoded vector
            symptoms_vector = [1 if symptom in selected_symptoms else 0 for symptom in SymptomSelectionForm.ALL_SYMPTOMS]

            symptoms_vector = np.array(symptoms_vector).reshape(1, -1)


            # Make predictions using the trained model
            prediction = model.predict(symptoms_vector)

            form_submitted = True

            # Render the result in prediction.html
            return render(request, 'app/prediction.html', {'prediction': prediction, 'selected_symptoms': selected_symptoms,'form_submitted':form_submitted, 'form': form})

    else:
        form = SymptomSelectionForm()

    return render(request, 'app/prediction.html', {'form': form})
