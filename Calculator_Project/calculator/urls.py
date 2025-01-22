from django.urls import path
from calculator.views import CalculatorView

urlpatterns = [
    path('<operation>/<num1>/<num2>/', CalculatorView.as_view(), name='calculator-operation'),
]
