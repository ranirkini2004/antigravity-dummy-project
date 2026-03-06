from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# In-memory database
tasks = []
task_id_counter = 1

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    global task_id_counter
    task_content = request.form.get('content')
    if task_content and task_content.strip() != "":
        tasks.append({'id': task_id_counter, 'content': task_content.strip(), 'completed': False})
        task_id_counter += 1
    return redirect('/')

@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = not task['completed'] # toggle completion status
            break
    return redirect('/')

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True, port=5000)
