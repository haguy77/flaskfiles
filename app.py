from flask import Flask, render_template, request, send_file, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/upload')
def upload_file():
    print(request.url_root)
    return render_template('upload.html')


@app.route('/uploader', methods=['GET', 'POST'])
def uploader():
    if request.method == 'POST':
        f = request.files['file']
        fn = secure_filename(f.filename)
        f.save(fn)
        print(app.root_path)
        return send_file('test.xlsx', as_attachment=True)
        # return 'worked !'
    if request.method == 'GET':
        f = request.files['file']
        fn = secure_filename(f.filename)
        return send_file(fn, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
