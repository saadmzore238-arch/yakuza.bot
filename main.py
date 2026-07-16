import telebot
import random
import os
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from datetime import datetime

BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)
CHANNEL = '@YAKUZA_CEO3'

# داتای بەکارهێنەران
user_stats = {}
user_langs = {}
daily_claimed = {}
gift_codes = {'YAKUZA2024': '🎁 کۆدەکە ڕاستە! تاوان: خۆش بە! 🔥', 'FREE100': '🎁 بەخشێنراوی تایبەت وەرگرتیت! 💎', 'HACK2024': '🎁 هاکی تایبەت بۆت کراوەتەوە! 🎮'}

LANGS = {
    'ku': {'welcome': 'بەخێربێیت', 'bot_name': 'بۆتی فەرمی یاکوزا ستۆر 🎮', 'join_msg': 'پێویستە سەرەتا بچیتە ناو کەناڵەکەمەوە!', 'join_btn': 'جۆین بکە 📢', 'check_btn': 'چێک بکەرەوە 🔄', 'not_joined': 'هێشتا جۆین نەکردووی!', 'back': 'گەڕانەوە ⬅️'},
    'ar': {'welcome': 'أهلاً وسهلاً', 'bot_name': 'بوت ياكوزا ستور الرسمي 🎮', 'join_msg': 'يجب عليك الانضمام للقناة أولاً!', 'join_btn': 'انضم الآن 📢', 'check_btn': 'تحقق 🔄', 'not_joined': 'لم تنضم بعد!', 'back': 'رجوع ⬅️'},
    'en': {'welcome': 'Welcome', 'bot_name': 'Yakuza Store Official Bot 🎮', 'join_msg': 'You must join our channel first!', 'join_btn': 'Join Now 📢', 'check_btn': 'Check 🔄', 'not_joined': 'You have not joined yet!', 'back': 'Back ⬅️'}
}

def get_lang(user_id):
    return user_langs.get(user_id, 'ku')

def tr(user_id, key):
    return LANGS[get_lang(user_id)].get(key, '')

def add_stat(user_id):
    if user_id not in user_stats:
        user_stats[user_id] = 0
    user_stats[user_id] += 1

def is_subscribed(user_id):
    try:
        member = bot.get_chat_member(CHANNEL, user_id)
        return member.status in ['member', 'administrator', 'creator']
    except:
        return False

def main_menu(user_id=None):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("🚀 نوێترین هاک", callback_data="get_latest_hack"))
    markup.add(InlineKeyboardButton("🛡️ چارەسەری باندبوون", callback_data="anti_ban_info"))
    markup.add(InlineKeyboardButton("🌍 جیهانی هاک", callback_data="hacker_world"))
    markup.add(InlineKeyboardButton("🎰 بەختەکەت تاقی بکەرەوە", callback_data="lucky"))
    markup.add(InlineKeyboardButton("❓ پرسیار و وەڵام", callback_data="faq"))
    markup.add(InlineKeyboardButton("🎮 یاریەکی ڕاندەم", callback_data="random_game"))
    markup.add(InlineKeyboardButton("🏆 لیستی باشترین هاکەران", callback_data="leaderboard"))
    markup.add(InlineKeyboardButton("🎁 هەدیەی ڕۆژانە", callback_data="daily_gift"))
    markup.add(InlineKeyboardButton("🔑 کۆدی هەدیە", callback_data="gift_code"))
    markup.add(InlineKeyboardButton("📊 ئامارەکانم", callback_data="my_stats"))
    markup.add(InlineKeyboardButton("🌐 گۆڕینی زمان", callback_data="change_lang"))
    markup.add(InlineKeyboardButton("📱 فرۆشگای یاکوزا", url="https://saadmzore238-arch.github.io/My.apps/"))
    markup.add(InlineKeyboardButton("📢 کەناڵی ئێمە", url="https://t.me/YAKUZA_CEO3"))
    return markup

def check_sub_markup(user_id):
    lang = get_lang(user_id)
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(f"✅ {tr(user_id,'join_btn')}", url="https://t.me/YAKUZA_CEO3"))
    markup.add(InlineKeyboardButton(tr(user_id,'check_btn'), callback_data="check_sub"))
    return markup

