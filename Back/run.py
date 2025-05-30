import app
from src.controller import user, dates,  product
import threading
from src.tasks import amount_and_calendar_dayli_routine

if __name__ == "__main__":
    thread = threading.Thread(target=amount_and_calendar_dayli_routine, daemon=True)
    thread.start()
    app.app.run(host="0.0.0.0", port=5000)
