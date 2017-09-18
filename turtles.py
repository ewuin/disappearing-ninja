from flask import Flask, render_template, request, redirect, Markup, escape, session
app = Flask(__name__)
app.secret_key="password"
validated=['red','blue','orange','purple']

users={
'red':{
'name':'raphael',
'photo':"url_for('static',filename='raphael.jpg')}}'>",
},

'blue':{
'name':'leonardo',
'photo':"<img src='{{ url_for('static', filename = 'farm.jpg') }}'>",
},

'purple':{
'name':'donatello',
'photo':"donatello.jpg",
},

'orange':{
'name':'michelangelo',
'photo':"<p>This is test</p>",
},
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninjas/<username>')
def show_user_profile(username):
    #accepted usernames are blue,red,orange,purple
    if username in users.keys():
        print "valid user"
        print username
        ninja_name=users[str(username)]['name']
        x1=escape('<img src=\"{{')
        x1+=users[str(username)]['photo']
        #x1+=escape('}}\">')
        x1=Markup(x1)
        #x1.strip()
        session['phot']=users[str(username)]['photo']
        print type(x1)
        print x1
        return render_template("ninjas.html", username=ninja_name, photo_url=x1)
    #else:
    #    print "invalid user"
    #    username="not april"
    ##    return render_template("ninjas.html", username=username, photo_url=photo_url)

app.run(debug=True)
