import ephem

def get_moon_phase(date):
    try:
        # Convert the date string to an ephem Date object
        date_obj = ephem.Date(date)

        # Calculate the moon phase for the given date
        moon = ephem.Moon(date_obj)
        phase = moon.phase

        # Define moon phase descriptions based on the phase value
        if phase < 3.69:
            return "New Moon"
        elif phase < 10.19:
            return "Waxing Crescent"
        elif phase < 18.69:
            return "First Quarter"
        elif phase < 25.19:
            return "Waxing Gibbous"
        elif phase < 29.69:
            return "Full Moon"
        elif phase < 36.19:
            return "Waning Gibbous"
        elif phase < 43.19:
            return "Last Quarter"
        else:
            return "Waning Crescent"
    except Exception as e:
        return None
