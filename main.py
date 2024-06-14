from flask import Flask, render_template
import json

app = Flask(__name__)

counter_file = 'count.json'


def read_counter():
    
    with open(counter_file, 'r') as file:
        data = json.load(file)
        return data.get('hits', 0)

def write_counter(count):
    with open(counter_file, 'w') as file:
        json.dump({'hits': count}, file)

@app.route('/')
def index():
    
   # Read the current count
    count = read_counter()
    # Increment the visit count
    count += 1
    # Write the new count back to the file
    write_counter(count)
    return render_template('converter.html', visit_count=count)

@app.route('/visits')
def visits():

    # Read the current count
    count = read_counter()
    return render_template('visits.html', visit_count=count)
    

if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
