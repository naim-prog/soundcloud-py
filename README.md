# soundcloud-py

Soundcloud API Wrapped for Python, simple and with only 1 file

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

## DISCLAIMER

I take no responsability for the issues you may have with your soundcloud account or for breaching the [Terms of Use](https://developers.soundcloud.com/docs/api/terms-of-use) of Use of soundcloud
