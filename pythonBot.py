from requests.structures import CaseInsensitiveDict
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
import requests
import datetime
import telegramcalendar
import cx_Oracle

TRUSTED_CHATS = [your chat]
REQUEST_KWARGS = {your proxy for example}
TELEGRAM_TOKEN = "your telegram token"
GRAFANA_TOKEN = "your grafana token"
STATE = ""
SID = ""
PERIOD = ""
SELECTED_DAY = ""


def space_in_tablespace(update, context):
    global SID
    if update.message.chat_id in TRUSTED_CHATS:
        sql_query = """SELECT df.tablespace_name,
ROUND(df.bytes / (1024 * 1024 * 1024),2),
ROUND(SUM(fs.bytes) / (1024 * 1024 * 1024),2),
ROUND(SUM(fs.bytes) * 100 / df.bytes,2)
FROM dba_free_space fs,
(SELECT tablespace_name, SUM(bytes) bytes
FROM dba_data_files GROUP BY tablespace_name) df
WHERE fs.tablespace_name(+)  = df.tablespace_name
GROUP BY df.tablespace_name, df.bytes
ORDER BY df.tablespace_name"""
        query_result = "<pre>________________________________________\n  TableSpace  |Size(GB)|Free(GB)|Free(%)\n" \
                       "¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\n"
        rows = oracle_connect(sql_query, update, context)
        for row in rows:
            query_result = query_result + format_text(str(row[0]), 14) + "|" + format_text(str(row[1]), 8) + "|" + \
                           format_text(str(row[2]), 8) + "|" + format_text(str(row[3]), 8) + "\n"
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Текущее состояние тейблспейсов системы " + SID + "\n" + query_result + "</pre>",
                                 parse_mode="HTML")
    else:
        update.message.reply_text("Unauthorized chat")


def format_text(text, len_ts):
    space = len_ts - len(text)
    return text + " " * space


def get_server_db_info(sid):
    server = {'your SID': ['your host', 'your port']}
    return server.get(sid)


def oracle_connect(query, update, context):
    global SID
    host_port = get_server_db_info(SID)
    dsn = cx_Oracle.makedsn(host_port[0], host_port[1], service_name=SID)
    try:
        connection = cx_Oracle.connect(user="your user", password="your pass", dsn=dsn)
    except cx_Oracle.DatabaseError as con_er:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Ошибка подключения к БД\n" + str(con_er))
    finally:
        cursor = connection.cursor()
        try:
            cursor.execute(query)
        except cx_Oracle.DatabaseError as exc_er:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Ошибка выполнения запроса\n" + str(exc_er))
        finally:
            rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return rows


def start(update, context):
    global SID, PERIOD, SELECTED_DAY
    if update.message.chat_id in TRUSTED_CHATS:
        SID = "your SID"
        PERIOD = "последние 3 часа"
        SELECTED_DAY = ""
        update.message.reply_text("Выбрана система " + SID + "\nЗа " + PERIOD)
    else:
        update.message.reply_text("Unauthorized chat")


def set_period(update, context):
    if update.message.chat_id in TRUSTED_CHATS:
        update.message.reply_text("""Показать график за последние:
1 час - /h1
3 часа - /h3
6 часов - /h6
12 часов - /h12
24 часа - /h24
48 часов - /h48
Другой день - /another_day""")
    else:
        update.message.reply_text("Unauthorized chat")


def h1(update, context):
    global PERIOD, SELECTED_DAY, SID
    if update.message.chat_id in TRUSTED_CHATS:
        SELECTED_DAY = ""
        PERIOD = "последний 1 час"
        update.message.reply_text("Выбрана система " + SID + "\nЗа " + PERIOD)
    else:
        update.message.reply_text("Unauthorized chat")


def h3(update, context):
    global PERIOD, SELECTED_DAY, SID
    if update.message.chat_id in TRUSTED_CHATS:
        SELECTED_DAY = ""
        PERIOD = "последние 3 часа"
        update.message.reply_text("Выбрана система " + SID + "\nЗа " + PERIOD)
    else:
        update.message.reply_text("Unauthorized chat")


