from app import app  # import the app object from the main app
from models import db, Episode, Guest, Appearance

def seed_data():
    # create instances of the models
    e1 = Episode(name="The Pilot", date="2023-01-01")
    e2 = Episode(name="The Finale", date="2023-12-31")
    
    g1 = Guest(name="John Doe")
    g2 = Guest(name="Jane Smith")
    
    a1 = Appearance(episode_id=1, guest_id=1)
    a2 = Appearance(episode_id=2, guest_id=2)
    
    # add and commit all data to the session
    db.session.add_all([e1, e2, g1, g2, a1, a2])
    db.session.commit()

# run the seeding inside the app context
if __name__ == "__main__":
    with app.app_context():
        seed_data()
