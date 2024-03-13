from flask import render_template, flash, request
from app import app, db
from models import Edge
from forms import EdgeForm
from graph import Grapher


@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    form = EdgeForm()
    if request.method == "POST":
        if form.validate_on_submit():
            edge = Edge(
                l=form.l.data,
                r=form.r.data,
                how=form.how.data,
            )
            db.session.add(edge)
            db.session.commit()
    edges = db.session.query(Edge).order_by(Edge.id.desc()).all()
    people = sorted({e.l for e in edges}.union({e.r for e in edges}))
    return render_template("index.html", form=form, edges=edges, people=people)


@app.route("/graph")
def graph():
    edges = db.session.query(Edge).all()
    g = Grapher(edges)
    return render_template("graph.html", graph=g.make_image())
