from flask import Flask, render_template, url_for, request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///music_group.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)

class Albums(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    intro = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return '<Albums %r>' % self.id
@app.route('/')
@app.route('/home')
def home():
    return render_template('homePage.html')


@app.route('/about')
def about():
    return render_template('aboutPage.html')


@app.route('/history')
def history():
    return render_template('historyPage.html')


@app.route('/albums')
def albums():
    albums = Albums.query.order_by(Albums.title.desc())
    return render_template('albumsPage.html', albums=albums)


@app.route('/albums/<int:id>')
def albums_detail(id):
    albums = Albums.query.get(id)

    return render_template('albumDetail.html', albums=albums)


@app.route('/albums/<int:id>/del')
def albums_delete(id):

    albums = Albums.query.get_or_404(id)

    try:
        db.session.delete(albums)
        db.session.commit()
        return redirect('/albums')
    except:
        return 'Помилка при видаленні'



@app.route('/albums/<int:id>/update', methods=['POST', 'GET'])
def update_albums(id):
    albums = Albums.query.get(id)
    if request.method =='POST':
        albums.title = request.form['title']
        albums.intro = request.form['intro']
        albums.text = request.form['text']

        try:
            db.session.commit()
            return redirect('/albums')
        except:
            return 'Помилка при додаванні'

    else:

        return render_template('albumUpdate.html', albums=albums)


@app.route('/add-albums', methods=['POST', 'GET'])
def add_albums():
    if request.method =='POST':
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']

        album = Albums(title=title, intro=intro, text=text)

        try:
            db.session.add(album)
            db.session.commit()
            return redirect('/albums')
        except:
            return 'Помилка при додаванні'

    else:
        return render_template('addAlbumsPage.html')


if __name__ == '__main__':
    app.run(debug=True)