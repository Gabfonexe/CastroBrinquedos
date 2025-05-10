
from src.model.calendar import DateUnavailable
from src.extensions.extensions import db


def list_dates_unavailables():
    dates = db.session.query(DateUnavailable).all()
    return dates