def h6(update, context):
    global PERIOD, SELECTED_DAY, SID
    if update.message.chat_id in TRUSTED_CHATS:
        SELECTED_DAY = ""
        PERIOD = "последние 6 часов"
        update.message.reply_text("Выбрана система " + SID + "\nЗа " + PERIOD)
    else:
        update.message.reply_text("Unauthorized chat")


def h12(update, context):
    global PERIOD, SELECTED_DAY, SID
    if update.message.chat_id in TRUSTED_CHATS:
        SELECTED_DAY = ""
        PERIOD = "последние 12 часов"
        update.message.reply_text("Выбрана система " + SID + "\nЗа " + PERIOD)
    else:
        update.message.reply_text("Unauthorized chat")


def h24(update, context):
    global PERIOD, SELECTED_DAY, SID
    if update.message.chat_id in TRUSTED_CHATS:
        SELECTED_DAY = ""
        PERIOD = "последние 24 часа"
        update.message.reply_text("Выбрана система " + SID + "\nЗа " + PERIOD)
    else:
        update.message.reply_text("Unauthorized chat")


def h48(update, context):
    global PERIOD, SELECTED_DAY, SID
    if update.message.chat_id in TRUSTED_CHATS:
        SELECTED_DAY = ""
        PERIOD = "последние 48 часов"
        update.message.reply_text("Выбрана система " + SID + "\nЗа " + PERIOD)
    else:
        update.message.reply_text("Unauthorized chat")


def another_day(update, context):
    global STATE
    if update.message.chat_id in TRUSTED_CHATS:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Date?",
                                 reply_markup=telegramcalendar.create_calendar())
        STATE = "UNIXTIME"
    else:
        update.message.reply_text("Unauthorized chat")


def another_sid(update, context):
    global STATE
    if update.message.chat_id in TRUSTED_CHATS:
        keyboard = [
            [InlineKeyboardButton("your SID", callback_data="your SID")]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text("SID?", reply_markup=reply_markup)
        STATE = "SID"
    else:
        update.message.reply_text("Unauthorized chat")


def button_click(update, context):
    global STATE, SID, SELECTED_DAY, PERIOD
    query = update.callback_query
    query.answer()
    if STATE == "SID":
        if len(query.data) > 3:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text="Нельзя, выбирая SID, кликать по каледарю.\n"
                                          "Произведите настройки, запустив бота - /start")
        else:
            SID = query.data
            query.message.reply_text(text="Выбрана система " + SID + "\nЗа " + PERIOD)
            context.bot.edit_message_reply_markup(chat_id=query.message.chat_id, message_id=query.message.message_id,
                                                  reply_markup=None)
            STATE = "UNIXTIME"
    elif STATE == "UNIXTIME":
        selected, date = telegramcalendar.process_calendar_selection(context.bot, update)
        if selected:
            SELECTED_DAY = date
            PERIOD = str(date).split(' ')[0]
            query.message.reply_text(text="Выбрана система " + SID + "\nЗа " + PERIOD,
                                     reply_markup=ReplyKeyboardRemove())


def get_unix_date(start_date):
    start_unix_date = datetime.datetime.strptime(start_date.strftime("%d/%m/%Y %H:%M:%S"),
                                                 "%d/%m/%Y %H:%M:%S").timestamp()
    end = datetime.datetime.combine(start_date, datetime.datetime.max.time())
    end_unix_date = datetime.datetime.strptime(end.strftime("%d/%m/%Y %H:%M:%S"), "%d/%m/%Y %H:%M:%S").timestamp()
    return str(start_unix_date).split('.')[0] + "000", str(end_unix_date).split('.')[0] + "000"


def get_unix_hour(hour):
    current_unixtime = datetime.datetime.now().timestamp()
    ago_unixtime = current_unixtime - (hour * 3600)
    return str(ago_unixtime).split('.')[0] + "000", str(current_unixtime).split('.')[0] + "000"


def get_period():
    global SELECTED_DAY, PERIOD
    if SELECTED_DAY == "":
        return get_unix_hour(int(str(PERIOD).split(' ')[1]))
    else:
        return get_unix_date(SELECTED_DAY)


