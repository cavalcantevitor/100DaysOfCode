from mastodon import Mastodon


class SendPost:
    def __init__(
            self,
            api_base_url='https://mastodon.social',
            client_credentials_file='pytooter_clientcred.secret',
            user_credentials_file='pytooter_usercred.secret'
    ):
        self.api_base_url = api_base_url
        self.client_credentials_file = client_credentials_file
        self.user_credentials_file = user_credentials_file

        try:
            Mastodon.create_app(
                'my_app',
                api_base_url=api_base_url,
                to_file=client_credentials_file
            )
        except FileExistsError:
            # If the file already exists, we skip app creation
            pass

        self.mastodon = Mastodon(
            client_id=client_credentials_file,
            api_base_url=api_base_url
        )

    def login(self, username, password):
        try:
            self.mastodon.log_in(
                username=username,
                password=password,
                to_file=self.user_credentials_file
            )
        except Exception as e:
            print(f"Login failed: {e}")

    def send_post(self, message):
        try:
            self.mastodon.toot(message)
        except Exception as e:
            print(f"Failed to post message: {e}")