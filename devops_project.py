from flask import Flask , render_template
app = Flask(__name__) ##Module Name = __name__ = __main__


uploads = [
        {
            "user": "RITIK VALA",
            "header": "Post No.1",
            "caption": "First Post Caption",
            "date_uploaded": "24 February, 2021"
        },
        {
            "user": "JAMES BOND",
            "header": "Post No.2",
            "caption": "Second Post Caption",
            "date_uploaded": "15 March, 2021"
        }

]


##Assigned URL for Home Page.
@app.route("/")
def home():
    return render_template("home_page.html", uploads=uploads)

##Assigned URL for About Page.
@app.route("/about")
def about():
    return render_template("about_page.html")

if __name__ == "__main__":
    app.run(debug=True)
