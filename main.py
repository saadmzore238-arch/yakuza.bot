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
    m.add(InlineKeyboardButton(t(uid,'btn_points'), callback_data="my_points"),
          InlineKeyboardButton(t(uid,'btn_ref'), callback_data="invite_friend"))
    m.add(InlineKeyboardButton(t(uid,'btn_quiz'), callback_data="quiz_start"),
          InlineKeyboardButton(t(uid,'btn_guess'), callback_data="guess_start"))
    m.add(InlineKeyboardButton(t(uid,'btn_vip'), callback_data="vip_info"),
          InlineKeyboardButton(t(uid,'btn_lang'), callback_data="change_lang"))
    m.add(InlineKeyboardButton(t(uid,'btn_store'), url="https://saadmzore238-arch.github.io/My.apps/"))
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

    except Exception as e:
        print(f"Error: {e}")

print("✅ بۆتەکە دەستی پێکرد!")
bot.infinity_polling()
