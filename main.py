import telebot
import random
import os
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from datetime import datetime

BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)
CHANNEL = '@YAKUZA_CEO3'

user_stats = {}
user_langs = {}
daily_claimed = {}
gift_codes = {
    'YAKUZAFREE2026': {'ku': '🎁 کۆدەکە ڕاستە! خۆش بە! 🔥', 'ar': '🎁 الكود صحيح! استمتع! 🔥', 'en': '🎁 Code is valid! Enjoy! 🔥'},
    'FREE100': {'ku': '🎁 بەخشێنراوی تایبەت وەرگرتیت! 💎', 'ar': '🎁 حصلت على هدية مميزة! 💎', 'en': '🎁 You got a special gift! 💎'},
    'HACKFREE2026': {'ku': '🎁 هاکی تایبەت بۆت کراوەتەوە! 🎮', 'ar': '🎁 تم فتح هاك مميز لك! 🎮', 'en': '🎁 Special hack unlocked for you! 🎮'}
}

T = {
    'ku': {
        'select_lang': '🌐 زمانەکەت هەڵبژێرە:',
        'welcome': 'بەخێربێیت',
        'bot_name': 'بۆتی فەرمی یاکوزا ستۆر 🎮',
        'join_msg': '❌ پێویستە سەرەتا بچیتە ناو کەناڵەکەمەوە!\n\n👇 جۆین بکە پاشان چێک بکەرەوە',
        'join_btn': '✅ جۆین بکە 📢',
        'check_btn': '🔄 چێک بکەرەوە',
        'not_joined': '❌ هێشتا جۆین نەکردووی!',
        'back': '⬅️ گەڕانەوە',
        'btn_hack': '🚀 نوێترین هاک',
        'btn_anti': '🛡️ چارەسەری باند',
        'btn_world': '🌍 جیهانی هاک',
        'btn_lucky': '🎰 بەختەکەت',
        'btn_faq': '❓ پرسیار و وەڵام',
        'btn_game': '🎮 یاریەکی ڕاندەم',
        'btn_lead': '🏆 باشترین هاکەران',
        'btn_daily': '🎁 هەدیەی ڕۆژانە',
        'btn_code': '🔑 کۆدی هەدیە',
        'btn_stats': '📊 ئامارەکانم',
        'btn_lang': '🌐 گۆڕینی زمان',
        'btn_store': '📱 فرۆشگای یاکوزا',
        'btn_channel': '📢 کەناڵی ئێمە',
        'latest_hack': '🔥 هاکە نوێەکان لە کەناڵەکەمان دان!',
        'faq_title': '❓ پرسیار و وەڵام\n\nکام پرسیارت هەیە؟',
        'faq_q1': '❓ چۆن ئەپەکان دابەزێنم؟',
        'faq_q2': '❓ ئایا ئەپەکان بەخۆڕاین؟',
        'faq_q3': '❓ چۆن Install بکەم؟',
        'faq_q4': '❓ ئایا ئەکاونتم باند دەبێت؟',
        'faq_q5': '❓ پەیوەندی بەیاکوزا',
        'faq_a1': '❓ چۆن ئەپەکان دابەزێنم؟\n\n✅ وەڵام:\n١. بچۆ بۆ فرۆشگای یاکوزا\n٢. ئەپەکەی دەتەوێت هەڵبژێرە\n٣. دوگمەی داونلۆد داپبەژێ\n٤. فایلەکە دادەبەزێت',
        'faq_a2': '❓ ئایا ئەپەکان بەخۆڕاین؟\n\n✅ بەڵێ! هەموو ئەپەکانی یاکوزا ستۆر بەخۆڕاین! 🎉',
        'faq_install_q': '❓ چۆن Install بکەم؟\n\nکام مۆبایلت هەیە؟',
        'faq_ios': '📱 iPhone',
        'faq_android': '🤖 Android',
        'faq_ios_a': '📱 Install کردن لەسەر iPhone\n\n١. AltStore دابەزێنە\n٢. فایلی IPA داونلۆد بکە\n٣. لە AltStore Install بکە\n\nیان TrollStore (iOS 14-16)',
        'faq_android_a': '🤖 Install کردن لەسەر ئەندرۆید\n\n١. APK داونلۆد بکە\n٢. Unknown Sources چالاک بکە\n٣. Install بکە ✅',
        'faq_a4': '❓ ئایا ئەکاونتم باند دەبێت؟\n\n✅ ئەگەر هاکی باش بەکاربهێنیت باند نابیت!\n\n👑 AIM KING\n🐍 Snake\n⚙️ Kos Engine\n\nئاگادار بە لە Auto Play!',
        'faq_contact': '📞 پەیوەندی بەیاکوزا',
        'hacker_world': '🌍 جیهانی هاک و فێرکاری 💪',
        'btn_best': '🎯 باشترین هاکەکان',
        'btn_ios': '📱 هاکی ئایفۆن',
        'btn_droid': '🤖 هاکی ئەندرۆید',
        'best_hacks': '🎯 باشترین هاکەکان\n\n🟢 ئەکاونتی خۆت\n👑 AIM KING\n🐍 Snake\n⚙️ Kos Engine\n🥷 Ninja Engine\n\n⚠️ تەنها Guest\n🕷️ Spider Engine\n💎 KPMods\n🎯 AimX\n🔮 Glass Engine\n\n❌ کراک کراو مەکاربهێنە',
        'ios_hacks': '📱 هاکی ئایفۆن\n\n✅ باند ناکەن\n💎 Flourite\n⚔️ MW Cheat\n🥷 Ninja Engine\n\n💡 لەسەر Guest یاری بکە!',
        'android_hacks': '🤖 هاکی ئەندرۆید\n\n✅ ئەکاونتی خۆت\n👑 AIM KING\n🐍 Snake\n⚙️ Kos Engine\n🥷 Ninja Engine\n\n⚠️ تەنها Guest\n🕷️ Spider Engine\n💎 KPMods\n🎯 AimX\n🔮 Glass Engine',
        'anti_ban': '🛡️ چارەسەری باندبوون 💪',
        'btn_protect': '🛡️ پاراستنی ئەکاونت',
        'btn_autoplay': '⚙️ Auto Play',
        'btn_shot': '🎯 تیپی گوڵەکێشان',
        'btn_protect2': '🔧 Play Protect',
        'protect_account': 'ئەری تەدڤێت ئەکاونتی تەیی شەخسی باند نەبێت دیف فان فەرمانا هەرە 👇\n\nهەمی گافا Auto Play بکارنەینە ئەو دبێتە ئەگەری باندبونا لیگایی ژی\n\nچجارا Auto Queue بکارنەینە گەلەک یا خەتەرە\n\nوەختئ تو داری دکێشی چ کوشنا نەدە ئاسای توپی ببە\n\n👑 AIM KING\n🐍 Snake\n⚙️ Kos Engine\n🥷 Ninja Engine\n\nبو ئایفون 👇\n💎 Flourite\n⚔️ MW Cheat\n🥷 Ninja Engine\n\nتەنها Guest 👇\n🕷️ Spider Engine\n💎 KPMods\n🎯 AimX\n🔮 Glass Engine\n\nو ئێت زخرا خرابتر ئەون ئێت (کراک کری) خو ژی پارێزن',
        'autoplay': '⚙️ Auto Play\n\n❌ Auto Play بەکارمەهێنە!\n❌ Auto Queue بەکارمەهێنە!\n\n✅ هەموو شتێک دەستی بکە',
        'shot_tips': '🎯 تیپی گوڵەکێشان\n\nوەختئ تو داری دکێشی چ کوشنا نەدە ئاسای توپی ببە\n\n💡 هاکەکە چالاک بکە پێش کێشان',
        'play_protect': '🔧 Play Protect\n\n١. Play Store بکەرەوە\n٢. پرۆفایل\n٣. Play Protect\n٤. کوژاندنەوە\n\n✅ ئێستا Install بکە!',
        'lucky_title': '🎰 بەختی ئەمڕۆی',
        'lucky_retry': '🔄 دووبارە تاقی بکەرەوە',
        'stats_title': '📊 ئامارەکانت',
        'stats_clicks': '🔢 کۆی کلیکەکان',
        'stats_lang': '🌐 زمانەکەت',
        'stats_date': '📅 ئەمڕۆ',
        'lead_title': '🏆 لیستی باشترین بەکارهێنەران',
        'lead_rank': '📊 جێگای تۆ',
        'lead_empty': 'هێشتا کەس نییە!',
        'lead_clicks': 'کلیک',
        'daily_claimed': '❌ ئەمڕۆ هەدیەکەت وەرگرتووە!\n\n⏰ سبەی دووبارە بگەڕێوە!',
        'daily_title': '🎁 هەدیەی ڕۆژانەت!',
        'daily_back': '✅ سبەی دووبارە بگەڕێوە!',
        'gift_prompt': '🔑 کۆدی هەدیەکەت بنووسە!\n\n💡 کۆدی نموونە: YAKUZA2024',
        'gift_invalid': '❌ کۆدەکە هەڵەیە!',
        'random_title': '🎮 یاریەکی ڕاندەم بۆت هەڵبژێردرا!',
        'random_retry': '🔄 یارییەکی تر',
        'random_dl': '📱 داونلۆد بکە',
        'lang_changed': '✅ زمانەکەت گۆڕدرا!'
    },
    'ar': {
        'select_lang': '🌐 اختر لغتك:',
        'welcome': 'أهلاً وسهلاً',
        'bot_name': 'بوت ياكوزا ستور الرسمي 🎮',
        'join_msg': '❌ يجب عليك الانضمام للقناة أولاً!\n\n👇 انضم ثم تحقق',
        'join_btn': '✅ انضم الآن 📢',
        'check_btn': '🔄 تحقق',
        'not_joined': '❌ لم تنضم بعد!',
        'back': '⬅️ رجوع',
        'btn_hack': '🚀 أحدث الهاكات',
        'btn_anti': '🛡️ حل الباند',
        'btn_world': '🌍 عالم الهاك',
        'btn_lucky': '🎰 جرب حظك',
        'btn_faq': '❓ أسئلة وأجوبة',
        'btn_game': '🎮 لعبة عشوائية',
        'btn_lead': '🏆 أفضل الهاكرز',
        'btn_daily': '🎁 هدية يومية',
        'btn_code': '🔑 كود هدية',
        'btn_stats': '📊 إحصائياتي',
        'btn_lang': '🌐 تغيير اللغة',
        'btn_store': '📱 متجر ياكوزا',
        'btn_channel': '📢 قناتنا',
        'latest_hack': '🔥 أحدث الهاكات في قناتنا!',
        'faq_title': '❓ أسئلة وأجوبة\n\nما هو سؤالك؟',
        'faq_q1': '❓ كيف أحمل التطبيقات؟',
        'faq_q2': '❓ هل التطبيقات مجانية؟',
        'faq_q3': '❓ كيف أثبت؟',
        'faq_q4': '❓ هل سيتم باند حسابي؟',
        'faq_q5': '❓ تواصل مع ياكوزا',
        'faq_a1': '❓ كيف أحمل التطبيقات؟\n\n✅ الجواب:\n١. اذهب لمتجر ياكوزا\n٢. اختر التطبيق\n٣. اضغط تحميل\n٤. سيتم التحميل تلقائياً',
        'faq_a2': '❓ هل التطبيقات مجانية؟\n\n✅ نعم! كل تطبيقات ياكوزا مجانية! 🎉',
        'faq_install_q': '❓ كيف أثبت؟\n\nما هو جهازك؟',
        'faq_ios': '📱 iPhone',
        'faq_android': '🤖 Android',
        'faq_ios_a': '📱 التثبيت على iPhone\n\n١. حمل AltStore\n٢. حمل ملف IPA\n٣. ثبت من AltStore\n\nأو استخدم TrollStore (iOS 14-16)',
        'faq_android_a': '🤖 التثبيت على أندرويد\n\n١. حمل ملف APK\n٢. فعّل Unknown Sources\n٣. ثبت ✅',
        'faq_a4': '❓ هل سيتم باند حسابي؟\n\n✅ إذا استخدمت هاك جيد لن يتم الباند!\n\n👑 AIM KING\n🐍 Snake\n⚙️ Kos Engine\n\nانتبه من Auto Play!',
        'faq_contact': '📞 تواصل مع ياكوزا',
        'hacker_world': '🌍 عالم الهاك والتعليم 💪',
        'btn_best': '🎯 أفضل الهاكات',
        'btn_ios': '📱 هاك iPhone',
        'btn_droid': '🤖 هاك Android',
        'best_hacks': '🎯 أفضل الهاكات\n\n🟢 لحسابك الشخصي\n👑 AIM KING\n🐍 Snake\n⚙️ Kos Engine\n🥷 Ninja Engine\n\n⚠️ فقط على Guest\n🕷️ Spider Engine\n💎 KPMods\n🎯 AimX\n🔮 Glass Engine\n\n❌ لا تستخدم المكركة',
        'ios_hacks': '📱 هاك iPhone\n\n✅ لن يتم باند حسابك\n💎 Flourite\n⚔️ MW Cheat\n🥷 Ninja Engine\n\n💡 العب على Guest!',
        'android_hacks': '🤖 هاك Android\n\n✅ حسابك الشخصي\n👑 AIM KING\n🐍 Snake\n⚙️ Kos Engine\n🥷 Ninja Engine\n\n⚠️ فقط Guest\n🕷️ Spider Engine\n💎 KPMods\n🎯 AimX\n🔮 Glass Engine',
        'anti_ban': '🛡️ حل الباند 💪',
        'btn_protect': '🛡️ حماية الحساب',
        'btn_autoplay': '⚙️ Auto Play',
        'btn_shot': '🎯 نصائح الرمي',
        'btn_protect2': '🔧 Play Protect',
        'protect_account': 'لحماية حسابك من الباند اتبع هذه التعليمات 👇\n\nلا تستخدم Auto Play فهو سبب الباند في الليغ\n\nلا تستخدم Auto Queue فهو خطير جداً\n\nعند رمي الكرة لا تضغط زر التصويب العادي\n\n👑 AIM KING\n🐍 Snake\n⚙️ Kos Engine\n🥷 Ninja Engine\n\nلـ iPhone 👇\n💎 Flourite\n⚔️ MW Cheat\n🥷 Ninja Engine\n\nفقط على Guest 👇\n🕷️ Spider Engine\n💎 KPMods\n🎯 AimX\n🔮 Glass Engine\n\nالهاكات المكركة تجنبها',
        'autoplay': '⚙️ Auto Play\n\n❌ لا تستخدم Auto Play!\n❌ لا تستخدم Auto Queue!\n\n✅ افعل كل شيء يدوياً',
        'shot_tips': '🎯 نصائح الرمي\n\nعند رمي الكرة لا تضغط زر التصويب العادي\n\n💡 فعّل الهاك قبل الرمي',
        'play_protect': '🔧 Play Protect\n\n١. افتح Play Store\n٢. الملف الشخصي\n٣. Play Protect\n٤. أوقفه\n\n✅ الآن يمكنك التثبيت!',
        'lucky_title': '🎰 حظ اليوم لـ',
        'lucky_retry': '🔄 جرب مرة أخرى',
        'stats_title': '📊 إحصائياتك',
        'stats_clicks': '🔢 إجمالي النقرات',
        'stats_lang': '🌐 لغتك',
        'stats_date': '📅 اليوم',
        'lead_title': '🏆 قائمة أفضل المستخدمين',
        'lead_rank': '📊 مرتبتك',
        'lead_empty': 'لا يوجد أحد بعد!',
        'lead_clicks': 'نقرة',
        'daily_claimed': '❌ لقد أخذت هديتك اليوم!\n\n⏰ عد غداً!',
        'daily_title': '🎁 هديتك اليومية!',
        'daily_back': '✅ عد غداً!',
        'gift_prompt': '🔑 اكتب كود الهدية!\n\n💡 مثال: YAKUZAFREE2026',
        'gift_invalid': '❌ الكود غير صحيح!',
        'random_title': '🎮 تم اختيار لعبة عشوائية لك!',
        'random_retry': '🔄 لعبة أخرى',
        'random_dl': '📱 تحميل',
        'lang_changed': '✅ تم تغيير اللغة!'
    },
    'en': {
        'select_lang': '🌐 Select your language:',
        'welcome': 'Welcome',
        'bot_name': 'Yakuza Store Official Bot 🎮',
        'join_msg': '❌ You must join our channel first!\n\n👇 Join then check',
        'join_btn': '✅ Join Now 📢',
        'check_btn': '🔄 Check',
        'not_joined': '❌ You have not joined yet!',
        'back': '⬅️ Back',
        'btn_hack': '🚀 Latest Hacks',
        'btn_anti': '🛡️ Anti Ban',
        'btn_world': '🌍 Hack World',
        'btn_lucky': '🎰 Try Your Luck',
        'btn_faq': '❓ FAQ',
        'btn_game': '🎮 Random Game',
        'btn_lead': '🏆 Top Hackers',
        'btn_daily': '🎁 Daily Gift',
        'btn_code': '🔑 Gift Code',
        'btn_stats': '📊 My Stats',
        'btn_lang': '🌐 Change Language',
        'btn_store': '📱 Yakuza Store',
        'btn_channel': '📢 Our Channel',
        'latest_hack': '🔥 Latest hacks are in our channel!',
        'faq_title': '❓ FAQ\n\nWhat is your question?',
        'faq_q1': '❓ How to download apps?',
        'faq_q2': '❓ Are the apps free?',
        'faq_q3': '❓ How to install?',
        'faq_q4': '❓ Will my account get banned?',
        'faq_q5': '❓ Contact Yakuza',
        'faq_a1': '❓ How to download apps?\n\n✅ Answer:\n1. Go to Yakuza Store\n2. Choose the app\n3. Press download\n4. File will download',
        'faq_a2': '❓ Are the apps free?\n\n✅ Yes! All Yakuza Store apps are free! 🎉',
        'faq_install_q': '❓ How to install?\n\nWhat device do you have?',
        'faq_ios': '📱 iPhone',
        'faq_android': '🤖 Android',
        'faq_ios_a': '📱 Install on iPhone\n\n1. Download AltStore\n2. Download IPA file\n3. Install from AltStore\n\nOr use TrollStore (iOS 14-16)',
        'faq_android_a': '🤖 Install on Android\n\n1. Download APK file\n2. Enable Unknown Sources\n3. Install ✅',
        'faq_a4': '❓ Will my account get banned?\n\n✅ If you use good hacks you won\'t get banned!\n\n👑 AIM KING\n🐍 Snake\n⚙️ Kos Engine\n\nBeware of Auto Play!',
        'faq_contact': '📞 Contact Yakuza',
        'hacker_world': '🌍 Hack World & Tutorials 💪',
        'btn_best': '🎯 Best Hacks',
        'btn_ios': '📱 iPhone Hacks',
        'btn_droid': '🤖 Android Hacks',
        'best_hacks': '🎯 Best Hacks\n\n🟢 Your personal account\n👑 AIM KING\n🐍 Snake\n⚙️ Kos Engine\n🥷 Ninja Engine\n\n⚠️ Guest account only\n🕷️ Spider Engine\n💎 KPMods\n🎯 AimX\n🔮 Glass Engine\n\n❌ Do not use cracked hacks',
        'ios_hacks': '📱 iPhone Hacks\n\n✅ Won\'t ban your account\n💎 Flourite\n⚔️ MW Cheat\n🥷 Ninja Engine\n\n💡 Play on Guest account!',
        'android_hacks': '🤖 Android Hacks\n\n✅ Personal account\n👑 AIM KING\n🐍 Snake\n⚙️ Kos Engine\n🥷 Ninja Engine\n\n⚠️ Guest only\n🕷️ Spider Engine\n💎 KPMods\n🎯 AimX\n🔮 Glass Engine',
        'anti_ban': '🛡️ Anti Ban 💪',
        'btn_protect': '🛡️ Account Protection',
        'btn_autoplay': '⚙️ Auto Play',
        'btn_shot': '🎯 Shot Tips',
        'btn_protect2': '🔧 Play Protect',
        'protect_account': 'To protect your account from ban follow these tips 👇\n\nNever use Auto Play it causes league ban\n\nNever use Auto Queue it is very dangerous\n\nWhen shooting do not press the normal shot button\n\n👑 AIM KING\n🐍 Snake\n⚙️ Kos Engine\n🥷 Ninja Engine\n\nFor iPhone 👇\n💎 Flourite\n⚔️ MW Cheat\n🥷 Ninja Engine\n\nGuest only 👇\n🕷️ Spider Engine\n💎 KPMods\n🎯 AimX\n🔮 Glass Engine\n\nAvoid cracked hacks',
        'autoplay': '⚙️ Auto Play\n\n❌ Never use Auto Play!\n❌ Never use Auto Queue!\n\n✅ Do everything manually',
        'shot_tips': '🎯 Shot Tips\n\nWhen shooting do not press the normal shot button\n\n💡 Activate hack before shooting',
        'play_protect': '🔧 Play Protect\n\n1. Open Play Store\n2. Profile\n3. Play Protect\n4. Disable it\n\n✅ Now you can install!',
        'lucky_title': '🎰 Today\'s Luck for',
        'lucky_retry': '🔄 Try Again',
        'stats_title': '📊 Your Stats',
        'stats_clicks': '🔢 Total Clicks',
        'stats_lang': '🌐 Your Language',
        'stats_date': '📅 Today',
        'lead_title': '🏆 Top Users Leaderboard',
        'lead_rank': '📊 Your rank',
        'lead_empty': 'No one yet!',
        'lead_clicks': 'clicks',
        'daily_claimed': '❌ You already claimed today\'s gift!\n\n⏰ Come back tomorrow!',
        'daily_title': '🎁 Your Daily Gift!',
        'daily_back': '✅ Come back tomorrow!',
        'gift_prompt': '🔑 Enter your gift code!\n\n💡 Example: YAKUZAFREE2026',
        'gift_invalid': '❌ Invalid code!',
        'random_title': '🎮 A random game was picked for you!',
        'random_retry': '🔄 Another Game',
        'random_dl': '📱 Download',
        'lang_changed': '✅ Language changed!'
    }
}

