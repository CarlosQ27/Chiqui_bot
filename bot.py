import discord
import random

# Credenciales del bot
intents = discord.Intents.default()
intents.message_content = True
bot_token = "MTIyOTgzMTgwNDYyMjYwNjQxNg.GHSGPB.oZPkE8jcH_3gsGsSYN-5bqELm2s5Mystsn3fZg"

# Canal de bienvenida (opcional)
channel_id = 1229877128083017850

# Lista de saludos
greetings = [
"Now I am become piggie, consumer of slop - Oppenheimer", 
"wah wah wah", "Soy adicto al crack", 
"Esto me duele más a mí que a vos - La doña antes de pegarle a 👴🏻",
"pthread (pronunciado pe-tred)"
]

# Cliente del bot
bot = discord.Client(intents=intents)

# Evento de inicio del bot
@bot.event
async def on_ready():
    print(f'Conectado como {bot.user} (ID: {bot.user.id})')
    print('Conectado a servidores:')
    # Envía un mensaje de bienvenida aleatorio
    try:
        channel = bot.get_channel(channel_id)
        if channel:
            random_greeting = random.choice(greetings)
            await channel.send(f"{random_greeting}")
            print(f"Mensaje de bienvenida enviado al canal: {channel.name}")
        else:
            print(f"Error: Canal con ID {channel_id} no encontrado.")
    except Exception as e:
        print(f"Error al enviar el mensaje de bienvenida: {e}")

# Evento de mensaje recibido
@bot.event
async def on_message(message):
    # Ignora los mensajes del propio bot
    if message.author == bot.user:
        return

    # Comprueba la frase de activación (sin distinción de mayúsculas y minúsculas)
    if message.content.lower() == "chiqui bot ayudame":
        # Envía una respuesta con saludo aleatorio
        random_greeting = random.choice(greetings)
        await message.channel.send(f"{random_greeting}, matese", reference=message)
        print(f"Respondió a '{message.content}' con '{random_greeting}' en el canal: {message.channel.name}")

# Ejecuta el bot con el token proporcionado
bot.run(bot_token)