import random
from datetime import datetime, timedelta
import time
from telegram import Bot, ParseMode

BOT_TOKEN = "7821383138:AAHHgS3A20IfJxw12gsUf8k3PI3ZD-qpILQ"
CHAT_ID = "7290655745"

bot = Bot(token=BOT_TOKEN)

def generate_signals():
    signals = []
    start_time = datetime.strptime("13:00", "%H:%M")  # Start at 1:00 PM PKT
    for i in range(20):
        time_stamp = (start_time + timedelta(minutes=i * 6)).strftime("%I:%M %p")
        direction = random.choice(["Up", "Down"])
        confidence = random.choice(["96%", "97%", "98%", "99%", "100%"])
        martingale = "Yes" if random.random() < 0.2 else "No"
        signals.append({
            "number": i + 1,
            "time": time_stamp,
            "direction": direction,
            "confidence": confidence,
            "martingale": martingale
        })
    return signals

def send_signals():
    signals = generate_signals()
    for signal in signals:
        message = (
            f"**Gold Signal (XAU/USD)**\n"
            f"Signal No: {signal['number']}\n"
            f"Time: {signal['time']} PKT (GMT+5)\n"
            f"Direction: {signal['direction']}\n"
            f"Expiry: 1 min\n"
            f"Confidence: {signal['confidence']}\n"
            f"Martingale Needed: {signal['martingale']}"
        )
        bot.send_message(chat_id=CHAT_ID, text=message, parse_mode=ParseMode.MARKDOWN)
        time.sleep(300)  # wait 5 minutes

if __name__ == "__main__":
    send_signals()