def db_avg_load(update, context):
    global SID
    if update.message.chat_id in TRUSTED_CHATS:
        pref_server = get_server(SID)
        if pref_server == "no_db_host":
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text="Графана не имеет данных по DB хосту.\n"
                                          "Будет показан график по первому в Графане аплику")
            pref_sid = "&var-system="
        else:
            pref_sid = pref_server + "&var-system="
        start_time, end_time = get_period()
        dashboard = "your dashboard"
        get_link(update, context, pref_sid, dashboard, start_time, end_time)
    else:
        update.message.reply_text("Unauthorized chat")


def db_wait_class(update, context):
    global SID
    if update.message.chat_id in TRUSTED_CHATS:
        pref_server = get_server(SID)
       if pref_server == "no_db_host":
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text="Графана не имеет данных по DB хосту.\n"
                                          "Будет показан график по первому в Графане аплику")
            pref_sid = "&var-system="
        else:
            pref_sid = pref_server + "&var-system="
        start_time, end_time = get_period()
        dashboard = "your dashboard"
        get_link(update, context, pref_sid, dashboard, start_time, end_time)
    else:
        update.message.reply_text("Unauthorized chat")


def cpu_load_percent(update, context):
    global SID
    if update.message.chat_id in TRUSTED_CHATS:
        pref_server = get_server(SID)
        if pref_server == "no_db_host":
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text="Графана не имеет данных по DB хосту.\n"
                                          "Будет показан график по первому в Графане аплику")
            pref_sid = "&var-system="
        else:
            pref_sid = pref_server + "&var-system="
        start_time, end_time = get_period()
        dashboard = "your dashboard"
        get_link(update, context, pref_sid, dashboard, start_time, end_time)
    else:
        update.message.reply_text("Unauthorized chat")


def num_in_locktab(update, context):
    if update.message.chat_id in TRUSTED_CHATS:
        pref_sid = "&var-SID="
        start_time, end_time = get_period()
        dashboard = "your dashboard"
        get_link(update, context, pref_sid, dashboard, start_time, end_time)
    else:
        update.message.reply_text("Unauthorized chat")


def test4_1k_locks(update, context):
    if update.message.chat_id in TRUSTED_CHATS:
        pref_sid = "&var-SID="
        start_time, end_time = get_period()
        dashboard = "your dashboard"
        get_link(update, context, pref_sid, dashboard, start_time, end_time)
    else:
        update.message.reply_text("Unauthorized chat")


def locks_per_sec(update, context):
    if update.message.chat_id in TRUSTED_CHATS:
        pref_sid = "&var-SID="
        start_time, end_time = get_period()
        dashboard = "your dashboard"
        get_link(update, context, pref_sid, dashboard, start_time, end_time)
    else:
        update.message.reply_text("Unauthorized chat")


def top_user_locks(update, context):
    if update.message.chat_id in TRUSTED_CHATS:
        pref_sid = "&var-SID="
        start_time, end_time = get_period()
        dashboard = "your dashboard"
        get_link(update, context, pref_sid, dashboard, start_time, end_time)
    else:
        update.message.reply_text("Unauthorized chat")


def proc_btc_await(update, context):
    if update.message.chat_id in TRUSTED_CHATS:
        pref_sid = "&var-SID="
        start_time, end_time = get_period()
        dashboard = "your dashboard"
        get_link(update, context, pref_sid, dashboard, start_time, end_time)
    else:
        update.message.reply_text("Unauthorized chat")


def luw_by_rfc(update, context):
    if update.message.chat_id in TRUSTED_CHATS:
        pref_sid = "&var-system="
        start_time, end_time = get_period()
        dashboard = "your dashboard"
        get_link(update, context, pref_sid, dashboard, start_time, end_time)
        luw_by_rfc_satellite(update, context)
    else:
        update.message.reply_text("Unauthorized chat")


def luw_by_rfc_satellite(update, context):
    pref_sid = "&var-system="
    start_time, end_time = get_period()
    dashboard = "your dashboard"
    get_link(update, context, pref_sid, dashboard, start_time, end_time)


