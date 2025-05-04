import logging
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Configurar logs
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Seu TOKEN
TOKEN = '7524791054:AAGLjU1eMHbj1fA6bkwXzZHt7_k_3mAd82c'

# Lista com os últimos resultados da FURIA
ULTIMOS_RESULTADOS = [
    "❌ FURIA 0 x 2 The MongolZ",
    "❌ FURIA 0 x 2 Virtus.pro",
    "❌ FURIA 1 x 2 Complexity"
]

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    mensagem = (
        "👋 Bem-vindo ao Bot da FURIA!\n\n"
        "Escolha um comando:\n"
        "/torcida - Apoiar a FURIA 🦁\n"
        "/xingamento - Zoar os adversários 🤡\n"
        "/proximosjogos - Ver os próximos jogos 📅\n"
        "/lineup - Ver a lineup atual da FURIA 🎯\n"
        "/ultimosresultados - Resultados recentes da FURIA 📊"
    )
    await update.message.reply_text(mensagem)

# /torcida
async def torcida(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    frases = [
        "🔥 Vamos FURIA! Aqui é raça e sangue no olho!",
        "🦁 A FURIA atropela sem pedir licença!",
        "🎯 Bala na cabeça é nossa assinatura!",
        "🏆 Vamos buscar esse título, FURIA!",
        "💣 Domina bombsite como quem domina o mundo!",
        "😎 Cada round da FURIA é um show à parte!",
        "👑 Hoje é massacre, hoje é FURIA!",
        "🎤 Solta o grito, torcedor! Aqui é FURIA!",
        "🚀 Rush é limpo, objetivo é vitória!",
        "🔝 Melhor time do Brasil e do mundo!"
    ]
    await update.message.reply_text(random.choice(frases))

# /xingamento
async def xingamento(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    frases = [
        "😂 Tá jogando com monitor desligado?",
        "🍋 Easy peasy lemon squeezy... pros RUINS!",
        "🎯 Mira na cabeça, acerta a parede!",
        "🏆 Prata querendo ser campeão, kkkkk!",
        "💣 Planta a bomba no pé, depois chora!",
        "🔫 Puxa a AWP mas não acerta nem o chão!",
        "👻 Smoke é invisibilidade pra esses bots!",
        "🎤 Cadê a call, seus perdidos?",
        "🔥 Rush B e morre todo mundo, parabéns!",
        "🧹 Varreu o mapa e não matou ninguém!"
    ]
    await update.message.reply_text(random.choice(frases))

# /proximosjogos
async def proximos_jogos(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    mensagem = (
        "📅 Próximos jogos da FURIA:\n\n"
        "🏆 FURIA vs Team Vitality - 10/05 às 5h00\n"
        "🏆 FURIA vs FaZe Clan - 02/05 às 21h00 (exemplo)\n"
        "🏆 FURIA vs G2 Esports - 05/05 às 17h30 (exemplo)\n\n"
        "🔥 Vamos pra cima FURIA!"
    )
    await update.message.reply_text(mensagem)

# /lineup
async def lineup(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    mensagem = (
        "🎯 Lineup Atual da FURIA:\n\n"
        "- 🇧🇷 yuurih (Yuri Boian)\n"
        "- 🇧🇷 KSCERATO (Kaike Cerato)\n"
        "- 🇧🇷 FalleN (Gabriel Toledo)\n"
        "- 🇰🇿 molodoy (Danil Golubenko)\n"
        "- 🇱🇻 YEKINDAR (Mareks Gaļinskis) [Stand-in]\n"
        "- 🎮 Coach: sidde (Sidnei Macedo)\n"
    )
    await update.message.reply_text(mensagem)

# /ultimosresultados
async def ultimos_resultados(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if isinstance(ULTIMOS_RESULTADOS, list) and ULTIMOS_RESULTADOS:
        mensagem = "📊 Últimos resultados da FURIA:\n\n" + "\n".join(ULTIMOS_RESULTADOS)
    else:
        mensagem = "Não há resultados disponíveis no momento."
    await update.message.reply_text(mensagem)

# main
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("torcida", torcida))
    app.add_handler(CommandHandler("xingamento", xingamento))
    app.add_handler(CommandHandler("proximosjogos", proximos_jogos))
    app.add_handler(CommandHandler("lineup", lineup))
    app.add_handler(CommandHandler("ultimosresultados", ultimos_resultados))

    app.run_polling()

if __name__ == '__main__':
    main()
