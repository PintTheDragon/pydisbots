import classyjson as cj
import asyncio
import aiohttp
import discord


class Client:
    def __init__(self, bot: discord.Client, secret: str, webhook_port: int = None, webhook_path: str = '/disbots_hook'):
        self.bot = bot

        self.secret = secret

        self.webhook_port = webhook_port
        self.webhook_path = webhook_path
        self._webhook_server = None

        self._webhook_task = None
        if self.webhook_port is not None:
            self._webhook_task = self.bot.loop.create_task(self._webhook_listener())

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

    async def close(self):
        if self._webhook_server is not None:
            await self._webhook_server.stop()
            self._webhook_task.cancel()
