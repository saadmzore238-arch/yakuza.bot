import telebot
import random
import os
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from datetime import datetime

BOT_TOKEN = os.environ.get('BOT_TOKEN')
ADMIN_ID = 8982730336  # ئایدی خۆت دابنێ بۆ ئەکسەسی ئەدمین
bot = telebot.TeleBot(BOT_TOKEN)
CHANNEL = '@YAKUZA_CEO3'

user_stats = {}
user_langs = {}
user_points = {}
user_referrals = {}
user_first_time = {}
daily_claimed = {}
guess_number = {}
awaiting_broadcast = {}
user_achievements = {}
user_streak = {}
user_last_active = {}
user_nickname = {}
user_favorites = {}
user_blocked = set()
weekly_points = {}
tictactoe_games = {}
memory_games = {}
speed_click_data = {}
qr_requested = {}
user_characters = {}
user_clans = {}
clan_members = {}
trade_offers = {}
treasure_map = {}
squad_groups = {}
user_squad = {}
app_updates_track = {}





gift_codes = {
    'YAKUZA2024': {'ku': '🎁 کۆدەکە ڕاستە! +50 خاڵ 🔥', 'ar': '🎁 الكود صحيح! +50 نقطة 🔥', 'en': '🎁 Valid code! +50 points 🔥'},
    'FREE100': {'ku': '🎁 بەخشێنراوی تایبەت! +100 خاڵ 💎', 'ar': '🎁 هدية مميزة! +100 نقطة 💎', 'en': '🎁 Special gift! +100 points 💎'},
    'HACK2024': {'ku': '🎁 هاکی تایبەت! +75 خاڵ 🎮', 'ar': '🎁 هاك مميز! +75 نقطة 🎮', 'en': '🎁 Special hack! +75 points 🎮'}
}
code_points = {'YAKUZA2024': 50, 'FREE100': 100, 'HACK2024': 75}

quiz_questions = {
    'ku': [
        {'q': 'کام یاری زۆرترین داونلۆدی هەیە لە یاکوزا ستۆر؟', 'opts': ['8 Ball Pool', 'Roblox', 'GTA'], 'correct': 1},
        {'q': 'IPA فایل بۆ کام سیستەمە؟', 'opts': ['Android', 'iOS', 'Windows'], 'correct': 1},
        {'q': 'کام ئەپ بۆ ڕیتاچ کردنی وێنەیە؟', 'opts': ['PicsArt', 'Spotify', 'CapCut'], 'correct': 0},
    ],
    'ar': [
        {'q': 'أي لعبة لديها أكثر تحميلات في ياكوزا ستور؟', 'opts': ['8 Ball Pool', 'Roblox', 'GTA'], 'correct': 1},
        {'q': 'ملف IPA لأي نظام؟', 'opts': ['Android', 'iOS', 'Windows'], 'correct': 1},
        {'q': 'أي تطبيق لتعديل الصور؟', 'opts': ['PicsArt', 'Spotify', 'CapCut'], 'correct': 0},
    ],
    'en': [
        {'q': 'Which game has the most downloads on Yakuza Store?', 'opts': ['8 Ball Pool', 'Roblox', 'GTA'], 'correct': 1},
        {'q': 'IPA file is for which system?', 'opts': ['Android', 'iOS', 'Windows'], 'correct': 1},
        {'q': 'Which app is for photo editing?', 'opts': ['PicsArt', 'Spotify', 'CapCut'], 'correct': 0},
    ]
}