def get_lang(uid): return user_langs.get(uid, None)
def t(uid, key): return T[get_lang(uid) or 'ku'].get(key, '')
def add_stat(uid):
    user_stats[uid] = user_stats.get(uid, 0) + 1

def is_subscribed(uid):
    try:
        m = bot.get_chat_member(CHANNEL, uid)
        return m.status in ['member', 'administrator', 'creator']
    except: return False

def lang_select_markup():
    m = InlineKeyboardMarkup()
    m.add(InlineKeyboardButton("🇹🇯 کوردی", callback_data="lang_ku"))
    m.add(InlineKeyboardButton("🇸🇦 عربي", callback_data="lang_ar"))
    m.add(InlineKeyboardButton("🇬🇧 English", callback_data="lang_en"))
    return m

def main_menu(uid):
    m = InlineKeyboardMarkup(row_width=2)
    m.add(InlineKeyboardButton(t(uid,'btn_hack'), callback_data="get_latest_hack"),
          InlineKeyboardButton(t(uid,'btn_anti'), callback_data="anti_ban_info"))
    m.add(InlineKeyboardButton(t(uid,'btn_world'), callback_data="hacker_world"),
          InlineKeyboardButton(t(uid,'btn_lucky'), callback_data="lucky"))
    m.add(InlineKeyboardButton(t(uid,'btn_faq'), callback_data="faq"),
          InlineKeyboardButton(t(uid,'btn_game'), callback_data="random_game"))
    m.add(InlineKeyboardButton(t(uid,'btn_lead'), callback_data="leaderboard"),
          InlineKeyboardButton(t(uid,'btn_daily'), callback_data="daily_gift"))
    m.add(InlineKeyboardButton(t(uid,'btn_code'), callback_data="gift_code"),
          InlineKeyboardButton(t(uid,'btn_stats'), callback_data="my_stats"))
    m.add(InlineKeyboardButton(t(uid,'btn_lang'), callback_data="change_lang"),
          InlineKeyboardButton(t(uid,'btn_store'), url="https://saadmzore238-arch.github.io/My.apps/"))
    m.add(InlineKeyboardButton(t(uid,'btn_channel'), url="https://t.me/YAKUZA_CEO3"))
    return m

