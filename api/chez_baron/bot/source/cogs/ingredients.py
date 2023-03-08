from discord.ext import commands
import discord.embeds
from models import Ingredient
from python.chez_baron.data.source.ingredient import (
    fetch_one_ingredient
)


async def create_ingredient_header():
    header = discord.Embed()
    header.set_image(url='https://cdn.discordapp.com/attachments/1071903676530167889/1071903931485147257/Picture3.png')
    return header


async def create_ingredient_panel(ingredient: Ingredient):
    panel = discord.Embed(title=f'The Ingredient of Today: {ingredient.name}', description=ingredient.description)
    panel.set_thumbnail(url=ingredient.thumbnail)
    return panel


class Ingredients(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.is_owner()
    @commands.command(name="get-ingredient", aliases=['ingredient'])
    async def get_ingredient(self, ctx, name):
        result = await fetch_one_ingredient(name)
        if result is None:
            ctx.send(f'🥺 Madam/Sir...., I have come to the realisation that this ingredient does not exist. Please '
                     f'try again.')
        else:
            header = await ctx.send(embed=await create_ingredient_header())
            panel = await ctx.send(embed=await create_ingredient_panel(Ingredient(**result)))


async def setup(bot):
    await bot.add_cog(Ingredients(bot))
