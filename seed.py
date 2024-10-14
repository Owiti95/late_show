from app import db
from models import Episode, Guest, Appearance

def seed_data():
    # Example seed data, replace with CSV loading code
    e1 = Episode(date="1/11/99", number=1)
    e2 = Episode(date="1/12/99", number=2)

    g1 = Guest(name="Michael J. Fox", occupation="actor")
    g2 = Guest(name="Sandra Bernhard", occupation="Comedian")

    a1 = Appearance(rating=4, episode=e1, guest=g1)
    a2 = Appearance(rating=5, episode=e2, guest=g2)

    db.session.add_all([e1, e2, g1, g2, a1, a2])
    db.session.commit()

if __name__ == "__main__":
    seed_data()
