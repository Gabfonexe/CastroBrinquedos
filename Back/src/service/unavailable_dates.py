
from datetime import datetime
from src.model.calendar import DateUnavailable
from src.extensions.extensions import db


def list_dates_unavailables():
    now = datetime.now().date()
    dates = db.session.query(DateUnavailable).filter(DateUnavailable.date >= now).all()
    return dates

