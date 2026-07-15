import telebot
import random
import os
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# دڵنیابە ڤی ناڤی ل پشکا Variables ل سەر Railway داناینە: BOT_TOKEN
BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)
CHANNELS = ["@YAKUZA_CEO3"]


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
    markup.add(InlineKeyboardButton("🎰 بەختەکەت تاقی بکەرەوە", callback_data="lucky"))
    markup.add(InlineKeyboardButton("❓ پرسیار و وەڵام", callback_data="faq"))
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
        elif call.data == "lucky":
            results = [("🏆 باشترین بەخت!", "ئەمڕۆ ڕۆژی تۆیە! هەموو شتێک باش دەبێت! 🌟"), ("🎯 بەختی باش!", "ئەمڕۆ بەخت لەگەڵتەوەیە! یاری بکە و ببەرە! 🎮"), ("💎 بەختی نزم!", "ئەمڕۆ ئاگاداربە، بەتاڤەت نییە! 😅"), ("🔥 بەختی گەرم!", "ئەمڕۆ زۆر باشی! هیچ شتێک ناتوانێت بیتەپێچێنێت! 💪"), ("⚡ بەختی بریق!", "ئەمڕۆ ڕۆژێکی تایبەتە بۆت! بەردەوام بە! ⚡"), ("🌙 بەختی ناو ناو!", "نە زۆر باشە نە زۆر خراپ، ئاسایییە! 🌙"), ("🎰 بەختی زەیف!", "ئەمڕۆ ئاگاداربە برا! 😬")]
            result = random.choice(results)
            markup = InlineKeyboardMarkup()
            markup.add(InlineKeyboardButton("🔄 دووبارە تاقی بکەرەوە", callback_data="lucky"))
            markup.add(InlineKeyboardButton("⬅️ گەڕانەوە", callback_data="back_to_main"))
            bot.edit_message_text(f"🎰 بەختی ئەمڕۆی {user_name}\n\n{result[0]}\n\n{result[1]}", chat_id, message_id, reply_markup=markup)
        elif call.data == "faq":
            markup = InlineKeyboardMarkup()
            markup.add(InlineKeyboardButton("❓ چۆن ئەپەکان دابەزێنم؟", callback_data="faq_download"))
            markup.add(InlineKeyboardButton("❓ ئایا ئەپەکان بەخۆڕاین؟", callback_data="faq_free"))
            markup.add(InlineKeyboardButton("❓ چۆن Install بکەم؟", callback_data="faq_install"))
            markup.add(InlineKeyboardButton("❓ ئایا ئەکاونتم باند دەبێت؟", callback_data="faq_ban"))
            markup.add(InlineKeyboardButton("❓ پەیوەندی بەیاکوزا", callback_data="faq_contact"))
            markup.add(InlineKeyboardButton("⬅️ گەڕانەوە", callback_data="back_to_main"))
            bot.edit_message_text("❓ پرسیار و وەڵام\n\nکام پرسیارت هەیە؟", chat_id, message_id, reply_markup=markup)
        elif call.data == "faq_download":
            bot.edit_message_text("❓ چۆن ئەپەکان دابەزێنم؟\n\n✅ وەڵام:\n١. بچۆ بۆ فرۆشگای یاکوزا\n٢. ئەپەکەی دەتەوێت هەڵبژێرە\n٣. دوگمەی داونلۆد داپبەژێ\n٤. فایلەکە دادەبەزێت بۆ مۆبایلەکەت", chat_id, message_id, reply_markup=back_btn("faq"))
        elif call.data == "faq_free":
            bot.edit_message_text("❓ ئایا ئەپەکان بەخۆڕاین؟\n\n✅ وەڵام:\nبەڵێ! هەموو ئەپەکانی یاکوزا ستۆر بەخۆڕاین و مۆدکراون! 🎉", chat_id, message_id, reply_markup=back_btn("faq"))
        elif call.data == "faq_install":
            markup = InlineKeyboardMarkup()
            markup.add(InlineKeyboardButton("📱 iPhone", callback_data="faq_install_ios"), InlineKeyboardButton("🤖 Android", callback_data="faq_install_android"))
            markup.add(InlineKeyboardButton("⬅️ گەڕانەوە", callback_data="faq"))
            bot.edit_message_text("❓ چۆن Install بکەم؟\n\nکام مۆبایلت هەیە؟", chat_id, message_id, reply_markup=markup)
        elif call.data == "faq_install_ios":
            bot.edit_message_text("📱 Install کردن لەسەر iPhone\n\n١. AltStore دابەزێنە\n٢. فایلی IPA داونلۆد بکە\n٣. لە AltStore فایلەکە Install بکە\n\nیان TrollStore بەکاربهێنە (iOS 14-16)", chat_id, message_id, reply_markup=back_btn("faq_install"))
        elif call.data == "faq_install_android":
            bot.edit_message_text("🤖 Install کردن لەسەر ئەندرۆید\n\n١. فایلی APK داونلۆد بکە\n٢. Settings → Unknown Sources چالاک بکە\n٣. فایلەکە Install بکە\n\nئاسانە! ✅", chat_id, message_id, reply_markup=back_btn("faq_install"))
        elif call.data == "faq_ban":
            bot.edit_message_text("❓ ئایا ئەکاونتم باند دەبێت؟\n\n✅ وەڵام:\nئەگەر هاکی باش بەکاربهێنیت باند نابیت!\n\n👑 AIM KING\n🐍 Snake\n⚙️ Kos Engine\n\nئاگادار بە لە Auto Play و Auto Queue!", chat_id, message_id, reply_markup=back_btn("faq"))
        elif call.data == "faq_contact":
            markup = InlineKeyboardMarkup()
            markup.add(InlineKeyboardButton("✈️ کەناڵی تەلەگرام", url="https://t.me/YAKUZA_CEO3"))
            markup.add(InlineKeyboardButton("▶️ یوتیوب", url="https://www.youtube.com/@YAKUZA_CEO"))
            markup.add(InlineKeyboardButton("⬅️ گەڕانەوە", callback_data="faq"))
            bot.edit_message_text("📞 پەیوەندی بەیاکوزا", chat_id, message_id, reply_markup=markup)
        elif call.data == "hacker_world":
            markup = InlineKeyboardMarkup()
            markup.add(InlineKeyboardButton("🎯 باشترین هاکەکان", callback_data="best_hacks"))
            markup.add(InlineKeyboardButton("📱 هاکی ئایفۆن", callback_data="ios_hacks"))
            markup.add(InlineKeyboardButton("🤖 هاکی ئەندرۆید", callback_data="android_hacks"))
            markup.add(InlineKeyboardButton("⬅️ گەڕانەوە", callback_data="back_to_main"))
            bot.edit_message_text("🌍 جیهانی هاک و فێرکاری\n\nهەموو زانیاری لەبارەی هاک و مۆدەکانەوە ئێرەیە! 💪", chat_id, message_id, reply_markup=markup)
        elif call.data == "best_hacks":
            bot.edit_message_text("🎯 باشترین هاکەکان بۆ ئەکاونت\n\n🟢 باشترینەکان\n👑 AIM KING\n🐍 Snake\n⚙️ Kos Engine\n🥷 Ninja Engine", chat_id, message_id, reply_markup=back_btn("hacker_world"))
        elif call.data == "ios_hacks":
            bot.edit_message_text("📱 باشترین هاکەکان بۆ ئایفۆن\n\n✅ ئەکاونتت باند ناکەن\n💎 Flourite\n⚔️ MW Cheat\n🥷 Ninja Engine", chat_id, message_id, reply_markup=back_btn("hacker_world"))
        elif call.data == "android_hacks":
            bot.edit_message_text("🤖 باشترین هاکەکان بۆ ئەندرۆید\n\n👑 AIM KING\n🐍 Snake\n⚙️ Kos Engine\n🥷 Ninja Engine", chat_id, message_id, reply_markup=back_btn("hacker_world"))
        elif call.data == "anti_ban_info":
            markup = InlineKeyboardMarkup()
            markup.add(InlineKeyboardButton("🛡️ پاراستنی ئەکاونت", callback_data="protect_account"))
            markup.add(InlineKeyboardButton("⚙️ ڕێکخستنی Auto Play", callback_data="auto_play_settings"))
            markup.add(InlineKeyboardButton("🎯 تیپی کێشانی گوڵە", callback_data="shot_tips"))
            markup.add(InlineKeyboardButton("🔧 چارەسەری Play Protect", callback_data="fix_install"))
            markup.add(InlineKeyboardButton("⬅️ گەڕانەوە", callback_data="back_to_main"))
            bot.edit_message_text("🛡️ چارەسەری باندبوون\n\nهەموو زانیاری بۆ پاراستنی ئەکاونتەکەت! 💪", chat_id, message_id, reply_markup=markup)
        elif call.data == "protect_account":
            bot.edit_message_text("پاراستنا ئەکاونتی:\n1. Auto Play بکارنەینە.\n2. Auto Queue بکارنەینە.\n3. تەنها هاکێن ئەسڵ بکاربینە.", chat_id, message_id, reply_markup=back_btn("anti_ban_info"))
        elif call.data == "auto_play_settings":
            bot.edit_message_text("❌ Auto Play و Auto Queue کار نەکە!", chat_id, message_id, reply_markup=back_btn("anti_ban_info"))
        elif call.data == "shot_tips":
            bot.edit_message_text("💡 پێش کێشانی گوڵە هاکەکە چالاک بکە.", chat_id, message_id, reply_markup=back_btn("anti_ban_info"))
        elif call.data == "fix_install":
            bot.edit_message_text("١. Play Store -> Play Protect -> کوژاندنەوە", chat_id, message_id, reply_markup=back_btn("anti_ban_info"))
    except Exception as e:
        print(f"Error: {e}")

bot.infinity_polling()
