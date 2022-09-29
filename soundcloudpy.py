import requests
import json

class Soundcloud:

    def __init__(self, o_auth, client_id):

        #: Client id for soundcloud account(must be 32bytes length)
        if len(client_id) != 32:
            raise ValueError("Not valid client id")
        self.client_id = client_id

        #: O-Auth code for requests headers
        self.o_auth = o_auth

        #: Default headers that work properly for the API
        #: User-Agent as if it was requested through Firefox Browser
        self.headers = {"Authorization" : o_auth, "Accept": "application/json",
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0"}

    # ---------------- USER ----------------

    def get_account_details(self):
        req = requests.get("https://api-v2.soundcloud.com/me", headers=self.headers)
        return req.text

    def get_user_details(self, user_id):
        """
        :param user_id: id of the user requested
        """
        req = requests.get(f"https://api-v2.soundcloud.com/users/{user_id}?client_id={self.client_id}", headers=self.headers)
        return req.text

    # ---------------- TRACKS ----------------

    def get_last_track_info(self, limit=1):
        """
        :param limit: number of last tracks reproduced
        """
        req = requests.get(f"https://api-v2.soundcloud.com/me/play-history/tracks?client_id={self.client_id}&limit={limit}", headers=self.headers)
        return req.text

    def get_track_likes_users(self, track_id):
        """
        :param track_id: track id 
        """
        req = requests.get(f"https://api-v2.soundcloud.com/tracks/{track_id}/likers?client_id={self.client_id}", headers=self.headers)
        return req.text

    def get_track_details(self, track_id):
        """
        :param track_id: track id 
        """
        req = requests.get(f"https://api-v2.soundcloud.com/tracks?ids={track_id}&client_id={self.client_id}", headers=self.headers)
        return req.text

    # ---------------- PLAYLISTS ----------------  

    def get_account_playlists(self):
        req = requests.get(f"https://api-v2.soundcloud.com/me/library/all?client_id{self.client_id}", headers=self.headers)
        return req.text

    def get_playlist_details(self, playlist_id):
        """
        :param playlist_id: playlist id 
        """
        req = requests.get(f"https://api-v2.soundcloud.com/playlists/{playlist_id}?representation=full&client_id={self.client_id}", headers=self.headers)
        return req.text

    # ---------------- MISCELLANEOUS ----------------

    def get_recommended(self, track_id):
        """
        :param track_id: track id to get recommended tracks from this
        """
        req = requests.get(f"https://api-v2.soundcloud.com/tracks/{track_id}/related?client_id={self.client_id}", headers=self.headers)
        return req.text

    def get_stream_url(self, track_id):
        """
        :param track_id: track id 
        """
        full_json = self.get_track_details(track_id)
        media_url = full_json[0]['media']['transcodings'][0]['url']
        track_auth = full_json[0]['track_authorization']

        stream_url = f"{media_url}?client_id={self.client_id}&track_authorization={track_auth}"

        req = requests.get(stream_url)

        return dict(json.loads(req.text)).get('url')

    def get_comments_track(self, track_id, limit=100):
        """
        :param track_id: track id for get the comments from
        :param limit:    limit of tracks to get

        :add: with the "next_href" in the return json you can keep getting more comments than the limit
        """
        req = requests.get(f"https://api-v2.soundcloud.com/tracks/{track_id}/comments?threaded=0&filter_replies=1&client_id={self.client_id}&limit={limit}&offset=0&linked_partitioning=1&app_version=1664196962", headers=self.headers)
        return req.text