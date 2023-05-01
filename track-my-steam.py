import steamapi

# Set up Steam API
steamapi.core.APIConnection(api_key='YOUR_API_KEY')

# Get list of all games in your library
my_games = steamapi.user.SteamUser().games

# Print name and playtime for each game in your library
for game in my_games:
    print(game.name, game.playtime_forever)
