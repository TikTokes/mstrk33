import time,requests,random,urllib3.request,datetime
from telegram import *
from telegram.ext import *
req = requests.session()
global timl,x2,IDDD,IDDDD,IDDDDD,token,timo,token_admin
tims = datetime.datetime.now()
timo = tims.strftime('%I:%M %p  [%x]')
IDDDDD="1372908153"
IDDD = "934949151"# ايدي المطور
IDDDD = "1242250697"#ايدي المطور الثانوي
token= "1747462591:AAFogmyGS9Xwayul-wmvddF66Ymf-WknuVU"
token_admin="1769548704:AAHBRyOLMLyT2Jg74vkReoYMugJokzB-AxA"#توكن بوت الادمن لاستلام رسايل الدخول
nep = datetime.datetime.now()
timl = nep.strftime('%I:%M %p')
MAIN, CHECKERTIKTOK, CHECKERTEL,CHECKERINSTA = range(4)
RETURNS, TIK, TEL, INSTA ,PROXY,FIVEINSTA,HELP,FOURTIK, FIVETIK, SIXTEL,FIVETEL = range(11)
back1=[[InlineKeyboardButton("GO BACK 🔙", callback_data=str(RETURNS))]]
back2=InlineKeyboardMarkup(back1)
print(f"{timo} -  Done Login No Errors")
def telegram5(update: Update, context: CallbackContext):
        query = update.callback_query
        count = 0
        remaining = 500
        available = 0
        notavailable = 0
        user = ""
        query.edit_message_text(
        text=f"CHECKER STARTED▶️\n\n[❓] Remaining: {remaining}\n\n[❇️] User: {user}\n\n[✅] Available: {available}\n\n[❌] Not Available: {notavailable}",
        )
        length = int(5)
        chars = "qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm12345678901234567890"
        try:
                while True:
                    time.sleep(1.2)
                    if count < 500:
                        count += 1
                        remaining -= 1
                        for user in range(1):
                            user = ""
                            for item in range(length):
                                user += random.choice(chars)
                        url = f"https://t.me/{user}"
                        send = req.get(url)

                        if send.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0:
                            available += 1
                            query.edit_message_text(
                                text=f"CHECKER STARTED▶️\n\n[❓] Remaining: {remaining}\n\n[❇️] User: {user}\n\n[✅] Available: {available}\n\n[❌] Not Available: {notavailable}",
                            )
                            query.message.reply_text(
                                text=f"NEW USER SIR [✅]\n\n[⥮] username : @{user}\n\n[⌛] Time:{timl}"
                            )
                        else:
                            notavailable += 1
                            query.edit_message_text(
                                text=f"CHECKER STARTED▶️\n\n[❓] Remaining: {remaining}\n\n[❇️] User: {user}\n\n[✅] Available: {available}\n\n[❌] Not Available: {notavailable}",
                            )
                        time.sleep(0.9)
                    else:
                        break
                query.edit_message_text(
                    text=f"[❇️] Done Checking {count} users\n[✅] Available: {available}\n[❌] Not Available: {notavailable}",reply_markup=back2)
                return MAIN
        except:
                pass
def telegram6(update: Update, _: CallbackContext):
    query = update.callback_query
    query.answer()
    count = 0
    remaining = 500
    available = 0
    notavailable = 0
    user = ""
    query.edit_message_text(
        text=f"CHECKER STARTED▶️\n\n[❓] Remaining: {remaining}\n\n[❇️] User: {user}\n\n[✅] Available: {available}\n\n[❌] Not Available: {notavailable}",
    )
    length = int(6)
    chars = "qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm12345678901234567890"
    try:
        while True:
            time.sleep(1.2)
            if count < 500:
                count += 1
                remaining -= 1
                for user in range(1):
                    user = ""
                    for item in range(length):
                        user += random.choice(chars)
                url = f"https://t.me/{user}"
                send = req.get(url)
                if send.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0:
                    available += 1
                    query.edit_message_text(
                         text=f"CHECKER STARTED▶️\n\n[❓] Remaining: {remaining}\n\n[❇️] User: {user}\n\n[✅] Available: {available}\n\n[❌] Not Available: {notavailable}",
                    )
                    query.message.reply_text(
                        text=f"NEW USER SIR [✅]\n\n[⥮] username : @{user}\n\n[⌛] Time:{timl}"
                    )
                else:
                    notavailable += 1
                    query.edit_message_text(
                        text=f"CHECKER STARTED▶️\n\n[❓] Remaining: {remaining}\n\n[❇️] User: {user}\n\n[✅] Available: {available}\n\n[❌] Not Available: {notavailable}",
                    )
                time.sleep(1)
            else:
                break
        query.edit_message_text(
            text=f"[❇️] Done Checking {count} users\n[✅] Available: {available}\n[❌] Not Available: {notavailable}", reply_markup=back2)
        return MAIN
    except:
        pass
