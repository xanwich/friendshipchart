from flask import render_template, flash, request
from app import app, db
from models import Edge
from forms import EdgeForm
from graph import Grapher
from networkx import NetworkXNoPath


def people_from_edges(edges):
    return sorted({e.l for e in edges}.union({e.r for e in edges}))


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
    people = people_from_edges(edges)
    return render_template("index.html", form=form, edges=edges, people=people)


@app.route("/graph", methods=["GET"])
def graph():
    edges = db.session.query(Edge).all()
    people = people_from_edges(edges)
    form = EdgeForm()
    g = Grapher(edges)
    l = request.args.get("l")
    r = request.args.get("r")
    text = None
    if l and l not in people:
        text = f"{l} isn't friends with anyone yet!"
        graph = g.make_image()
    elif r and r not in people:
        text = f"{r} isn't friends with anyone yet!"
        graph = g.make_image()
    elif l and r:
        try:
            path = g.shortest_path(l, r)
            graph = g.make_shortest_path_image(path)
            text = g.shortest_path_text(path)
        except NetworkXNoPath:
            graph = g.make_image()
            text = f"No friendship found between {l} and {r}! Maybe you should introduce them"
    else:
        graph = g.make_image()
    return render_template(
        "graph.html", graph=graph, text=text, form=form, people=people
    )
