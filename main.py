from flask import Flask,render_template,request,redirect,url_for
import json
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin
#variable defining 
app = Flask(__name__)
global classes
global message
message = ""
try:
    with open("/home/hangar/DashboardV2/data/problems.json","r",encoding="utf-8") as my_file:
        classes = json.load(my_file)
except: 
    classes = {}

try:
    with open("/home/hangar/DashboardV2/data/users.json","r",encoding="utf-8") as my_file:
        users = json.load(my_file)
except: 
    users = {}    
app.config['SECRET_KEY'] = 'ThisIsSecretKeyVerySecret'

# Flask-Login setup
login_manager = LoginManager()
login_manager.init_app(app)

# User model
class User(UserMixin):
    def __init__(self, user_id):
        self.id = user_id

    @staticmethod
    def get(user_id):
        return User(user_id)



@app.route("/edit",methods=["GET","POST"])
@login_required
def edit():
    if request.method == "POST":
        room = request.form.get("room")
        problems = request.form.getlist("problem")
        print(problems)
        if problems == []:
            print("test")
            classes.pop(room)
            save(classes=classes)
        else:
            classes[room] = {"problems":[i for i in classes[room]["problems"] if i not in problems],"isFree":classes[room]["isFree"]}
            save(classes=classes)
    return render_template("edit.html", rooms=classes)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("https://dashboard.bee-vernier.ts.net"+url_for('index'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users.get(username)
        if user and password == user['password']:
            login_user(User(user_id=username))
            return redirect("https://dashboard.bee-vernier.ts.net"+url_for('edit'))
        else:
            return render_template('login.html', error='Invalid username or password')
    else:
        return render_template('login.html')

def extract_jotform_data():
    output = {}
    f = open("file.txt","w",encoding="utf-8")
    form_data = request.form.to_dict()
    f.write(str(form_data))
    f.close()
    if form_data.get("rawRequest"):
        for key, value in json.loads(form_data["rawRequest"]).items():
            # Removes the "q<number>_" part from the key name
            # Instead of "q5_quantity" we want "quantity" as the key
            temp = key.split("_")
            new_key = key if len(temp) == 1 else "_".join(temp[1:])
            # Saves the item with the new key in the dictionary
            output[new_key] = value

    return output

def save(classes):
    with open("/home/hangar/DashboardV2/data/problems.json","w",encoding="utf-8") as my_file:
        json.dump(classes,my_file,ensure_ascii=False)

def save_users(users):
    with open("/home/hangar/DashboardV2/data/users.json","w",encoding="utf-8") as my_file:
        json.dump(users,my_file,ensure_ascii=False)

def update_classes(jotform):
    room = jotform["typeA16"]
    if room in classes:
            if jotform['input2'] not in classes[room]['problems']:
                classes[room]["problems"].append(jotform['input2'])
            return 'ok'
    classes[room] = ({"problems":[jotform['input2']],"isFree":"פנוי"})
    save(classes=classes)
    print(classes)

@app.route('/jotform', methods=['GET', 'POST'])
def jotform():
    if request.method == 'POST':
        jotform = extract_jotform_data()
        update_classes(jotform)
        print(jotform)
        return "ok", 200
    return "no go away"    

@app.route("/data",methods=['POST'])
def getData():
    return classes

@app.route("/message",methods=['POST'])
def getMessage():
    return message

@app.route("/users",methods=["GET","POST"])
@login_required
def edit_users():
    if request.method == "POST":
        user = request.form.get("user")
        password = request.form.get("password")
        print(password)
        if password:
            users[user] = {"password":password}
        else:
            users.pop(user)
    save_users(users)
    return render_template("changeUser.html", users=users)

@app.route("/get_classes",methods=["POST"])
def get_classes():
    if request.form.get("key") == "wajitalslkmLatkolkadws":
        room = request.form.get("room")
        isFree = request.form.get("class")
        if room in classes: 
            classes[room]["isFree"] = isFree
        else:
            print("room not in classes")
            classes[room] = {"problems":[],"isFree":isFree}
    save(classes=classes)
    return "ok"

@app.route("/announce",methods=["POST","GET"])
def announce():
    if request.method == "POST":
        global message
        message = request.form.get("message")
        
    return render_template("announce.html",message=message)


@app.route("/")
def index():
    return render_template("index.html",message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
