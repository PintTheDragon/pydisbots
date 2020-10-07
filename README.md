# PyDisbots
*An async library for disbots.gg made in Python*

- Built to be used around [discord.py](https://discordpy.readthedocs.io/en/latest/)
- Covers all public API endpoints
- Supports auto-posting of stats to the disbots.gg API
- Supports webhooks in an easy to use manner

## Examples
[Example Cog/Extension](https://github.com/disbots-gg/pydisbots/blob/master/examples/discord.py%20example%20cog/disbots.py)

## Documentation
#### *class* pydisbots.**Client**(bot: *discord.Client*, secret: *str*, \*, autopost_stats: *bool*, webhook_port: *int*, webhook_path: *str*)
* Constructor Arguments:
  * **bot**: *discord.Client* (required) Note that `discord.ext.Commands.bot` is a subclass of a `discord.Client` and can also be used
  * **secret**: *str* (required) The authorization token / secret that is used when posting stats to the api and receiving a webhook request
  * **autopost_stats**: *bool* (optional) Whether or not to autopost stats to the API
  * **webhook_port**: *int* (optional) What port the webhook listener server will be started on (If it's not passed to the constructor, then no webhook server will be started)
  * **webhook_path**: *str* (optional, defaults to '/disbots_hook') What url to listen for post requests from the webhook server on
