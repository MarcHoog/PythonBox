import discord
from discord.ext import commands

initial_extensions = (
    'cogs.ingredients',
)


class Baron(commands.Bot):
    user: discord.ClientUser
    bot_app_info: discord.AppInfo

    def __init__(self):
        allowed_mentions = discord.AllowedMentions(roles=False, everyone=False, users=True)
        intents = discord.Intents(
            guilds=True,
            members=True,
            bans=True,
            emojis=True,
            voice_states=True,
            messages=True,
            reactions=True,
            message_content=True,
        )
        super().__init__(
            command_prefix='$',
            intents=intents,
            allowed_mentions=allowed_mentions
        )

    async def setup_hook(self) -> None:
        self.bot_app_info = await self.application_info()

        for extension in initial_extensions:
            await self.load_extension(extension)

    @property
    def owner(self) -> discord.User:
        return self.bot_app_info.owner

    async def on_ready(self):
        if not hasattr(self, 'uptime'):
            self.uptime = discord.utils.utcnow()
            print('🐈 We are online bitches!')

    async def process_commands(message):

    async def on_message(self, message: discord.Message) -> None:
        if message.author.bot:
            return
        await self.procces_commands(message)
