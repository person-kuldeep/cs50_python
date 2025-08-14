SHOWS = [
    "Avatar: The Last Airbender",
    "Ben 10",
    "Arthur",
    "Spongebob Squarepants",
    "Phineas and Ferb",
    "Kim Possible",
    "Jimmy Neutron",
    "The Proud Family"
]

def main():
    cleaned_shows = []
    for show in SHOWS:
        cleaned_shows.append(show.title().strip())
    print(":)".join(cleaned_shows)) # Join shows with ":)"
    #join can take list of strings 
    #and join them with a string 
main()        