T = {
    'ku': {
        'select_lang': '🌐 زمانەکەت هەڵبژێرە:', 'welcome': 'بەخێربێیت', 'bot_name': 'بۆتی فەرمی یاکوزا ستۆر 🎮',
        'first_welcome': '🎉 خۆشحاڵین بە یەکەم جار بینینت!\n\nئێمە هیوادارین کاتێکی خۆشت لەگەڵمان بێت! 💜',
        'join_msg': '❌ پێویستە سەرەتا بچیتە ناو کەناڵەکەمەوە!\n\n👇 جۆین بکە پاشان چێک بکەرەوە',
        'join_btn': '✅ جۆین بکە 📢', 'check_btn': '🔄 چێک بکەرەوە', 'not_joined': '❌ هێشتا جۆین نەکردووی!', 'back': '⬅️ گەڕانەوە',
        'btn_hack': '🚀 نوێترین هاک', 'btn_anti': '🛡️ چارەسەری باند', 'btn_world': '🌍 جیهانی هاک', 'btn_lucky': '🎰 بەختەکەت',
        'btn_faq': '❓ پرسیار و وەڵام', 'btn_game': '🎮 یاریەکی ڕاندەم', 'btn_lead': '🏆 باشترین هاکەران', 'btn_daily': '🎁 هەدیەی ڕۆژانە',
        'btn_code': '🔑 کۆدی هەدیە', 'btn_stats': '📊 ئامارەکانم', 'btn_lang': '🌐 گۆڕینی زمان', 'btn_store': '📱 فرۆشگای یاکوزا',
        'btn_channel': '📢 کەناڵی ئێمە', 'btn_points': '🪙 خاڵەکانم', 'btn_ref': '⭐ بانگهێشتی هاوڕێ',
        'btn_quiz': '🎲 کوویزی یاری', 'btn_guess': '🎯 ژمارە بدۆزەرەوە', 'btn_vip': '💎 پلەی VIP',
        'latest_hack': '🔥 هاکە نوێەکان لە کەناڵەکەمان دان!', 'faq_title': '❓ پرسیار و وەڵام\n\nکام پرسیارت هەیە؟',
        'faq_q1': '❓ چۆن ئەپەکان دابەزێنم؟', 'faq_q2': '❓ ئایا ئەپەکان بەخۆڕاین؟', 'faq_q3': '❓ چۆن Install بکەم؟',
        'faq_q4': '❓ ئایا ئەکاونتم باند دەبێت؟', 'faq_q5': '❓ پەیوەندی بەیاکوزا',
        'faq_a1': '❓ چۆن ئەپەکان دابەزێنم؟\n\n✅ وەڵام:\n١. بچۆ بۆ فرۆشگای یاکوزا\n٢. ئەپەکەی دەتەوێت هەڵبژێرە\n٣. دوگمەی داونلۆد داپبەژێ\n٤. فایلەکە دادەبەزێت',
        'faq_a2': '❓ ئایا ئەپەکان بەخۆڕاین؟\n\n✅ بەڵێ! هەموو ئەپەکانی یاکوزا ستۆر بەخۆڕاین! 🎉',
        'faq_install_q': '❓ چۆن Install بکەم؟\n\nکام مۆبایلت هەیە؟', 'faq_ios': '📱 iPhone', 'faq_android': '🤖 Android',
        'faq_ios_a': '📱 Install کردن لەسەر iPhone\n\n١. AltStore دابەزێنە\n٢. فایلی IPA داونلۆد بکە\n٣. لە AltStore Install بکە\n\nیان TrollStore (iOS 14-16)',
        'faq_android_a': '🤖 Install کردن لەسەر ئەندرۆید\n\n١. APK داونلۆد بکە\n٢. Unknown Sources چالاک بکە\n٣. Install بکە ✅',
        'faq_a4': '❓ ئایا ئەکاونتم باند دەبێت؟\n\n✅ ئەگەر هاکی باش بەکاربهێنیت باند نابیت!\n\n👑 AIM KING\n🐍 Snake\n⚙️ Kos Engine\n\nئاگادار بە لە Auto Play!',
        'faq_contact': '📞 پەیوەندی بەیاکوزا', 'hacker_world': '🌍 جیهانی هاک و فێرکاری 💪',
        'btn_best': '🎯 باشترین هاکەکان', 'btn_ios': '📱 هاکی ئایفۆن', 'btn_droid': '🤖 هاکی ئەندرۆید',
        'best_hacks': '🎯 باشترین هاکەکان\n\n🟢 ئەکاونتی خۆت\n👑 AIM KING\n🐍 Snake\n⚙️ Kos Engine\n🥷 Ninja Engine\n\n⚠️ تەنها Guest\n🕷️ Spider Engine\n💎 KPMods\n🎯 AimX\n🔮 Glass Engine\n\n❌ کراک کراو مەکاربهێنە',
        'ios_hacks': '📱 هاکی ئایفۆن\n\n✅ باند ناکەن\n💎 Flourite\n⚔️ MW Cheat\n🥷 Ninja Engine\n\n💡 لەسەر Guest یاری بکە!',
        'android_hacks': '🤖 هاکی ئەندرۆید\n\n✅ ئەکاونتی خۆت\n👑 AIM KING\n🐍 Snake\n⚙️ Kos Engine\n🥷 Ninja Engine\n\n⚠️ تەنها Guest\n🕷️ Spider Engine\n💎 KPMods\n🎯 AimX\n🔮 Glass Engine',
        'anti_ban': '🛡️ چارەسەری باندبوون 💪', 'btn_protect': '🛡️ پاراستنی ئەکاونت', 'btn_autoplay': '⚙️ Auto Play',
        'btn_shot': '🎯 تیپی گوڵەکێشان', 'btn_protect2': '🔧 Play Protect',
        'protect_account': 'ئەری تەدڤێت ئەکاونتی تەیی شەخسی باند نەبێت دیف فان فەرمانا هەرە 👇\n\nهەمی گافا Auto Play بکارنەینە ئەو دبێتە ئەگەری باندبونا لیگایی ژی\n\nچجارا Auto Queue بکارنەینە گەلەک یا خەتەرە\n\nوەختئ تو داری دکێشی چ کوشنا نەدە ئاسای توپی ببە\n\n👑 AIM KING\n🐍 Snake\n⚙️ Kos Engine\n🥷 Ninja Engine\n\nبو ئایفون 👇\n💎 Flourite\n⚔️ MW Cheat\n🥷 Ninja Engine\n\nتەنها Guest 👇\n🕷️ Spider Engine\n💎 KPMods\n🎯 AimX\n🔮 Glass Engine\n\nو ئێت زخرا خرابتر ئەون ئێت (کراک کری) خو ژی پارێزن',
        'autoplay': '⚙️ Auto Play\n\n❌ Auto Play بەکارمەهێنە!\n❌ Auto Queue بەکارمەهێنە!\n\n✅ هەموو شتێک دەستی بکە',
        'shot_tips': '🎯 تیپی گوڵەکێشان\n\nوەختئ تو داری دکێشی چ کوشنا نەدە ئاسای توپی ببە\n\n💡 هاکەکە چالاک بکە پێش کێشان',
        'play_protect': '🔧 Play Protect\n\n١. Play Store بکەرەوە\n٢. پرۆفایل\n٣. Play Protect\n٤. کوژاندنەوە\n\n✅ ئێستا Install بکە!',
        'lucky_title': '🎰 بەختی ئەمڕۆی', 'lucky_retry': '🔄 دووبارە تاقی بکەرەوە',
        'stats_title': '📊 ئامارەکانت', 'stats_clicks': '🔢 کۆی کلیکەکان', 'stats_lang': '🌐 زمانەکەت', 'stats_date': '📅 ئەمڕۆ',
        'lead_title': '🏆 لیستی باشترین بەکارهێنەران', 'lead_rank': '📊 جێگای تۆ', 'lead_empty': 'هێشتا کەس نییە!', 'lead_clicks': 'کلیک',
        'daily_claimed': '❌ ئەمڕۆ هەدیەکەت وەرگرتووە!\n\n⏰ سبەی دووبارە بگەڕێوە!', 'daily_title': '🎁 هەدیەی ڕۆژانەت!',
        'daily_back': '✅ سبەی دووبارە بگەڕێوە!', 'gift_prompt': '🔑 کۆدی هەدیەکەت بنووسە!\n\n💡 کۆدی نموونە: YAKUZA2024',
        'gift_invalid': '❌ کۆدەکە هەڵەیە!', 'random_title': '🎮 یاریەکی ڕاندەم بۆت هەڵبژێردرا!', 'random_retry': '🔄 یارییەکی تر',
        'random_dl': '📱 داونلۆد بکە', 'lang_changed': '✅ زمانەکەت گۆڕدرا!',
        'points_title': '🪙 خاڵەکانت', 'points_have': '💰 خاڵی هەیە', 'points_earn': '📈 چۆن خاڵ کۆبکەمەوە؟',
        'points_info': '🪙 چۆن خاڵ کۆبکەمەوە؟\n\n✅ ڕێگاکان:\n🔑 کۆدی هەدیە: 50-100 خاڵ\n🎁 هەدیەی ڕۆژانە: 10-30 خاڵ\n⭐ بانگهێشتی هاوڕێ: 25 خاڵ\n🎲 کوویز: 15 خاڵ\n🎯 دۆزینەوەی ژمارە: 20 خاڵ',
        'ref_title': '⭐ بانگهێشتی هاوڕێ', 'ref_desc': 'لینکی تایبەتی خۆت بنێرە بۆ هاوڕێکانت!\n\nبۆ هەر هاوڕێیەک، 25 خاڵ وەردەگریت! 🎉',
        'ref_link': '🔗 لینکی تۆ', 'ref_count': '👥 ژمارەی بانگهێشتەکان',
        'new_ref': '🎉 هاوڕێیەک بەڕێی تۆ هاتووە! +25 خاڵ 🪙',
        'quiz_title': '🎲 کوویزی یاری', 'quiz_correct': '✅ وەڵامی ڕاست! +15 خاڵ 🎉', 'quiz_wrong': '❌ وەڵامی هەڵە! دووبارە هەوڵبدە',
        'guess_title': '🎯 ژمارەیەک لە نێوان 1 و 10 بدۆزەرەوە!\n\nژمارەکە بنووسە:', 'guess_correct': '🎉 ڕاستە! +20 خاڵ 🪙',
        'guess_wrong': '❌ هەڵەیە! دووبارە هەوڵبدە', 'guess_hint_up': '⬆️ ژمارەکە گەورەترە',
        'guess_hint_down': '⬇️ ژمارەکە بچووکترە',
        'vip_title': '💎 پلەی VIP', 'vip_bronze': '🥉 بڕۆنز', 'vip_silver': '🥈 زیو', 'vip_gold': '🥇 زێڕ', 'vip_diamond': '💎 داماند',
        'vip_none': '⚪ ئاسایی',
        'vip_info': '💎 پلەکانی VIP\n\n⚪ ئاسایی: 0-99 خاڵ\n🥉 بڕۆنز: 100-299 خاڵ\n🥈 زیو: 300-599 خاڵ\n🥇 زێڕ: 600-999 خاڵ\n💎 داماند: 1000+ خاڵ\n\nپلەی تۆ: ',
        'broadcast_prompt': '📢 پەیامەکەت بنووسە بۆ ناردن بۆ هەموو بەکارهێنەران:',
        'broadcast_sent': '✅ پەیامەکە نێردرا بۆ هەموو بەکارهێنەران!'
    },
    'ar': {
        'select_lang': '🌐 اختر لغتك:', 'welcome': 'أهلاً وسهلاً', 'bot_name': 'بوت ياكوزا ستور الرسمي 🎮',
        'first_welcome': '🎉 سعداء برؤيتك لأول مرة!\n\nنتمنى لك وقتاً ممتعاً معنا! 💜',
        'join_msg': '❌ يجب عليك الانضمام للقناة أولاً!\n\n👇 انضم ثم تحقق',
        'join_btn': '✅ انضم الآن 📢', 'check_btn': '🔄 تحقق', 'not_joined': '❌ لم تنضم بعد!', 'back': '⬅️ رجوع',
        'btn_hack': '🚀 أحدث الهاكات', 'btn_anti': '🛡️ حل الباند', 'btn_world': '🌍 عالم الهاك', 'btn_lucky': '🎰 جرب حظك',
        'btn_faq': '❓ أسئلة وأجوبة', 'btn_game': '🎮 لعبة عشوائية', 'btn_lead': '🏆 أفضل الهاكرز', 'btn_daily': '🎁 هدية يومية',
        'btn_code': '🔑 كود هدية', 'btn_stats': '📊 إحصائياتي', 'btn_lang': '🌐 تغيير اللغة', 'btn_store': '📱 متجر ياكوزا',
        'btn_channel': '📢 قناتنا', 'btn_points': '🪙 نقاطي', 'btn_ref': '⭐ دعوة صديق',
        'btn_quiz': '🎲 اختبار الألعاب', 'btn_guess': '🎯 خمن الرقم', 'btn_vip': '💎 مستوى VIP',
        'latest_hack': '🔥 أحدث الهاكات في قناتنا!', 'faq_title': '❓ أسئلة وأجوبة\n\nما هو سؤالك؟',
        'faq_q1': '❓ كيف أحمل التطبيقات؟', 'faq_q2': '❓ هل التطبيقات مجانية؟', 'faq_q3': '❓ كيف أثبت؟',
        'faq_q4': '❓ هل سيتم باند حسابي؟', 'faq_q5': '❓ تواصل مع ياكوزا',
        'faq_a1': '❓ كيف أحمل التطبيقات؟\n\n✅ الجواب:\n١. اذهب لمتجر ياكوزا\n٢. اختر التطبيق\n٣. اضغط تحميل\n٤. سيتم التحميل تلقائياً',
        'faq_a2': '❓ هل التطبيقات مجانية؟\n\n✅ نعم! كل تطبيقات ياكوزا مجانية! 🎉',
        'faq_install_q': '❓ كيف أثبت؟\n\nما هو جهازك؟', 'faq_ios': '📱 iPhone', 'faq_android': '🤖 Android',
        'faq_ios_a': '📱 التثبيت على iPhone\n\n١. حمل AltStore\n٢. حمل ملف IPA\n٣. ثبت من AltStore\n\nأو استخدم TrollStore (iOS 14-16)',
        'faq_android_a': '🤖 التثبيت على أندرويد\n\n١. حمل ملف APK\n٢. فعّل Unknown Sources\n٣. ثبت ✅',
        'faq_a4': '❓ هل سيتم باند حسابي؟\n\n✅ إذا استخدمت هاك جيد لن يتم الباند!\n\n👑 AIM KING\n🐍 Snake\n⚙️ Kos Engine\n\nانتبه من Auto Play!',
        'faq_contact': '📞 تواصل مع ياكوزا', 'hacker_world': '🌍 عالم الهاك والتعليم 💪',
        'btn_best': '🎯 أفضل الهاكات', 'btn_ios': '📱 هاك iPhone', 'btn_droid': '🤖 هاك Android',
        'best_hacks': '🎯 أفضل الهاكات\n\n🟢 لحسابك الشخصي\n👑 AIM KING\n🐍 Snake\n⚙️ Kos Engine\n🥷 Ninja Engine\n\n⚠️ فقط على Guest\n🕷️ Spider Engine\n💎 KPMods\n🎯 AimX\n🔮 Glass Engine\n\n❌ لا تستخدم المكركة',
        'ios_hacks': '📱 هاك iPhone\n\n✅ لن يتم باند حسابك\n💎 Flourite\n⚔️ MW Cheat\n🥷 Ninja Engine\n\n💡 العب على Guest!',
        'android_hacks': '🤖 هاك Android\n\n✅ حسابك الشخصي\n👑 AIM KING\n🐍 Snake\n⚙️ Kos Engine\n🥷 Ninja Engine\n\n⚠️ فقط Guest\n🕷️ Spider Engine\n💎 KPMods\n🎯 AimX\n🔮 Glass Engine',
        'anti_ban': '🛡️ حل الباند 💪', 'btn_protect': '🛡️ حماية الحساب', 'btn_autoplay': '⚙️ Auto Play',
        'btn_shot': '🎯 نصائح الرمي', 'btn_protect2': '🔧 Play Protect',
        'protect_account': 'لحماية حسابك من الباند اتبع هذه التعليمات 👇\n\nلا تستخدم Auto Play فهو سبب الباند في الليغ\n\nلا تستخدم Auto Queue فهو خطير جداً\n\nعند رمي الكرة لا تضغط زر التصويب العادي\n\n👑 AIM KING\n🐍 Snake\n⚙️ Kos Engine\n🥷 Ninja Engine\n\nلـ iPhone 👇\n💎 Flourite\n⚔️ MW Cheat\n🥷 Ninja Engine\n\nفقط على Guest 👇\n🕷️ Spider Engine\n💎 KPMods\n🎯 AimX\n🔮 Glass Engine\n\nالهاكات المكركة تجنبها',
        'autoplay': '⚙️ Auto Play\n\n❌ لا تستخدم Auto Play!\n❌ لا تستخدم Auto Queue!\n\n✅ افعل كل شيء يدوياً',
        'shot_tips': '🎯 نصائح الرمي\n\nعند رمي الكرة لا تضغط زر التصويب العادي\n\n💡 فعّل الهاك قبل الرمي',
        'play_protect': '🔧 Play Protect\n\n١. افتح Play Store\n٢. الملف الشخصي\n٣. Play Protect\n٤. أوقفه\n\n✅ الآن يمكنك التثبيت!',
        'lucky_title': '🎰 حظ اليوم لـ', 'lucky_retry': '🔄 جرب مرة أخرى',
        'stats_title': '📊 إحصائياتك', 'stats_clicks': '🔢 إجمالي النقرات', 'stats_lang': '🌐 لغتك', 'stats_date': '📅 اليوم',
        'lead_title': '🏆 قائمة أفضل المستخدمين', 'lead_rank': '📊 مرتبتك', 'lead_empty': 'لا يوجد أحد بعد!', 'lead_clicks': 'نقرة',
        'daily_claimed': '❌ لقد أخذت هديتك اليوم!\n\n⏰ عد غداً!', 'daily_title': '🎁 هديتك اليومية!',
        'daily_back': '✅ عد غداً!', 'gift_prompt': '🔑 اكتب كود الهدية!\n\n💡 مثال: YAKUZA2024',
        'gift_invalid': '❌ الكود غير صحيح!', 'random_title': '🎮 تم اختيار لعبة عشوائية لك!', 'random_retry': '🔄 لعبة أخرى',
        'random_dl': '📱 تحميل', 'lang_changed': '✅ تم تغيير اللغة!',
        'points_title': '🪙 نقاطك', 'points_have': '💰 لديك نقاط', 'points_earn': '📈 كيف أجمع النقاط؟',
        'points_info': '🪙 كيف أجمع النقاط؟\n\n✅ الطرق:\n🔑 كود هدية: 50-100 نقطة\n🎁 هدية يومية: 10-30 نقطة\n⭐ دعوة صديق: 25 نقطة\n🎲 اختبار: 15 نقطة\n🎯 تخمين الرقم: 20 نقطة',
        'ref_title': '⭐ دعوة صديق', 'ref_desc': 'أرسل رابطك الخاص لأصدقائك!\n\nلكل صديق، تحصل على 25 نقطة! 🎉',
        'ref_link': '🔗 رابطك', 'ref_count': '👥 عدد الدعوات',
        'new_ref': '🎉 صديق انضم عن طريقك! +25 نقطة 🪙',
        'quiz_title': '🎲 اختبار الألعاب', 'quiz_correct': '✅ إجابة صحيحة! +15 نقطة 🎉', 'quiz_wrong': '❌ إجابة خاطئة! حاول مرة أخرى',
        'guess_title': '🎯 خمن رقماً بين 1 و 10!\n\nاكتب الرقم:', 'guess_correct': '🎉 صحيح! +20 نقطة 🪙',
        'guess_wrong': '❌ خاطئ! حاول مرة أخرى', 'guess_hint_up': '⬆️ الرقم أكبر',
        'guess_hint_down': '⬇️ الرقم أصغر',
        'vip_title': '💎 مستوى VIP', 'vip_bronze': '🥉 برونزي', 'vip_silver': '🥈 فضي', 'vip_gold': '🥇 ذهبي', 'vip_diamond': '💎 ماسي',
        'vip_none': '⚪ عادي',
        'vip_info': '💎 مستويات VIP\n\n⚪ عادي: 0-99 نقطة\n🥉 برونزي: 100-299 نقطة\n🥈 فضي: 300-599 نقطة\n🥇 ذهبي: 600-999 نقطة\n💎 ماسي: 1000+ نقطة\n\nمستواك: ',
        'broadcast_prompt': '📢 اكتب رسالتك لإرسالها لجميع المستخدمين:',
        'broadcast_sent': '✅ تم إرسال الرسالة لجميع المستخدمين!'
    },
    'en': {
        'select_lang': '🌐 Select your language:', 'welcome': 'Welcome', 'bot_name': 'Yakuza Store Official Bot 🎮',
        'first_welcome': '🎉 Happy to see you for the first time!\n\nWe hope you have a great time with us! 💜',
        'join_msg': '❌ You must join our channel first!\n\n👇 Join then check',
        'join_btn': '✅ Join Now 📢', 'check_btn': '🔄 Check', 'not_joined': '❌ You have not joined yet!', 'back': '⬅️ Back',
        'btn_hack': '🚀 Latest Hacks', 'btn_anti': '🛡️ Anti Ban', 'btn_world': '🌍 Hack World', 'btn_lucky': '🎰 Try Your Luck',
        'btn_faq': '❓ FAQ', 'btn_game': '🎮 Random Game', 'btn_lead': '🏆 Top Hackers', 'btn_daily': '🎁 Daily Gift',
        'btn_code': '🔑 Gift Code', 'btn_stats': '📊 My Stats', 'btn_lang': '🌐 Change Language', 'btn_store': '📱 Yakuza Store',
        'btn_channel': '📢 Our Channel', 'btn_points': '🪙 My Points', 'btn_ref': '⭐ Invite Friend',
        'btn_quiz': '🎲 Game Quiz', 'btn_guess': '🎯 Guess Number', 'btn_vip': '💎 VIP Level',
        'latest_hack': '🔥 Latest hacks are in our channel!', 'faq_title': '❓ FAQ\n\nWhat is your question?',
        'faq_q1': '❓ How to download apps?', 'faq_q2': '❓ Are the apps free?', 'faq_q3': '❓ How to install?',
        'faq_q4': '❓ Will my account get banned?', 'faq_q5': '❓ Contact Yakuza',
        'faq_a1': '❓ How to download apps?\n\n✅ Answer:\n1. Go to Yakuza Store\n2. Choose the app\n3. Press download\n4. File will download',
        'faq_a2': '❓ Are the apps free?\n\n✅ Yes! All Yakuza Store apps are free! 🎉',
        'faq_install_q': '❓ How to install?\n\nWhat device do you have?', 'faq_ios': '📱 iPhone', 'faq_android': '🤖 Android',
        'faq_ios_a': '📱 Install on iPhone\n\n1. Download AltStore\n2. Download IPA file\n3. Install from AltStore\n\nOr use TrollStore (iOS 14-16)',
        'faq_android_a': '🤖 Install on Android\n\n1. Download APK file\n2. Enable Unknown Sources\n3. Install ✅',
        'faq_a4': '❓ Will my account get banned?\n\n✅ If you use good hacks you won\'t get banned!\n\n👑 AIM KING\n🐍 Snake\n⚙️ Kos Engine\n\nBeware of Auto Play!',
        'faq_contact': '📞 Contact Yakuza', 'hacker_world': '🌍 Hack World & Tutorials 💪',
        'btn_best': '🎯 Best Hacks', 'btn_ios': '📱 iPhone Hacks', 'btn_droid': '🤖 Android Hacks',
        'best_hacks': '🎯 Best Hacks\n\n🟢 Your personal account\n👑 AIM KING\n🐍 Snake\n⚙️ Kos Engine\n🥷 Ninja Engine\n\n⚠️ Guest account only\n🕷️ Spider Engine\n💎 KPMods\n🎯 AimX\n🔮 Glass Engine\n\n❌ Do not use cracked hacks',
        'ios_hacks': '📱 iPhone Hacks\n\n✅ Won\'t ban your account\n💎 Flourite\n⚔️ MW Cheat\n🥷 Ninja Engine\n\n💡 Play on Guest account!',
        'android_hacks': '🤖 Android Hacks\n\n✅ Personal account\n👑 AIM KING\n🐍 Snake\n⚙️ Kos Engine\n🥷 Ninja Engine\n\n⚠️ Guest only\n🕷️ Spider Engine\n💎 KPMods\n🎯 AimX\n🔮 Glass Engine',
        'anti_ban': '🛡️ Anti Ban 💪', 'btn_protect': '🛡️ Account Protection', 'btn_autoplay': '⚙️ Auto Play',
        'btn_shot': '🎯 Shot Tips', 'btn_protect2': '🔧 Play Protect',
        'protect_account': 'To protect your account from ban follow these tips 👇\n\nNever use Auto Play it causes league ban\n\nNever use Auto Queue it is very dangerous\n\nWhen shooting do not press the normal shot button\n\n👑 AIM KING\n🐍 Snake\n⚙️ Kos Engine\n🥷 Ninja Engine\n\nFor iPhone 👇\n💎 Flourite\n⚔️ MW Cheat\n🥷 Ninja Engine\n\nGuest only 👇\n🕷️ Spider Engine\n💎 KPMods\n🎯 AimX\n🔮 Glass Engine\n\nAvoid cracked hacks',
        'autoplay': '⚙️ Auto Play\n\n❌ Never use Auto Play!\n❌ Never use Auto Queue!\n\n✅ Do everything manually',
        'shot_tips': '🎯 Shot Tips\n\nWhen shooting do not press the normal shot button\n\n💡 Activate hack before shooting',
        'play_protect': '🔧 Play Protect\n\n1. Open Play Store\n2. Profile\n3. Play Protect\n4. Disable it\n\n✅ Now you can install!',
        'lucky_title': '🎰 Today\'s Luck for', 'lucky_retry': '🔄 Try Again',
        'stats_title': '📊 Your Stats', 'stats_clicks': '🔢 Total Clicks', 'stats_lang': '🌐 Your Language', 'stats_date': '📅 Today',
        'lead_title': '🏆 Top Users Leaderboard', 'lead_rank': '📊 Your rank', 'lead_empty': 'No one yet!', 'lead_clicks': 'clicks',
        'daily_claimed': '❌ You already claimed today\'s gift!\n\n⏰ Come back tomorrow!', 'daily_title': '🎁 Your Daily Gift!',
        'daily_back': '✅ Come back tomorrow!', 'gift_prompt': '🔑 Enter your gift code!\n\n💡 Example: YAKUZA2024',
        'gift_invalid': '❌ Invalid code!', 'random_title': '🎮 A random game was picked for you!', 'random_retry': '🔄 Another Game',
        'random_dl': '📱 Download', 'lang_changed': '✅ Language changed!',
        'points_title': '🪙 Your Points', 'points_have': '💰 Points you have', 'points_earn': '📈 How to earn points?',
        'points_info': '🪙 How to earn points?\n\n✅ Ways:\n🔑 Gift code: 50-100 points\n🎁 Daily gift: 10-30 points\n⭐ Invite friend: 25 points\n🎲 Quiz: 15 points\n🎯 Guess number: 20 points',
        'ref_title': '⭐ Invite Friend', 'ref_desc': 'Send your special link to your friends!\n\nFor every friend, you get 25 points! 🎉',
        'ref_link': '🔗 Your Link', 'ref_count': '👥 Invite Count',
        'new_ref': '🎉 A friend joined via your link! +25 points 🪙',
        'quiz_title': '🎲 Game Quiz', 'quiz_correct': '✅ Correct answer! +15 points 🎉', 'quiz_wrong': '❌ Wrong answer! Try again',
        'guess_title': '🎯 Guess a number between 1 and 10!\n\nType the number:', 'guess_correct': '🎉 Correct! +20 points 🪙',
        'guess_wrong': '❌ Wrong! Try again', 'guess_hint_up': '⬆️ Number is bigger',
        'guess_hint_down': '⬇️ Number is smaller',
        'vip_title': '💎 VIP Level', 'vip_bronze': '🥉 Bronze', 'vip_silver': '🥈 Silver', 'vip_gold': '🥇 Gold', 'vip_diamond': '💎 Diamond',
        'vip_none': '⚪ Normal',
        'vip_info': '💎 VIP Levels\n\n⚪ Normal: 0-99 points\n🥉 Bronze: 100-299 points\n🥈 Silver: 300-599 points\n🥇 Gold: 600-999 points\n💎 Diamond: 1000+ points\n\nYour level: ',
        'broadcast_prompt': '📢 Type your message to send to all users:',
        'broadcast_sent': '✅ Message sent to all users!'
    }
}


