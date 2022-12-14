# /// DISCORD EMBED COLOR CODER BY DustinFoes & CrignleySDays /// #
# /// TO GET COLOR, USE: from discordcolors.py import colourcoder /// #
# /// EXAMPLE: /// #

# import discord
# from discordcolors.py import colourcoder
# 
# BOT SET HERE
#
# @client.command(description="Sends a colorful embed!")
# async def color(ctx, color)
# em = discord.Embed(description="This is Your Embed!", color=colourcoder(color))
# await ctx.respond(embed=em)



def colourcoder(colour):
    try:
        Colour_Choice = {
            "Default": (0),
            "Aqua": (1752220),
            "DarkAqua": (1146986),
            "Green": (5763719),
            "DarkGreen": (2067276),
            "Blue": (3447003),
            "DarkBlue": (2123412),
            "Purple": (10181046),
            "DarkPurple": (7419530),
            "LuminousVividPink": (15277667),
            "DarkVividPink": (11342935),
            "Gold": (15844367),
            "DarkGold": (12745742),
            "Orange": (15105570),
            "DarkOrange": (11027200),
            "Red": (15548997),
            "DarkRed": (10038562),
            "Grey": (9807270),
            "DarkGrey": (9936031),
            "DarkerGrey": (8359053),
            "LightGrey": (12370112),
            "Navy": (3426654),
            "DarkNavy": (2899536),
            "Yellow": (16776960),
        
        }

        return Colour_Choice[colour]
    
    except: return Colour_Choice["Default"]  # IF COLOUR CANNOT BE FOUND : CHOOSE "DEFAULT"