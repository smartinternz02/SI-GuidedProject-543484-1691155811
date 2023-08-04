from flask import Flask,render_template,request
import ibm_db

app = Flask(__name__)

conn = ibm_db.connect("DATABASE=bludb; HOSTNAME=b0aebb68-94fa-46ec-a1fc-1c999edb6187.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud; PORT=31249; UID=cpy32301;PWD=jYysQ9k91qPupfam;SECURITY = SSL; SSLSERVERCERTIFICATE=DigiCertGlobalRootCA.crt"," "," ")
print (ibm_db.active(conn))

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/contact")
def contact():
  return render_template("contact.html")

@app.route("/login", methods=["GET","POST"])
def login():
  if request.method == "POST":
    uname=request.form['username']
    pword=request.form['password']
    print(uname,pword)
    sql= 'SELECT * FROM REGISTER WHERE USERNAME=? AND PASSWORD=?'
    stmt=ibm_db.prepare(conn,sql)
    ibm_db.bind_param(stmt,1,uname)
    ibm_db.bind_param(stmt,2,pword)
    ibm_db.execute(stmt)
    out=ibm_db.fetch_assoc(stmt)
    print(out)
    if out==False:
      msg="Invalid Credentials"
      return render_template("login.html",login_message=msg) 
    else:
      role=out['ROLE']
      if role == 0:
        return render_template("profile_admin.html")
      elif role == 1:
        return render_template("profile_student.html")
      else:
        return render_template("profile_faculty.html") 
  return render_template("login.html")


@app.route('/register', methods=["GET","POST"])
def register():
  if request.method == "POST":
   
   return render_template("registration.html")

if __name__== "__main__":
  app.run(debug=True,host="0.0.0.0")