def tiktok4(update: Update, _: CallbackContext):
    query = update.callback_query
    query.answer()
    count = 0
    remaining = 1000
    available = 0
    notavailable = 0
    user = ""
    query.edit_message_text(
        text=f"CHECKER STARTED▶️\n\n[❓] Remaining: {remaining}\n\n[❇️] User: {user}\n\n[✅] Available: {available}\n\n[❌] Not Available: {notavailable}",
    )
    length = int(4)
    chars = "qwertyuiopasdfghjklzxcvbnm1234567890_"
    try:
        while True:
            time.sleep(1.2)
            if count < 1000:
                count += 1
                remaining -= 1
                for user in range(1):
                    user = ""
                    for item in range(length):
                        user += random.choice(chars)
                urltik = f'https://www.tiktok.com/@{user}?'
                headertik = {
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'ar',
                    'cookie': 'bm_sz=D629F4942531777D6F7147A73605EDCB~YAAQhVQqLrT8ldN3AQAAvY4T+ArC4uvjnuxrV9pt2l0rKHkp1yqSFyVmqphzleo0kRsXlfI+NbB+LOM88S46yTNKJFjRIpTtPq9rKwsrBBAAkfcyq8+RZH7/Zf6msaZJtLNn/zxAtwnratRpub7m5xD5rufF7yyEZj5G5HxIutar/qCFiClDrwMZN4g39vBR; tt_webid_v2=6935404800675710465; tt_webid=6935404800675710465; tt_csrf_token=FHAWXV6vFZXlSM2eXSRS_6r1; MONITOR_WEB_ID=6935404800675710465; R6kq3TV7=AGOZE_h3AQAArT8QptQP5vh_zveCf-y5-BiUgB0w7IMZfUWedXYgJcIz57M8|1|0|75dd6b518f206372e6d404294a187c94b8126b35; s_v_web_id=verify_kltf64da_CijHZlfi_FdX3_4WE8_9Wwj_IAzVIICoeMBw; csrf_session_id=b2c399a35aae464682b040c14d913de2; bm_mi=DA047E87F2170B8EAEED36DFA89B7EEF~bFZTXUHt/x7P3I0BVhrEb4Td9L8oZ2GpyXZfW+xchO9i3D+JVDz88ASSnmIDwoAj9eNBEr2CRBfBybeh1gzxhUQkMpaXPauZmHFnxobirm+t2tUztvSHjRe7wVmEAzher5o6mgZFo3yICvGZj7Gl0DyAKf9IiMHUCT+P8WchaRo1zn2Tw+i7zcYmVNPFfKCWvBcFurSr7yHOl1W8DBZeM4NciHkWUQ4ZfRSnka5nPBc31710HS6gQL31mYIk5MCC2YzSf89SGSJodJGAkp1fZA==; bm_sv=7C1373BFC9FD4E0464B305E04E391F85~zYvKe8AvrP//Bh3yGBkN9hPkGyzM7JmwI5oyhbcxUHmMaMVX7A54ASSE97V9odLFyKW4B+RTI+2G3FqAeKElYXB+bw5DGu2vwRq89tI2ByGHuHWfJNmJPt+MLaUA1zVjxulAySr/HmXVp82syg2Hct0OfKH5FotWYANjWbWlwVU=; ak_bmsc=546A35303DC5B1DC24F699698FF233DC2E2A54854E2B0000EF813F605E1F4B1A~plMbX0Ui2pNYPSS/i1qPeHNc2xCUddsUFoAOF7Gbmm02GwXrVhn+fZfkeLsnlVZk33Fr4MD6SaesEjx/FclzePXXzOhSiJQ2GdQ996OpIB8lX+kjgVtkeQBXxQ139Neumt8jckA7jT81sgEzIDOZmLO6/KSDSaK95vwDjYEALYND6n9oYpmykVu2KGQYzRg6WueWyO0OrXSINNYmdYO7SF8ktYdO0didVcLX8JwAsFOIli2c6Ou6lhvuvoQeJClQQg; _abck=16220A303EE334985E7B40A39E10EC7F~0~YAAQhVQqLgT9ldN3AQAAwyUV+AUdqGmQv3CIqQnIyXwZFxf1lLyDf3M0i4kSrb/oGfOh9haoEWo2QxMzarNFIHPVzvja0C0ozETE+OS5CBaAx9+79ehyau7EX/wo3QgpVs1CS4v3sh0hclzVhl5LlwXtkCE3e3RCdvbNHXJiBpRf/+MD9HGuPlG1Ns83Auxj/eN8lMXLP3lQng/5xGgcDwXlNWO97iimgzB7FFhMa8cvLh5+7ua4P5HQ3T6O2WJAZZHsqK58z/u1W8NjeSUXh0dqrerPIc10L2hIcOpo6dGkFdG/SX/n9oqWpS4O8A3V640cN3rXoCb9JQFJZBrdRV/qJcpLt2ZdHby+/Igbtq1TFf6CD55L6DCvH8Q1pb1qA8z2zv9Rx1xyiXTnsYwY/YxCqyQrMPvK~-1~||-1||~-1',
                    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'none',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36'
                }
                send = req.get(urltik, headers=headertik)
                if send.status_code == 404:
                    available += 1
                    query.edit_message_text(
                        text=f"CHECKER STARTED▶️\n\n[❓] Remaining: {remaining}\n\n[❇️] User: {user}\n\n[✅] Available: {available}\n\n[❌] Not Available: {notavailable}",
                    )
                    query.message.reply_text(
                        text=f"NEW USER SIR [✅]\n\n[⥮] username : {user}\n\n[⌛] Time:{timl}"
                    )
                else:
                    notavailable += 1
                    query.edit_message_text(
                        text=f"CHECKER STARTED▶️\n\n[❓] Remaining: {remaining}\n\n[❇️] User: {user}\n\n[✅] Available: {available}\n\n[❌] Not Available: {notavailable}",
                    )
                time.sleep(1)
            else:
                break
        query.edit_message_text(
            text=f"Done Checking {count} Users.\nAvailable: {available}\n[❌] Not Available: {notavailable}",reply_markup=back2 )
        return MAIN
    except:
        pass
