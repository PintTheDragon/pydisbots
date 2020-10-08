# PyDisbots
*An async library for disbots.gg made in Python*

- Built to be used around [discord.py](https://discordpy.readthedocs.io/en/latest/)
- Covers all public API endpoints
- Supports auto-posting of stats to the disbots.gg API
- Supports webhooks in an easy to use manner

## Examples
[Example Cog/Extension](https://github.com/disbots-gg/pydisbots/blob/master/examples/discord.py%20example%20cog/disbots.py)
[Example Without Cogs](https://github.com/disbots-gg/pydisbots/blob/master/examples/with%20commands.Bot%20outside%20a%20cog/bot.py)

## Quick Start! (For setting up webhooks + auto-posting stats)
* First, obtain your authorization token / secret from the edit page for your bot, remember that!
* While you're still there, type in the URL you want disbots.gg to send the data to when someone votes for your bot! This should look something like `youripgoeshere:port/disbots_hook` or `example.com:port/disbots_hook`
* Now lets get to the programming part! In your code create a `pydisbots.Client` like this:
```
dbc = pydisbots.Client(bot, 'secret', True, 5000, '/disbots_hook')
```
* This code creates our Client and tells it to auto post stats every 30 minutes, and listen for incoming requests notifying of users voting for you bot on disbots.gg
* The URL we'd put into the text box for "Webhook URL" on the edit page would be `ourip:5000/disbots_hook`
* Now, you may be asking, where in heqq do I register event handlers / functions which will be called when someone votes? Well, this part differs on what version of Discord.py you're using (and how you're using it)!
* If you're using the latest version of Discord.py and are setting up the client in a cog (requires a commands.Bot or commands.AutoShardedBot) (which is meant to be a class) you'll want to use the `@commands.Cog.listener()` decorator like so:
```
  @commands.Cog.listener()
  async def on_disbots_like(self, data):
    print(data.user_id, ' has voted for the bot!')

  @commands.Cog.listener()
  async def on_disbots_test(self, data):
    print('This is a test! ', data)
```
* If you're using the newest version of Discord.py (a commands.Bot or commands.AutoShardedBot) without cogs, you'll want to use the `@bot.listen` decorator:
```
@bot.listen()
async def on_disbots_like(self, data):
  print(data.user_id, ' has voted for the bot!')

@bot.listen()
async def on_disbots_test(self, data):
  print('This is a test! ', data)
```
* If you're using a regular `discord.Client` you can use this code:
```
@client.event
async def on_disbots_like(self, data):
  print(data.user_id, ' has voted for the bot!')

@client.event
async def on_disbots_test(self, data):
  print('This is a test! ', data)
```


## Documentation
#### *class* pydisbots.**Client**(bot: *discord.Client*, secret: *str*, \*, autopost_stats: *bool*, webhook_port: *int*, webhook_path: *str*)
* Constructor Arguments:
  * **bot**: *discord.Client* (required) Note that `discord.ext.commands.bot` is a subclass of a `discord.Client` and can also be used
  * **secret**: *str* (required) The authorization token / secret that is used when posting stats to the api and receiving a webhook request
  * **autopost_stats**: *bool* (optional) Whether or not to auto-post stats to the API
  * **webhook_port**: *int* (optional) What port the webhook listener server will be started on (If it's not passed to the constructor, then no webhook server will be started)
  * **webhook_path**: *str* (optional, defaults to `'/disbots_hook'`) What url to listen for post requests from the webhook server on