def queues_in_smq2(update, context):
    if update.message.chat_id in TRUSTED_CHATS:
        pref_sid = "&var-SID="
        start_time, end_time = get_period()
        dashboard = "your dashboard"
        get_link(update, context, pref_sid, dashboard, start_time, end_time)
        queues_in_smq2_satellite(update, context)
    else:
        update.message.reply_text("Unauthorized chat")


def queues_in_smq2_satellite(update, context):
    pref_sid = "&var-SID="
    start_time, end_time = get_period()
    dashboard = "your dashboard"
    get_link(update, context, pref_sid, dashboard, start_time, end_time)
    queues_in_smq2_satellite2(update, context)


def queues_in_smq2_satellite2(update, context):
    pref_sid = "&var-SID="
    start_time, end_time = get_period()
    dashboard = "your dashboard"
    get_link(update, context, pref_sid, dashboard, start_time, end_time)


def top_sql_by_cputime(update, context):
    if update.message.chat_id in TRUSTED_CHATS:
        pref_sid = "&var-SID="
        start_time, end_time = get_period()
        dashboard = "your dashboard"
        get_link(update, context, pref_sid, dashboard, start_time, end_time)
        top_sql_by_cputime_satellite(update, context)
    else:
        update.message.reply_text("Unauthorized chat")


def top_sql_by_cputime_satellite(update, context):
    pref_sid = "&var-SID="
    start_time, end_time = get_period()
    dashboard = "your dashboard"
    get_link(update, context, pref_sid, dashboard, start_time, end_time)


def get_link(update, context, prefsid, dashboard, start_time, end_time):
    global SID
    link = (dashboard + start_time + "&to=" + end_time + prefsid + SID)
    #context.bot.send_message(chat_id=update.effective_chat.id, text="Grafana link=" + link)
    get_screen(update, context, link)


def get_screen(update, context, link):
   global SID, PERIOD
    headers = CaseInsensitiveDict()
    headers["Authorization"] = GRAFANA_TOKEN
    open('file.png', 'wb').write(requests.get(link, headers=headers).content)
    context.bot.send_photo(chat_id=update.effective_chat.id, caption="График для системы " + SID + "\nЗа " + PERIOD,
                           photo=open('file.png', 'rb'))


def get_server(sid):
    db_servers = dict(your SID="your server")
    return db_servers[sid]


def main():
    updater = Updater(TELEGRAM_TOKEN, request_kwargs=REQUEST_KWARGS, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("another_sid", another_sid))
    dispatcher.add_handler(CommandHandler("another_day", another_day))
    dispatcher.add_handler(CommandHandler("set_period", set_period))
    dispatcher.add_handler(CommandHandler("h1", h1))
    dispatcher.add_handler(CommandHandler("h3", h3))
    dispatcher.add_handler(CommandHandler("h6", h6))
    dispatcher.add_handler(CommandHandler("h12", h12))
    dispatcher.add_handler(CommandHandler("h24", h24))
    dispatcher.add_handler(CommandHandler("h48", h48))
    dispatcher.add_handler(CommandHandler("num_in_locktab", num_in_locktab))
    dispatcher.add_handler(CommandHandler("test4_1k_locks", test4_1k_locks))
    dispatcher.add_handler(CommandHandler("locks_per_sec", locks_per_sec))
    dispatcher.add_handler(CommandHandler("top_user_locks", top_user_locks))
    dispatcher.add_handler(CommandHandler("proc_btc_await", proc_btc_await))
    dispatcher.add_handler(CommandHandler("luw_by_rfc", luw_by_rfc))
    dispatcher.add_handler(CommandHandler("queues_in_smq2", queues_in_smq2))
    dispatcher.add_handler(CommandHandler("db_avg_load", db_avg_load))
    dispatcher.add_handler(CommandHandler("db_wait_class", db_wait_class))
    dispatcher.add_handler(CommandHandler("cpu_load_percent", cpu_load_percent))
    dispatcher.add_handler(CommandHandler("top_sql_by_cputime", top_sql_by_cputime))
   dispatcher.add_handler(CommandHandler("space_in_tablespace", space_in_tablespace))
    dispatcher.add_handler(CallbackQueryHandler(button_click))
    updater.start_polling(drop_pending_updates=True)
    updater.idle()


if __name__ == '__main__':
    main()