
# forms.py
from django import forms

class SymptomSelectionForm(forms.Form):
    ALL_SYMPTOMS = [
        'Chest discomfort', 'Shortness of breath', 'Fatigue', 'Rapid heartbeat', 'Dizziness',
        'Cough', 'Fever', 'Chronic cough', 'Wheezing', 'Chest tightness',
        'Frequent respiratory infections', 'Increased thirst', 'Frequent urination', 'Unexplained weight loss',
        'Slow healing infections', 'Pain', 'Changes in the skin', 'Changes in bowel habits', 'Headaches',
        'Blurred vision', 'Nosebleeds', 'Memory loss', 'Difficulty solving problems', 'Challenges in completing familiar tasks',
        'Confusion with time', 'Changes in mood', 'Diarrhea', 'Abdominal cramps', 'Nausea', 'Vomiting',
        'Cough lasting more than three weeks', 'Chest pain', 'Weight loss', 'Chills', 'Sweating',
        'Nausea and vomiting', 'Swollen lymph nodes', 'Recurrent infections', 'Weakness', 'Swelling of extremities',
        'Delayed wound healing', 'Swelling in legs', 'Persistent itching', 'High blood pressure', 'Jaundice',
        'Abdominal pain', 'Easy bruising', 'Dark urine', 'Joint pain', 'Stiffness', 'Decreased range of motion',
        'Swelling', 'Grating sensation in the joints', 'Loss of height over time', 'Back pain', 'Stooped posture',
        'Fractures', 'Gradual loss of bone density', 'Sudden high fever', 'Severe headaches', 'Pain behind the eyes',
        'Joint and muscle pain', 'Skin rash', 'Persistent sadness', 'Loss of interest', 'Changes in appetite',
        'Sleep disturbances', 'Excessive worrying', 'Restlessness', 'Difficulty concentrating', 'Muscle tension',
        'Irritability', 'Delusions', 'Hallucinations', 'Disorganized thinking', 'Impaired concentration', 'Lack of motivation',
        'Excessive body weight', 'Increased body fat', 'Breathlessness', 'Low energy levels', 'Weight changes',
        'Hair loss', 'Intolerance to cold or heat', 'Changes in heart rate', 'Rectal bleeding', 'Clay colored stools',
        'Joint pain and swelling', 'Warmth and redness around joints', 'Reduced joint function', 'Sensitivity to light and sound',
        'Visual disturbances', 'Throbbing pain', 'Seizures', 'Temporary confusion', 'Staring spells',
        'Uncontrollable jerking movements', 'Loss of consciousness', 'Fading of colors', 'Sensitivity to light',
        'Difficulty seeing at night', 'Double vision', 'Gradual loss of peripheral vision', 'Halos around lights',
        'Eye redness', 'Itching in the anal region', 'Swelling around the anus', 'Pain during bowel movements',
        'Lumps near the anus'
    ]

    symptoms = forms.MultipleChoiceField(
        choices=[(symptom, symptom) for symptom in ALL_SYMPTOMS],
        widget=forms.CheckboxSelectMultiple,
        required=True,
    )

    def clean_symptoms(self):
        selected_symptoms = self.cleaned_data.get('symptoms', [])
        if len(selected_symptoms) > 5:
            raise forms.ValidationError('You can select up to 5 symptoms.')
        return selected_symptoms
