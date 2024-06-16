# lance-ify
This project makes use of the Spotify API to take the top 10 artists listened to over the past month and recommends new artists to listen to, as well as their latest projects.  

# Spotify Top Artists and Recommendations

This Python script uses the Spotify API to:
1. Retrieve a user's top artists of the past month.
2. Recommend new artists based on the user's top artists.
3. Suggest the latest projects (albums or singles) from these recommended new artists.

## Prerequisites

- Python 3.x
- Spotify Developer Account

## Installation

1. Clone this repository or download the script.
2. Install the required libraries:
    ```sh
    pip install spotipy
    ```

## Spotify Developer Setup

1. Create a Spotify Developer account and register an application.
2. Obtain your `Client ID` and `Client Secret` from the Spotify Developer Dashboard.
3. Set the `Redirect URI` in your Spotify Developer Dashboard (e.g., `http://localhost:8888/callback`).

## Configuration

Update the script with your Spotify Developer credentials:

```python
CLIENT_ID = 'your_client_id'
CLIENT_SECRET = 'your_client_secret'
REDIRECT_URI = 'http://localhost:8888/callback'

And that should be it! I apologize for not making an easier way for the user to do this. If I had time, I could have built a front end that takes a username as input and returns the results. I will eventually go back and do something like that. In any case, if you do not wish to create a Spotify Dev account, I will include the results from my own testing within this repo. I want to thank the crew for running a great program. 