def back_btn(data="back_to_main"):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("⬅️ گەڕانەوە", callback_data=data))
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name or "برا"
    add_stat(user_id)
    if is_subscribed(user_id):
        bot.send_message(message.chat.id, f"{tr(user_id,'welcome')} {user_name} 🔥\n{tr(user_id,'bot_name')}", reply_markup=main_menu(user_id))
    else:
        bot.send_message(message.chat.id, f"سڵاو {user_name} 👋\n\n❌ {tr(user_id,'join_msg')}\n\n👇 جۆین بکە پاشان چێک بکەرەوە", reply_markup=check_sub_markup(user_id))

@bot.message_handler(func=lambda m: True)
def handle_text(message):
    user_id = message.from_user.id
    text = message.text.strip()
    # چێک بکردنی کۆدی هەدیە
    if text.upper() in gift_codes:
        bot.send_message(message.chat.id, gift_codes[text.upper()])
    else:
        add_stat(user_id)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    user_id = call.from_user.id
    user_name = call.from_user.first_name or "برا"
    add_stat(user_id)

    try:
        if call.data == "check_sub":
            if is_subscribed(user_id):
                bot.edit_message_text(f"{tr(user_id,'welcome')} {user_name} 🔥\n{tr(user_id,'bot_name')}", chat_id, message_id, reply_markup=main_menu(user_id))
            else:
                bot.answer_callback_query(call.id, f"❌ {tr(user_id,'not_joined')}", show_alert=True)

        elif call.data == "back_to_main":
            bot.edit_message_text(f"{tr(user_id,'welcome')} {user_name} 🔥\n{tr(user_id,'bot_name')}", chat_id, message_id, reply_markup=main_menu(user_id))

        elif call.data == "get_latest_hack":
            bot.answer_callback_query(call.id, "🔥 هاکە نوێەکان لە کەناڵەکەمان دان!", show_alert=True)

        # ── گۆڕینی زمان ──
        elif call.data == "change_lang":
            markup = InlineKeyboardMarkup()
            markup.add(InlineKeyboardButton("🇹🇯 کوردی", callback_data="lang_ku"))
            markup.add(InlineKeyboardButton("🇸🇦 عەرەبی", callback_data="lang_ar"))
            markup.add(InlineKeyboardButton("🇬🇧 English", callback_data="lang_en"))
            markup.add(InlineKeyboardButton("⬅️ گەڕانەوە", callback_data="back_to_main"))
            bot.edit_message_text("🌐 زمانەکەت هەڵبژێرە:", chat_id, message_id, reply_markup=markup)

        elif call.data.startswith("lang_"):
            lang = call.data.split("_")[1]
            user_langs[user_id] = lang
            bot.edit_message_text(f"{tr(user_id,'welcome')} {user_name} 🔥\n{tr(user_id,'bot_name')}", chat_id, message_id, reply_markup=main_menu(user_id))

        # ── ئامارەکانم ──
        elif call.data == "my_stats":
            count = user_stats.get(user_id, 0)
            lang = get_lang(user_id)
            text = (f"📊 ئامارەکانت {user_name}\n\n"
                f"🔢 کۆی کلیکەکان: {count}\n"
                f"🌐 زمانەکەت: {'کوردی' if lang=='ku' else 'عەرەبی' if lang=='ar' else 'English'}\n"
                f"🎮 بەکارهێنەری: یاکوزا ستۆر\n"
                f"📅 ئەمڕۆ: {datetime.now().strftime('%Y-%m-%d')}")
            bot.edit_message_text(text, chat_id, message_id, reply_markup=back_btn())

        # ── یاریەکی ڕاندەم ──
        elif call.data == "random_game":
            games = [
                ("🎮 Roblox", "یاریەکی زۆر باشە! دەتوانیت لە فرۆشگای یاکوزا داونلۆد بکەیت!"),
                ("⚔️ Shadow Fight", "یاریەکی شەڕ و شمشێر! زۆر سەرگەرمە!"),
                ("🏙️ GTA San Andreas", "یاریەکی کلاسیک! هەموو کەس دەیزانێت!"),
                ("⛏️ Minecraft", "دنیایەکی تایبەت دروست بکە!"),
                ("🔫 Free Fire", "بەتاڵ مەبە، ببەرە ئەو دووانەی!"),
                ("⚽ DLS 22", "فوتبۆلی مۆبایل! تیمی خۆت دروست بکە!"),
                ("🍬 Candy Crush", "یاریەکی ئاسان و سەرگەرم!"),
                ("🏄 Subway Surfers", "بازبدە و تاریک مەکەوە!"),
            ]
            game = random.choice(games)
            markup = InlineKeyboardMarkup()
            markup.add(InlineKeyboardButton("🔄 یارییەکی تر", callback_data="random_game"))
            markup.add(InlineKeyboardButton("📱 داونلۆد بکە", url="https://saadmzore238-arch.github.io/My.apps/"))
            markup.add(InlineKeyboardButton("⬅️ گەڕانەوە", callback_data="back_to_main"))
            bot.edit_message_text(f"🎮 یاریەکی ڕاندەم بۆت هەڵبژێردرا!\n\n{game[0]}\n\n{game[1]}", chat_id, message_id, reply_markup=markup)

        # ── لیستی باشترین هاکەران ──
        elif call.data == "leaderboard":
            sorted_users = sorted(user_stats.items(), key=lambda x: x[1], reverse=True)[:5]
            medals = ["🥇", "🥈", "🥉", "4️⃣", "5️⃣"]
            text = "🏆 لیستی باشترین بەکارهێنەران\n\n"
            if sorted_users:
                for i, (uid, count) in enumerate(sorted_users):
                    text += f"{medals[i]} بەکارهێنەر #{i+1}: {count} کلیک\n"
            else:
                text += "هێشتا کەس نییە!"
            text += f"\n\n📊 جێگای تۆ: {user_stats.get(user_id, 0)} کلیک"
            bot.edit_message_text(text, chat_id, message_id, reply_markup=back_btn())

        # ── هەدیەی ڕۆژانە ──
        elif call.data == "daily_gift":
            today = datetime.now().strftime('%Y-%m-%d')
            key = f"{user_id}_{today}"
            if key in daily_claimed:
                bot.edit_message_text("❌ ئەمڕۆ هەدیەکەت وەرگرتووە!\n\n⏰ سبەی دووبارە بگەڕێوە!", chat_id, message_id, reply_markup=back_btn())
            else:
                daily_claimed[key] = True
                gifts = ["🎁 هاکی تایبەت: AIM KING بەخۆڕایە بۆت!", "💎 تاوانی تایبەت: ئەمڕۆ بەختت باشە!", "🔥 هاکی نوێ: Ninja Engine تاقی بکەرەوە!", "⚡ پێشنیاری تایبەت: Snake هاک بەکاربهێنە!", "🏆 ئەمڕۆ ڕۆژی تۆیە! هەموو شتێک باش دەبێت!"]
                gift = random.choice(gifts)
                bot.edit_message_text(f"🎁 هەدیەی ڕۆژانەت!\n\n{gift}\n\n✅ سبەی دووبارە بگەڕێوە!", chat_id, message_id, reply_markup=back_btn())

        # ── کۆدی هەدیە ──
        elif call.data == "gift_code":
            markup = InlineKeyboardMarkup()
            markup.add(InlineKeyboardButton("⬅️ گەڕانەوە", callback_data="back_to_main"))
            bot.edit_message_text("🔑 کۆدی هەدیەکەت بنووسە!\n\nکۆدەکە بنووسە و بینێرە بۆ بۆتەکە!\n\n💡 کۆدی نموونە: YAKUZA2024", chat_id, message_id, reply_markup=markup)

        # ── بەختەکەت ──
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
            bot.edit_message_text(f"🎰 بەختی ئەمڕۆی {user_name}\n\n{result[0]}\n\n{result[1]}", chat_id, message_id, reply_markup=markup)

        # ── پرسیار و وەڵام ──
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
            bot.edit_message_text("❓ چۆن ئەپەکان دابەزێنم؟\n\n✅ وەڵام:\n١. بچۆ بۆ فرۆشگای یاکوزا\n٢. ئەپەکەی دەتەوێت هەڵبژێرە\n٣. دوگمەی داونلۆد داپبەژێ\n٤. فایلەکە دادەبەزێت", chat_id, message_id, reply_markup=back_btn("faq"))
        elif call.data == "faq_free":
            bot.edit_message_text("❓ ئایا ئەپەکان بەخۆڕاین؟\n\n✅ بەڵێ! هەموو ئەپەکانی یاکوزا ستۆر بەخۆڕاین! 🎉", chat_id, message_id, reply_markup=back_btn("faq"))
        elif call.data == "faq_install":
            markup = InlineKeyboardMarkup()
            markup.add(InlineKeyboardButton("📱 iPhone", callback_data="faq_install_ios"))
            markup.add(InlineKeyboardButton("🤖 Android", callback_data="faq_install_android"))
            markup.add(InlineKeyboardButton("⬅️ گەڕانەوە", callback_data="faq"))
            bot.edit_message_text("❓ چۆن Install بکەم؟\n\nکام مۆبایلت هەیە؟", chat_id, message_id, reply_markup=markup)
        elif call.data == "faq_install_ios":
            bot.edit_message_text("📱 Install کردن لەسەر iPhone\n\n١. AltStore دابەزێنە\n٢. فایلی IPA داونلۆد بکە\n٣. لە AltStore Install بکە\n\nیان TrollStore (iOS 14-16)", chat_id, message_id, reply_markup=back_btn("faq_install"))
        elif call.data == "faq_install_android":
            bot.edit_message_text("🤖 Install کردن لەسەر ئەندرۆید\n\n١. APK داونلۆد بکە\n٢. Unknown Sources چالاک بکە\n٣. Install بکە ✅", chat_id, message_id, reply_markup=back_btn("faq_install"))
        elif call.data == "faq_ban":
            bot.edit_message_text("❓ ئایا ئەکاونتم باند دەبێت؟\n\n✅ ئەگەر هاکی باش بەکاربهێنیت باند نابیت!\n\n👑 AIM KING\n🐍 Snake\n⚙️ Kos Engine\n\nئاگادار بە لە Auto Play!", chat_id, message_id, reply_markup=back_btn("faq"))
        elif call.data == "faq_contact":
            markup = InlineKeyboardMarkup()
            markup.add(InlineKeyboardButton("✈️ تەلەگرام", url="https://t.me/YAKUZA_CEO3"))
            markup.add(InlineKeyboardButton("▶️ یوتیوب", url="https://www.youtube.com/@YAKUZA_CEO"))
            markup.add(InlineKeyboardButton("⬅️ گەڕانەوە", callback_data="faq"))
            bot.edit_message_text("📞 پەیوەندی بەیاکوزا", chat_id, message_id, reply_markup=markup)

        # ── جیهانی هاک ──
        elif call.data == "hacker_world":
            markup = InlineKeyboardMarkup()
            markup.add(InlineKeyboardButton("🎯 باشترین هاکەکان", callback_data="best_hacks"))
            markup.add(InlineKeyboardButton("📱 هاکی ئایفۆن", callback_data="ios_hacks"))
            markup.add(InlineKeyboardButton("🤖 هاکی ئەندرۆید", callback_data="android_hacks"))
            markup.add(InlineKeyboardButton("⬅️ گەڕانەوە", callback_data="back_to_main"))
            bot.edit_message_text("🌍 جیهانی هاک و فێرکاری 💪", chat_id, message_id, reply_markup=markup)

        elif call.data == "best_hacks":
            bot.edit_message_text("🎯 باشترین هاکەکان\n\n🟢 ئەکاونتی خۆت\n👑 AIM KING\n🐍 Snake\n⚙️ Kos Engine\n🥷 Ninja Engine\n\n⚠️ تەنها Guest\n🕷️ Spider Engine\n💎 KPMods\n🎯 AimX\n🔮 Glass Engine\n\n❌ کراک کراو مەکاربهێنە", chat_id, message_id, reply_markup=back_btn("hacker_world"))
        elif call.data == "ios_hacks":
            bot.edit_message_text("📱 هاکی ئایفۆن\n\n✅ باند ناکەن\n💎 Flourite\n⚔️ MW Cheat\n🥷 Ninja Engine\n\n💡 لەسەر Guest یاری بکە!", chat_id, message_id, reply_markup=back_btn("hacker_world"))
        elif call.data == "android_hacks":
            bot.edit_message_text("🤖 هاکی ئەندرۆید\n\n✅ ئەکاونتی خۆت\n👑 AIM KING\n🐍 Snake\n⚙️ Kos Engine\n🥷 Ninja Engine\n\n⚠️ Guest\n🕷️ Spider Engine\n💎 KPMods\n🎯 AimX\n🔮 Glass Engine", chat_id, message_id, reply_markup=back_btn("hacker_world"))

        # ── چارەسەری باندبوون ──
        elif call.data == "anti_ban_info":
            markup = InlineKeyboardMarkup()
            markup.add(InlineKeyboardButton("🛡️ پاراستنی ئەکاونت", callback_data="protect_account"))
            markup.add(InlineKeyboardButton("⚙️ Auto Play", callback_data="auto_play_settings"))
            markup.add(InlineKeyboardButton("🎯 تیپی گوڵەکێشان", callback_data="shot_tips"))
            markup.add(InlineKeyboardButton("🔧 Play Protect", callback_data="fix_install"))
            markup.add(InlineKeyboardButton("⬅️ گەڕانەوە", callback_data="back_to_main"))
            bot.edit_message_text("🛡️ چارەسەری باندبوون 💪", chat_id, message_id, reply_markup=markup)

        elif call.data == "protect_account":
            bot.edit_message_text("ئەری تەدڤێت ئەکاونتی تەیی شەخسی باند نەبێت دیف فان فەرمانا هەرە 👇\n\nهەمی گافا Auto Play بکارنەینە ئەو دبێتە ئەگەری باندبونا لیگایی ژی\n\nچجارا Auto Queue بکارنەینە گەلەک یا خەتەرە\n\nوەختئ تو داری دکێشی چ کوشنا نەدە ئاسای توپی ببە\n\n👑 AIM KING\n🐍 Snake\n⚙️ Kos Engine\n🥷 Ninja Engine\n\nبو ئایفون 👇\n💎 Flourite\n⚔️ MW Cheat\n🥷 Ninja Engine\n\nتەنها Guest 👇\n🕷️ Spider Engine\n💎 KPMods\n🎯 AimX\n🔮 Glass Engine\n\nو ئێت زخرا خرابتر ئەون ئێت (کراک کری) خو ژی پارێزن", chat_id, message_id, reply_markup=back_btn("anti_ban_info"))
        elif call.data == "auto_play_settings":
            bot.edit_message_text("⚙️ Auto Play\n\n❌ Auto Play بەکارمەهێنە!\n❌ Auto Queue بەکارمەهێنە!\n\n✅ هەموو شتێک دەستی بکە", chat_id, message_id, reply_markup=back_btn("anti_ban_info"))
        elif call.data == "shot_tips":
            bot.edit_message_text("🎯 تیپی گوڵەکێشان\n\nوەختئ تو داری دکێشی چ کوشنا نەدە ئاسای توپی ببە\n\n💡 هاکەکە چالاک بکە پێش کێشان", chat_id, message_id, reply_markup=back_btn("anti_ban_info"))
        elif call.data == "fix_install":
            bot.edit_message_text("🔧 Play Protect\n\n١. Play Store بکەرەوە\n٢. پرۆفایل\n٣. Play Protect\n٤. کوژاندنەوە\n\n✅ ئێستا Install بکە!", chat_id, message_id, reply_markup=back_btn("anti_ban_info"))

    except Exception as e:
        print(f"Error: {e}")

print("✅ بۆتەکە دەستی پێکرد!")
bot.infinity_polling()
