from modules.currency import latest_value

def main(): 
  from discord.ext import commands
  import os  

  DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
  
  bot = commands.Bot(command_prefix="$", description="Currency Bot")

  @bot.event
  async def on_ready():
    print('I am connected yei')

  @bot.command()
  async def currency(ctx, arg):
    await ctx.send(latest_value(arg))

  bot.run(DISCORD_TOKEN)


if __name__ == '__main__':
  main()
  