EXTRA_T = {
    'ku': {
        'btn_wheel': '🎡 چەرخی بەخت', 'btn_dice': '🎳 تاسی بەخت', 'btn_achieve': '🎖️ باجەکانم', 'btn_streak': '📅 بەردەوامیم',
        'btn_nickname': '📝 نازناوم', 'btn_fav': '📋 لیستی تایبەتم', 'btn_gift_pts': '💌 خاڵ بنێرە', 'btn_weekly': '🏅 پێشبڕکێی هەفتانە',
        'btn_report': '⚠️ ڕاپۆرت کردن', 'btn_admin': '👑 پانێڵی ئەدمین',
        'wheel_title': '🎡 چەرخی بەخت', 'wheel_spin': '🎡 بجولێنە!', 'wheel_result': '🎡 ئەنجامەکەت:',
        'dice_title': '🎳 تاسی بەخت', 'dice_roll': '🎲 فڕێی بدە!', 'dice_result': '🎲 تاسەکەت:',
        'achieve_title': '🎖️ باجەکانت', 'achieve_locked': '🔒 نەکراوەتەوە', 'achieve_unlocked': '✅ کراوەتەوە',
        'streak_title': '📅 بەردەوامیت', 'streak_days': 'ڕۆژ بەردەوام', 'streak_today': '✅ ئەمڕۆ هاتووی!',
        'nickname_prompt': '📝 نازناوی نوێت بنووسە:', 'nickname_set': '✅ نازناوەکەت گۆڕدرا بۆ:',
        'fav_title': '📋 لیستی تایبەتت', 'fav_empty': 'هیچ ئەپێکت زیاد نەکردووە!', 'fav_added': '✅ زیاد کرا بۆ لیستەکەت!',
        'gift_pts_prompt': '💌 ID ی بەکارهێنەرەکە و ژمارەی خاڵ بنووسە\n\nنموونە: 123456 10',
        'gift_pts_sent': '✅ خاڵ نێردرا!', 'gift_pts_received': '🎁 خاڵت وەرگرت لە هاوڕێیەک!',
        'weekly_title': '🏅 پێشبڕکێی هەفتانە', 'weekly_desc': 'باشترین بەکارهێنەری ئەم هەفتەیە!',
        'report_prompt': '⚠️ کێشەکەت بنووسە، دەگاتە ئەدمین:', 'report_sent': '✅ ڕاپۆرتەکەت نێردرا بۆ ئەدمین!',
        'admin_panel': '👑 پانێڵی ئەدمین', 'admin_users': '👥 کۆی بەکارهێنەران', 'admin_broadcast': '📢 Broadcast',
        'ach_click10': '🥉 10 کلیک', 'ach_click50': '🥈 50 کلیک', 'ach_click100': '🥇 100 کلیک',
        'ach_points100': '💰 100 خاڵ', 'ach_ref5': '⭐ 5 بانگهێشت', 'ach_streak7': '🔥 7 ڕۆژ بەردەوام'
    },
    'ar': {
        'btn_wheel': '🎡 عجلة الحظ', 'btn_dice': '🎳 نرد الحظ', 'btn_achieve': '🎖️ إنجازاتي', 'btn_streak': '📅 تتابعي',
        'btn_nickname': '📝 لقبي', 'btn_fav': '📋 قائمتي المفضلة', 'btn_gift_pts': '💌 أرسل نقاط', 'btn_weekly': '🏅 مسابقة أسبوعية',
        'btn_report': '⚠️ إبلاغ', 'btn_admin': '👑 لوحة الإدارة',
        'wheel_title': '🎡 عجلة الحظ', 'wheel_spin': '🎡 أدر!', 'wheel_result': '🎡 نتيجتك:',
        'dice_title': '🎳 نرد الحظ', 'dice_roll': '🎲 ارمِ!', 'dice_result': '🎲 نردك:',
        'achieve_title': '🎖️ إنجازاتك', 'achieve_locked': '🔒 مقفل', 'achieve_unlocked': '✅ مفتوح',
        'streak_title': '📅 تتابعك', 'streak_days': 'يوم متتالي', 'streak_today': '✅ جئت اليوم!',
        'nickname_prompt': '📝 اكتب لقبك الجديد:', 'nickname_set': '✅ تم تغيير لقبك إلى:',
        'fav_title': '📋 قائمتك المفضلة', 'fav_empty': 'لم تضف أي تطبيق!', 'fav_added': '✅ تمت الإضافة لقائمتك!',
        'gift_pts_prompt': '💌 اكتب ID المستخدم وعدد النقاط\n\nمثال: 123456 10',
        'gift_pts_sent': '✅ تم إرسال النقاط!', 'gift_pts_received': '🎁 حصلت على نقاط من صديق!',
        'weekly_title': '🏅 مسابقة أسبوعية', 'weekly_desc': 'أفضل مستخدم هذا الأسبوع!',
        'report_prompt': '⚠️ اكتب مشكلتك، ستصل للإدارة:', 'report_sent': '✅ تم إرسال بلاغك للإدارة!',
        'admin_panel': '👑 لوحة الإدارة', 'admin_users': '👥 إجمالي المستخدمين', 'admin_broadcast': '📢 Broadcast',
        'ach_click10': '🥉 10 نقرات', 'ach_click50': '🥈 50 نقرة', 'ach_click100': '🥇 100 نقرة',
        'ach_points100': '💰 100 نقطة', 'ach_ref5': '⭐ 5 دعوات', 'ach_streak7': '🔥 7 أيام متتالية'
    },
    'en': {
        'btn_wheel': '🎡 Lucky Wheel', 'btn_dice': '🎳 Lucky Dice', 'btn_achieve': '🎖️ My Achievements', 'btn_streak': '📅 My Streak',
        'btn_nickname': '📝 My Nickname', 'btn_fav': '📋 My Favorites', 'btn_gift_pts': '💌 Send Points', 'btn_weekly': '🏅 Weekly Contest',
        'btn_report': '⚠️ Report Issue', 'btn_admin': '👑 Admin Panel',
        'wheel_title': '🎡 Lucky Wheel', 'wheel_spin': '🎡 Spin!', 'wheel_result': '🎡 Your result:',
        'dice_title': '🎳 Lucky Dice', 'dice_roll': '🎲 Roll!', 'dice_result': '🎲 Your dice:',
        'achieve_title': '🎖️ Your Achievements', 'achieve_locked': '🔒 Locked', 'achieve_unlocked': '✅ Unlocked',
        'streak_title': '📅 Your Streak', 'streak_days': 'days in a row', 'streak_today': '✅ You came today!',
        'nickname_prompt': '📝 Type your new nickname:', 'nickname_set': '✅ Your nickname changed to:',
        'fav_title': '📋 Your Favorites List', 'fav_empty': 'You haven\'t added any apps!', 'fav_added': '✅ Added to your list!',
        'gift_pts_prompt': '💌 Type user ID and points amount\n\nExample: 123456 10',
        'gift_pts_sent': '✅ Points sent!', 'gift_pts_received': '🎁 You received points from a friend!',
        'weekly_title': '🏅 Weekly Contest', 'weekly_desc': 'Best user of this week!',
        'report_prompt': '⚠️ Type your issue, it will reach the admin:', 'report_sent': '✅ Your report sent to admin!',
        'admin_panel': '👑 Admin Panel', 'admin_users': '👥 Total Users', 'admin_broadcast': '📢 Broadcast',
        'ach_click10': '🥉 10 clicks', 'ach_click50': '🥈 50 clicks', 'ach_click100': '🥇 100 clicks',
        'ach_points100': '💰 100 points', 'ach_ref5': '⭐ 5 invites', 'ach_streak7': '🔥 7 day streak'
    }
}

for lang in T:
    T[lang].update(EXTRA_T[lang])


EXTRA_T2 = {
    'ku': {
        'btn_rps': '✊ کیش کیش کیش', 'btn_joke': '😂 نکتەیەک', 'btn_tip': '💡 تیپی ڕۆژانە', 'btn_countdown': '⏰ ژماردنی داهاتوو',
        'rps_title': '✊✋✌️ کیش کیش کیش', 'rps_choose': 'یەکێک هەڵبژێرە:', 'rps_you': 'تۆ', 'rps_bot': 'من',
        'rps_win': '🎉 بردت! +10 خاڵ', 'rps_lose': '❌ زۆرت! دووبارە هەوڵبدە', 'rps_draw': '🤝 یەکسانە!',
        'joke_title': '😂 نکتەیەک بۆت', 'tip_title': '💡 تیپی ئەمڕۆ',
        'countdown_title': '⏰ ژماردنەوە بۆ ئەپی داهاتوو', 'countdown_text': 'ئەپی نوێ بەم زووانە!'
    },
    'ar': {
        'btn_rps': '✊ حجر ورقة مقص', 'btn_joke': '😂 نكتة', 'btn_tip': '💡 نصيحة اليوم', 'btn_countdown': '⏰ العد التنازلي',
        'rps_title': '✊✋✌️ حجر ورقة مقص', 'rps_choose': 'اختر واحد:', 'rps_you': 'أنت', 'rps_bot': 'أنا',
        'rps_win': '🎉 فزت! +10 نقطة', 'rps_lose': '❌ خسرت! حاول مرة أخرى', 'rps_draw': '🤝 تعادل!',
        'joke_title': '😂 نكتة لك', 'tip_title': '💡 نصيحة اليوم',
        'countdown_title': '⏰ العد التنازلي للتطبيق القادم', 'countdown_text': 'تطبيق جديد قريباً!'
    },
    'en': {
        'btn_rps': '✊ Rock Paper Scissors', 'btn_joke': '😂 Joke', 'btn_tip': '💡 Daily Tip', 'btn_countdown': '⏰ Countdown',
        'rps_title': '✊✋✌️ Rock Paper Scissors', 'rps_choose': 'Choose one:', 'rps_you': 'You', 'rps_bot': 'Me',
        'rps_win': '🎉 You win! +10 points', 'rps_lose': '❌ You lose! Try again', 'rps_draw': '🤝 Draw!',
        'joke_title': '😂 A joke for you', 'tip_title': '💡 Today\'s Tip',
        'countdown_title': '⏰ Countdown to next app', 'countdown_text': 'New app coming soon!'
    }
}
for lang in T:
    T[lang].update(EXTRA_T2[lang])

