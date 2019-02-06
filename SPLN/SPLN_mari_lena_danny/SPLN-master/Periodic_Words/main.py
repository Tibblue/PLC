import os
from flask import Flask, flash, send_from_directory, request, redirect, url_for, render_template, send_file
from werkzeug.utils import secure_filename
from subprocess import getoutput
from PIL import Image
from io import BytesIO
import random
import fileinput
import re

UPLOAD_FOLDER = os.getcwd() + '/uploads'
ALLOWED_EXTENSIONS = set(['txt'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

def allowed_file(filename):
    """Verifica se um ficheiro serve como input ao programa """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def split_word(word, elements):
    """Devolve, se possível, uma lista de símbolos químicos que formam uma dada palavra"""
    w_it = 0
    word_size = len(word)
    ws = []
    ws_it = 0
    ws_size = 0
    while(w_it < word_size):
        o = find_prefix(0, word[w_it:], elements)
        if o >= 118 and ws_it > 0:
            back = 1
            while ws_it > 0 and back == 1:
                ws_it -= 1
                w_it -= len(elements[ws[ws_it]])
                o = find_prefix(ws[ws_it] + 1, word[w_it:], elements)
                ws.pop()
                if o != 118:
                    ws.append(o)
                    w_it += len(elements[o])
                    ws_it += 1
                    back = 0
            if (ws_it <= 0):
                ws = []
                break
        elif o >= 118 and ws_it <= 0:
            ws = []
            break
        else:
            ws.append(o)
            w_it += len(elements[o])
            ws_it += 1
    return (ws, ws_it)

def find_prefix(i, word, elements):
    """Encontra um possível símbolo químico como prefixo da palavra pretendida """
    size = len(elements)
    found = 0
    while i < size and not found :
        if re.match(elements[i], word, re.IGNORECASE): 
            found = 1
        else: i+=1
    return i


def gen_word(result, elements):
    """Para uma dada palavra, obtém as imagens dos respetivos símbolos químicos"""
    temp = []
    for el in result:
        filename = str(el + 1) + '.png'
        temp.append((url_for('uploaded_file', filename =
            filename),elements[el]))

    return temp


@app.route('/result')
def result():
    """Gera a página com o resultado"""
    lines = []

    (symbols, elements) = elems()
    
    with open('uploads/palavras.txt') as fl:
        fc = fl.readlines()

    fc = [l.strip() for l in fc]

    for word in fc:
        (ws, ws_count) = split_word(word, symbols)
        lines.append((word, gen_word(ws, elements)))

    return render_template("result.html", lines = lines)

@app.route('/download_img/', methods=['POST'])
def download_img():
    """Efetua o download da imagem pretendida"""
    line = request.form.get('downloadBtn')
    words = list(filter(None, re.split('\(|\)| |[^\']*\'\)|,|\[|\]|,|\'', line)))
    result_width = 100 * len(words[1:])
    result = Image.new('RGB',(result_width, 100))

    it = 0;
    imageTransp = Image.open('uploads/transp.png')
    for symbol in words[1:]:
        image1 = Image.open(symbol[1:])
        result.paste(im = image1, box = (it * 100 + 10, 0))
        it += 1
        if it < len(words[1:]):
            result.paste(im = imageTransp, box = (it * 100, 0))
        

    img_io = BytesIO()
    result.save(img_io, 'PNG', quality = 70)
    img_io.seek(0)

    return send_file(img_io,
                     mimetype = 'image/png',
                     attachment_filename = words[0] + '.png',
                     as_attachment = True)

@app.route('/', methods=['GET', 'POST'])
def index():
    """Gera a página inicial, onde se pode fornecer um ficheiro, ou uma única palavra"""    
    if request.method == 'POST':
        if 'fileButton' in request.form:
            if 'file' not in request.files:
                flash('No selected file!')
                return redirect(url_for('index'))
            elif not allowed_file(request.files['file'].filename):
                flash('Invalid file! Allowed file types: .txt')
                return redirect(url_for('index'))
            else:
                file = request.files['file']
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'palavras.txt'))
                return redirect('/result')
        elif 'wordButton' in request.form:
            if 'word' in request.form and request.form['word'] != "":
                word = request.form['word']
                with open('uploads/palavras.txt', 'w') as f:
                    f.write(word)
                return redirect('/result')
            else:
                flash('No word was provided!')
                return redirect(url_for('index'))

    return render_template("index.html")

def elems():
    """Obtenção de elementos"""
    out = getoutput("cat uploads/elements.txt | awk -F \"[ \t]+\" '{ print $2 }'")
    symbols = out.split("\n")
    out = getoutput("cat uploads/elements.txt | awk -F \"[ \t]+\" '{ print $3 }'")
    elements = out.split("\n")

    return (symbols, elements)

if __name__ == "__main__":
    app.run(debug = True)