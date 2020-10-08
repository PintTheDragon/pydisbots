from typing import Union
import classyjson as cj
import asyncio
import aiohttp
import discord

from .Exceptions import *

base_url = 'https://disbots.gg'


class Client:
    def __init__(self, bot: discord.Client, secret: str, *, autopost_stats: bool = False, webhook_port: int = 80, webhook_path: str = '/disbots_hook'):
        self.bot = bot

        self.ses = aiohttp.ClientSession()

        self.secret = secret

        self.webhook_port = webhook_port
        self.webhook_path = webhook_path
        self._webhook_server = None

        self._webhook_task = None
        if self.webhook_port is not None:
            self._webhook_task = bot.loop.create_task(self._webhook_listener())

        if autopost_stats:
            self._autopost_task = bot.loop.create_task(self._autopost_stats())

    async def _webhook_listener(self):
        async def handler(req):
            if req.headers.get('Authorization') != self.secret:
                return web.Response(status=401)

            data = cj.classify(await req.json())

            if data.get('type') == 'like':
                event_name = 'disbots_like'
            else:
                event_name = 'disbots_test'

            self.bot.dispatch(event_name, data)

            return web.Response()

        app = aiohttp.web.Application()

        app.router.add_post(self.webhook_path, handler)

        runner = aiohttp.web.AppRunner(app)
        await runner.setup()

        self._webhook_server = aiohttp.web.TCPSite(runner, '0.0.0.0', self.webhook_port)

    async def _autopost_stats(self):
        await self.bot.wait_until_ready()

        while not self.bot.closed:
            try:
                await self.post_guild_count()
            except Exception as e:
                print('Exception occured in stats autoposting:', e)

            await asyncio.sleep(1800)


    async def fetch_bot(self, bot: Union[int, str]):
        try:
            resp = await self.ses.get(f'{base_url}/api/bot/{bot}')
        except Exception as e:
            raise APIError(e)

        if resp.status == 404:
            raise BotNotFound(bot)

        if resp.status == 400:
            raise InvalidBot(bot)

        if resp.status != 200:
            raise APIError(f'Status is not 200 OK (Status was {resp.status})')

        try:
            data = cj.classify(await resp.json())
        except Exception as e:
            raise APIError(e)

        return data

    async def fetch_user_bots(self, uid: int):
        try:
            resp = await self.ses.get(f'{base_url}/api/user/{uid}/bots')
        except Exception as e:
            raise APIError(e)

        if resp.status == 404:
            raise UserNotFound(uid)

        if resp.status == 400:
            raise InvalidUser(uid)

        if resp.status != 200:
            raise APIError(f'Status is not 200 OK (Status was {resp.status})')

        try:
            data = cj.classify(await resp.json())
        except Exception as e:
            raise APIError(e)

        return data

    async def post_guild_count(self):
        headers = {'Authorization': self.secret}
        data = {'servers': str(len(self.bot.guilds))}

        try:
            await self.ses.put(f'{base_url}/api/stats', headers=headers, json=data)
        except Exception as e:
            raise APIError(e)

        if resp.status == 401:
            raise UnauthorizedError

        if resp.status != 200:
            raise APIError(f'Status is not 200 OK (Status was {resp.status})')

    async def close(self):
        if self._webhook_server is not None:
            await self._webhook_server.stop()

            self._webhook_task.cancel()
            self._autopost_task.cancel()