jokes = {
    'ku': ["🎮 بۆچی گەیمەر هەرگیز نانخۆرێت؟ چونکە دەترسێت لێول up بکات! 😂", "💻 بۆچی کۆمپیوتەرەکە سارد بوو؟ چونکە پەنجەرەکانی کراوە بوون! 🪟", "🕹️ گەیمەرێک دەڵێت: من هەرگیز درۆ ناکەم، تەنها لاگ دەکەم! 😆"],
    'ar': ["🎮 لماذا لا يأكل اللاعب أبداً؟ لأنه يخاف أن يرتفع مستواه! 😂", "💻 لماذا كان الكمبيوتر بارداً؟ لأن نوافذه كانت مفتوحة! 🪟", "🕹️ يقول أحد اللاعبين: أنا لا أكذب أبداً، أنا فقط أتأخر! 😆"],
    'en': ["🎮 Why does a gamer never eat? Because they're afraid of leveling up! 😂", "💻 Why was the computer cold? Because it left its Windows open! 🪟", "🕹️ A gamer says: I never lie, I just lag! 😆"]
}

daily_tips = {
    'ku': ["💡 هەمیشە فایلی بەکاپ بگرە پێش Install کردنی هەر ئەپێک!", "💡 VPN بەکاربهێنە بۆ ئەمنیەتی زیاتر!", "💡 هەرگیز پاسۆردی خۆت لەگەڵ کەس بەشدار مەکە!"],
    'ar': ["💡 دائماً احفظ نسخة احتياطية قبل تثبيت أي تطبيق!", "💡 استخدم VPN لأمان أكثر!", "💡 لا تشارك كلمة مرورك مع أحد أبداً!"],
    'en': ["💡 Always backup before installing any app!", "💡 Use VPN for extra security!", "💡 Never share your password with anyone!"]
}


EXTRA_T3 = {
    'ku': {
        'btn_ttt': '⭕ Tic Tac Toe', 'btn_memory': '🃏 یاریی مێمۆری', 'btn_speed': '⚡ کلیکی خێرا',
        'btn_rank': '🏆 پلەی من', 'btn_shop': '🛒 فرۆشگای خاڵ', 'btn_history': '📜 مێژووم',
        'btn_challenge': '👫 پێشبڕکێی هاوڕێ', 'btn_qr': '📱 QR کۆد', 'btn_tutorial': '📖 فێرکاری',
        'ttt_title': '⭕ Tic Tac Toe - نۆرەی تۆیە', 'ttt_win': '🎉 تۆ بردت! +30 خاڵ', 'ttt_lose': '❌ بۆت بردی!', 'ttt_draw': '🤝 یەکسانە!',
        'memory_title': '🃏 یاریی مێمۆری\n\nهەردوو کارتی هاوشێوە هەڵبژێرە!', 'memory_match': '✅ هاوتایە! +15 خاڵ', 'memory_nomatch': '❌ هاوتا نییە!',
        'speed_title': '⚡ کلیکی خێرا\n\nلە ماوەی 5 چرکەدا زۆرترین کلیک بکە!', 'speed_click': '👆 کلیک!', 'speed_result': '⚡ ئەنجام:', 'speed_clicks': 'کلیک',
        'rank_bronze': '🥉 بڕۆنز', 'rank_silver': '🥈 زیو', 'rank_gold': '🥇 زێڕ', 'rank_platinum': '💠 پلاتینیۆم', 'rank_diamond': '💎 داماند', 'rank_legend': '👑 ئەفسانە',
        'rank_title': '🏆 پلەی تۆ', 'rank_progress': 'پێشکەوتن بۆ پلەی داهاتوو',
        'shop_title': '🛒 فرۆشگای خاڵ', 'shop_item1': '🎨 تیمی ڕەنگی تایبەت - 200 خاڵ', 'shop_item2': '👑 باجی VIP مانگ - 500 خاڵ', 'shop_item3': '🎁 هەدیەی نهێنی - 1000 خاڵ',
        'shop_buy': '🛒 کڕین', 'shop_bought': '✅ کڕدرا!', 'shop_no_points': '❌ خاڵت پێویست نییە!',
        'history_title': '📜 مێژووی چالاکیەکانت', 'history_empty': 'هیچ چالاکیەک تۆمار نەکراوە',
        'challenge_prompt': '👫 ID ی هاوڕێکەت بنووسە بۆ پێشبڕکێ:', 'challenge_sent': '✅ داواکاری پێشبڕکێ نێردرا!',
        'challenge_received': '👫 هاوڕێیەک داوای پێشبڕکێی لێکردی!',
        'qr_title': '📱 QR کۆدی لینکی بانگهێشتت', 'qr_desc': 'ئەم لینکە بنێرە بۆ هاوڕێکانت:',
        'tutorial_title': '📖 فێرکاری بۆتەکە', 'tutorial_text': '👋 بەخێربێیت بۆ یاکوزا ستۆر بۆت!\n\n1️⃣ لە بەشی 🎮 هاک و یاری، هاکەکان ببینە\n2️⃣ لە بەشی 🎁 خاڵ و هەدیە، خاڵ کۆبکەرەوە\n3️⃣ لە بەشی 🎲 گەیم و کاری، یاری بکە و ڕابواردنە\n4️⃣ لە بەشی ⚙️ ڕێکخستن، هەموو شتێک کۆنترۆڵ بکە\n\nسەرکەوتوو بیت! 🎉'
    },
    'ar': {
        'btn_ttt': '⭕ إكس أو', 'btn_memory': '🃏 لعبة الذاكرة', 'btn_speed': '⚡ نقر سريع',
        'btn_rank': '🏆 رتبتي', 'btn_shop': '🛒 متجر النقاط', 'btn_history': '📜 سجلي',
        'btn_challenge': '👫 تحدي صديق', 'btn_qr': '📱 رمز QR', 'btn_tutorial': '📖 دليل الاستخدام',
        'ttt_title': '⭕ إكس أو - دورك', 'ttt_win': '🎉 فزت! +30 نقطة', 'ttt_lose': '❌ فاز البوت!', 'ttt_draw': '🤝 تعادل!',
        'memory_title': '🃏 لعبة الذاكرة\n\nاختر بطاقتين متشابهتين!', 'memory_match': '✅ متطابقتان! +15 نقطة', 'memory_nomatch': '❌ غير متطابقتان!',
        'speed_title': '⚡ نقر سريع\n\nانقر أكبر عدد ممكن خلال 5 ثواني!', 'speed_click': '👆 انقر!', 'speed_result': '⚡ النتيجة:', 'speed_clicks': 'نقرة',
        'rank_bronze': '🥉 برونزي', 'rank_silver': '🥈 فضي', 'rank_gold': '🥇 ذهبي', 'rank_platinum': '💠 بلاتيني', 'rank_diamond': '💎 ماسي', 'rank_legend': '👑 أسطورة',
        'rank_title': '🏆 رتبتك', 'rank_progress': 'التقدم للرتبة القادمة',
        'shop_title': '🛒 متجر النقاط', 'shop_item1': '🎨 تيم ألوان خاص - 200 نقطة', 'shop_item2': '👑 شارة VIP شهر - 500 نقطة', 'shop_item3': '🎁 هدية سرية - 1000 نقطة',
        'shop_buy': '🛒 شراء', 'shop_bought': '✅ تم الشراء!', 'shop_no_points': '❌ نقاطك غير كافية!',
        'history_title': '📜 سجل نشاطاتك', 'history_empty': 'لا يوجد نشاط مسجل',
        'challenge_prompt': '👫 اكتب ID صديقك للتحدي:', 'challenge_sent': '✅ تم إرسال طلب التحدي!',
        'challenge_received': '👫 صديق طلب تحديك!',
        'qr_title': '📱 رمز QR لرابط دعوتك', 'qr_desc': 'أرسل هذا الرابط لأصدقائك:',
        'tutorial_title': '📖 دليل استخدام البوت', 'tutorial_text': '👋 مرحباً بك في بوت ياكوزا ستور!\n\n1️⃣ من قسم 🎮 هاك وألعاب، شاهد الهاكات\n2️⃣ من قسم 🎁 نقاط وهدايا، اجمع النقاط\n3️⃣ من قسم 🎲 ألعاب ونشاطات، العب واستمتع\n4️⃣ من قسم ⚙️ إعدادات، تحكم بكل شيء\n\nبالتوفيق! 🎉'
    },
    'en': {
        'btn_ttt': '⭕ Tic Tac Toe', 'btn_memory': '🃏 Memory Game', 'btn_speed': '⚡ Speed Click',
        'btn_rank': '🏆 My Rank', 'btn_shop': '🛒 Points Shop', 'btn_history': '📜 My History',
        'btn_challenge': '👫 Challenge Friend', 'btn_qr': '📱 QR Code', 'btn_tutorial': '📖 Tutorial',
        'ttt_title': '⭕ Tic Tac Toe - Your turn', 'ttt_win': '🎉 You won! +30 points', 'ttt_lose': '❌ Bot won!', 'ttt_draw': '🤝 Draw!',
        'memory_title': '🃏 Memory Game\n\nPick two matching cards!', 'memory_match': '✅ Match! +15 points', 'memory_nomatch': '❌ No match!',
        'speed_title': '⚡ Speed Click\n\nClick as much as possible in 5 seconds!', 'speed_click': '👆 Click!', 'speed_result': '⚡ Result:', 'speed_clicks': 'clicks',
        'rank_bronze': '🥉 Bronze', 'rank_silver': '🥈 Silver', 'rank_gold': '🥇 Gold', 'rank_platinum': '💠 Platinum', 'rank_diamond': '💎 Diamond', 'rank_legend': '👑 Legend',
        'rank_title': '🏆 Your Rank', 'rank_progress': 'Progress to next rank',
        'shop_title': '🛒 Points Shop', 'shop_item1': '🎨 Custom Color Theme - 200 points', 'shop_item2': '👑 VIP Badge Month - 500 points', 'shop_item3': '🎁 Secret Gift - 1000 points',
        'shop_buy': '🛒 Buy', 'shop_bought': '✅ Purchased!', 'shop_no_points': '❌ Not enough points!',
        'history_title': '📜 Your Activity History', 'history_empty': 'No activity recorded',
        'challenge_prompt': '👫 Type your friend\'s ID to challenge:', 'challenge_sent': '✅ Challenge request sent!',
        'challenge_received': '👫 A friend challenged you!',
        'qr_title': '📱 QR Code for your invite link', 'qr_desc': 'Send this link to your friends:',
        'tutorial_title': '📖 Bot Tutorial', 'tutorial_text': '👋 Welcome to Yakuza Store Bot!\n\n1️⃣ In 🎮 Hacks & Games section, view hacks\n2️⃣ In 🎁 Points & Gifts section, collect points\n3️⃣ In 🎲 Fun & Activities section, play and enjoy\n4️⃣ In ⚙️ Settings section, control everything\n\nGood luck! 🎉'
    }
}
for lang in T:
    T[lang].update(EXTRA_T3[lang])

def get_rank(uid, lang='ku'):
    pts = get_points(uid)
    if pts >= 2000: return T[lang]['rank_legend']
    elif pts >= 1000: return T[lang]['rank_diamond']
    elif pts >= 600: return T[lang]['rank_platinum']
    elif pts >= 300: return T[lang]['rank_gold']
    elif pts >= 100: return T[lang]['rank_silver']
    else: return T[lang]['rank_bronze']

def check_ttt_winner(board):
    wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for a,b,c in wins:
        if board[a] and board[a]==board[b]==board[c]:
            return board[a]
    if all(board): return 'draw'
    return None

def ttt_bot_move(board):
    empty = [i for i,v in enumerate(board) if not v]
    return random.choice(empty) if empty else None


