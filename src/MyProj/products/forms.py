from django import forms

from .models import Product

class ProductCreateForm(forms.ModelForm):
  title = forms.CharField(label = '',
                          widget = forms.TextInput(
                                   attrs = {"placeholder":"UR TITLE"}
                                                  )
                          )
  v_email = forms.EmailField()
  description = forms.CharField(required = False, widget = forms.Textarea(
                                                  attrs = {
                                                     "placeholder" : "UR description",
                                                     "rows":15,
                                                     "cols":20,
                                                     "id": "my_id_for_TA"
                                                          }
                                                                         )
                               )
  price = forms.DecimalField(initial = 99.99)
  class Meta:
    model = Product
    fields = [ 
                'title',
                'description',
                'price'

             ]

  #Form validation methods
  def clean_title_method(self,*args, **kwargs):
    var_title = self.cleaned_data.get("title")
    if not "CFE" in var_title:
      raise forms.ValidationError("This is not a valid title")
    if not "News" in var_title:
      raise forms.ValidationError("This is not a valid title")
    return var_title

  def clean_email_method(self,*args, **kwargs):
    var_email = self.cleaned_data.get("v_email")
    if not var_email.endswith("edu"):
      raise forms.ValidationError("This is not a valid email")
    return var_email


    # class ProductCreateForm(forms.ModelForm):
#   class Meta:
#     model = Product
#     fields = [ 
#                 'title',
#                 'description',
#                 'price'

#              ]

# class RawDjangoProductForm(forms.Form):
#   title = forms.CharField()
#   description = forms.CharField()
#   price = forms.DecimalField()
 

class RawDjangoProductForm(forms.Form):
  title = forms.CharField(label = '',
                          widget = forms.TextInput(
                                   attrs = {"placeholder":"UR TITLE"}
                                                  )
                          )
  description = forms.CharField(required = False, widget = forms.Textarea(
                                                  attrs = {
                                                     "placeholder" : "UR description",
                                                     "rows":15,
                                                     "cols":20,
                                                     "id": "my_id_for_TA"
                                                          }
                                                                         )
                               )
  price = forms.DecimalField()

