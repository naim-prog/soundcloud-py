# soundcloud-py

Soundcloud API Wrapped for Python, simple and with only 1 file

This is a Wrapped API that it is used from soundcloud web browser, its is subjected to changes and `NOT OFFICIAL`

## Installation

1. For installation see use requirements.txt for installation packages
2. Get the O-Auth from soundcloud headers
3. Get the Client id from soundcloud URL's

## How to get O-Auth and Client id

1. Go to [soundcloud](https://soundcloud.com) and login in
2. Open the "Inspect" tool (F12 on most browsers)
3. Refresh the page
4. Go to the page "Network" on the inspect terminal
5. Search on the column "File" for the "client_id" and "Request headers" for "Authorization"

`client_id`: string of 32 bytes alphanumeric

`authorization`: string that begins with O-Auth and a string (the o-auth token is "O-Auth . . .")

Example code snippet (O-Auth and client_id are NOT real, use yours):

```python
from soundcloudpy import Soundcloud

account = Soundcloud("O-Auth 3-26432-21446-asdif2309fj", "jHvc9wa0Ejf092wj3f3920w3F920as02")

print(account.get_account_details())
```


## Functions

* Own account details
* User public details
* Own followers
* Last tracks reproduced info
* User profiles from tracks likes
* Track details
* Tracks liked
* Like a track
* Unlike a track
* Repost a track
* Unrepost a track
* Own playlists
* Playlists details
* Create a playlist
* Delete a playlist
* Recommended tracks of a track
* Strem URL's of a track (you can use it to reproduce the audio in VLC for example)
* Comments of a track
* Get mixed selection of playlists

## DISCLAIMER

I take no responsability for the issues you may have with your soundcloud account or for breaching the [Terms of Use](https://developers.soundcloud.com/docs/api/terms-of-use) of soundcloud
