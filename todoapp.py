from flask import Flask, render_template, request, redirect
import re
app = Flask(__name__)

todo_list = []

@app.route('/')
def todos():
    return render_template('index.html', todo_list = todo_list)

@app.route('/submit', methods = ['POST'])
def submit():
    valid = True
    task = request.form['task']
    email = request.form['email']
    pattern = '^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$'
    if re.match(pattern,email) == None:
        valid = False
    
    priority = request.form['priority']
    if priority not in ['low', 'medium', 'high']:
        valid = False
    
    if valid:
        todo = {'task': task,
                'email': email,
                'priority': priority}
        todo_list.append(todo)
    return redirect('/')

@app.route('/clear', methods = ['POST'])
def clear():
    todo_list.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run()