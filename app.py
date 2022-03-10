from flask import Flask, request, render_template
from scala import get_scale

app = Flask(__name__)


@app.route('/info')
def info():
    return render_template("info.html")


@app.route('/', methods=["GET", "POST"])
def punctation():
    if request.method == "POST":
        point = request.form.get("pkt2")
        if point == "":
            point = 10
        try:
            int(point)
        except:
            return render_template("form.html")
        x = get_scale(int(point))
        return render_template("final.html", arr=x)
    return render_template("form.html")


if __name__ == '__main__':
    app.run()
'''

ocena celująca – 100%;
ocena bardzo dobra – od 88% do 99%;
ocena dobra – od 72% do 87%;
ocena dostateczna – od 56% do 71%;
ocena dopuszczająca – od 41% do 55%;
ocena niedostateczna – 0% do 40%;

'''
