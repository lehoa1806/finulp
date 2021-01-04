import os

from common.functools import cached_property
from scraper.common import BrowserType


class Env:
    @classmethod
    def get_environment_variable(
        cls,
        env: str,
        default=None,
        require=False,
    ) -> str:
        val = os.getenv(env) or default
        if val is None and require:
            raise Exception(f'Environment variable [{env}] not available')
        return val

    @cached_property
    def config_file(self) -> str:
        return self.get_environment_variable('FINLP_CONFIG_FILE', '')

    @cached_property
    def rakuten_creds_code(self) -> str:
        return self.get_environment_variable('RAKUTEN_CREDS_CODE')

    @cached_property
    def i3investor_credentials(self) -> str:
        return self.get_environment_variable('I3INVESTOR_CREDS_CODE')

    # Slack
    @cached_property
    def slack_token_code(self) -> str:
        return self.get_environment_variable('FINLP_SLACK_TOKEN_CODE')

    # Scraper
    @cached_property
    def headless(self) -> bool:
        headless = self.get_environment_variable('SCRAPER_HEADLESS')
        return headless in {'True', 'true'}

    @cached_property
    def browser_type(self) -> BrowserType:
        """
        SCRAPER_BROWSER_TYPE: CHROME or FIREFOX
        """
        return BrowserType(
            self.get_environment_variable('SCRAPER_BROWSER_TYPE', 'Chrome'))

    # PostgreSQL
    @cached_property
    def postgresql_host(self) -> str:
        return self.get_environment_variable('POSTGRESQL_HOST')

    @cached_property
    def postgresql_port(self) -> int:
        return int(self.get_environment_variable('POSTGRESQL_PORT'))

    @cached_property
    def postgresql_database(self) -> str:
        return self.get_environment_variable('POSTGRESQL_DATABASE')

    @cached_property
    def postgresql_creds_code(self) -> str:
        return self.get_environment_variable('POSTGRESQL_CREDS_CODE')

    ########
    @cached_property
    def google_credentials_path(self) -> str:
        return self.get_environment_variable('GOOGLE_CREDENTIALS_PATH')

    @cached_property
    def google_token_path(self) -> str:
        return self.get_environment_variable('GOOGLE_TOKEN_PATH')
