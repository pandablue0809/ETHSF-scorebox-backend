from sqlalchemy.orm import Session
from supp import models


def add_row(db: Session, data: dict):
    event = models.EncryptTable(
        wallet = data['wallet'],
        oracle = data['oracle'],
        blockchain = data['blockchain'],
        is_encrypted = data['is_encrypted'],
        permit = data['permit'],
        score_int = data['score_int'],
        score_blurb = data['score_blurb'],
        timestamp = data['timestamp']
        )

    try:
        # save to database
        db.add(event)
        db.commit()
        db.refresh(event)

    except Exception as e:
        print(f'\033[35m Error! Not saving to database: {e}\033[0m')