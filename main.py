import telebot
import random
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

BOT_TOKEN = 'YOUR_TOKEN_HERE'
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
        bot.send_message(
            message.chat.id,
            f"بەخێربێیت {user_name} 🔥\nبۆتی فەرمی یاکوزا ستۆر 🎮",
            reply_markup=main_menu()
        )
    else:
        bot.send_message(
            message.chat.id,
            f"سڵاو {user_name} 👋\n\n❌ پێویستە سەرەتا بچیتە ناو کەناڵەکەمەوە!\n\n👇 جۆین بکە پاشان چێک بکەرەوە",
            reply_markup=check_sub_markup()
        )

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    user_name = call.from_user.first_name or "برا"

    try:
        if call.data == "check_sub":
            if is_subscribed(call.from_user.id):
                bot.edit_message_text(
                    f"بەخێربێیت {user_name} 🔥\nبۆتی فەرمی یاکوزا ستۆر 🎮",
                    chat_id, message_id, reply_markup=main_menu()
                )
            else:
                bot.answer_callback_query(call.id, "❌ هێشتا جۆین نەکردووی!", show_alert=True)

        elif call.data == "back_to_main":
            bot.edit_message_text(
                f"بەخێربێیت {user_name} 🔥\nبۆتی فەرمی یاکوزا ستۆر 🎮",
                chat_id, message_id, reply_markup=main_menu()
            )

        elif call.data == "get_latest_hack":
            bot.answer_callback_query(call.id, "🔥 هاکە نوێەکان لە کەناڵەکەمان دان!", show_alert=True)

        # ── بەختەکەت تاقی بکەرەوە ──
        elif call.data == "lucky":
            results = [
                ("🏆 باشترین بەخت!", "ئەمڕۆ ڕۆژی تۆیە! هەموو شتێک باش دەبێت! 🌟"),
                ("🎯 بەختی باش!", "ئەمڕۆ بەخت لەگەڵتەوەیە! یاری بکە و ببەرە! 🎮"),
                ("💎 بەختی نزم!", "ئەمڕۆ ئاگاداربە، بەتاڤەت نییە! 😅"),
                ("🔥 بەختی گەرم!", "ئەمڕۆ زۆر باشی! هیچ شتێک ناتوانێت بیتەپێچێنێت! 💪"),
                ("⚡ بەختی بریق!", "ئەمڕۆ ڕۆژێکی تایبەتە بۆت! بەردەوام بە! ⚡"),
                ("🌙 بەختی ناو ناو!", "نە زۆر باشە نە زۆر خراپ، ئاسایییە! 🌙"),
                ("🎰 بەختی زەیف!", "ئەمڕۆ ئاگاداربە برا! 😬"),
            ]
            result = random.choice(results)
            markup = InlineKeyboardMarkup()
            markup.add(InlineKeyboardButton("🔄 دووبارە تاقی بکەرەوە", callback_data="lucky"))
            markup.add(InlineKeyboardButton("⬅️ گەڕانەوە", callback_data="back_to_main"))
            bot.edit_message_text(
                f"🎰 بەختی ئەمڕۆی {user_name}\n\n{result[0]}\n\n{result[1]}",
                chat_id, message_id, reply_markup=markup
            )

        # ── پرسیار و وەڵام ──
        elif call.data == "faq":
            markup = InlineKeyboardMarkup()
            markup.add(InlineKeyboardButton("❓ چۆن ئەپەکان دابەزێنم؟", callback_data="faq_download"))
            markup.add(InlineKeyboardButton("❓ ئایا ئەپەکان بەخۆڕاین؟", callback_data="faq_free"))
            markup.add(InlineKeyboardButton("❓ چۆن Install بکەم؟", callback_data="faq_install"))
            markup.add(InlineKeyboardButton("❓ ئایا ئەکاونتم باند دەبێت؟", callback_data="faq_ban"))
            markup.add(InlineKeyboardButton("❓ پەیوەندی بەیاکوزا", callback_data="faq_contact"))
            markup.add(InlineKeyboardButton("⬅️ گەڕانەوە", callback_data="back_to_main"))
            bot.edit_message_text(
                "❓ پرسیار و وەڵام\n\nکام پرسیارت هەیە؟",
                chat_id, message_id, reply_markup=markup
            )

        elif call.data == "faq_download":
            bot.edit_message_text(
                "❓ چۆن ئەپەکان دابەزێنم؟\n\n✅ وەڵام:\n١. بچۆ بۆ فرۆشگای یاکوزا\n٢. ئەپەکەی دەتەوێت هەڵبژێرە\n٣. دوگمەی داونلۆد داپبەژێ\n٤. فایلەکە دادەبەزێت بۆ مۆبایلەکەت",
                chat_id, message_id, reply_markup=back_btn("faq")
            )

        elif call.data == "faq_free":
            bot.edit_message_text(
                "❓ ئایا ئەپەکان بەخۆڕاین؟\n\n✅ وەڵام:\nبەڵێ! هەموو ئەپەکانی یاکوزا ستۆر بەخۆڕاین و مۆدکراون! 🎉\nهیچ پارەیەک پێویست نییە!",
                chat_id, message_id, reply_markup=back_btn("faq")
            )

        elif call.data == "faq_install":
            markup = InlineKeyboardMarkup()
            markup.add(InlineKeyboardButton("📱 iPhone", callback_data="faq_install_ios"))
            markup.add(InlineKeyboardButton("🤖 Android", callback_data="faq_install_android"))
            markup.add(InlineKeyboardButton("⬅️ گەڕانەوە", callback_data="faq"))
            bot.edit_message_text(
                "❓ چۆن Install بکەم؟\n\nکام مۆبایلت هەیە؟",
                chat_id, message_id, reply_markup=markup
            )

        elif call.data == "faq_install_ios":
            bot.edit_message_text(
                "📱 Install کردن لەسەر iPhone\n\n١. AltStore دابەزێنە\n٢. فایلی IPA داونلۆد بکە\n٣. لە AltStore فایلەکە Install بکە\n\nیان TrollStore بەکاربهێنە (iOS 14-16)",
                chat_id, message_id, reply_markup=back_btn("faq_install")
            )

        elif call.data == "faq_install_android":
            bot.edit_message_text(
                "🤖 Install کردن لەسەر ئەندرۆید\n\n١. فایلی APK داونلۆد بکە\n٢. Settings → Unknown Sources چالاک بکە\n٣. فایلەکە Install بکە\n\nئاسانە! ✅",
                chat_id, message_id, reply_markup=back_btn("faq_install")
            )

        elif call.data == "faq_ban":
            bot.edit_message_text(
                "❓ ئایا ئەکاونتم باند دەبێت؟\n\n✅ وەڵام:\nئەگەر هاکی باش بەکاربهێنیت باند نابیت!\n\nباشترین هاکەکان بۆ ئامنیەت:\n👑 AIM KING\n🐍 Snake\n⚙️ Kos Engine\n\nئاگادار بە لە Auto Play و Auto Queue!",
                chat_id, message_id, reply_markup=back_btn("faq")
            )

        elif call.data == "faq_contact":
            markup = InlineKeyboardMarkup()
            markup.add(InlineKeyboardButton("✈️ کەناڵی تەلەگرام", url="https://t.me/YAKUZA_CEO3"))
            markup.add(InlineKeyboardButton("▶️ یوتیوب", url="https://www.youtube.com/@YAKUZA_CEO"))
            markup.add(InlineKeyboardButton("⬅️ گەڕانەوە", callback_data="faq"))
            bot.edit_message_text(
                "📞 پەیوەندی بەیاکوزا\n\nلە ئەم کەناڵانەوە دەتوانیت پەیوەندی بکەیت:",
                chat_id, message_id, reply_markup=markup
            )

        # ── جیهانی هاک ──
        elif call.data == "hacker_world":
            markup = InlineKeyboardMarkup()
            markup.add(InlineKeyboardButton("🎯 باشترین هاکەکان", callback_data="best_hacks"))
            markup.add(InlineKeyboardButton("📱 هاکی ئایفۆن", callback_data="ios_hacks"))
            markup.add(InlineKeyboardButton("🤖 هاکی ئەندرۆید", callback_data="android_hacks"))
            markup.add(InlineKeyboardButton("⬅️ گەڕانەوە", callback_data="back_to_main"))
            bot.edit_message_text(
                "🌍 جیهانی هاک و فێرکاری\n\nهەموو زانیاری لەبارەی هاک و مۆدەکانەوە ئێرەیە! 💪",
                chat_id, message_id, reply_markup=markup
            )

        elif call.data == "best_hacks":
            text = ("🎯 باشترین هاکەکان بۆ ئەکاونت\n\n"
                "🟢 باشترینەکان (Security زۆر باشە)\n"
                "👑 AIM KING (ژخرا باشتر)\n"
                "🐍 Snake\n⚙️ Kos Engine\n🥷 Ninja Engine\n\n"
                "⚠️ ئەمانە تەنها لەسەر ئەکاونتی Guest\n"
                "🕷️ Spider Engine\n💎 KPMods\n🎯 AimX\n🔮 Glass Engine\n\n"
                "❌ ئەمانە بەکارمەهێنە (کراک کراون)")
            bot.edit_message_text(text, chat_id, message_id, reply_markup=back_btn("hacker_world"))

        elif call.data == "ios_hacks":
            text = ("📱 باشترین هاکەکان بۆ ئایفۆن\n\n"
                "✅ ئەمانە ئەکاونتت باند ناکەن\n"
                "💎 Flourite\n⚔️ MW Cheat\n🥷 Ninja Engine\n\n"
                "💡 پێشنیار: لەسەر ئەکاونتی Guest یاری بکە!")
            bot.edit_message_text(text, chat_id, message_id, reply_markup=back_btn("hacker_world"))

        elif call.data == "android_hacks":
            text = ("🤖 باشترین هاکەکان بۆ ئەندرۆید\n\n"
                "✅ Security باشە\n"
                "👑 AIM KING\n🐍 Snake\n⚙️ Kos Engine\n🥷 Ninja Engine\n\n"
                "⚠️ تەنها لەسەر ئەکاونتی Guest\n"
                "🕷️ Spider Engine\n💎 KPMods\n🎯 AimX\n🔮 Glass Engine")
            bot.edit_message_text(text, chat_id, message_id, reply_markup=back_btn("hacker_world"))

        # ── چارەسەری باندبوون ──
        elif call.data == "anti_ban_info":
            markup = InlineKeyboardMarkup()
            markup.add(InlineKeyboardButton("🛡️ پاراستنی ئەکاونت", callback_data="protect_account"))
            markup.add(InlineKeyboardButton("⚙️ ڕێکخستنی Auto Play", callback_data="auto_play_settings"))
            markup.add(InlineKeyboardButton("🎯 تیپی کێشانی گوڵە", callback_data="shot_tips"))
            markup.add(InlineKeyboardButton("🔧 چارەسەری Play Protect", callback_data="fix_install"))
            markup.add(InlineKeyboardButton("⬅️ گەڕانەوە", callback_data="back_to_main"))
            bot.edit_message_text(
                "🛡️ چارەسەری باندبوون\n\nهەموو زانیاری بۆ پاراستنی ئەکاونتەکەت! 💪",
                chat_id, message_id, reply_markup=markup
            )

        elif call.data == "protect_account":
            text = ("ئەری تەدڤێت ئەکاونتی تەیی شەخسی باند نەبێت دیف فان فەرمانا هەرە 👇\n\n"
                "هەمی گافا Auto Play بکارنەینە ئەو دبێتە ئەگەری باندبونا لیگایی ژی\n\n"
                "چجارا Auto Queue بکارنەینە گەلەک یا خەتەرە\n\n"
                "وەختئ تو داری دکێشی چ کوشنا نەدە ئاسای توپی ببە\n\n"
                "ئەڤە ئەو هاکن کو باشترینن و Security زور باشە بو باندبونی 👇\n\n"
                "👑 AIM KING (ژخرا باشتر)\n🐍 Snake\n⚙️ Kos Engine\n🥷 Ninja Engine\n\n"
                "بو ئایفونی باشترین کو ئەکاونتی تە باند نەبێت 👇\n\n"
                "💎 Flourite\n⚔️ MW Cheat\n🥷 Ninja Engine\n\n"
                "ئەو هاکئن پێدڤیە لەسەر ئەکاونتی Guest یاریی بکە 👇\n\n"
                "🕷️ Spider Engine\n💎 KPMods\n🎯 AimX\n🔮 Glass Engine\n\n"
                "و ئێت زخرا خرابتر ئەون ئێت (کراک کری) خو ژی پارێزن")
            bot.edit_message_text(text, chat_id, message_id, reply_markup=back_btn("anti_ban_info"))

        elif call.data == "auto_play_settings":
            text = ("⚙️ ڕێکخستنی Auto Play\n\n"
                "❌ Auto Play بەکارمەهێنە!\nئەمە دەبێتە هۆی باندبوونی لیگایی\n\n"
                "❌ Auto Queue بەکارمەهێنە!\nزۆر خەتەرناکە\n\n"
                "✅ پێشنیار:\nهەموو شتێک دەستی بکە")
            bot.edit_message_text(text, chat_id, message_id, reply_markup=back_btn("anti_ban_info"))

        elif call.data == "shot_tips":
            text = ("🎯 تیپی کێشانی گوڵە\n\n"
                "وەختئ تو داری دکێشی چ کوشنا نەدە ئاسای توپی ببە\n\n"
                "💡 پێشنیار:\nپێش کێشانی گوڵە هاکەکە چالاک بکە\n"
                "دوای گوڵەکە دەستی ببە")
            bot.edit_message_text(text, chat_id, message_id, reply_markup=back_btn("anti_ban_info"))

        elif call.data == "fix_install":
            text = ("🔧 چارەسەری Play Protect\n\n"
                "١. Play Store بکەرەوە\n"
                "٢. کلیک لەسەر پرۆفایل\n"
                "٣. Play Protect هەڵبژێرە\n"
                "٤. کوژاندنەوە\n\n"
                "✅ ئێستا دەتوانیت Install بکەیت!")
            bot.edit_message_text(text, chat_id, message_id, reply_markup=back_btn("anti_ban_info"))

    except Exception as e:
        print(f"Error: {e}")

print("✅ بۆتەکە دەستی پێکرد!")
bot.infinity_polling()
