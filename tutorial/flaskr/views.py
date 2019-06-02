import flask
from flaskr import app, db
from flaskr.models import Entry

@app.route('/')
def show_entries():
    entries = Entry.query.all()
    return flask.render_template('show_entries.html',entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
    entry=Entry(
        title = flask.request.form['title'],
        text = flask.request.form['text']
    )
    db.session.add(entry)
    db.session.commit()
    return flask.redirect(flask.url_for('show_entries'))