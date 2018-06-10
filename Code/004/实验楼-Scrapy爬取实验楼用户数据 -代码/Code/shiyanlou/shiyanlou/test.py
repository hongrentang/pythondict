
from sqlalchemy.orm import sessionmaker
from models import Course,engine

Session = sessionmaker(bind=engine)
session = Session()
session.add(('erew','wrew','wrew',2))
session.commit()