def back_btn(uid, data="back_to_main"):
    m = InlineKeyboardMarkup()
    m.add(InlineKeyboardButton(t(uid,'back'), callback_data=data))
    return m

def check_sub_markup(uid):
    m = InlineKeyboardMarkup()
    m.add(InlineKeyboardButton(t(uid,'join_btn'), url="https://t.me/YAKUZA_CEO3"))
    m.add(InlineKeyboardButton(t(uid,'check_btn'), callback_data="check_sub"))
    return m

@bot.message_handler(commands=['start'])
def start(message):
    uid = message.from_user.id
    name = message.from_user.first_name or "👋"
    add_stat(uid)
    if get_lang(uid) is None:
        bot.send_message(message.chat.id, f"سڵاو {name} 👋\n\n" + T['ku']['select_lang'] + "\n" + T['ar']['select_lang'] + "\n" + T['en']['select_lang'], reply_markup=lang_select_markup())
    elif is_subscribed(uid):
        bot.send_message(message.chat.id, f"{t(uid,'welcome')} {name} 🔥\n{t(uid,'bot_name')}", reply_markup=main_menu(uid))
    else:
        bot.send_message(message.chat.id, f"سڵاو {name} 👋\n\n{t(uid,'join_msg')}", reply_markup=check_sub_markup(uid))