def tiktok5(update: Update, _: CallbackContext):
    query = update.callback_query
    query.answer()
    count = 0
    remaining = 1000
    available = 0
    notavailable = 0
    user = ""
    query.edit_message_text(
        text=f"CHECKER STARTED▶️\n\n[❓] Remaining: {remaining}\n\n[❇️] User: {user}\n\n[✅] Available: {available}\n\n[❌] Not Available: {notavailable}",
    )
    length = int(5)
    chars = "qwertyuiopasdfghjklzxcvbnm1234567890_"
    try:
        while True:
            time.sleep(1.2)
            if count < 1000:
                count += 1
                remaining -= 1
                for user in range(1):
                    user = ""
                    for item in range(length):
                        user += random.choice(chars)
                urltik = f'https://www.tiktok.com/@{user}?'
                headertik = {
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'ar',
                    'cookie': 'bm_sz=D629F4942531777D6F7147A73605EDCB~YAAQhVQqLrT8ldN3AQAAvY4T+ArC4uvjnuxrV9pt2l0rKHkp1yqSFyVmqphzleo0kRsXlfI+NbB+LOM88S46yTNKJFjRIpTtPq9rKwsrBBAAkfcyq8+RZH7/Zf6msaZJtLNn/zxAtwnratRpub7m5xD5rufF7yyEZj5G5HxIutar/qCFiClDrwMZN4g39vBR; tt_webid_v2=6935404800675710465; tt_webid=6935404800675710465; tt_csrf_token=FHAWXV6vFZXlSM2eXSRS_6r1; MONITOR_WEB_ID=6935404800675710465; R6kq3TV7=AGOZE_h3AQAArT8QptQP5vh_zveCf-y5-BiUgB0w7IMZfUWedXYgJcIz57M8|1|0|75dd6b518f206372e6d404294a187c94b8126b35; s_v_web_id=verify_kltf64da_CijHZlfi_FdX3_4WE8_9Wwj_IAzVIICoeMBw; csrf_session_id=b2c399a35aae464682b040c14d913de2; bm_mi=DA047E87F2170B8EAEED36DFA89B7EEF~bFZTXUHt/x7P3I0BVhrEb4Td9L8oZ2GpyXZfW+xchO9i3D+JVDz88ASSnmIDwoAj9eNBEr2CRBfBybeh1gzxhUQkMpaXPauZmHFnxobirm+t2tUztvSHjRe7wVmEAzher5o6mgZFo3yICvGZj7Gl0DyAKf9IiMHUCT+P8WchaRo1zn2Tw+i7zcYmVNPFfKCWvBcFurSr7yHOl1W8DBZeM4NciHkWUQ4ZfRSnka5nPBc31710HS6gQL31mYIk5MCC2YzSf89SGSJodJGAkp1fZA==; bm_sv=7C1373BFC9FD4E0464B305E04E391F85~zYvKe8AvrP//Bh3yGBkN9hPkGyzM7JmwI5oyhbcxUHmMaMVX7A54ASSE97V9odLFyKW4B+RTI+2G3FqAeKElYXB+bw5DGu2vwRq89tI2ByGHuHWfJNmJPt+MLaUA1zVjxulAySr/HmXVp82syg2Hct0OfKH5FotWYANjWbWlwVU=; ak_bmsc=546A35303DC5B1DC24F699698FF233DC2E2A54854E2B0000EF813F605E1F4B1A~plMbX0Ui2pNYPSS/i1qPeHNc2xCUddsUFoAOF7Gbmm02GwXrVhn+fZfkeLsnlVZk33Fr4MD6SaesEjx/FclzePXXzOhSiJQ2GdQ996OpIB8lX+kjgVtkeQBXxQ139Neumt8jckA7jT81sgEzIDOZmLO6/KSDSaK95vwDjYEALYND6n9oYpmykVu2KGQYzRg6WueWyO0OrXSINNYmdYO7SF8ktYdO0didVcLX8JwAsFOIli2c6Ou6lhvuvoQeJClQQg; _abck=16220A303EE334985E7B40A39E10EC7F~0~YAAQhVQqLgT9ldN3AQAAwyUV+AUdqGmQv3CIqQnIyXwZFxf1lLyDf3M0i4kSrb/oGfOh9haoEWo2QxMzarNFIHPVzvja0C0ozETE+OS5CBaAx9+79ehyau7EX/wo3QgpVs1CS4v3sh0hclzVhl5LlwXtkCE3e3RCdvbNHXJiBpRf/+MD9HGuPlG1Ns83Auxj/eN8lMXLP3lQng/5xGgcDwXlNWO97iimgzB7FFhMa8cvLh5+7ua4P5HQ3T6O2WJAZZHsqK58z/u1W8NjeSUXh0dqrerPIc10L2hIcOpo6dGkFdG/SX/n9oqWpS4O8A3V640cN3rXoCb9JQFJZBrdRV/qJcpLt2ZdHby+/Igbtq1TFf6CD55L6DCvH8Q1pb1qA8z2zv9Rx1xyiXTnsYwY/YxCqyQrMPvK~-1~||-1||~-1',
                    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'none',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36'
                }
                send = req.get(urltik, headers=headertik)
                if send.status_code == 404:
                    available += 1
                    query.edit_message_text(
                        text=f"CHECKER STARTED▶️\n\n[❓] Remaining: {remaining}\n\n[❇️] User: {user}\n\n[✅] Available: {available}\n\n[❌] Not Available: {notavailable}",
                    )
                    query.message.reply_text(
                        text=f"NEW USER SIR [✅]\n\n[⥮] username : {user}\n\n[⌛] Time:{timl}"
                    )
                else:
                    notavailable += 1
                    query.edit_message_text(
                        text=f"CHECKER STARTED▶️\n\n[❓] Remaining: {remaining}\n\n[❇️] User: {user}\n\n[✅] Available: {available}\n\n[❌] Not Available: {notavailable}",
                    )
                time.sleep(1)
            else:
                break
        query.edit_message_text(
            text=f"[❇️] Done Checking {count} users\n[✅] Available: {available}\n[❌] Not Available: {notavailable}",reply_markup=back2)
        return MAIN
    except:
        pass
