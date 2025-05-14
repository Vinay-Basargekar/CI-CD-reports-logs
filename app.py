from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        # You can store the data here
        return render_template('success.html', name=name)
    return render_template('register.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
