from flask import Flask, render_template, request, send_file, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)


# interface for uploading files
@app.route('/upload')
def upload_file():
    print(request.url_root)
    return render_template('upload.html')


# endpoint that actually uploads the files (the interface send a request to this endpoint when the button is pushed)
@app.route('/uploader', methods=['GET', 'POST'])
def uploader():
    if request.method == 'POST':
        # in the request you send a file and the key for it called "file"
        f = request.files['file']
        # not actually necessary for our situation
        fn = secure_filename(f.filename)
        f.save(fn)
        # returning the file, works the same with send_from_directory
        return send_file('test.xlsx', as_attachment=True)
        # return 'worked !'


if __name__ == '__main__':
    app.run(debug=True)
