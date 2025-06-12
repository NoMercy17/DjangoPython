from django import forms


class CreateNewList(forms.Form):
#the inheritance will have us have the form auto generated and smth else
    name=forms.CharField(label="Name", max_length=200, required=True, error_messages={"required":"Please provide a name!"})   #these fields are the exact same as in our database!! 
    #the label shows before the little box!
    check = forms.BooleanField(required=False)
 



