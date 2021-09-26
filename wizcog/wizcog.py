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
        
        for bulb in bulbs:
            print(bulb.__dict__)
            
        await ctx.send(f"Bulb IP address: {bulbs[0].ip}")