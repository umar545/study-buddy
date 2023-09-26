from django.forms import ModelForm
from  .views import Room

class RoomForm (ModelForm):
    model = Room
    fields = '__all__'