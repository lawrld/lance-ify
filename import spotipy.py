import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Replace these with your actual Spotify Developer credentials
CLIENT_ID = 'your_client_id'
CLIENT_SECRET = 'your_client_secret'
REDIRECT_URI = 'http://localhost:8888/callback'

# Define the scope
scope = 'user-top-read'

def main():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                   client_secret=CLIENT_SECRET,
                                                   redirect_uri=REDIRECT_URI,
                                                   scope=scope))

    # Get the current user's top artists of the past month
    results = sp.current_user_top_artists(limit=5, time_range='short_term')
    top_artists = results['items']
    
    print("Your Top 5 Artists of the Past Month:")
    for idx, artist in enumerate(top_artists):
        print(f"{idx+1}. {artist['name']}")

    # Collect artist IDs for recommendations
    artist_ids = [artist['id'] for artist in top_artists]

    # Get recommendations based on the top artists
    recommendations = sp.recommendations(seed_artists=artist_ids, limit=10)

    # Extract unique new artists from recommendations
    recommended_artists = {}
    for track in recommendations['tracks']:
        for artist in track['artists']:
            if artist['id'] not in artist_ids:  # Only add new artists
                recommended_artists[artist['id']] = artist['name']

    print("\nRecommended New Artists for You:")
    for idx, (artist_id, artist_name) in enumerate(recommended_artists.items()):
        print(f"{idx+1}. {artist_name}")

    # Get the latest albums or singles from each recommended new artist
    print("\nLatest Projects from Recommended New Artists:")
    for artist_id, artist_name in recommended_artists.items():
        # Get the artist's albums, sorted by release date
        albums = sp.artist_albums(artist_id, album_type='album,single', limit=1)
        if albums['items']:
            latest_project = albums['items'][0]
            project_name = latest_project['name']
            release_date = latest_project['release_date']
            print(f"{artist_name}'s latest project: {project_name} (Released on {release_date})")
        else:
            print(f"{artist_name} has no available projects.")

if __name__ == '__main__':
    main()
