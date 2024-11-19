from django import forms
from loja.models import Cliente, Produto

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"
        widgets = {
            'nome_completo': forms.TextInput(attrs={'class': 'input-class', 'placeholder': 'Digite seu nome completo'}),
            'email': forms.EmailInput(attrs={'class': 'input-class', 'placeholder': 'Digite seu email'}),
            'telefone': forms.TextInput(attrs={'class': 'input-class', 'placeholder': 'Digite seu telefone'}),
            'data_nascimento': forms.DateInput(attrs={'class': 'input-class', 'placeholder': 'Selecione sua data de nascimento', 'type': 'date'}),
            'cpf': forms.TextInput(attrs={'class': 'input-class', 'placeholder': 'Digite seu CPF'}),
            'endereco': forms.TextInput(attrs={'class': 'input-class', 'placeholder': 'Digite seu endereço'}),
            'numero': forms.TextInput(attrs={'class': 'input-class', 'placeholder': 'Número'}),
            'complemento': forms.TextInput(attrs={'class': 'input-class', 'placeholder': 'Complemento'}),
            'bairro': forms.TextInput(attrs={'class': 'input-class', 'placeholder': 'Bairro'}),
            'cidade': forms.TextInput(attrs={'class': 'input-class', 'placeholder': 'Cidade'}),
            'estado': forms.TextInput(attrs={'class': 'input-class', 'placeholder': 'Estado'}),
            'cep': forms.TextInput(attrs={'class': 'input-class', 'placeholder': 'CEP'}),
        }

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = "__all__"
