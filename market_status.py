from datetime import datetime
from zoneinfo import ZoneInfo

def is_market_open():
    ny_time = datetime.now(ZoneInfo("America/New_York"))

    weekday = ny_time.weekday()
    hour = ny_time.hour

    if weekday == 4 and hour >= 17:
        return False
    
    if weekday == 5:
        return False
    
    if weekday == 6 and hour < 17:
        return False
    
    return True