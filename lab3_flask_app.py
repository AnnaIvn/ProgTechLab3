from flask import Flask, render_template, request

app = Flask(__name__)


# def some_output():
#     return "My dockerised app using flask"

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/process_input', methods=['POST'])
# def process_input():
#     input_data = request.form['input_data']
#     result = process_data(input_data)
#     return render_template('result.html', result=result)

# def process_data(arg):
#     try:
#         check_format(arg)
#         arg = two_dot_formating(arg)
#         arg = space_formating(arg)
#         arg = distrib_by_age(arg)
#         arg = exception(arg)
#         return arg
#     except Exception as e:
#         return str(e)

# @app.route('/check_format/{arg}')
def check_format(arg):
    if arg[0] == '6' or arg[0] == '7' or arg[0] == '8' and len(arg) >= 4:
        return True
    raise ValueError("Incorrect input format")

# @app.route('/two_dot_formating/{arg}')
def two_dot_formating(arg):
    if arg[1] != ':':
        return str(arg[:1] + ':' + arg[1:])
    return arg

# @app.route('/space_formating/{arg}')
def space_formating(arg):
    if arg[2] != ' ':

        return str(arg[:2] + ' ' + arg[2:])
    return arg

# @app.route('/distrib_by_age/{arg}')
def distrib_by_age(arg):
    if int(arg[0]) == 6:
        return str(arg + ' -> 1st grade')
    elif int(arg[0]) == 7:
        return str(arg + ' -> 2nd grade')
    elif int(arg[0]) == 8:
        return str(arg + ' -> 3rd grade')
    else:
        raise ValueError("Incorrect age")

def exception(arg):
    if int(arg[0]) == 5:
        raise Exception("Age exception | 5 years -> 1st grade")
    return arg

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