def insta5(update: Update, _: CallbackContext):
    query = update.callback_query
    query.answer()
    count = 0
    remaining = 1000
    available = 0
    notavailable = 0
    user = ""
    query.edit_message_text(
        text=f"CHECKER STARTED▶️\n\n[❓] Remaining: {remaining}\n\n[❇️] User: {user}\n\n[✅] Available: {available}\n\n[❌] Not Available: {notavailable}",
    )
    length = int(5)
    chars = "qwertyuiopasdfghjklzxcvbnm1234567890_"
    while True:
        if count < 1000:
            count += 1
            remaining -= 1
            for user in range(1):
                user = ""
                for item in range(length):
                    user += random.choice(chars)
            urlinsta = f'https://www.instagram.com/{user}'
            headerinsta = {
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
                'cache-control': 'max-age=0',
                'sec-ch-ua': '"Google Chrome";v="89","Chromium";v="89", ";Not A Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
            }
            send = req.get(urlinsta, headers=headerinsta)
            if send.status_code == 404:
                available += 1
                query.edit_message_text(
                    text=f"CHECKER STARTED▶️\n\n[❓] Remaining: {remaining}\n\n[❇️] User: {user}\n\n[✅] Available: {available}\n\n[❌] Not Available: {notavailable}",
                )
                query.message.reply_text(
                    text=f"NEW USER SIR [✅]\n\n[⥮] username : {user}\n\n[⌛] Time:{timl}"
                )
            else:
                notavailable += 1
                query.edit_message_text(
                    text=f"CHECKER STARTED▶️\n\n[❓] Remaining: {remaining}\n\n[❇️] User: {user}\n\n[✅] Available: {available}\n\n[❌] Not Available: {notavailable}",
                )
            time.sleep(1)
        else:
            break
    query.edit_message_text(
        text=f"[❇️] Done Checking {count} users\n[✅] Available: {available}\n[❌] Not Available: {notavailable}",reply_markup=back2)
    return MAIN