@bot.message_handler(func=lambda m: True)
def handle_text(message):
    uid = message.from_user.id
    text = message.text.strip().upper()
    if text in gift_codes:
        lang = get_lang(uid) or 'ku'
        bot.send_message(message.chat.id, gift_codes[text][lang])
    else:
        add_stat(uid)

@bot.callback_query_handler(func=lambda call: True)
def cb(call):
    cid = call.message.chat.id
    mid = call.message.message_id
    uid = call.from_user.id
    name = call.from_user.first_name or "👋"
    add_stat(uid)

    try:
        # زمان
        if call.data.startswith("lang_"):
            lang = call.data.split("_")[1]
            user_langs[uid] = lang
            if is_subscribed(uid):
                bot.edit_message_text(f"{t(uid,'welcome')} {name} 🔥\n{t(uid,'bot_name')}", cid, mid, reply_markup=main_menu(uid))
            else:
                bot.edit_message_text(f"سڵاو {name} 👋\n\n{t(uid,'join_msg')}", cid, mid, reply_markup=check_sub_markup(uid))

        elif call.data == "change_lang":
            bot.edit_message_text(t(uid,'select_lang'), cid, mid, reply_markup=lang_select_markup())

        elif call.data == "check_sub":
            if is_subscribed(uid):
                bot.edit_message_text(f"{t(uid,'welcome')} {name} 🔥\n{t(uid,'bot_name')}", cid, mid, reply_markup=main_menu(uid))
            else:
                bot.answer_callback_query(call.id, t(uid,'not_joined'), show_alert=True)

        elif call.data == "back_to_main":
            bot.edit_message_text(f"{t(uid,'welcome')} {name} 🔥\n{t(uid,'bot_name')}", cid, mid, reply_markup=main_menu(uid))

        elif call.data == "get_latest_hack":
            bot.answer_callback_query(call.id, t(uid,'latest_hack'), show_alert=True)

        elif call.data == "lucky":
            results_ku = [("🏆 باشترین بەخت!", "ئەمڕۆ ڕۆژی تۆیە! 🌟"), ("🎯 بەختی باش!", "یاری بکە و ببەرە! 🎮"), ("💎 بەختی نزم!", "ئاگاداربە! 😅"), ("🔥 بەختی گەرم!", "هیچ شتێک ناتوانێت بیتەپێچێنێت! 💪"), ("⚡ بەختی بریق!", "بەردەوام بە! ⚡"), ("🌙 بەختی ناو ناو!", "ئاسایییە! 🌙"), ("🎰 بەختی زەیف!", "ئاگاداربە برا! 😬")]
            results_ar = [("🏆 أفضل حظ!", "اليوم يومك! 🌟"), ("🎯 حظ جيد!", "العب وانتصر! 🎮"), ("💎 حظ منخفض!", "كن حذراً! 😅"), ("🔥 حظ ساخن!", "لا شيء يوقفك! 💪"), ("⚡ حظ مشرق!", "استمر! ⚡"), ("🌙 حظ متوسط!", "عادي! 🌙"), ("🎰 حظ ضعيف!", "كن حذراً! 😬")]
            results_en = [("🏆 Best Luck!", "Today is your day! 🌟"), ("🎯 Good Luck!", "Play and win! 🎮"), ("💎 Low Luck!", "Be careful! 😅"), ("🔥 Hot Luck!", "Nothing can stop you! 💪"), ("⚡ Bright Luck!", "Keep going! ⚡"), ("🌙 Average Luck!", "It's normal! 🌙"), ("🎰 Weak Luck!", "Be careful! 😬")]
            lang = get_lang(uid) or 'ku'
            results = results_ku if lang=='ku' else results_ar if lang=='ar' else results_en
            r = random.choice(results)
            mm = InlineKeyboardMarkup()
            mm.add(InlineKeyboardButton(t(uid,'lucky_retry'), callback_data="lucky"))
            mm.add(InlineKeyboardButton(t(uid,'back'), callback_data="back_to_main"))
            bot.edit_message_text(f"{t(uid,'lucky_title')} {name}\n\n{r[0]}\n\n{r[1]}", cid, mid, reply_markup=mm)

        elif call.data == "my_stats":
            count = user_stats.get(uid, 0)
            lang = get_lang(uid) or 'ku'
            lang_name = 'کوردی' if lang=='ku' else 'عربي' if lang=='ar' else 'English'
            bot.edit_message_text(f"{t(uid,'stats_title')} {name}\n\n{t(uid,'stats_clicks')}: {count}\n{t(uid,'stats_lang')}: {lang_name}\n{t(uid,'stats_date')}: {datetime.now().strftime('%Y-%m-%d')}", cid, mid, reply_markup=back_btn(uid))

        elif call.data == "leaderboard":
            sorted_u = sorted(user_stats.items(), key=lambda x: x[1], reverse=True)[:5]
            medals = ["🥇","🥈","🥉","4️⃣","5️⃣"]
            text = t(uid,'lead_title') + "\n\n"
            if sorted_u:
                for i,(u,c) in enumerate(sorted_u):
                    text += f"{medals[i]} #{i+1}: {c} {t(uid,'lead_clicks')}\n"
            else:
                text += t(uid,'lead_empty')
            text += f"\n\n{t(uid,'lead_rank')}: {user_stats.get(uid,0)} {t(uid,'lead_clicks')}"
            bot.edit_message_text(text, cid, mid, reply_markup=back_btn(uid))

        elif call.data == "daily_gift":
            today = datetime.now().strftime('%Y-%m-%d')
            key = f"{uid}_{today}"
            if key in daily_claimed:
                bot.edit_message_text(t(uid,'daily_claimed'), cid, mid, reply_markup=back_btn(uid))
            else:
                daily_claimed[key] = True
                lang = get_lang(uid) or 'ku'
                gifts_ku = ["🎁 هاکی تایبەت: AIM KING!", "💎 ئەمڕۆ بەختت باشە!", "🔥 Ninja Engine تاقی بکەرەوە!", "⚡ Snake هاک بەکاربهێنە!", "🏆 ئەمڕۆ ڕۆژی تۆیە!"]
                gifts_ar = ["🎁 هاك مميز: AIM KING!", "💎 حظك اليوم جيد!", "🔥 جرب Ninja Engine!", "⚡ استخدم Snake هاك!", "🏆 اليوم يومك!"]
                gifts_en = ["🎁 Special hack: AIM KING!", "💎 Your luck is good today!", "🔥 Try Ninja Engine!", "⚡ Use Snake hack!", "🏆 Today is your day!"]
                gifts = gifts_ku if lang=='ku' else gifts_ar if lang=='ar' else gifts_en
                bot.edit_message_text(f"{t(uid,'daily_title')}\n\n{random.choice(gifts)}\n\n{t(uid,'daily_back')}", cid, mid, reply_markup=back_btn(uid))

        elif call.data == "gift_code":
            mm = InlineKeyboardMarkup()
            mm.add(InlineKeyboardButton(t(uid,'back'), callback_data="back_to_main"))
            bot.edit_message_text(t(uid,'gift_prompt'), cid, mid, reply_markup=mm)

        elif call.data == "random_game":
            lang = get_lang(uid) or 'ku'
            games_ku = [("🎮 Roblox","زۆر باشە!"),("⚔️ Shadow Fight","شەڕ و شمشێر!"),("🏙️ GTA San Andreas","کلاسیک!"),("⛏️ Minecraft","دنیایەکی تایبەت!"),("🔫 Free Fire","ببەرە!"),("⚽ DLS 22","فوتبۆل!"),("🍬 Candy Crush","ئاسان و سەرگەرم!"),("🏄 Subway Surfers","بازبدە!")]
            games_ar = [("🎮 Roblox","ممتازة!"),("⚔️ Shadow Fight","قتال وسيوف!"),("🏙️ GTA San Andreas","كلاسيك!"),("⛏️ Minecraft","اصنع عالمك!"),("🔫 Free Fire","انتصر!"),("⚽ DLS 22","كرة القدم!"),("🍬 Candy Crush","ممتعة!"),("🏄 Subway Surfers","اركض!")]
            games_en = [("🎮 Roblox","So fun!"),("⚔️ Shadow Fight","Fight!"),("🏙️ GTA San Andreas","Classic!"),("⛏️ Minecraft","Build your world!"),("🔫 Free Fire","Win!"),("⚽ DLS 22","Football!"),("🍬 Candy Crush","Easy & fun!"),("🏄 Subway Surfers","Run!")]
            games = games_ku if lang=='ku' else games_ar if lang=='ar' else games_en
            g = random.choice(games)
            mm = InlineKeyboardMarkup()
            mm.add(InlineKeyboardButton(t(uid,'random_retry'), callback_data="random_game"))
            mm.add(InlineKeyboardButton(t(uid,'random_dl'), url="https://saadmzore238-arch.github.io/My.apps/"))
            mm.add(InlineKeyboardButton(t(uid,'back'), callback_data="back_to_main"))
            bot.edit_message_text(f"{t(uid,'random_title')}\n\n{g[0]}\n\n{g[1]}", cid, mid, reply_markup=mm)

        elif call.data == "faq":
            mm = InlineKeyboardMarkup()
            mm.add(InlineKeyboardButton(t(uid,'faq_q1'), callback_data="faq_download"))
            mm.add(InlineKeyboardButton(t(uid,'faq_q2'), callback_data="faq_free"))
            mm.add(InlineKeyboardButton(t(uid,'faq_q3'), callback_data="faq_install"))
            mm.add(InlineKeyboardButton(t(uid,'faq_q4'), callback_data="faq_ban"))
            mm.add(InlineKeyboardButton(t(uid,'faq_q5'), callback_data="faq_contact"))
            mm.add(InlineKeyboardButton(t(uid,'back'), callback_data="back_to_main"))
            bot.edit_message_text(t(uid,'faq_title'), cid, mid, reply_markup=mm)

        elif call.data == "faq_download":
            bot.edit_message_text(t(uid,'faq_a1'), cid, mid, reply_markup=back_btn(uid,"faq"))
        elif call.data == "faq_free":
            bot.edit_message_text(t(uid,'faq_a2'), cid, mid, reply_markup=back_btn(uid,"faq"))
        elif call.data == "faq_install":
            mm = InlineKeyboardMarkup()
            mm.add(InlineKeyboardButton(t(uid,'faq_ios'), callback_data="faq_install_ios"),
                   InlineKeyboardButton(t(uid,'faq_android'), callback_data="faq_install_android"))
            mm.add(InlineKeyboardButton(t(uid,'back'), callback_data="faq"))
            bot.edit_message_text(t(uid,'faq_install_q'), cid, mid, reply_markup=mm)
        elif call.data == "faq_install_ios":
            bot.edit_message_text(t(uid,'faq_ios_a'), cid, mid, reply_markup=back_btn(uid,"faq_install"))
        elif call.data == "faq_install_android":
            bot.edit_message_text(t(uid,'faq_android_a'), cid, mid, reply_markup=back_btn(uid,"faq_install"))
        elif call.data == "faq_ban":
            bot.edit_message_text(t(uid,'faq_a4'), cid, mid, reply_markup=back_btn(uid,"faq"))
        elif call.data == "faq_contact":
            mm = InlineKeyboardMarkup()
            mm.add(InlineKeyboardButton("✈️ Telegram", url="https://t.me/YAKUZA_CEO3"))
            mm.add(InlineKeyboardButton("▶️ YouTube", url="https://www.youtube.com/@YAKUZA_CEO"))
            mm.add(InlineKeyboardButton(t(uid,'back'), callback_data="faq"))
            bot.edit_message_text(t(uid,'faq_contact'), cid, mid, reply_markup=mm)

        elif call.data == "hacker_world":
            mm = InlineKeyboardMarkup()
            mm.add(InlineKeyboardButton(t(uid,'btn_best'), callback_data="best_hacks"),
                   InlineKeyboardButton(t(uid,'btn_ios'), callback_data="ios_hacks"))
            mm.add(InlineKeyboardButton(t(uid,'btn_droid'), callback_data="android_hacks"))
            mm.add(InlineKeyboardButton(t(uid,'back'), callback_data="back_to_main"))
            bot.edit_message_text(t(uid,'hacker_world'), cid, mid, reply_markup=mm)

        elif call.data == "best_hacks":
            bot.edit_message_text(t(uid,'best_hacks'), cid, mid, reply_markup=back_btn(uid,"hacker_world"))
        elif call.data == "ios_hacks":
            bot.edit_message_text(t(uid,'ios_hacks'), cid, mid, reply_markup=back_btn(uid,"hacker_world"))
        elif call.data == "android_hacks":
            bot.edit_message_text(t(uid,'android_hacks'), cid, mid, reply_markup=back_btn(uid,"hacker_world"))

        elif call.data == "anti_ban_info":
            mm = InlineKeyboardMarkup()
            mm.add(InlineKeyboardButton(t(uid,'btn_protect'), callback_data="protect_account"),
                   InlineKeyboardButton(t(uid,'btn_autoplay'), callback_data="auto_play_settings"))
            mm.add(InlineKeyboardButton(t(uid,'btn_shot'), callback_data="shot_tips"),
                   InlineKeyboardButton(t(uid,'btn_protect2'), callback_data="fix_install"))
            mm.add(InlineKeyboardButton(t(uid,'back'), callback_data="back_to_main"))
            bot.edit_message_text(t(uid,'anti_ban'), cid, mid, reply_markup=mm)

        elif call.data == "protect_account":
            bot.edit_message_text(t(uid,'protect_account'), cid, mid, reply_markup=back_btn(uid,"anti_ban_info"))
        elif call.data == "auto_play_settings":
            bot.edit_message_text(t(uid,'autoplay'), cid, mid, reply_markup=back_btn(uid,"anti_ban_info"))
        elif call.data == "shot_tips":
            bot.edit_message_text(t(uid,'shot_tips'), cid, mid, reply_markup=back_btn(uid,"anti_ban_info"))
        elif call.data == "fix_install":
            bot.edit_message_text(t(uid,'play_protect'), cid, mid, reply_markup=back_btn(uid,"anti_ban_info"))

    except Exception as e:
        print(f"Error: {e}")

print("✅ بۆتەکە دەستی پێکرد!")
bot.infinity_polling()
