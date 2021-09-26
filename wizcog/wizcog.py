import asyncio

from redbot.core import commands
from pywizlight import wizlight, PilotBuilder, discovery

class Wizcog(commands.Cog):
    """My custom cog"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def lights(self, ctx):
        bulbs = await discovery.discover_lights(broadcast_space="192.168.1.255")
        
        bulb = wizlight("bulbs[0].ip")
        await bulb.turn_on(PilotBuilder(rgb = (0, 128, 255)))
        
        await ctx.send(f"Turning on: {bulbs[0].ip}")