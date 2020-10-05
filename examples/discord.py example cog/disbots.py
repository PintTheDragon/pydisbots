from discord.ext import commands
from pydisbots import Client as DisbotsClient


class Disbots(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.dbc = DisbotsClient(bot, 'secret', autopost_stats=True, webhook_port=5000, webhook_path='/disbots_hook')

    @commands.Cog.listener()
    async def on_disbots_test(self, data):
        print('A webhooks test occurred successfully! Data: ', data)

    @commands.Cog.listener()
    async def on_disbots_like(self, data):
        bot_id = data.bot_id  # bot id of the bot that was voted for
        user_id = data.user_id  # user id of the user who voted

        print(f'User {user_id} voted for bot {bot_id}')

# This setup function is ONLY used if you're loading this file like an extension
# You can remove this if you're just using the cog outside of an extension
def setup(bot):
    bot.add_cog(Disbots(bot))