def start(update: Update,context: CallbackContext):
    global user,pppppp
    user = str(update.message.from_user.username).upper()
    Keyboard = [
        [InlineKeyboardButton("📲 Share", switch_inline_query_current_chat="")],
        [InlineKeyboardButton("⛏ Bot Channel", url='https://t.me/TweakPY'),
         InlineKeyboardButton("🔭 𝙳𝙴𝚅", url='https://t.me/Filza2')],
        [InlineKeyboardButton("📰 TELEGRAM CHEACKER", callback_data=str(TEL))],
        [InlineKeyboardButton("🎵 TIKTOK CHEACKER", callback_data=str(TIK))],
        [InlineKeyboardButton("💡 INSTAGRAM CHEACKER", callback_data=str(INSTA))],
        [InlineKeyboardButton("🅿️ PROXY", callback_data=str(PROXY)),InlineKeyboardButton("❔ HELP", callback_data=str(HELP))],
        ]
    reply_markup = InlineKeyboardMarkup(Keyboard)
    name = update.message.from_user.first_name
    idd = update.message.chat_id
    ID = str(idd)
    url_url_user=f"tg://user_id?={ID}"
    sosoa = f'𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄: {name}\n𝐈𝐃: {ID}\n𝐔𝐒𝐄𝐑 𝐔𝐑𝐋: {url_url_user}\n𝐓𝐈𝐌𝐄: {timo}'
    tadk = (f'https://api.telegram.org/bot{token_admin}/sendMessage?chat_id={IDDD}&text={sosoa}')
    if IDDD in ID:
        update.message.reply_text(
            text=f""" اهلا عزيزي المطور منور البوت قلبي ✪ """,
            reply_markup=reply_markup
        )
    elif IDDDD in ID:
        update.message.reply_text(
            text=f""" اهلا عزيزي المطور منور البوت قلبي ✪ """,
            reply_markup=reply_markup
        )
    elif "-" in ID:
        update.message.reply_text(text=
"""عذرا البوت لايعمل بالمجموعات!
Sorry, the bot does not work 
in groups!
@TweakPY
""")
    elif IDDDDD == ID:
        update.message.reply_text(
            text=f"""
📅 🆃🅸🅼🅴:{timo}

WELCOME BOOS {name} ♥️️

Check 🚸 & Proxy Download 🌐

رجاء اضغط زر الهيلب قبل بدء الاستخدام 🚷
""",
            reply_markup=reply_markup
            )
        pppppp = requests.post(tadk)
    elif ID == "958306236":
        update.message.reply_text(text=f"""عذرا البوت لايخدم الحيوانات روح سوي تخطي كابتشا وتعال""")
        pppppp = requests.post(tadk)
    elif ID == "1626966367":
        update.message.reply_text(text=f"""شتدور سرقه جديده؟ هههههه وضعك صعب""")
        pppppp = requests.post(tadk)
    else:
        pass
    return MAIN