RPG_T = {
    'ku': {
        'btn_universe': '🎪 دنیای یاکوزا', 'universe_title': '🎪 دنیای یاکوزا',
        'btn_create_char': '🎭 کاراکتەرم دروست بکە', 'btn_my_char': '👤 کاراکتەرەکەم', 'btn_battle': '⚔️ شەڕ لەگەڵ دوژمن',
        'btn_clan': '🏰 باڵکۆنی من', 'btn_trade': '💰 بازرگانی', 'btn_treasure': '🗺️ دۆزینەوەی گەنجینە',
        'char_choose_class': '🎭 پیشەیەک هەڵبژێرە:', 'class_hacker': '💻 هاکەر', 'class_gamer': '🎮 گەیمەر', 'class_warrior': '⚔️ جەنگاوەر',
        'char_created': '🎉 کاراکتەرەکەت دروست بوو!', 'char_level': '📈 ئاست', 'char_hp': '❤️ تەندروستی', 'char_class': '🎭 پیشە',
        'char_exists': '⚠️ کاراکتەرێکت هەیە پێشتر!', 'char_none': '❌ هێشتا کاراکتەرت نییە! دروستی بکە',
        'battle_title': '⚔️ شەڕ لەگەڵ دوژمن', 'battle_enemy': '👹 دوژمن دۆزرایەوە!', 'battle_win': '🎉 بردتیانەوە! +30 خاڵ و +1 ئاست',
        'battle_lose': '💀 شکستت خوارد! دووبارە هەوڵبدە', 'battle_attack': '⚔️ هێرش!',
        'clan_title': '🏰 باڵکۆنەکان', 'clan_create': '🏗️ باڵکۆنێک دروست بکە', 'clan_join': '➕ چوونە باڵکۆنێک', 'clan_my': '👥 باڵکۆنەکەم',
        'clan_create_prompt': '🏰 ناوی باڵکۆنەکەت بنووسە:', 'clan_created': '🎉 باڵکۆنەکەت دروست بوو!',
        'clan_none': '❌ هێشتا لە هیچ باڵکۆنێک نیت!', 'clan_members': '👥 ئەندامان',
        'trade_title': '💰 بازرگانی خاڵ', 'trade_prompt': '💰 ID ی کەسەکە و ژمارەی خاڵ بنووسە بۆ بازرگانی\n\nنموونە: 123456 50',
        'treasure_title': '🗺️ گەشتی گەنجینە', 'treasure_search': '🔍 بگەڕێ', 'treasure_found': '💎 گەنجینەیەکت دۆزیەوە! +',
        'treasure_empty': '😢 هیچ نەدۆزرایەوە، دووبارە هەوڵبدە!'
    },
    'ar': {
        'btn_universe': '🎪 عالم ياكوزا', 'universe_title': '🎪 عالم ياكوزا',
        'btn_create_char': '🎭 أنشئ شخصيتي', 'btn_my_char': '👤 شخصيتي', 'btn_battle': '⚔️ قاتل عدو',
        'btn_clan': '🏰 عشيرتي', 'btn_trade': '💰 تجارة', 'btn_treasure': '🗺️ ابحث عن كنز',
        'char_choose_class': '🎭 اختر مهنة:', 'class_hacker': '💻 هاكر', 'class_gamer': '🎮 لاعب', 'class_warrior': '⚔️ محارب',
        'char_created': '🎉 تم إنشاء شخصيتك!', 'char_level': '📈 المستوى', 'char_hp': '❤️ الصحة', 'char_class': '🎭 المهنة',
        'char_exists': '⚠️ لديك شخصية بالفعل!', 'char_none': '❌ ليس لديك شخصية بعد! أنشئها',
        'battle_title': '⚔️ قتال عدو', 'battle_enemy': '👹 تم العثور على عدو!', 'battle_win': '🎉 فزت! +30 نقطة و+1 مستوى',
        'battle_lose': '💀 خسرت! حاول مرة أخرى', 'battle_attack': '⚔️ هجوم!',
        'clan_title': '🏰 العشائر', 'clan_create': '🏗️ أنشئ عشيرة', 'clan_join': '➕ انضم لعشيرة', 'clan_my': '👥 عشيرتي',
        'clan_create_prompt': '🏰 اكتب اسم عشيرتك:', 'clan_created': '🎉 تم إنشاء عشيرتك!',
        'clan_none': '❌ لست في أي عشيرة بعد!', 'clan_members': '👥 الأعضاء',
        'trade_title': '💰 تجارة النقاط', 'trade_prompt': '💰 اكتب ID الشخص وعدد النقاط للتجارة\n\nمثال: 123456 50',
        'treasure_title': '🗺️ رحلة الكنز', 'treasure_search': '🔍 ابحث', 'treasure_found': '💎 وجدت كنزاً! +',
        'treasure_empty': '😢 لم تجد شيئاً، حاول مرة أخرى!'
    },
    'en': {
        'btn_universe': '🎪 Yakuza Universe', 'universe_title': '🎪 Yakuza Universe',
        'btn_create_char': '🎭 Create My Character', 'btn_my_char': '👤 My Character', 'btn_battle': '⚔️ Battle Enemy',
        'btn_clan': '🏰 My Clan', 'btn_trade': '💰 Trade', 'btn_treasure': '🗺️ Treasure Hunt',
        'char_choose_class': '🎭 Choose a class:', 'class_hacker': '💻 Hacker', 'class_gamer': '🎮 Gamer', 'class_warrior': '⚔️ Warrior',
        'char_created': '🎉 Your character was created!', 'char_level': '📈 Level', 'char_hp': '❤️ HP', 'char_class': '🎭 Class',
        'char_exists': '⚠️ You already have a character!', 'char_none': '❌ You don\'t have a character yet! Create one',
        'battle_title': '⚔️ Battle Enemy', 'battle_enemy': '👹 Enemy found!', 'battle_win': '🎉 You won! +30 points and +1 level',
        'battle_lose': '💀 You lost! Try again', 'battle_attack': '⚔️ Attack!',
        'clan_title': '🏰 Clans', 'clan_create': '🏗️ Create a Clan', 'clan_join': '➕ Join a Clan', 'clan_my': '👥 My Clan',
        'clan_create_prompt': '🏰 Type your clan\'s name:', 'clan_created': '🎉 Your clan was created!',
        'clan_none': '❌ You are not in any clan yet!', 'clan_members': '👥 Members',
        'trade_title': '💰 Points Trade', 'trade_prompt': '💰 Type person\'s ID and points to trade\n\nExample: 123456 50',
        'treasure_title': '🗺️ Treasure Hunt', 'treasure_search': '🔍 Search', 'treasure_found': '💎 You found treasure! +',
        'treasure_empty': '😢 Found nothing, try again!'
    }
}
for lang in T:
    T[lang].update(RPG_T[lang])


NEW_T = {
    'ku': {
        'btn_smart_search': '🎯 گەڕانی زیرەک', 'btn_squad': '👥 تیمەکەم', 'btn_ref_tree': '📈 دارەخۆشی بانگهێشت',
        'btn_update_track': '🔔 شوێنپێدانی نوێکردنەوە',
        'smart_search_prompt': '🎯 ناوی ئەپێک بنووسە، شتی گونجاو پێشنیار دەکەم:',
        'smart_search_result': '🎯 پێشنیارەکانم بۆت:',
        'squad_title': '👥 تیمی خۆت', 'squad_create': '🏗️ تیمێک دروست بکە', 'squad_join': '➕ چوونە تیمێک', 'squad_none': '❌ لە هیچ تیمێک نیت',
        'squad_create_prompt': '👥 ناوی تیمەکەت بنووسە:', 'squad_created': '🎉 تیمەکەت دروست بوو!',
        'squad_members': '👥 ئەندامان', 'squad_id_prompt': '➕ ناوی تیمی هاوڕێکەت بنووسە بۆ چوونە ناوی:',
        'squad_joined': '✅ چوویتە ناو تیمەکە!', 'squad_not_found': '❌ تیمەکە نەدۆزرایەوە!',
        'ref_tree_title': '📈 دارەخۆشی بانگهێشتی تۆ', 'ref_tree_direct': '👤 ڕاستەوخۆ بانگهێشتکراوان',
        'ref_tree_total': '🌳 کۆی گشتی لە هەموو ئاستەکان', 'ref_tree_empty': 'هێشتا کەست بانگهێشت نەکردووە',
        'update_track_title': '🔔 شوێنپێدانی نوێکردنەوە', 'update_track_desc': 'ئاگادارت دەکەمەوە کاتێک ئەپێک نوێ دەبێتەوە!',
        'update_track_added': '✅ زیاد کرا بۆ شوێنپێدان!'
    },
    'ar': {
        'btn_smart_search': '🎯 البحث الذكي', 'btn_squad': '👥 فريقي', 'btn_ref_tree': '📈 شجرة الدعوات',
        'btn_update_track': '🔔 تتبع التحديثات',
        'smart_search_prompt': '🎯 اكتب اسم تطبيق، سأقترح لك ما يناسبك:',
        'smart_search_result': '🎯 اقتراحاتي لك:',
        'squad_title': '👥 فريقك', 'squad_create': '🏗️ أنشئ فريق', 'squad_join': '➕ انضم لفريق', 'squad_none': '❌ لست في أي فريق',
        'squad_create_prompt': '👥 اكتب اسم فريقك:', 'squad_created': '🎉 تم إنشاء فريقك!',
        'squad_members': '👥 الأعضاء', 'squad_id_prompt': '➕ اكتب اسم فريق صديقك للانضمام:',
        'squad_joined': '✅ انضممت للفريق!', 'squad_not_found': '❌ الفريق غير موجود!',
        'ref_tree_title': '📈 شجرة دعواتك', 'ref_tree_direct': '👤 المدعوون مباشرة',
        'ref_tree_total': '🌳 المجموع الكلي لكل المستويات', 'ref_tree_empty': 'لم تدعُ أحداً بعد',
        'update_track_title': '🔔 تتبع التحديثات', 'update_track_desc': 'سأنبهك عندما يتم تحديث أي تطبيق!',
        'update_track_added': '✅ تمت الإضافة للتتبع!'
    },
    'en': {
        'btn_smart_search': '🎯 Smart Search', 'btn_squad': '👥 My Squad', 'btn_ref_tree': '📈 Referral Tree',
        'btn_update_track': '🔔 Update Tracker',
        'smart_search_prompt': '🎯 Type an app name, I\'ll suggest something similar:',
        'smart_search_result': '🎯 My suggestions for you:',
        'squad_title': '👥 Your Squad', 'squad_create': '🏗️ Create Squad', 'squad_join': '➕ Join Squad', 'squad_none': '❌ You are not in any squad',
        'squad_create_prompt': '👥 Type your squad name:', 'squad_created': '🎉 Your squad was created!',
        'squad_members': '👥 Members', 'squad_id_prompt': '➕ Type your friend\'s squad name to join:',
        'squad_joined': '✅ Joined the squad!', 'squad_not_found': '❌ Squad not found!',
        'ref_tree_title': '📈 Your Referral Tree', 'ref_tree_direct': '👤 Direct invites',
        'ref_tree_total': '🌳 Total across all levels', 'ref_tree_empty': 'You haven\'t invited anyone yet',
        'update_track_title': '🔔 Update Tracker', 'update_track_desc': 'I\'ll notify you when any app is updated!',
        'update_track_added': '✅ Added to tracking!'
    }
}
for lang in T:
    T[lang].update(NEW_T[lang])

app_names_db = ['PicsArt', 'Spotify', 'Instagram', 'YouTube', 'CapCut', 'Roblox', 'Minecraft', 'GTA', 'Free Fire', 'Candy Crush', 'InShot', 'SnapTube']

def smart_search_suggest(query):
    query_lower = query.lower()
    matches = [a for a in app_names_db if query_lower in a.lower() or a.lower() in query_lower]
    if not matches:
        matches = random.sample(app_names_db, 3)
    return matches[:3]

def get_lang(uid): return user_langs.get(uid, None)
def t(uid, key): return T[get_lang(uid) or 'ku'].get(key, '')
def add_stat(uid): user_stats[uid] = user_stats.get(uid, 0) + 1
def add_points(uid, pts): user_points[uid] = user_points.get(uid, 0) + pts
def get_points(uid): return user_points.get(uid, 0)

def get_vip_level(uid, lang='ku'):
    pts = get_points(uid)
    if pts >= 1000: return T[lang]['vip_diamond']
    elif pts >= 600: return T[lang]['vip_gold']
    elif pts >= 300: return T[lang]['vip_silver']
    elif pts >= 100: return T[lang]['vip_bronze']
    else: return T[lang]['vip_none']


def update_streak(uid):
    today = datetime.now().strftime('%Y-%m-%d')
    last = user_last_active.get(uid)
    if last != today:
        if last:
            from datetime import timedelta
            last_date = datetime.strptime(last, '%Y-%m-%d')
            if (datetime.now() - last_date).days == 1:
                user_streak[uid] = user_streak.get(uid, 0) + 1
            else:
                user_streak[uid] = 1
        else:
            user_streak[uid] = 1
        user_last_active[uid] = today
    return user_streak.get(uid, 0)

def check_achievements(uid, lang):
    unlocked = []
    clicks = user_stats.get(uid, 0)
    pts = user_points.get(uid, 0)
    refs = len(user_referrals.get(uid, []))
    streak = user_streak.get(uid, 0)
    if clicks >= 10: unlocked.append(T[lang]['ach_click10'])
    if clicks >= 50: unlocked.append(T[lang]['ach_click50'])
    if clicks >= 100: unlocked.append(T[lang]['ach_click100'])
    if pts >= 100: unlocked.append(T[lang]['ach_points100'])
    if refs >= 5: unlocked.append(T[lang]['ach_ref5'])
    if streak >= 7: unlocked.append(T[lang]['ach_streak7'])
    return unlocked

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

CAT_T = {
    'ku': {'cat_hack': '🎮 هاک و یاری', 'cat_gift': '🎁 خاڵ و هەدیە', 'cat_fun': '🎲 گەیم و کاری', 'cat_settings': '⚙️ ڕێکخستن'},
    'ar': {'cat_hack': '🎮 هاك وألعاب', 'cat_gift': '🎁 نقاط وهدايا', 'cat_fun': '🎲 ألعاب ونشاطات', 'cat_settings': '⚙️ إعدادات'},
    'en': {'cat_hack': '🎮 Hacks & Games', 'cat_gift': '🎁 Points & Gifts', 'cat_fun': '🎲 Fun & Activities', 'cat_settings': '⚙️ Settings'}
}
for lang in T:
    T[lang].update(CAT_T[lang])

def main_menu(uid):
    m = InlineKeyboardMarkup(row_width=2)
    m.add(InlineKeyboardButton(t(uid,'cat_hack'), callback_data="cat_hack"),
          InlineKeyboardButton(t(uid,'cat_gift'), callback_data="cat_gift"))
    m.add(InlineKeyboardButton(t(uid,'cat_fun'), callback_data="cat_fun"),
          InlineKeyboardButton(t(uid,'cat_settings'), callback_data="cat_settings"))
    m.add(InlineKeyboardButton(t(uid,'btn_universe'), callback_data="universe_menu"))
    m.add(InlineKeyboardButton(t(uid,'btn_store'), url="https://saadmzore238-arch.github.io/My.apps/"))
    m.add(InlineKeyboardButton(t(uid,'btn_channel'), url="https://t.me/YAKUZA_CEO3"))
    if uid == ADMIN_ID:
        m.add(InlineKeyboardButton(t(uid,'btn_admin'), callback_data="admin_panel"))
    return m

def cat_hack_menu(uid):
    m = InlineKeyboardMarkup(row_width=2)
    m.add(InlineKeyboardButton(t(uid,'btn_hack'), callback_data="get_latest_hack"),
          InlineKeyboardButton(t(uid,'btn_anti'), callback_data="anti_ban_info"))
    m.add(InlineKeyboardButton(t(uid,'btn_world'), callback_data="hacker_world"),
          InlineKeyboardButton(t(uid,'btn_game'), callback_data="random_game"))
    m.add(InlineKeyboardButton(t(uid,'btn_smart_search'), callback_data="smart_search"),
          InlineKeyboardButton(t(uid,'btn_update_track'), callback_data="update_track"))
    m.add(InlineKeyboardButton(t(uid,'btn_faq'), callback_data="faq"))
    m.add(InlineKeyboardButton(t(uid,'back'), callback_data="back_to_main"))
    return m

