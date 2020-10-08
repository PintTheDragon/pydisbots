from discord.ext import commands
from pydisbots import Client as DisbotsClient


bot = commands.Bot(command_prefix='!')
dbc = DisbotsClient(bot, 'secret', autopost_stats=True, webhook_port=5000, webhook_path='/disbots_hook')

@bot.listen()
async def on_disbots_test(self, data):
    print('A webhooks test occurred successfully! Data: ', data)

@bot.listen()
async def on_disbots_like(self, data):
    bot_id = data.bot_id  # bot id of the bot that was voted for
    user_id = data.user_id  # user id of the user who voted

    print(f'User {user_id} voted for bot {bot_id}')

@bot.listen()
async def on_ready(self):
    print('Bot is ready and connected!')

bot.run('discord token')
