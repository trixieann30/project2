from django.shortcuts import render

def index(request):
    """
    Renders the main calculator page.
    """
    return render(request, 'MrChips/index.html')

def calculate(request):
    """
    Handles the calculation logic. This is not strictly necessary for a front-end
    calculator, but is included to show how Django views can be used.
    """
    result = None
    error_message = None
    
    if request.method == 'POST':
        try:
            expression = request.POST.get('expression', '')
            # Using eval() is not safe in production, but is used here for simplicity
            # in this example. For a real app, you would need to use a safer
            # expression parser.
            result = eval(expression.replace('x', '*'))
        except (SyntaxError, NameError, TypeError, ZeroDivisionError) as e:
            error_message = f"Invalid expression: {e}"
        except Exception as e:
            error_message = f"An unexpected error occurred: {e}"

    return render(request, 'MrChips/index.html', {'result': result, 'error_message': error_message})