def cat_gift_menu(uid):
    m = InlineKeyboardMarkup(row_width=2)
    m.add(InlineKeyboardButton(t(uid,'btn_lucky'), callback_data="lucky"),
          InlineKeyboardButton(t(uid,'btn_daily'), callback_data="daily_gift"))
    m.add(InlineKeyboardButton(t(uid,'btn_code'), callback_data="gift_code"),
          InlineKeyboardButton(t(uid,'btn_points'), callback_data="my_points"))
    m.add(InlineKeyboardButton(t(uid,'btn_ref'), callback_data="invite_friend"),
          InlineKeyboardButton(t(uid,'btn_gift_pts'), callback_data="gift_points"))
    m.add(InlineKeyboardButton(t(uid,'btn_vip'), callback_data="vip_info"),
          InlineKeyboardButton(t(uid,'btn_shop'), callback_data="points_shop"))
    m.add(InlineKeyboardButton(t(uid,'back'), callback_data="back_to_main"))
    return m

def cat_fun_menu(uid):
    m = InlineKeyboardMarkup(row_width=2)
    m.add(InlineKeyboardButton(t(uid,'btn_quiz'), callback_data="quiz_start"),
          InlineKeyboardButton(t(uid,'btn_guess'), callback_data="guess_start"))
    m.add(InlineKeyboardButton(t(uid,'btn_wheel'), callback_data="wheel_spin"),
          InlineKeyboardButton(t(uid,'btn_dice'), callback_data="dice_roll"))
    m.add(InlineKeyboardButton(t(uid,'btn_rps'), callback_data="rps_start"),
          InlineKeyboardButton(t(uid,'btn_joke'), callback_data="tell_joke"))
    m.add(InlineKeyboardButton(t(uid,'btn_tip'), callback_data="daily_tip"),
          InlineKeyboardButton(t(uid,'btn_countdown'), callback_data="countdown"))
    m.add(InlineKeyboardButton(t(uid,'btn_ttt'), callback_data="ttt_start"),
          InlineKeyboardButton(t(uid,'btn_memory'), callback_data="memory_start"))
    m.add(InlineKeyboardButton(t(uid,'btn_speed'), callback_data="speed_start"),
          InlineKeyboardButton(t(uid,'btn_challenge'), callback_data="challenge_start"))
    m.add(InlineKeyboardButton(t(uid,'btn_achieve'), callback_data="my_achievements"),
          InlineKeyboardButton(t(uid,'btn_streak'), callback_data="my_streak"))
    m.add(InlineKeyboardButton(t(uid,'btn_lead'), callback_data="leaderboard"),
          InlineKeyboardButton(t(uid,'btn_weekly'), callback_data="weekly_contest"))
    m.add(InlineKeyboardButton(t(uid,'btn_rank'), callback_data="my_rank"),
          InlineKeyboardButton(t(uid,'btn_squad'), callback_data="squad_menu"))
    m.add(InlineKeyboardButton(t(uid,'back'), callback_data="back_to_main"))
    return m

def cat_settings_menu(uid):
    m = InlineKeyboardMarkup(row_width=2)
    m.add(InlineKeyboardButton(t(uid,'btn_stats'), callback_data="my_stats"),
          InlineKeyboardButton(t(uid,'btn_nickname'), callback_data="set_nickname"))
    m.add(InlineKeyboardButton(t(uid,'btn_fav'), callback_data="my_favorites"),
          InlineKeyboardButton(t(uid,'btn_lang'), callback_data="change_lang"))
    m.add(InlineKeyboardButton(t(uid,'btn_history'), callback_data="my_history"),
          InlineKeyboardButton(t(uid,'btn_qr'), callback_data="my_qr"))
    m.add(InlineKeyboardButton(t(uid,'btn_tutorial'), callback_data="tutorial"),
          InlineKeyboardButton(t(uid,'btn_report'), callback_data="report_issue"))
    m.add(InlineKeyboardButton(t(uid,'btn_ref_tree'), callback_data="ref_tree"))
    m.add(InlineKeyboardButton(t(uid,'back'), callback_data="back_to_main"))
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
    update_streak(uid)
    is_first = uid not in user_first_time
    if is_first:
        user_first_time[uid] = True

    args = message.text.split()
    if len(args) > 1 and args[1].startswith('ref'):
        try:
            ref_id = int(args[1].replace('ref', ''))
            if ref_id != uid and uid not in user_referrals.get(ref_id, []):
                if ref_id not in user_referrals: user_referrals[ref_id] = []
                user_referrals[ref_id].append(uid)
                add_points(ref_id, 25)
                try:
                    ref_lang = get_lang(ref_id) or 'ku'
                    bot.send_message(ref_id, T[ref_lang]['new_ref'])
                except: pass
        except: pass

    if get_lang(uid) is None:
        bot.send_message(message.chat.id, f"سڵاو {name} 👋\n\n" + T['ku']['select_lang'] + "\n" + T['ar']['select_lang'] + "\n" + T['en']['select_lang'], reply_markup=lang_select_markup())
    elif is_subscribed(uid):
        welcome_extra = f"\n\n{t(uid,'first_welcome')}" if is_first else ""
        bot.send_message(message.chat.id, f"{t(uid,'welcome')} {name} 🔥\n{t(uid,'bot_name')}{welcome_extra}", reply_markup=main_menu(uid))
    else:
        bot.send_message(message.chat.id, f"سڵاو {name} 👋\n\n{t(uid,'join_msg')}", reply_markup=check_sub_markup(uid))

@bot.message_handler(commands=['broadcast'])
def broadcast_cmd(message):
    if message.from_user.id == ADMIN_ID:
        awaiting_broadcast[message.from_user.id] = True
        bot.send_message(message.chat.id, t(message.from_user.id,'broadcast_prompt'))

