from flask import Flask, render_template_string, request
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


@app.route('/', methods=['GET', 'POST'])
def upload():
    upload_message = ""
    if request.method == 'POST':
        file = request.files['file']
        file_name = file.filename

        # print(type(file_name), file_name)

        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file_name)
        file.save(filepath)
        upload_message = "The file was uploaded successfully"

    return render_template_string("""
        <html>
        <title>Upload new File</title>
        
        <h1>Upload new File</h1>
        <form method=post enctype=multipart/form-data>
        <input type=file name=file>
        <input type=submit value=Upload>
        {% if upload_message %}
        {{ upload_message }}
        {% endif %}
    """, upload_message=upload_message)


app.run(debug=True)