def returns(update: Update, _: CallbackContext):
    query = update.callback_query
    query.answer()
    Keyboard = [
        [InlineKeyboardButton("📲 Share", switch_inline_query_current_chat="")],
        [InlineKeyboardButton("⛏ Bot Channel", url='https://t.me/TweakPY'),
         InlineKeyboardButton("🔭 𝙳𝙴𝚅", url='https://t.me/Filza2')],
        [InlineKeyboardButton("📰 TELEGRAM CHEACKER", callback_data=str(TEL))],
        [InlineKeyboardButton("🎵 TIKTOK CHEACKER", callback_data=str(TIK))],
        [InlineKeyboardButton("💡 INSTAGRAM CHEACKER", callback_data=str(INSTA))],
        [InlineKeyboardButton("🅿️ PROXY", callback_data=str(PROXY)),
         InlineKeyboardButton("❔ HELP", callback_data=str(HELP))],
    ]
    reply_markup = InlineKeyboardMarkup(Keyboard)
    query.edit_message_text(
        text=f"""
📅 🆃🅸🅼🅴:{timo}

WELCOME BOOS ♥️️

Check 🚸 & Proxy Download 🌐

رجاء اضغط زر الهيلب قبل بدء الاستخدام 🚷
""",

            reply_markup=reply_markup
        )
    return MAIN
def tiktok(update: Update, _: CallbackContext):
    query = update.callback_query
    try:
        Keyboard = [
            [InlineKeyboardButton("4 letters", callback_data=str(FOURTIK))],
            [InlineKeyboardButton("5 letters", callback_data=str(FIVETIK))],
            [InlineKeyboardButton("GO BACK 🔙", callback_data=str(RETURNS))]
        ]
        reply_markup = InlineKeyboardMarkup(Keyboard)
        time.sleep(1.2)
        query.edit_message_text(
            text="Choose From The Allowed Lengths.\nThe Bot Will Automatically Check ( 1000 Users )",
            reply_markup=reply_markup
        )
        return CHECKERTIKTOK
    except:
        pass
def telegrams(update: Update, _: CallbackContext):
    query = update.callback_query
    try:
        Keyboard = [
            [InlineKeyboardButton("5 letters", callback_data=str(FIVETEL))],
            [InlineKeyboardButton("6 letters", callback_data=str(SIXTEL))],
            [InlineKeyboardButton("GO BACK 🔙", callback_data=str(RETURNS))]
        ]
        reply_markup = InlineKeyboardMarkup(Keyboard)
        query.edit_message_text(
            text="Choose From The Allowed Lengths.\nThe Bot Will Automatically Check ( 500 Users )",
            reply_markup=reply_markup
        )
        return CHECKERTEL
    except:
        pass
