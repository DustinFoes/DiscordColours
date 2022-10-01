DISCORD EMBED COLOR CODER BY:
         DustinFoes & CrignleySDays


TO GET COLOR, USE: 
        
        from discordcolors.py import colourcoder


EXAMPLE:

import discord
from discordcolors.py import colourcoder

BOT SET HERE
@client.command(description="Sends a colorful embed!")
async def color(ctx, color)
em = discord.Embed(description="This is Your Embed!", color=colourcoder(color)) # COLOR TAKES IN A STRING LIKE BLUE, GREEN, RED, ETC...
await ctx.respond(embed=em)