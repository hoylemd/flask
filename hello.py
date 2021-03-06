from flask import Flask, url_for
from people import people
app = Flask(__name__)

me = 'mike'


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/whoami')
def whoami():
    person = people[me]
    output = 'I am ' + person['name'] + ', ' + str(person['age'])
    output += ' year old ' + person['job'] + ', and ' + person['tidbit']
    return output


@app.route('/person/')
def person_index():
    output = 'People I know<br><ul>'
    for name in people:
        output += '<li><a href="' + url_for('person', shortname=name) + '">'
        output += people[name]['name'] + '</a></li>'

    return output


@app.route('/person/<shortname>')
def person(shortname):
    output = "<p>"
    if shortname in people:
        person = people[shortname]
        output += person['name'] + ' is a ' + str(person['age'])
        output += ' year old ' + person['job'] + ', ' + person['tidbit']
    else:
        output += shortname + ' is not a person I know.'

    output += '</p><a href="' + url_for('person_index') + '">back to list</a>'

    return output


def run_app():
    app.run(host='0.0.0.0', debug=False)


if __name__ == '__main__':
    app.run(debug=True)
