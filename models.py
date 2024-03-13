from app import db


class Edge(db.Model):
    __tablename__ = "edges"
    __table_args__ = {"extend_existing": True}
    id = db.Column(db.Integer, primary_key=True)
    l = db.Column(db.String(64))
    r = db.Column(db.String(64))
    how = db.Column(db.String(64))


if __name__ == "__main__":
    print("creating databases...")
    db.create_all()
