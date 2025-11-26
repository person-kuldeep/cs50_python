def main():
    pace = get_pace(miles=26.2, minutes=0)
    print(f"You need to run each mile in {round(pace)} minutes.")


def get_pace(miles, minutes):
        if not minutes > 0:
            raise Exception("Miles must be greater than zero.")
            
        return minutes/ miles
main()
