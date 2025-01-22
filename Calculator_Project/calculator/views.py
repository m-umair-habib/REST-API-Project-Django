from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class CalculatorView(APIView):
    def get(self, request, operation, num1, num2):
        try:
            num1 = float(num1)
            num2 = float(num2)

            if operation == 'add':
                result = num1 + num2
            elif operation == 'subtract':
                result = num1 - num2
            elif operation == 'multiply':
                result = num1 * num2
            elif operation == 'divide':
                if num2 == 0:
                    return Response({'error': 'Cannot divide by zero'}, status=status.HTTP_400_BAD_REQUEST)
                result = num1 / num2
            else:
                return Response({'error': 'Invalid operation'}, status=status.HTTP_400_BAD_REQUEST)

            return Response({'result': result}, status=status.HTTP_200_OK)
        except ValueError:
            return Response({'error': 'Invalid numbers'}, status=status.HTTP_400_BAD_REQUEST)