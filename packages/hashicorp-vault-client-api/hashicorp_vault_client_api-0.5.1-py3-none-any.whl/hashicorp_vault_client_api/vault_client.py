#!/usr/bin/env python3.9
"""HashiCorp Vault Client API -> Vault Client
Copyright (C) 2021 Jerod Gawne <https://github.com/jerodg/>

This program is free software: you can redistribute it and/or modify
it under the terms of the Server Side Public License (SSPL) as
published by MongoDB, Inc., either version 1 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
SSPL for more details.

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

You should have received a copy of the SSPL along with this program.
If not, see <https://www.mongodb.com/licensing/server-side-public-license>."""
import asyncio
from os import getenv
from typing import List, NoReturn, Optional, Union

from base_client_api.base_client import BaseClientApi
from base_client_api.models.record import Record
from base_client_api.models.results import Results
from rich import print

from hashicorp_vault_client_api.models.auth import AuthAppRole


class VaultClient(BaseClientApi):
    """HashiCorp Vault Client"""

    def __init__(self, cfg: Optional[Union[str, dict]] = None, platform_prefix: Optional[str] = 'VLT_',
                 instance_prefix: Optional[str] = None):
        """Initializes Class

        Args:
            cfg (Union[str, dict]): As a str it should contain a full path
                pointing to a configuration file (json/toml). See
                config.* in the examples folder for reference."""
        super().__init__(cfg=cfg, platform_prefix=platform_prefix, instance_prefix=instance_prefix)
        self.load_custom_config()
        self.authorized: bool = False

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type: None, exc_val: None, exc_tb: None) -> NoReturn:
        await super().__aexit__(exc_type, exc_val, exc_tb)

    async def login(self) -> NoReturn:
        """Login

        Returns:
            (NoReturn)"""
        # debug(self.cfg)
        results = await asyncio.gather(asyncio.create_task(self.request(AuthAppRole(**self.cfg['Auth']))))
        response = await self.process_results(results=Results(responses=results), model=AuthAppRole)
        # debug(response)
        self.header['X-Vault-Token'] = response.success[0]['auth']['client_token']
        self.authorized = True

        return

    async def make_request(self, models: List[Record]) -> Results:
        """Make Request

        This is a convenience method to make calling easier.
        It can be overridden to provide additional functionality.

        Args:
            models (List[Record]): If sending a list of models they must be all of the same type

        Returns:
            results (Reults)"""
        if not self.authorized:
            await self.login()

        if type(models) is not list:
            models = [models]

        tasks = [asyncio.create_task(self.request(m)) for m in models]

        results = await asyncio.gather(*tasks)

        return await self.process_results(results=Results(responses=results), model=models[0].__class__)

    def load_custom_config(self) -> NoReturn:
        """Load Custom Configuration Data

        Args:

        Returns:
            (NoReturn)"""

        if role_id := getenv(f'{self.platform_prefix}{self.instance_prefix}Auth_Role_Id'):
            self.cfg['Auth']['role_id'] = role_id
            # debug(role_id)

        if secret_id := getenv(f'{self.platform_prefix}{self.instance_prefix}Auth_Secret_Id'):
            self.cfg['Auth']['secret_id'] = secret_id
            # debug(secret_id)

        return


if __name__ == '__main__':
    print(__doc__)
