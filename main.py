import telebot
import os
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# تۆکن نوکە ژ سێرڤەری (Environment Variables) دێ هێت، نهێ د کۆدی دا
BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)
CHANNEL = '@YAKUZA_CEO3'

def is_subscribed(user_id):
    try:
        member = bot.get_chat_member(CHANNEL, user_id)
        return member.status in ['member', 'administrator', 'creator']
    except:
        return False

def main_menu():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("🚀 نوێترین هاک", callback_data="get_latest_hack"))
    markup.add(InlineKeyboardButton("🛡️ چارەسەری باندبوون", callback_data="anti_ban_info"))
    markup.add(InlineKeyboardButton("🌍 جیهانی هاک", callback_data="hacker_world"))
    markup.add(InlineKeyboardButton("📱 فرۆشگای یاکوزا", url="https://saadmzore238-arch.github.io/My.apps/"))
    markup.add(InlineKeyboardButton("📢 کەناڵی ئێمە", url="https://t.me/YAKUZA_CEO3"))
    return markup

def check_sub_markup():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("✅ جۆین بکە 📢", url="https://t.me/YAKUZA_CEO3"))
    markup.add(InlineKeyboardButton("🔄 چێک بکەرەوە", callback_data="check_sub"))
    return markup

def back_btn(data="back_to_main"):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("⬅️ گەڕانەوە", callback_data=data))
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    user_name = message.from_user.first_name or "برا"
    if is_subscribed(message.from_user.id):
        bot.send_message(message.chat.id, f"بەخێربێیت {user_name} 🔥\nبۆتی فەرمی یاکوزا ستۆر 🎮", reply_markup=main_menu())
    else:
        bot.send_message(message.chat.id, f"سڵاو {user_name} 👋\n\n❌ پێویستە سەرەتا بچیتە ناو کەناڵەکەمەوە!\n\n👇 جۆین بکە پاشان چێک بکەرەوە", reply_markup=check_sub_markup())

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    user_name = call.from_user.first_name or "برا"
    try:
        if call.data == "check_sub":
            if is_subscribed(call.from_user.id):
                bot.edit_message_text(f"بەخێربێیت {user_name} 🔥\nبۆتی فەرمی یاکوزا ستۆر 🎮", chat_id, message_id, reply_markup=main_menu())
            else:
                bot.answer_callback_query(call.id, "❌ هێشتا جۆین نەکردووی!", show_alert=True)
        elif call.data == "back_to_main":
            bot.edit_message_text(f"بەخێربێیت {user_name} 🔥\nبۆتی فەرمی یاکوزا ستۆر 🎮", chat_id, message_id, reply_markup=main_menu())
        elif call.data == "get_latest_hack":
            bot.answer_callback_query(call.id, "🔥 هاکە نوێەکان لە کەناڵەکەمان دان!", show_alert=True)
        elif call.data == "hacker_world":
            markup = InlineKeyboardMarkup()
            markup.add(InlineKeyboardButton("🎯 باشترین هاکەکان", callback_data="best_hacks"))
            markup.add(InlineKeyboardButton("📱 هاکی ئایفۆن", callback_data="ios_hacks"))
            markup.add(InlineKeyboardButton("🤖 هاکی ئەندرۆید", callback_data="android_hacks"))
            markup.add(InlineKeyboardButton("⬅️ گەڕانەوە", callback_data="back_to_main"))
            bot.edit_message_text("🌍 جیهانی هاک و فێرکاری\n\nهەموو زانیاری لەبارەی هاک و مۆدەکانەوە ئێرەیە! 💪", chat_id, message_id, reply_markup=markup)
        elif call.data == "best_hacks":
            text = "🎯 باشترین هاکەکان بۆ ئەکاونت\n\n🟢 باشترینەکان (Security زۆر باشە)\n👑 AIM KING (ژخرا باشتر)\n🐍 Snake\n⚙️ Kos Engine\n🥷 Ninja Engine\n\n⚠️ ئەمانە تەنها لەسەر ئەکاونتی Guest\n🕷️ Spider Engine\n💎 KPMods\n🎯 AimX\n🔮 Glass Engine\n\n❌ ئەمانە بەکارمەهێنە (کراک کراون)"
            bot.edit_message_text(text, chat_id, message_id, reply_markup=back_btn("hacker_world"))
        elif call.data == "ios_hacks":
            text = "📱 باشترین هاکەکان بۆ ئایفۆن\n\n✅ ئەمانە ئەکاونتت باند ناکەن\n💎 Flourite\n⚔️ MW Cheat\n🥷 Ninja Engine\n\n💡 پێشنیار: لەسەر ئەکاونتی Guest یاری بکە!"
            bot.edit_message_text(text, chat_id, message_id, reply_markup=back_btn("hacker_world"))
        elif call.data == "android_hacks":
            text = "🤖 باشترین هاکەکان بۆ ئەندرۆید\n\n✅ Security باشە\n👑 AIM KING\n🐍 Snake\n⚙️ Kos Engine\n🥷 Ninja Engine\n\n⚠️ تەنها لەسەر ئەکاونتی Guest\n🕷️ Spider Engine\n💎 KPMods\n🎯 AimX\n🔮 Glass Engine"
            bot.edit_message_text(text, chat_id, message_id, reply_markup=back_btn("hacker_world"))
        elif call.data == "anti_ban_info":
            markup = InlineKeyboardMarkup()
            markup.add(InlineKeyboardButton("🛡️ پاراستنی ئەکاونت", callback_data="protect_account"))
            markup.add(InlineKeyboardButton("⚙️ ڕێکخستنی Auto Play", callback_data="auto_play_settings"))
            markup.add(InlineKeyboardButton("🎯 تیپی کێشانی گوڵە", callback_data="shot_tips"))
            markup.add(InlineKeyboardButton("🔧 چارەسەری Play Protect", callback_data="fix_install"))
            markup.add(InlineKeyboardButton("⬅️ گەڕانەوە", callback_data="back_to_main"))
            bot.edit_message_text("🛡️ چارەسەری باندبوون\n\nهەموو زانیاری بۆ پاراستنی ئەکاونتەکەت! 💪", chat_id, message_id, reply_markup=markup)
        elif call.data == "protect_account":
            text = "ئەری تەدڤێت ئەکاونتی تەیی شەخسی باند نەبێت دیف فان فەرمانا هەرە 👇\n\nهەمی گافا Auto Play بکارنەینە ئەو دبێتە ئەگەری باندبونا لیگایی ژی\n\nچجارا Auto Queue بکارنەینە گەلەک یا خەتەرە\n\nوەختئ تو داری دکێشی چ کوشنا نەدە ئاسای توپی ببە\n\nئەڤە ئەو هاکن کو باشترینن و Security زور باشە بو باندبونی 👇\n\n👑 AIM KING (ژخرا باشتر)\n🐍 Snake\n⚙️ Kos Engine\n🥷 Ninja Engine\n\nبو ئایفونی باشترین کو ئەکاونتی تە باند نەبێت 👇\n\n💎 Flourite\n⚔️ MW Cheat\n🥷 Ninja Engine\n\nئەو هاکئن پێدڤیە لەسەر ئەکاونتی Guest یاریی بکە 👇\n\n🕷️ Spider Engine\n💎 KPMods\n🎯 AimX\n🔮 Glass Engine\n\nو ئێت زخرا خرابتر ئەون ئێت (کراک کری) خو ژی پارێزن"
            bot.edit_message_text(text, chat_id, message_id, reply_markup=back_btn("anti_ban_info"))
        elif call.data == "auto_play_settings":
            text = "⚙️ ڕێکخستنی Auto Play\n\n❌ Auto Play بەکارمەهێنە!\nئەمە دەبێتە هۆی باندبوونی لیگایی\n\n❌ Auto Queue بەکارمەهێنە!\nزۆر خەتەرناکە\n\n✅ پێشنیار:\nهەموو شتێک دەستی بکە"
            bot.edit_message_text(text, chat_id, message_id, reply_markup=back_btn("anti_ban_info"))
        elif call.data == "shot_tips":
            text = "🎯 تیپی کێشانی گوڵە\n\nوەختئ تو داری دکێشی چ کوشنا نەدە ئاسای توپی ببە\n\n💡 پێشنیار:\nپێش کێشانی گوڵە هاکەکە چالاک بکە\nدوای گوڵەکە دەستی ببە"
            bot.edit_message_text(text, chat_id, message_id, reply_markup=back_btn("anti_ban_info"))
        elif call.data == "fix_install":
            text = "🔧 چارەسەری Play Protect\n\n١. Play Store بکەرەوە\n٢. کلیک لەسەر پرۆفایل\n٣. Play Protect هەڵبژێرە\n٤. کوژاندنەوە\n\n✅ ئێستا دەتوانیت Install بکەیت!"
            bot.edit_message_text(text, chat_id, message_id, reply_markup=back_btn("anti_ban_info"))
    except Exception as e:
        print(f"Error: {e}")

print("✅ بۆتەکە دەستی پێکرد!")
bot.infinity_polling()
