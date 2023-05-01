import csv
import steamapi

# Set up Steam API
steamapi.core.APIConnection(api_key='YOUR_API_KEY')

# Get list of all games in your library
my_games = steamapi.user.SteamUser().games

# Define CSV header row
header = ['Name', 'App ID', 'Playtime (2 weeks)', 'Playtime (total)']

# Open CSV file for writing
with open('steam_library.csv', mode='w', newline='') as file:
    # Create CSV writer object
    writer = csv.writer(file)

    # Write header row to CSV
    writer.writerow(header)

    # Write game info to CSV
    for game in my_games:
        writer.writerow([game.name, game.appid, game.playtime_2weeks, game.playtime_forever])

