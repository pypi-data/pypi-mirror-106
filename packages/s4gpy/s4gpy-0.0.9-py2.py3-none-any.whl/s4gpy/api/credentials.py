class CredentialAPI():
    """Wraps credential API."""

    def __init__(self, session):
        """intialiaze a new Credential API"""
        self.session = session

    def get_credentials(self, provider_name):
        """Get a tuple containing credentials for the supplied provider."""
        credentials = self.session.get(f'/providers/{provider_name}').json()
        single_credentials_link = credentials['links'][0]['href']

        single_credentials = self.session.get(
            single_credentials_link,
        ).json()
        login = single_credentials['credentials']['login']
        password = single_credentials['credentials']['password']
        return login, password

    def get_providers(self):
        """get a tuple containing the names providers for which we have at least a credential available"""
        providers = self.session.get(f'/providers').json()
        providers_links = [provider['name'] for provider in providers]
        return providers_links
