import requests
import datetime

def get_next_race():
    """
    Fetches the next F1 race from the Ergast API and calculates the days until the race.
    """
    try:
        response = requests.get("http://api.jolpi.ca/ergast/f1/current.json")
        response.raise_for_status()  # Raise an exception for bad status codes
        schedule = response.json()['MRData']['RaceTable']['Races']
        today = datetime.datetime.now().date()

        for race in schedule:
            race_date_str = race['date']
            race_date = datetime.datetime.strptime(race_date_str, '%Y-%m-%d').date()
            if race_date >= today:
                days_until = (race_date - today).days
                return f"Next race: {race['raceName']} on {race_date_str} (in {days_until} days)"

        return "No upcoming races found for the current season."
    except requests.exceptions.RequestException as e:
        return f"Error fetching race schedule: {e}"

def get_driver_standings():
    """
    Fetches the current F1 driver standings from the Ergast API.
    """
    try:
        response = requests.get("http://api.jolpi.ca/ergast/f1/current/driverStandings.json")
        response.raise_for_status()
        standings = response.json()['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings']

        result = "\n--- Driver Standings ---\n"
        for driver_standing in standings:
            position = driver_standing['position']
            driver = driver_standing['Driver']['givenName'] + " " + driver_standing['Driver']['familyName']
            constructor = driver_standing['Constructors'][0]['name']
            points = driver_standing['points']
            result += f"{position}. {driver} ({constructor}) - {points} points\n"
        return result
    except requests.exceptions.RequestException as e:
        return f"Error fetching driver standings: {e}"
    except (KeyError, IndexError):
        return "Could not parse driver standings. The season may not have started yet."

def get_constructor_standings():
    """
    Fetches the current F1 constructor standings from the Ergast API.
    """
    try:
        response = requests.get("http://api.jolpi.ca/ergast/f1/current/constructorStandings.json")
        response.raise_for_status()
        standings = response.json()['MRData']['StandingsTable']['StandingsLists'][0]['ConstructorStandings']

        result = "\n--- Constructor Standings ---\n"
        for constructor_standing in standings:
            position = constructor_standing['position']
            constructor = constructor_standing['Constructor']['name']
            points = constructor_standing['points']
            result += f"{position}. {constructor} - {points} points\n"
        return result
    except requests.exceptions.RequestException as e:
        return f"Error fetching constructor standings: {e}"
    except (KeyError, IndexError):
        return "Could not parse constructor standings. The season may not have started yet."

if __name__ == "__main__":
    print("F1 Info:")
    print(get_next_race())
    print(get_driver_standings())
    print(get_constructor_standings())
