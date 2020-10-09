# PyDisbots
*Official asynchronous python library for the disbots.gg public API*

- Includes all public API endpoints
- Built to be used around [discord.py](https://discordpy.readthedocs.io/en/latest/)
- Supports auto-posting of stats to the disbots.gg API
- Supports webhooks in an easy to use manner

## Installation
* You can install it [from PYPI](https://pypi.org/project/pydisbots) using `python3 -m pip install -U pydisbots` or `py -m pip install -U pydisbots` depending on what platform you're on.
* Alternatively, you can clone this repository and run `python3 -m pip install .` or `py -m pip install .` in the folder in which the repository resides.

## Examples
[Example Cog/Extension](https://github.com/disbots-gg/pydisbots/blob/master/examples/discord.py%20example%20cog/disbots.py)
 |
[Example Without Cogs](https://github.com/disbots-gg/pydisbots/blob/master/examples/with%20commands.Bot%20outside%20a%20cog/bot.py)

## Quick Start! (For setting up webhooks + auto-posting stats)
* First, obtain your authorization token from the edit page for your bot!
* While you're still on the site, type in the URL you want disbots.gg to send the data to when someone likes your bot! This should look something like `protocol://youripgoeshere:port/disbots_hook` or `protocol://example.com:port/disbots_hook`
* Now lets get to the programming part! In your code create a `pydisbots.Client` like this:
```
dbc = pydisbots.Client(bot, 'secret', autopost_stats=True, webhook_port=5000, webhook_path='/disbots_hook')
```
* This code creates our Client and tells it to auto post stats every 30 minutes, and listens for any incoming requests that notify you about users liking your bot on disbots.gg!
* The URL we'd put into the text box for "Webhook URL" on the edit page would be `protocol://ourip:5000/disbots_hook`
* Now, you may be asking, where would do I register event handlers / functions which will be called when someone votes? Well, this part differs on what version of discord.py you're using (and how you're using it)!
* If you're using the latest version of discord.py and are setting up the client in a cog (requires a commands.Bot or commands.AutoShardedBot) (which is meant to be a class) you'll want to use the `@commands.Cog.listener()` decorator like so:
```
  @commands.Cog.listener()
  async def on_disbots_like(self, data):
    print(data.user_id, ' has voted for the bot!')

  @commands.Cog.listener()
  async def on_disbots_test(self, data):
    print('This is a test! ', data)
```
* If you're using the newest version of discord.py (a commands.Bot or commands.AutoShardedBot) without cogs, you'll want to use the `@bot.listen` decorator:
```
@bot.listen()
async def on_disbots_like(data):
  print(data.user_id, ' has voted for the bot!')

@bot.listen()
async def on_disbots_test(data):
  print('This is a test! ', data)
```
* If you're using a regular `discord.Client` you can use this code:
```
@client.event
async def on_disbots_like(data):
  print(data.user_id, ' has voted for the bot!')

@client.event
async def on_disbots_test(data):
  print('This is a test! ', data)
```

## Documentation
### *class* pydisbots.**Client**(bot: *discord.Client*, secret: *str*, \*, autopost_stats: *bool*, webhook_port: *int*, webhook_path: *str*, verbose: *bool*)
* Constructor Arguments:
  * **bot**: *discord.Client* (required) Note that `discord.ext.commands.bot` is a subclass of a `discord.Client` and can also be used
  * **secret**: *str* (required) The authorization token / secret that is used when posting stats to the api and receiving a webhook request
  * **autopost_stats**: *bool* (optional) Whether or not to auto-post stats to the API
  * **webhook_port**: *int* (optional) What port the webhook listener server will be started on (If it's not passed to the constructor, then no webhook server will be started)
  * **webhook_path**: *str* (optional, defaults to `'/disbots_hook'`) What url to listen for post requests from the webhook server on

#### *await* pydisbots.Client.**fetch_bot**(bot: *Union[int, str]*)
* *fetches a bot from disbots.gg via a bot id or bot vanity url*
* Arguments:
  * **bot**: *Union[int, str]* (required) Takes either a Discord snowflake id of a bot or the vanity url of a bot that is on disbots.gg
* Returns:
  * A [*ClassyDict*](https://github.com/Iapetus-11/classy-json#how-do-i-use-classy-json) (usable as a normal Python dict) object filled with data from the `/bot/:bot_id` endpoint ([click here for example response](https://docs.disbots.gg/reference/bots))

#### *await* pydisbots.Client.**fetch_user_bots**(uid: *int*)
* *fetches the bots that are on disbots.gg of a given user*
* Arguments:
  * **uid**: *int* (required) The Discord snowflake id of a user who has bots on disbots.gg
* Returns:
  * A [*ClassyDict*](https://github.com/Iapetus-11/classy-json#how-do-i-use-classy-json) (usable as a normal Python dict) object filled with data from the `/user/:user_id/bots` endpoint ([click here for example response](https://docs.disbots.gg/reference/users))

#### *await* pydisbots.Client.**post_guild_count**()
* *posts the guild/server count of your bot to the disbots.gg API*
* Arguments:
  * Does not take any arguments
* Returns:
  * Does not return anything

#### *await* pydisbots.Client.**close**()
* *closes all client connections, sessions, and servers nicely*
* Arguments:
  * Does not take any arguments
* Returns
  * Does not return anything
