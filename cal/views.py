from django.shortcuts import render

def calculate(request):
    result = ""

    if request.method == "GET":
        pass
    elif request.method == "POST":
        number1 = int(request.POST['number1'])
        number2 = int(request.POST['number2'])
        operation = request.POST['operation']

        if operation == "plus":
            result = number1 + number2
        elif operation == "minus":
            result = number1 - number2
        elif operation == "multiply":
            result = number1 * number2
        elif operation == "divide":
            result = number1 / number2
        else:
            result = "Nothing"

    return render(request, 'calculate.html', {
        'result': result,
    })