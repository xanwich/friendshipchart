from app import db

max_length = 64


class Edge(db.Model):
    __tablename__ = "edges"
    __table_args__ = {"extend_existing": True}
    id = db.Column(db.Integer, primary_key=True)
    l = db.Column(db.String(max_length))
    r = db.Column(db.String(max_length))
    how = db.Column(db.String(max_length))


if __name__ == "__main__":
    print("creating databases...")
    db.create_all()
