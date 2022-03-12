from django import forms

class SearchForm(forms.Form):
    response_time = forms.CharField(required=False)
    availability = forms.CharField(required=False)
    throughput = forms.CharField(required=False)
    successability = forms.CharField(required=False)
    reliability = forms.CharField(required=False)
    compliance = forms.CharField(required=False)
    best_practices = forms.CharField(required=False)
    latency = forms.CharField(required=False)
    documentation = forms.CharField(required=False)
    service_name = forms.CharField(required=False)
    Wsdl_address = forms.CharField(required=False)
    
    