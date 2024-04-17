import discord
import random
from discord.ext import tasks
import datetime

# Credenciales del bot
intents = discord.Intents.default()
intents.message_content = True
with open('token.txt', 'r') as f:
    bot_token = f.read().strip()
# Canal de bienvenida (opcional)
channel_id = 1229877128083017850

utc = datetime.timezone.utc
random_time = datetime.time(hour=2, minute=0, tzinfo=utc)

n_random_messages = 3

# Lista de saludos
greetings = [
    'Now I am become piggie, consumer of slop - Oppenheimer', 
    'wah wah wah', 'Soy adicto al crack', 
    'Esto me duele más a mí que a vos - La doña antes de pegarle a 👴🏻',
    'pthread (pronunciado pe-tred)',
    'Venga y le mamo el culo',
    'Alguien mande a callar a Mar',
    'Quisiera haber muerto en el vientre',
    'ISRA PONETE LAS MEDIAS Y VENITE',
    'En las profundidades del invierno finalmente aprendí que en mi interior habita un verano invencible - Camus',
    'Empujame contra la pared, soy tu sorra',
    'Recuerde no usar condon',
    'A veces tengo sueños sexuales potentes',
    'Imagínese que un camión va a atropellar al gato de Carlos',
    'Esteban deje de gastar 50 rojos en wilas y no culiarselas',
    'COMPUTADORA',
    'Isra, a usted Pamela le dió apoyo moral con la garganta?',
    'Chabestias',
    'La doña me metió 200 rojos de pensión y diez pichasos',
    'Imagínese que un camión va a atropellar al gato de Carlos',
    'Daniel te puedo llamar? No es del quiz',
    'Te gusta que te ahorque?',
    'Pégueme'
]

# Cliente del bot
bot = discord.Client(intents=intents)

# Evento de inicio del bot
@bot.event
async def on_ready():
    print(f'Conectado como {bot.user} (ID: {bot.user.id})')
    print('Conectado a servidores:')

    random_time_phrases.start()

    # Envía un mensaje de bienvenida aleatorio
    try:
        channel = bot.get_channel(channel_id)
        if channel:
            random_greeting = random.choice(greetings)
            await channel.send(f'{random_greeting}')
            print(f'Mensaje de bienvenida enviado al canal: {channel.name}')
        else:
            print(f'Error: Canal con ID {channel_id} no encontrado.')
    except Exception as e:
        print(f'Error al enviar el mensaje de bienvenida: {e}')

# Evento de mensaje recibido
@bot.event
async def on_message(message):
    # Ignora los mensajes del propio bot
    if message.author == bot.user:
        return

    # Comprueba la frase de activación (sin distinción de mayúsculas y minúsculas)
    if message.content.lower() == 'chiqui bot ayudame':
        # Envía una respuesta con saludo aleatorio
        random_greeting = random.choice(greetings)
        await message.channel.send(f'{random_greeting}, matese', reference=message)
        print(f'Respondió a '{message.content}' con '{random_greeting}' en el canal: {message.channel.name}')


@tasks.loop(time=random_time)
async def random_time_phrases():
    channel = bot.get_channel(channel_id)
    if channel:
        for index in n_random_messages:
            await channel.send(random.choice(greetings))
    else:
        print('Channel not found!')


# Ejecuta el bot con el token proporcionado
bot.run(bot_token)