@bot.message_handler(func=lambda m: True)
def handle_text(message):
    uid = message.from_user.id
    text = message.text.strip()

    # ── گەڕانی زیرەک ──
    if awaiting_broadcast.get(f"search_{uid}"):
        awaiting_broadcast[f"search_{uid}"] = False
        suggestions = smart_search_suggest(text)
        result_text = f"{t(uid,'smart_search_result')}\n\n" + "\n".join([f"📱 {s}" for s in suggestions])
        bot.send_message(message.chat.id, result_text)
        return

    # ── دروستکردنی تیم ──
    if awaiting_broadcast.get(f"squadcreate_{uid}"):
        awaiting_broadcast[f"squadcreate_{uid}"] = False
        user_squad[uid] = text
        if text not in squad_groups: squad_groups[text] = []
        squad_groups[text].append(uid)
        bot.send_message(message.chat.id, t(uid,'squad_created'))
        return

    # ── چوونە تیم ──
    if awaiting_broadcast.get(f"squadjoin_{uid}"):
        awaiting_broadcast[f"squadjoin_{uid}"] = False
        if text in squad_groups:
            user_squad[uid] = text
            squad_groups[text].append(uid)
            bot.send_message(message.chat.id, t(uid,'squad_joined'))
        else:
            bot.send_message(message.chat.id, t(uid,'squad_not_found'))
        return

    # ── دروستکردنی باڵکۆن ──
    if awaiting_broadcast.get(f"clan_{uid}"):
        awaiting_broadcast[f"clan_{uid}"] = False
        user_clans[uid] = text
        if text not in clan_members:
            clan_members[text] = []
        clan_members[text].append(uid)
        bot.send_message(message.chat.id, t(uid,'clan_created'))
        return

    # ── بازرگانی ──
    if awaiting_broadcast.get(f"trade_{uid}"):
        awaiting_broadcast[f"trade_{uid}"] = False
        try:
            parts = text.split()
            target_id, amount = int(parts[0]), int(parts[1])
            if get_points(uid) >= amount:
                user_points[uid] -= amount
                add_points(target_id, amount)
                bot.send_message(message.chat.id, "✅")
                try:
                    bot.send_message(target_id, f"💰 +{amount} 🪙")
                except: pass
            else:
                bot.send_message(message.chat.id, "❌")
        except:
            bot.send_message(message.chat.id, "❌")
        return

    # ── چالینج ──
    if awaiting_broadcast.get(f"challenge_{uid}"):
        awaiting_broadcast[f"challenge_{uid}"] = False
        try:
            target_id = int(text)
            bot.send_message(message.chat.id, t(uid,'challenge_sent'))
            try:
                target_lang = get_lang(target_id) or 'ku'
                bot.send_message(target_id, T[target_lang]['challenge_received'])
            except: pass
        except:
            bot.send_message(message.chat.id, "❌")
        return

    # ── نازناو ──
    if awaiting_broadcast.get(f"nick_{uid}"):
        awaiting_broadcast[f"nick_{uid}"] = False
        user_nickname[uid] = text
        bot.send_message(message.chat.id, f"{t(uid,'nickname_set')} {text}")
        return

    # ── ناردنی خاڵ ──
    if awaiting_broadcast.get(f"giftpts_{uid}"):
        awaiting_broadcast[f"giftpts_{uid}"] = False
        try:
            parts = text.split()
            target_id, amount = int(parts[0]), int(parts[1])
            if get_points(uid) >= amount:
                user_points[uid] -= amount
                add_points(target_id, amount)
                bot.send_message(message.chat.id, t(uid,'gift_pts_sent'))
                try:
                    target_lang = get_lang(target_id) or 'ku'
                    bot.send_message(target_id, T[target_lang]['gift_pts_received'] + f" +{amount} 🪙")
                except: pass
            else:
                bot.send_message(message.chat.id, "❌")
        except:
            bot.send_message(message.chat.id, "❌")
        return

    # ── ڕاپۆرت ──
    if awaiting_broadcast.get(f"report_{uid}"):
        awaiting_broadcast[f"report_{uid}"] = False
        try:
            bot.send_message(ADMIN_ID, f"⚠️ Report from {uid}:\n\n{text}")
        except: pass
        bot.send_message(message.chat.id, t(uid,'report_sent'))
        return

    # ── Broadcast ──
    if uid == ADMIN_ID and awaiting_broadcast.get(uid):
        awaiting_broadcast[uid] = False
        sent = 0
        for u in list(user_langs.keys()):
            try:
                bot.send_message(u, text)
                sent += 1
            except: pass
        bot.send_message(message.chat.id, f"{t(uid,'broadcast_sent')} ({sent})")
        return

    # ── دۆزینەوەی ژمارە ──
    if uid in guess_number:
        try:
            guess = int(text)
            target = guess_number[uid]
            if guess == target:
                add_points(uid, 20)
                del guess_number[uid]
                bot.send_message(message.chat.id, t(uid,'guess_correct'))
            elif guess < target:
                bot.send_message(message.chat.id, t(uid,'guess_hint_up'))
            else:
                bot.send_message(message.chat.id, t(uid,'guess_hint_down'))
        except:
            pass
        return

    text_upper = text.upper()
    if text_upper in gift_codes:
        lang = get_lang(uid) or 'ku'
        add_points(uid, code_points.get(text_upper, 0))
        bot.send_message(message.chat.id, gift_codes[text_upper][lang])
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

        elif call.data == "cat_hack":
            bot.edit_message_text(t(uid,'cat_hack'), cid, mid, reply_markup=cat_hack_menu(uid))
        elif call.data == "cat_gift":
            bot.edit_message_text(t(uid,'cat_gift'), cid, mid, reply_markup=cat_gift_menu(uid))
        elif call.data == "cat_fun":
            bot.edit_message_text(t(uid,'cat_fun'), cid, mid, reply_markup=cat_fun_menu(uid))
        elif call.data == "cat_settings":
            bot.edit_message_text(t(uid,'cat_settings'), cid, mid, reply_markup=cat_settings_menu(uid))

        # ── کیش کیش کیش ──
        elif call.data == "rps_start":
            mm = InlineKeyboardMarkup(row_width=3)
            mm.add(InlineKeyboardButton("✊", callback_data="rps_rock"),
                   InlineKeyboardButton("✋", callback_data="rps_paper"),
                   InlineKeyboardButton("✌️", callback_data="rps_scissors"))
            mm.add(InlineKeyboardButton(t(uid,'back'), callback_data="cat_fun"))
            bot.edit_message_text(f"{t(uid,'rps_title')}\n\n{t(uid,'rps_choose')}", cid, mid, reply_markup=mm)

        elif call.data.startswith("rps_") and call.data != "rps_start":
            choice = call.data.split("_")[1]
            choices = ['rock', 'paper', 'scissors']
            emojis = {'rock':'✊','paper':'✋','scissors':'✌️'}
            bot_choice = random.choice(choices)
            if choice == bot_choice:
                result = t(uid,'rps_draw')
            elif (choice=='rock' and bot_choice=='scissors') or (choice=='paper' and bot_choice=='rock') or (choice=='scissors' and bot_choice=='paper'):
                add_points(uid, 10)
                result = t(uid,'rps_win')
            else:
                result = t(uid,'rps_lose')
            mm = InlineKeyboardMarkup()
            mm.add(InlineKeyboardButton(t(uid,'btn_rps'), callback_data="rps_start"))
            mm.add(InlineKeyboardButton(t(uid,'back'), callback_data="cat_fun"))
            bot.edit_message_text(f"{t(uid,'rps_you')}: {emojis[choice]}\n{t(uid,'rps_bot')}: {emojis[bot_choice]}\n\n{result}", cid, mid, reply_markup=mm)

        # ── نکتە ──
        elif call.data == "tell_joke":
            lang = get_lang(uid) or 'ku'
            joke = random.choice(jokes[lang])
            bot.edit_message_text(f"{t(uid,'joke_title')}\n\n{joke}", cid, mid, reply_markup=back_btn(uid,"cat_fun"))

        # ── تیپی ڕۆژانە ──
        elif call.data == "daily_tip":
            lang = get_lang(uid) or 'ku'
            tip = random.choice(daily_tips[lang])
            bot.edit_message_text(f"{t(uid,'tip_title')}\n\n{tip}", cid, mid, reply_markup=back_btn(uid,"cat_fun"))

        # ── ژماردنەوە ──
        elif call.data == "countdown":
            bot.edit_message_text(f"{t(uid,'countdown_title')}\n\n{t(uid,'countdown_text')}", cid, mid, reply_markup=back_btn(uid,"cat_fun"))

        # ── Tic Tac Toe ──
        elif call.data == "ttt_start":
            tictactoe_games[uid] = [None]*9
            board = tictactoe_games[uid]
            mm = InlineKeyboardMarkup(row_width=3)
            for i in range(9):
                mm.add(InlineKeyboardButton(board[i] or "⬜", callback_data=f"ttt_{i}"))
            mm.add(InlineKeyboardButton(t(uid,'back'), callback_data="cat_fun"))
            bot.edit_message_text(t(uid,'ttt_title'), cid, mid, reply_markup=mm)

        elif call.data.startswith("ttt_") and call.data != "ttt_start":
            idx = int(call.data.split("_")[1])
            board = tictactoe_games.get(uid, [None]*9)
            if board[idx] is None:
                board[idx] = 'X'
                winner = check_ttt_winner(board)
                if not winner:
                    bot_idx = ttt_bot_move(board)
                    if bot_idx is not None:
                        board[bot_idx] = 'O'
                        winner = check_ttt_winner(board)
                tictactoe_games[uid] = board
                mm = InlineKeyboardMarkup(row_width=3)
                for i in range(9):
                    mm.add(InlineKeyboardButton(board[i] or "⬜", callback_data=f"ttt_{i}"))
                mm.add(InlineKeyboardButton(t(uid,'back'), callback_data="cat_fun"))
                if winner == 'X':
                    add_points(uid, 30)
                    bot.edit_message_text(t(uid,'ttt_win'), cid, mid, reply_markup=back_btn(uid,"cat_fun"))
                elif winner == 'O':
                    bot.edit_message_text(t(uid,'ttt_lose'), cid, mid, reply_markup=back_btn(uid,"cat_fun"))
                elif winner == 'draw':
                    bot.edit_message_text(t(uid,'ttt_draw'), cid, mid, reply_markup=back_btn(uid,"cat_fun"))
                else:
                    bot.edit_message_text(t(uid,'ttt_title'), cid, mid, reply_markup=mm)

        # ── یاریی مێمۆری ──
        elif call.data == "memory_start":
            emojis = ["🍎","🍎","🍌","🍌","🍇","🍇","🍒","🍒"]
            random.shuffle(emojis)
            memory_games[uid] = {'board': emojis, 'revealed': [False]*8, 'first': None}
            mm = InlineKeyboardMarkup(row_width=4)
            for i in range(8):
                mm.add(InlineKeyboardButton("❓", callback_data=f"mem_{i}"))
            mm.add(InlineKeyboardButton(t(uid,'back'), callback_data="cat_fun"))
            bot.edit_message_text(t(uid,'memory_title'), cid, mid, reply_markup=mm)

        elif call.data.startswith("mem_"):
            idx = int(call.data.split("_")[1])
            game = memory_games.get(uid)
            if game and not game['revealed'][idx]:
                if game['first'] is None:
                    game['first'] = idx
                    game['revealed'][idx] = True
                else:
                    first = game['first']
                    if game['board'][first] == game['board'][idx] and first != idx:
                        game['revealed'][idx] = True
                        add_points(uid, 15)
                        bot.answer_callback_query(call.id, t(uid,'memory_match'))
                    else:
                        bot.answer_callback_query(call.id, t(uid,'memory_nomatch'))
                        game['revealed'][first] = False
                    game['first'] = None
                mm = InlineKeyboardMarkup(row_width=4)
                for i in range(8):
                    label = game['board'][i] if game['revealed'][i] else "❓"
                    mm.add(InlineKeyboardButton(label, callback_data=f"mem_{i}"))
                mm.add(InlineKeyboardButton(t(uid,'back'), callback_data="cat_fun"))
                bot.edit_message_text(t(uid,'memory_title'), cid, mid, reply_markup=mm)

        # ── کلیکی خێرا ──
        elif call.data == "speed_start":
            import time
            speed_click_data[uid] = {'count': 0, 'start': time.time()}
            mm = InlineKeyboardMarkup()
            mm.add(InlineKeyboardButton(t(uid,'speed_click'), callback_data="speed_click"))
            mm.add(InlineKeyboardButton(t(uid,'back'), callback_data="cat_fun"))
            bot.edit_message_text(t(uid,'speed_title'), cid, mid, reply_markup=mm)

        elif call.data == "speed_click":
            import time
            data = speed_click_data.get(uid)
            if data:
                elapsed = time.time() - data['start']
                if elapsed <= 5:
                    data['count'] += 1
                    bot.answer_callback_query(call.id, f"👆 {data['count']}")
                else:
                    pts = data['count'] * 2
                    add_points(uid, pts)
                    mm = InlineKeyboardMarkup()
                    mm.add(InlineKeyboardButton(t(uid,'btn_speed'), callback_data="speed_start"))
                    mm.add(InlineKeyboardButton(t(uid,'back'), callback_data="cat_fun"))
                    bot.edit_message_text(f"{t(uid,'speed_result')} {data['count']} {t(uid,'speed_clicks')} = +{pts} 🪙", cid, mid, reply_markup=mm)
                    del speed_click_data[uid]

        # ── پلەی من ──
        elif call.data == "my_rank":
            lang = get_lang(uid) or 'ku'
            rank = get_rank(uid, lang)
            pts = get_points(uid)
            bot.edit_message_text(f"{t(uid,'rank_title')}\n\n{rank}\n\n🪙 {pts}", cid, mid, reply_markup=back_btn(uid,"cat_fun"))

        # ── فرۆشگای خاڵ ──
        elif call.data == "points_shop":
            mm = InlineKeyboardMarkup()
            mm.add(InlineKeyboardButton(t(uid,'shop_item1'), callback_data="buy_item1"))
            mm.add(InlineKeyboardButton(t(uid,'shop_item2'), callback_data="buy_item2"))
            mm.add(InlineKeyboardButton(t(uid,'shop_item3'), callback_data="buy_item3"))
            mm.add(InlineKeyboardButton(t(uid,'back'), callback_data="cat_gift"))
            bot.edit_message_text(t(uid,'shop_title'), cid, mid, reply_markup=mm)

        elif call.data.startswith("buy_item"):
            costs = {'buy_item1': 200, 'buy_item2': 500, 'buy_item3': 1000}
            cost = costs.get(call.data, 0)
            if get_points(uid) >= cost:
                user_points[uid] -= cost
                bot.answer_callback_query(call.id, t(uid,'shop_bought'), show_alert=True)
            else:
                bot.answer_callback_query(call.id, t(uid,'shop_no_points'), show_alert=True)

        # ── مێژووم ──
        elif call.data == "my_history":
            clicks = user_stats.get(uid, 0)
            pts = get_points(uid)
            streak = user_streak.get(uid, 0)
            text = f"{t(uid,'history_title')}\n\n🔢 {clicks} کلیک\n🪙 {pts} خاڵ\n🔥 {streak} ڕۆژ بەردەوام"
            bot.edit_message_text(text, cid, mid, reply_markup=back_btn(uid))

        # ── چالینج ──
        elif call.data == "challenge_start":
            mm = InlineKeyboardMarkup()
            mm.add(InlineKeyboardButton(t(uid,'back'), callback_data="cat_fun"))
            awaiting_broadcast[f"challenge_{uid}"] = True
            bot.edit_message_text(t(uid,'challenge_prompt'), cid, mid, reply_markup=mm)

        # ── QR ──
        elif call.data == "my_qr":
            bot_username = bot.get_me().username
            link = f"https://t.me/{bot_username}?start=ref{uid}"
            bot.edit_message_text(f"{t(uid,'qr_title')}\n\n{t(uid,'qr_desc')}\n{link}", cid, mid, reply_markup=back_btn(uid))

        # ── فێرکاری ──
        elif call.data == "tutorial":
            bot.edit_message_text(t(uid,'tutorial_text'), cid, mid, reply_markup=back_btn(uid))

        # ══════ دنیای یاکوزا ══════
        elif call.data == "universe_menu":
            mm = InlineKeyboardMarkup(row_width=2)
            mm.add(InlineKeyboardButton(t(uid,'btn_create_char'), callback_data="create_char"),
                   InlineKeyboardButton(t(uid,'btn_my_char'), callback_data="my_char"))
            mm.add(InlineKeyboardButton(t(uid,'btn_battle'), callback_data="battle_start"),
                   InlineKeyboardButton(t(uid,'btn_treasure'), callback_data="treasure_search"))
            mm.add(InlineKeyboardButton(t(uid,'btn_clan'), callback_data="clan_menu"),
                   InlineKeyboardButton(t(uid,'btn_trade'), callback_data="trade_start"))
            mm.add(InlineKeyboardButton(t(uid,'back'), callback_data="back_to_main"))
            bot.edit_message_text(t(uid,'universe_title'), cid, mid, reply_markup=mm)

        # ── دروستکردنی کاراکتەر ──
        elif call.data == "create_char":
            if uid in user_characters:
                bot.answer_callback_query(call.id, t(uid,'char_exists'), show_alert=True)
            else:
                mm = InlineKeyboardMarkup()
                mm.add(InlineKeyboardButton(t(uid,'class_hacker'), callback_data="class_hacker"))
                mm.add(InlineKeyboardButton(t(uid,'class_gamer'), callback_data="class_gamer"))
                mm.add(InlineKeyboardButton(t(uid,'class_warrior'), callback_data="class_warrior"))
                mm.add(InlineKeyboardButton(t(uid,'back'), callback_data="universe_menu"))
                bot.edit_message_text(t(uid,'char_choose_class'), cid, mid, reply_markup=mm)

        elif call.data.startswith("class_"):
            cls = call.data.split("_")[1]
            user_characters[uid] = {'class': cls, 'level': 1, 'hp': 100, 'name': name}
            bot.edit_message_text(t(uid,'char_created'), cid, mid, reply_markup=back_btn(uid,"universe_menu"))

        # ── کاراکتەرەکەم ──
        elif call.data == "my_char":
            char = user_characters.get(uid)
            if not char:
                bot.edit_message_text(t(uid,'char_none'), cid, mid, reply_markup=back_btn(uid,"universe_menu"))
            else:
                cls_name = t(uid, f"class_{char['class']}")
                text = f"👤 {char['name']}\n\n{t(uid,'char_class')}: {cls_name}\n{t(uid,'char_level')}: {char['level']}\n{t(uid,'char_hp')}: {char['hp']}"
                bot.edit_message_text(text, cid, mid, reply_markup=back_btn(uid,"universe_menu"))

        # ── شەڕ ──
        elif call.data == "battle_start":
            char = user_characters.get(uid)
            if not char:
                bot.answer_callback_query(call.id, t(uid,'char_none'), show_alert=True)
            else:
                mm = InlineKeyboardMarkup()
                mm.add(InlineKeyboardButton(t(uid,'battle_attack'), callback_data="battle_attack"))
                mm.add(InlineKeyboardButton(t(uid,'back'), callback_data="universe_menu"))
                bot.edit_message_text(f"{t(uid,'battle_title')}\n\n{t(uid,'battle_enemy')}", cid, mid, reply_markup=mm)

        elif call.data == "battle_attack":
            char = user_characters.get(uid)
            if char:
                if random.random() > 0.35:
                    add_points(uid, 30)
                    char['level'] += 1
                    bot.edit_message_text(t(uid,'battle_win'), cid, mid, reply_markup=back_btn(uid,"universe_menu"))
                else:
                    bot.edit_message_text(t(uid,'battle_lose'), cid, mid, reply_markup=back_btn(uid,"universe_menu"))

        # ── گەنجینە ──
        elif call.data == "treasure_search":
            char = user_characters.get(uid)
            if not char:
                bot.answer_callback_query(call.id, t(uid,'char_none'), show_alert=True)
            else:
                if random.random() > 0.4:
                    pts = random.choice([15, 25, 40, 60])
                    add_points(uid, pts)
                    text = f"{t(uid,'treasure_title')}\n\n{t(uid,'treasure_found')}{pts} 🪙"
                else:
                    text = f"{t(uid,'treasure_title')}\n\n{t(uid,'treasure_empty')}"
                mm = InlineKeyboardMarkup()
                mm.add(InlineKeyboardButton(t(uid,'treasure_search'), callback_data="treasure_search"))
                mm.add(InlineKeyboardButton(t(uid,'back'), callback_data="universe_menu"))
                bot.edit_message_text(text, cid, mid, reply_markup=mm)

        # ── باڵکۆن ──
        elif call.data == "clan_menu":
            mm = InlineKeyboardMarkup()
            mm.add(InlineKeyboardButton(t(uid,'clan_create'), callback_data="clan_create"))
            mm.add(InlineKeyboardButton(t(uid,'clan_my'), callback_data="clan_my"))
            mm.add(InlineKeyboardButton(t(uid,'back'), callback_data="universe_menu"))
            bot.edit_message_text(t(uid,'clan_title'), cid, mid, reply_markup=mm)

        elif call.data == "clan_create":
            mm = InlineKeyboardMarkup()
            mm.add(InlineKeyboardButton(t(uid,'back'), callback_data="clan_menu"))
            awaiting_broadcast[f"clan_{uid}"] = True
            bot.edit_message_text(t(uid,'clan_create_prompt'), cid, mid, reply_markup=mm)

        elif call.data == "clan_my":
            clan = user_clans.get(uid)
            if not clan:
                bot.edit_message_text(t(uid,'clan_none'), cid, mid, reply_markup=back_btn(uid,"clan_menu"))
            else:
                members = clan_members.get(clan, [])
                text = f"🏰 {clan}\n\n{t(uid,'clan_members')}: {len(members)}"
                bot.edit_message_text(text, cid, mid, reply_markup=back_btn(uid,"clan_menu"))

        # ── بازرگانی ──
        elif call.data == "trade_start":
            mm = InlineKeyboardMarkup()
            mm.add(InlineKeyboardButton(t(uid,'back'), callback_data="universe_menu"))
            awaiting_broadcast[f"trade_{uid}"] = True
            bot.edit_message_text(t(uid,'trade_prompt'), cid, mid, reply_markup=mm)

        # ── گەڕانی زیرەک ──
        elif call.data == "smart_search":
            mm = InlineKeyboardMarkup()
            mm.add(InlineKeyboardButton(t(uid,'back'), callback_data="cat_hack"))
            awaiting_broadcast[f"search_{uid}"] = True
            bot.edit_message_text(t(uid,'smart_search_prompt'), cid, mid, reply_markup=mm)

        # ── شوێنپێدانی نوێکردنەوە ──
        elif call.data == "update_track":
            app_updates_track[uid] = True
            mm = InlineKeyboardMarkup()
            mm.add(InlineKeyboardButton(t(uid,'btn_store'), url="https://saadmzore238-arch.github.io/My.apps/"))
            mm.add(InlineKeyboardButton(t(uid,'back'), callback_data="cat_hack"))
            bot.edit_message_text(f"{t(uid,'update_track_title')}\n\n{t(uid,'update_track_desc')}\n\n{t(uid,'update_track_added')}", cid, mid, reply_markup=mm)

        # ── تیم ──
        elif call.data == "squad_menu":
            squad = user_squad.get(uid)
            mm = InlineKeyboardMarkup()
            if squad:
                mm.add(InlineKeyboardButton(t(uid,'squad_members'), callback_data="squad_view"))
            else:
                mm.add(InlineKeyboardButton(t(uid,'squad_create'), callback_data="squad_create"))
                mm.add(InlineKeyboardButton(t(uid,'squad_join'), callback_data="squad_join"))
            mm.add(InlineKeyboardButton(t(uid,'back'), callback_data="cat_fun"))
            title = f"🏰 {squad}" if squad else t(uid,'squad_none')
            bot.edit_message_text(title, cid, mid, reply_markup=mm)

        elif call.data == "squad_create":
            mm = InlineKeyboardMarkup()
            mm.add(InlineKeyboardButton(t(uid,'back'), callback_data="squad_menu"))
            awaiting_broadcast[f"squadcreate_{uid}"] = True
            bot.edit_message_text(t(uid,'squad_create_prompt'), cid, mid, reply_markup=mm)

        elif call.data == "squad_join":
            mm = InlineKeyboardMarkup()
            mm.add(InlineKeyboardButton(t(uid,'back'), callback_data="squad_menu"))
            awaiting_broadcast[f"squadjoin_{uid}"] = True
            bot.edit_message_text(t(uid,'squad_id_prompt'), cid, mid, reply_markup=mm)

        elif call.data == "squad_view":
            squad = user_squad.get(uid)
            members = squad_groups.get(squad, [])
            text = f"🏰 {squad}\n\n{t(uid,'squad_members')}: {len(members)}"
            bot.edit_message_text(text, cid, mid, reply_markup=back_btn(uid,"squad_menu"))

        # ── دارەخۆشی بانگهێشت ──
        elif call.data == "ref_tree":
            direct = user_referrals.get(uid, [])
            total = len(direct)
            for r in direct:
                total += len(user_referrals.get(r, []))
            text = f"{t(uid,'ref_tree_title')}\n\n{t(uid,'ref_tree_direct')}: {len(direct)}\n{t(uid,'ref_tree_total')}: {total}"
            if not direct:
                text = f"{t(uid,'ref_tree_title')}\n\n{t(uid,'ref_tree_empty')}"
            bot.edit_message_text(text, cid, mid, reply_markup=back_btn(uid))






        # ── کوویز ──
        elif call.data == "quiz_start":
            lang = get_lang(uid) or 'ku'
            q = random.choice(quiz_questions[lang])
            mm = InlineKeyboardMarkup()
            for i, opt in enumerate(q['opts']):
                mm.add(InlineKeyboardButton(opt, callback_data=f"quiz_ans_{i}_{q['correct']}"))
            mm.add(InlineKeyboardButton(t(uid,'back'), callback_data="back_to_main"))
            bot.edit_message_text(f"{t(uid,'quiz_title')}\n\n❓ {q['q']}", cid, mid, reply_markup=mm)

        elif call.data.startswith("quiz_ans_"):
            parts = call.data.split("_")
            chosen, correct = int(parts[2]), int(parts[3])
            if chosen == correct:
                add_points(uid, 15)
                bot.answer_callback_query(call.id, t(uid,'quiz_correct'), show_alert=True)
            else:
                bot.answer_callback_query(call.id, t(uid,'quiz_wrong'), show_alert=True)
            bot.edit_message_text(f"{t(uid,'welcome')} {name} 🔥\n{t(uid,'bot_name')}", cid, mid, reply_markup=main_menu(uid))

        # ── دۆزینەوەی ژمارە ──
        elif call.data == "guess_start":
            guess_number[uid] = random.randint(1, 10)
            bot.edit_message_text(t(uid,'guess_title'), cid, mid, reply_markup=back_btn(uid))

        # ── VIP ──
        elif call.data == "vip_info":
            lang = get_lang(uid) or 'ku'
            level = get_vip_level(uid, lang)
            bot.edit_message_text(f"{t(uid,'vip_info')}{level}", cid, mid, reply_markup=back_btn(uid))

        # ── خاڵەکانم ──
        elif call.data == "my_points":
            mm = InlineKeyboardMarkup()
            mm.add(InlineKeyboardButton(t(uid,'points_earn'), callback_data="points_info"))
            mm.add(InlineKeyboardButton(t(uid,'back'), callback_data="back_to_main"))
            bot.edit_message_text(f"{t(uid,'points_title')} {name}\n\n🪙 {t(uid,'points_have')}: {get_points(uid)}", cid, mid, reply_markup=mm)

        elif call.data == "points_info":
            bot.edit_message_text(t(uid,'points_info'), cid, mid, reply_markup=back_btn(uid,"my_points"))

        # ── بانگهێشتی هاوڕێ ──
        elif call.data == "invite_friend":
            bot_username = bot.get_me().username
            link = f"https://t.me/{bot_username}?start=ref{uid}"
            count = len(user_referrals.get(uid, []))
            mm = InlineKeyboardMarkup()
            mm.add(InlineKeyboardButton(t(uid,'back'), callback_data="back_to_main"))
            bot.edit_message_text(f"{t(uid,'ref_title')}\n\n{t(uid,'ref_desc')}\n\n{t(uid,'ref_link')}:\n{link}\n\n{t(uid,'ref_count')}: {count}", cid, mid, reply_markup=mm)

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
            level = get_vip_level(uid, lang)
            bot.edit_message_text(f"{t(uid,'stats_title')} {name}\n\n{t(uid,'stats_clicks')}: {count}\n{t(uid,'stats_lang')}: {lang_name}\n🪙 {t(uid,'points_have')}: {get_points(uid)}\n{level}\n{t(uid,'stats_date')}: {datetime.now().strftime('%Y-%m-%d')}", cid, mid, reply_markup=back_btn(uid))

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
                pts = random.choice([10, 15, 20, 25, 30])
                add_points(uid, pts)
                lang = get_lang(uid) or 'ku'
                gifts_ku = [f"🎁 هاکی تایبەت: AIM KING! +{pts} خاڵ", f"💎 ئەمڕۆ بەختت باشە! +{pts} خاڵ", f"🔥 Ninja Engine تاقی بکەرەوە! +{pts} خاڵ", f"⚡ Snake هاک بەکاربهێنە! +{pts} خاڵ", f"🏆 ئەمڕۆ ڕۆژی تۆیە! +{pts} خاڵ"]
                gifts_ar = [f"🎁 هاك مميز: AIM KING! +{pts} نقطة", f"💎 حظك اليوم جيد! +{pts} نقطة", f"🔥 جرب Ninja Engine! +{pts} نقطة", f"⚡ استخدم Snake هاك! +{pts} نقطة", f"🏆 اليوم يومك! +{pts} نقطة"]
                gifts_en = [f"🎁 Special hack: AIM KING! +{pts} points", f"💎 Your luck is good today! +{pts} points", f"🔥 Try Ninja Engine! +{pts} points", f"⚡ Use Snake hack! +{pts} points", f"🏆 Today is your day! +{pts} points"]
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


        # ── چەرخی بەخت ──
        elif call.data == "wheel_spin":
            pts = random.choice([5, 10, 15, 20, 25, 30, 50])
            add_points(uid, pts)
            emojis = ["🍒","🍋","💎","⭐","7️⃣","🔔","🍀"]
            result = " ".join(random.choices(emojis, k=3))
            mm = InlineKeyboardMarkup()
            mm.add(InlineKeyboardButton(t(uid,'wheel_spin'), callback_data="wheel_spin"))
            mm.add(InlineKeyboardButton(t(uid,'back'), callback_data="back_to_main"))
            bot.edit_message_text(f"{t(uid,'wheel_title')}\n\n{result}\n\n{t(uid,'wheel_result')} +{pts} 🪙", cid, mid, reply_markup=mm)

        # ── تاسی بەخت ──
        elif call.data == "dice_roll":
            d1, d2 = random.randint(1,6), random.randint(1,6)
            pts = (d1 + d2) * 2
            add_points(uid, pts)
            dice_emoji = ["⚀","⚁","⚂","⚃","⚄","⚅"]
            mm = InlineKeyboardMarkup()
            mm.add(InlineKeyboardButton(t(uid,'dice_roll'), callback_data="dice_roll"))
            mm.add(InlineKeyboardButton(t(uid,'back'), callback_data="back_to_main"))
            bot.edit_message_text(f"{t(uid,'dice_title')}\n\n{dice_emoji[d1-1]} {dice_emoji[d2-1]}\n\n{t(uid,'dice_result')} {d1}+{d2} = +{pts} 🪙", cid, mid, reply_markup=mm)

        # ── باجەکان ──
        elif call.data == "my_achievements":
            lang = get_lang(uid) or 'ku'
            unlocked = check_achievements(uid, lang)
            all_ach = [T[lang]['ach_click10'], T[lang]['ach_click50'], T[lang]['ach_click100'], T[lang]['ach_points100'], T[lang]['ach_ref5'], T[lang]['ach_streak7']]
            text = f"{t(uid,'achieve_title')}\n\n"
            for a in all_ach:
                status = t(uid,'achieve_unlocked') if a in unlocked else t(uid,'achieve_locked')
                text += f"{a}: {status}\n"
            bot.edit_message_text(text, cid, mid, reply_markup=back_btn(uid))

        # ── بەردەوامی ──
        elif call.data == "my_streak":
            streak = update_streak(uid)
            bot.edit_message_text(f"{t(uid,'streak_title')}\n\n🔥 {streak} {t(uid,'streak_days')}\n\n{t(uid,'streak_today')}", cid, mid, reply_markup=back_btn(uid))

        # ── نازناو ──
        elif call.data == "set_nickname":
            mm = InlineKeyboardMarkup()
            mm.add(InlineKeyboardButton(t(uid,'back'), callback_data="back_to_main"))
            awaiting_broadcast[f"nick_{uid}"] = True
            bot.edit_message_text(t(uid,'nickname_prompt'), cid, mid, reply_markup=mm)

        # ── لیستی تایبەت ──
        elif call.data == "my_favorites":
            favs = user_favorites.get(uid, [])
            text = f"{t(uid,'fav_title')}\n\n"
            text += "\n".join(favs) if favs else t(uid,'fav_empty')
            bot.edit_message_text(text, cid, mid, reply_markup=back_btn(uid))

        # ── ناردنی خاڵ ──
        elif call.data == "gift_points":
            mm = InlineKeyboardMarkup()
            mm.add(InlineKeyboardButton(t(uid,'back'), callback_data="back_to_main"))
            awaiting_broadcast[f"giftpts_{uid}"] = True
            bot.edit_message_text(t(uid,'gift_pts_prompt'), cid, mid, reply_markup=mm)

        # ── پێشبڕکێی هەفتانە ──
        elif call.data == "weekly_contest":
            sorted_u = sorted(weekly_points.items(), key=lambda x: x[1], reverse=True)[:5]
            medals = ["🥇","🥈","🥉","4️⃣","5️⃣"]
            text = f"{t(uid,'weekly_title')}\n\n{t(uid,'weekly_desc')}\n\n"
            if sorted_u:
                for i,(u,p) in enumerate(sorted_u):
                    text += f"{medals[i]} #{i+1}: {p} 🪙\n"
            else:
                text += t(uid,'lead_empty')
            bot.edit_message_text(text, cid, mid, reply_markup=back_btn(uid))

        # ── ڕاپۆرت ──
        elif call.data == "report_issue":
            mm = InlineKeyboardMarkup()
            mm.add(InlineKeyboardButton(t(uid,'back'), callback_data="back_to_main"))
            awaiting_broadcast[f"report_{uid}"] = True
            bot.edit_message_text(t(uid,'report_prompt'), cid, mid, reply_markup=mm)

        # ── پانێڵی ئەدمین ──
        elif call.data == "admin_panel" and uid == ADMIN_ID:
            mm = InlineKeyboardMarkup()
            mm.add(InlineKeyboardButton(t(uid,'admin_users'), callback_data="admin_users"))
            mm.add(InlineKeyboardButton(t(uid,'admin_broadcast'), callback_data="admin_broadcast_btn"))
            mm.add(InlineKeyboardButton(t(uid,'back'), callback_data="back_to_main"))
            bot.edit_message_text(t(uid,'admin_panel'), cid, mid, reply_markup=mm)

        elif call.data == "admin_users" and uid == ADMIN_ID:
            total = len(user_langs)
            bot.edit_message_text(f"{t(uid,'admin_users')}: {total}", cid, mid, reply_markup=back_btn(uid,"admin_panel"))

        elif call.data == "admin_broadcast_btn" and uid == ADMIN_ID:
            awaiting_broadcast[uid] = True
            bot.edit_message_text(t(uid,'broadcast_prompt'), cid, mid, reply_markup=back_btn(uid,"admin_panel"))

    except Exception as e:
        print(f"Error: {e}")

print("✅ بۆتەکە دەستی پێکرد!")
bot.infinity_polling()