def instas(update: Update, _: CallbackContext):
    query = update.callback_query
    query.answer()
    Keyboard = [
        [InlineKeyboardButton("5 letters", callback_data=str(FIVEINSTA))],
        [InlineKeyboardButton("GO BACK 🔙", callback_data=str(RETURNS))]
    ]
    reply_markup = InlineKeyboardMarkup(Keyboard)
    query.edit_message_text(
        text="Choose From The Allowed Lengths.\nThe Bot Will Automatically Check ( 1000 Users )",
        reply_markup=reply_markup
    )
    return CHECKERINSTA
def proxy(update: Update, _: CallbackContext):
    query = update.callback_query
    query.answer()
    url = 'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt'
    headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9',
                'if-none-match': 'W/"11cd2e7c01d9ff7aa4333364a5b0e80aeb825b0641fa17e4e5980b32bdf7be6d"',
                'referer': 'https://github.com/ShiftyTR/Proxy-List/blob/master/https.txt',
                'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'cross-site',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.3'}
    re = requests.get(url, headers=headers).text
    query.edit_message_text(text=re,reply_markup=back2)
    return main
def help(update,context):
    tef="""THIS IS PAID BOT BY FILZA AND NO ONE CAN SELL THIS BOT EXCEPT @Filza2 - @TweakPY\n\n
اهلا صديقي البوت مخصص للتشيكرات وقريبا المزيد

حسناً اظن بانك تعلم ما وظيفة البوت الان وماذا يفعل لذالك ارجوا منك عدم اللعب به 
وعمل سبام وتثقيل على السيرفر علفاضي 😉

هنالك حكمه تقول خلك مثل الوايل ترو لاتوقف فحص

استمتع ☑️

ملاحظة  لا احلل من يبيعه..
/start """
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=tef, reply_markup=back2)
def main() -> None:
    updater = Updater(token, use_context=True)
    dispatcher = updater.dispatcher
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start,run_async=True)],
        states={
            MAIN: [
                CallbackQueryHandler(returns, pattern='^' + str(RETURNS) + '$',run_async=True),
                CallbackQueryHandler(tiktok, pattern='^' + str(TIK) + '$'),
                CallbackQueryHandler(telegrams, pattern='^' + str(TEL) + '$',run_async=True),
                CallbackQueryHandler(instas, pattern='^' + str(INSTA) + '$',run_async=True),
                CallbackQueryHandler(proxy, pattern='^' + str(PROXY) + '$', run_async=True),
                CallbackQueryHandler(help, pattern='^' + str(HELP) + '$', run_async=True),
            ],
            CHECKERTIKTOK: [
                CallbackQueryHandler(tiktok4, pattern='^' + str(FOURTIK) + '$',run_async=True),
                CallbackQueryHandler(tiktok5, pattern='^' + str(FIVETIK) + '$',run_async=True),
                CallbackQueryHandler(returns, pattern='^' + str(RETURNS) + '$',run_async=True),
            ],
            CHECKERTEL: [
                CallbackQueryHandler(telegram5, pattern='^' + str(FIVETEL) + '$',run_async=True),
                CallbackQueryHandler(telegram6, pattern='^' + str(SIXTEL) + '$',run_async=True),
                CallbackQueryHandler(returns, pattern='^' + str(RETURNS) + '$',run_async=True),
            ],
            CHECKERINSTA:[
                CallbackQueryHandler(insta5, pattern='^' + str(FIVEINSTA) + '$',run_async=True),
                CallbackQueryHandler(returns, pattern='^' + str(RETURNS) + '$',run_async=True),
            ]

        },
        fallbacks=[CommandHandler('start', start,run_async=True)],
    )
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, tiktok,run_async=True))
    dispatcher.add_handler(conv_handler)
    updater.start_polling()
    updater.idle()
if __name__ == '__main__':
    main()
