
from kivy.app import App
# if you not import label and use it it through error
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import asyncio
import datetime
from netschoolapi import NetSchoolAPI
from kivy.uix.boxlayout import BoxLayout
login = 'ТруновА3'
password = '5710727a'
school = 'ОГБОУ «ТФТЛ»'
week = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"]
textt =""
o = 0
# defining the App class

class MyLabelApp(App):
    def update_lable(self):
        self.txt.text=self.formula
        self.value.text=""
        print(self.txt.text)
    def build(self):
        self.formula="0"
        box = BoxLayout(orientation='vertical')
        self.value = TextInput(text="")
        sudmit = Button(text="push", on_press=self.sudmit)
        self.txt = Label(text=textt)
        box.add_widget(self.value)
        box.add_widget(sudmit)
        box.add_widget(self.txt)
        return box


    def sudmit(self, odj):
        g = self.value.text


        async def main():
            textt = ""
            toda = datetime.datetime.now()

            if g.find("понедельник") != -1 or g.find("вторник") != -1 or g.find("сред") != -1 or g.find(
                    "пятниц") != -1 or g.find("четверг") != -1 or g.find("суббо") != -1:
                j = datetime.datetime.isoweekday(toda)
                if g.find("понедельн") != -1:

                    if 1 < j:
                        toda = toda + datetime.timedelta(days=7 - j + 1)
                    else:
                        toda = toda + datetime.timedelta(days=1 - j)
                if g.find("вторни") != -1:
                    if 2 < j:
                        toda = toda + datetime.timedelta(days=7 - j + 2)
                    else:
                        toda = toda + datetime.timedelta(days=2 - j)
                if g.find("сред") != -1:

                    if 3 < j:
                        toda = toda + datetime.timedelta(days=7 - j + 3)
                    else:
                        toda = toda + datetime.timedelta(days=3 - j)
                if g.find("четверг") != -1:

                    if 4 < j:
                        toda = toda + datetime.timedelta(days=7 - j + 4)
                    else:
                        toda = toda + datetime.timedelta(days=4 - j)
                if g.find("пятниц") != -1:

                    if 5 < j:
                        toda = toda + datetime.timedelta(days=7 - j + 5)
                    else:
                        toda = toda + datetime.timedelta(days=5 - j)
                if g.find("суббот") != -1:

                    if 6 < j:
                        toda = toda + datetime.timedelta(days=7 - j + 6)
                    else:
                        toda = toda + datetime.timedelta(days=6 - j)

                y = int(toda.strftime('%y')) + 2000
                m = int(toda.strftime('%m'))
                d = int(toda.strftime('%d'))

            elif g.find("декаб") != -1 or g.find("янва") != -1 or g.find("февр") != -1 or g.find("мар") != -1 or g.find(
                    "апре") != -1 or g.find("мая") != -1 or g.find("сентяб") != -1 or g.find("октяб") != -1 or g.find(
                "нояб") != -1:
                y = ""

                for i in range(0, len(list(filter(str.isdigit, g)))):
                    y = y + str(list(filter(str.isdigit, g))[i])
                d = int(y)
                # print(d)
                y = int(toda.strftime('%y')) + 2000
                if g.find("декаб") != -1:
                    m = 12
                    if int(toda.strftime('%m')) < 9:
                        y = int(toda.strftime('%y')) + 2000 - 1
                elif g.find("янва") != -1:
                    m = 1
                elif g.find("февр") != -1:
                    m = 2
                elif g.find("мар") != -1:
                    m = 3
                elif g.find("апрел") != -1:
                    m = 4
                elif g.find("мая") != -1:
                    m = 5
                elif g.find("сентябр") != -1:
                    m = 9
                    if int(toda.strftime('%m')) < 9:
                        y = int(toda.strftime('%y')) + 2000 - 1
                elif g.find("октябр") != -1:
                    m = 10
                    if int(toda.strftime('%m')) < 9:
                        y = int(toda.strftime('%y')) + 2000 - 1
                elif g.find("ноябр") != -1:
                    m = 11
                    if int(toda.strftime('%m')) < 9:
                        y = int(toda.strftime('%y')) + 2000 - 1
                y = int(toda.strftime('%y')) + 2000

            elif g.find("сегод") != -1:
                y = int(toda.strftime('%y')) + 2000
                m = int(toda.strftime('%m'))
                d = int(toda.strftime('%d'))
            else:
                y = int(toda.strftime('%y')) + 2000
                m = int(toda.strftime('%m'))
                d = int(toda.strftime('%d')) + 1
            # print(g)
            # print(y)
            # print(m)
            # print(d)

            # l = input()
            await ns.login(
                login,  # Логин
                password,  # Пароль
                school,  # Название школы
            )
            f = []
            x = (await ns.diary(datetime.date(y, m, d), ))
            await ns.logout()

            z = (x['schedule'])

            d = (z[0])
            for p in (d["lessons"]):
                if (p["assignments"]) != []:
                    for i in range(0, len(p["assignments"])):
                        x = str(str(p["subject"]) + ": " + str(p["assignments"][i]["content"]))
                        textt = textt + x + "\n"
                        global o
                        o = 1
            self.formula = textt
            if o == 0:
                textt="Ниче не задали"
                self.formula = textt

        # ************************************ СРЕДНИЙ БАЛЛ
        async def marks(q=0):
            textt = ""
            if g.find("английск") != -1:
                predm = "Английский язык"
            elif g.find("мате") != -1:
                predm = "Математика"
            elif g.find("алгеб") != -1:
                predm = "Алгебра"
            elif g.find("физик") != -1:
                predm = "Физика"
            elif g.find("русск") != -1:
                predm = "Русский язык"
            elif g.find("геоме") != -1:
                predm = "Геометрия"
            elif g.find("геогр") != -1:
                predm = "География"
            elif g.find("инф") != -1:
                predm = "Информатика"
            elif g.find("Биол") != -1:
                predm = "Биология"
            elif g.find("лит") != -1:
                predm = "Литература"
            elif g.find("истор") != -1:
                predm = "История"
            elif g.find("хими") != -1:
                predm = "Химия"
            elif g.find("обществ") != -1:
                predm = "Обществознание"
            elif g.find("черче") != -1:
                predm = "Черчение"
            elif g.find("обж") != -1:
                predm = "Основы безопасности жизнедеятельности"
            elif g.find("физр") != -1 or g.find("физкульт") != -1:
                predm = "Физкультура"

            await ns.login(
                login,  # Логин
                password,  # Пароль
                school,  # Название школы
            )

            dn = datetime.date.today()
            if 9 <= int(dn.month) <= 12:
                yearn = int(dn.year)
            else:
                yearn = int(dn.year) - 1

            if g.find('1 четверть') != -1:
                times = datetime.date(yearn, 9, 1)
                timee = datetime.date(yearn, 10, 26)
            elif g.find('2 четверть') != -1:
                times = datetime.date(yearn, 11, 5)
                timee = datetime.date(yearn, 12, 28)
            elif g.find('3 четверть') != -1:
                times = datetime.date(yearn + 1, 1, 9)
                timee = datetime.date(yearn + 1, 3, 23)
            elif g.find('4 четверть') != -1:
                times = datetime.date(yearn + 1, 4, 3)
                timee = datetime.date(yearn + 1, 5, 31)
            elif g.find('1 полугодие') != -1:
                times = datetime.date(yearn, 9, 1)
                timee = datetime.date(yearn, 12, 28)
            elif g.find('2 полугодие') != -1:
                times = datetime.date(yearn + 1, 1, 9)
                timee = datetime.date(yearn + 1, 5, 31)
            else:
                times = datetime.date(yearn, 9, 1)
                timee = datetime.date(yearn + 1, 5, 31)
                period = "Все время"

            x = await ns.diary(times, timee)
            await ns.logout()

            otmetki = {}
            cnt = {}

            try:

                for i in range(len(x['schedule'])):
                    day = x['schedule'][i]
                    for j in range(len(day['lessons'])):
                        less = day['lessons'][j]
                        if less["subject"] == predm:
                            for k in range(len(less['assignments'])):
                                if less['assignments'][k]['mark']:
                                    otmetki[less['subject']] = otmetki.get(less['subject'], 0) + int(
                                        less['assignments'][k]['mark'])
                                    cnt[less['subject']] = cnt.get(less['subject'], 0) + 1
                                    q = 1
                                    break
            except:
                pass

            if q == 0:
                textt="У тебя нет такого предмета"
                return
            if len(predm.split()) == 1:
                textt = (('Оценок по ' + predm[:-1] + 'е' + ' - ' + str(cnt.get(predm))).capitalize())
                textt = textt + "\n" + (('Средний балл по ' + predm[:-1] + 'е' + ' - ' + str(
                    float('{:.2f}'.format((otmetki.get(predm) / cnt.get(predm)))))).capitalize())
                self.formula = textt
            else:
                textt = (('Оценок по ' + predm.replace("ский", "скому").replace("ык", "ыку") + ' - '
                          + str(cnt.get(predm))).capitalize())
                textt = textt + "\n" + ((
                                                'Средний балл по ' + predm.replace("ский", "скому").replace("ык",
                                                                                                            "ыку") + ' - ' +
                                                str(float('{:.2f}'.format(
                                                    (otmetki.get(predm) / cnt.get(predm)))))).capitalize())
                self.formula = textt

        # ************************************ РАСПИСАНИЕ
        async def listt():
            textt = ""
            try:
                toda = datetime.datetime.now()
                if g.find("понедельник") != -1 or g.find("вторник") != -1 or g.find("сред") != -1 or g.find(
                        "пятниц") != -1 or g.find("четверг") != -1 or g.find("суббо") != -1:
                    j = datetime.datetime.isoweekday(toda)
                    if g.find("понедельн") != -1:

                        if 1 < j:
                            toda = toda + datetime.timedelta(days=7 - j + 1)
                        else:
                            toda = toda + datetime.timedelta(days=1 - j)
                    if g.find("вторник") != -1:

                        if 2 < j:
                            toda = toda + datetime.timedelta(days=7 - j + 2)
                        else:
                            toda = toda + datetime.timedelta(days=2 - j)
                    if g.find("сред") != -1:

                        if 3 < j:
                            toda = toda + datetime.timedelta(days=7 - j + 3)
                        else:
                            toda = toda + datetime.timedelta(days=3 - j)
                    if g.find("четверг") != -1:

                        if 4 < j:
                            toda = toda + datetime.timedelta(days=7 - j + 4)
                        else:
                            toda = toda + datetime.timedelta(days=4 - j)
                    if g.find("пятниц") != -1:

                        if 5 < j:
                            toda = toda + datetime.timedelta(days=7 - j + 5)
                        else:
                            toda = toda + datetime.timedelta(days=5 - j)
                    if g.find("суббот") != -1:

                        if 6 < j:
                            toda = toda + datetime.timedelta(days=7 - j + 6)
                        else:
                            toda = toda + datetime.timedelta(days=6 - j)

                    y = int(toda.strftime('%y')) + 2000
                    m = int(toda.strftime('%m'))
                    d = int(toda.strftime('%d'))

                elif g.find("сегод") != -1:

                    y = int(toda.strftime('%y')) + 2000

                    m = int(toda.strftime('%m'))

                    d = int(toda.strftime('%d'))



                elif g.find("завтр") != -1:

                    y = int(toda.strftime('%y')) + 2000

                    m = int(toda.strftime('%m'))

                    d = int(toda.strftime('%d')) + 1
                else:

                    # l = input()
                    await ns.login(
                        login,  # Логин
                        password,  # Пароль
                        school,  # Название школы
                    )
                    f = []
                    x = (await ns.diary())
                    b = 0
                    for d in x["schedule"]:
                        for i in range(0, 7):
                            #print(week[b])
                            textt = textt + "\n" + week[b]
                            break
                        b = b + 1
                        for p in (d["lessons"]):
                            # for day in week:
                            textt = textt + "\n" + (str(p["number"]) + ". " + str(p["subject"]))
                    self.formula = textt

                    return
                # print(g)
                # print(y)
                # print(m)
                # print(d)
                # l = input()
                await ns.login(
                    login,  # Логин
                    password,  # Пароль
                    school,  # Название школы
                )
                f = []
                x = (await ns.diary(datetime.date(y, m, d), ))
                await ns.logout()
                z = (x['schedule'])
                d = ((z[0]))
                for p in (d["lessons"]):
                    textt = textt + "\n" + (str(p["number"]) + ". " + str(p["subject"]))

                self.formula = textt
            except:
                pass

        # ************************************ ОЦЕНКИ ЗА ОПРЕДЕЛЕННЫЙ ДЕНЬ
        async def mark_day(o=0):
            textt = ""

            toda = datetime.datetime.now()

            if g.find("понедельник") != -1 or g.find("вторник") != -1 or g.find("сред") != -1 or g.find(
                    "пятниц") != -1 or g.find("четверг") != -1 or g.find("суббо") != -1:
                j = datetime.datetime.isoweekday(toda)

                if g.find("понедельн") != -1:
                    toda = toda - datetime.timedelta(days=j - 1)
                if g.find("вторник") != -1:
                    toda = toda - datetime.timedelta(days=j - 2)
                if g.find("сред") != -1:
                    toda = toda - datetime.timedelta(days=j - 3)
                if g.find("четверг") != -1:
                    toda = toda - datetime.timedelta(days=j - 4)
                if g.find("пятниц") != -1:
                    toda = toda - datetime.timedelta(days=j - 5)
                if g.find("суббот") != -1:
                    toda = toda - datetime.timedelta(days=j - 6)
                y = int(toda.strftime('%y')) + 2000
                m = int(toda.strftime('%m'))
                d = int(toda.strftime('%d'))
            elif g.find("декаб") != -1 or g.find("янва") != -1 or g.find("февр") != -1 or g.find(
                    "мар") != -1 or g.find(
                    "апре") != -1 or g.find("мая") != -1 or g.find("сентяб") != -1 or g.find(
                "октяб") != -1 or g.find(
                "нояб") != -1:
                y = ""
                for i in range(0, len(list(filter(str.isdigit, g)))):
                    y = y + str(list(filter(str.isdigit, g))[i])
                d = int(y)
                y = int(toda.strftime('%y')) + 2000
                if g.find("декаб") != -1:
                    m = 12
                    if int(toda.strftime('%m')) < 9:
                        y = int(toda.strftime('%y')) + 2000 - 1
                elif g.find("янва") != -1:
                    m = 1
                elif g.find("февр") != -1:
                    m = 2
                elif g.find("мар") != -1:
                    m = 3
                elif g.find("апрел") != -1:
                    m = 4
                elif g.find("мая") != -1:
                    m = 5
                elif g.find("сентябр") != -1:
                    m = 9
                    if int(toda.strftime('%m')) < 9:
                        y = int(toda.strftime('%y')) + 2000 - 1
                elif g.find("октябр") != -1:
                    m = 10
                    if int(toda.strftime('%m')) < 9:
                        y = int(toda.strftime('%y')) + 2000 - 1
                elif g.find("ноябр") != -1:
                    m = 11
                    if int(toda.strftime('%m')) < 9:
                        y = int(toda.strftime('%y')) + 2000 - 1
            elif g.find("сегод") != -1:
                print('g')
                y = int(toda.strftime('%y')) + 2000
                m = int(toda.strftime('%m'))
                d = int(toda.strftime('%d'))
                print(y)
                print(m)
                print(d)


            # l = input()
            await ns.login(
                login,  # Логин
                password,  # Пароль
                school,  # Название школы
            )
            f = []
            x = (await ns.diary(datetime.date(y, m, d), ))
            await ns.logout()

            z = (x['schedule'])
            d = ((z[0]))
            for p in (d["lessons"]):
                if (p["assignments"]) != []:
                    for i in range(0, len(p["assignments"])):
                        x = str(str(p["subject"]) + ": " + str(p["assignments"][i]["mark"]))
                        if x.find("None") == -1:
                            #print(x)
                            textt = x + "\n" + textt
                        o = 1
            self.formula = textt

            #print(textt)


        # ************************************ ДИНАМИЧЕСКОЕ РАСПИСАНИЕ
        async def dinamik():
            textt = ""
            ns = NetSchoolAPI("https://sgo.tomedu.ru/")

            await ns.login(
                login,  # Логин
                password,  # Пароль
                school,  # Название школы
            )

            x = await ns.diary(datetime.date.today(), datetime.date.today())  # Реальная дата
            await ns.logout()
            # x = await ns.diary(datetime.date(2022,12,7), datetime.date(2022,12,7))   # Дата для теста (год, месяц, день)

            ttt = {}

            for i in range(len(x['schedule'])):
                day = x['schedule'][i]
                for j in range(len(day['lessons'])):
                    less = day['lessons'][j]
                    raspis = {
                        'subject': less['subject'],
                        'start': less['start'],
                        'end': less['end'],
                    }

                    if less['room']:
                        raspis['room'] = " в " + less['room'] + " кабинете"
                    else:
                        raspis['room'] = "(кабинет не указан)"

                    ttt[j + 1] = raspis

            timen = datetime.time(datetime.datetime.now().hour, datetime.datetime.now().minute, 0)  # Реальное время

            # timen = datetime.time(9, 30, 0)  # Время для теста

            if timen < ttt[list(ttt.keys())[-1]]['end']:
                for u in range(len(ttt)):
                    if ttt[u + 1]['start'] > timen:
                        textt = textt + "\n" + ("Следующий урок - " + ttt[u + 1]['subject'] + "; Начало в " + str(
                            ttt[u + 1]['start'])[:-3]
                                                + ttt[u + 1]['room'])
                        break
                    if ttt[u + 1]['start'] <= timen <= ttt[u + 1]['end']:
                        textt = textt + "\n" + ("Сейчас " + ttt[u + 1]['subject'])
                    elif ttt[u + 1]['end'] <= timen <= ttt[u + 2]['start']:
                        textt = textt + "\n" + ("Сейчас перемена")
            else:
                textt = textt + "\n" + ("На сегодня уроков в расписании больше нет")
            self.formula = textt
            # print(ttt)
            # print("\n\n\n")
            # print(datetime.date(2,2,2))
            # print("\n\n\n")

        # ************************************ НАЧАЛЬНЫЕ ДАННЫЕ
        o = 0
        n = 1
        ns = NetSchoolAPI("https://sgo.tomedu.ru/")
        try:
            if g.find("задали") != -1 or g.find("дз") != -1:

                for i in range(0, 100):
                    try:
                        asyncio.run(main())
                        break
                    except:
                        print("ошибка")
                        pass

            elif g.find("средний") != -1 or g.find("выходит") != -1:
                for i in range(0, 1):
                    try:
                        asyncio.run(marks())
                        break
                    except:
                        pass

            elif g.find("уроки") != -1 or g.find("распис") != -1:
                for i in range(0, 100):
                    try:
                        asyncio.run(listt())
                        break
                    except:
                        print("ошибка")
                        pass

            elif g.find("оценк") != -1 or g.find("получил") != -1:

                for i in range(0, 100):
                    try:
                        asyncio.run(mark_day())
                        break
                    except:
                        print("ошибка")
                        pass

            elif g.find("след") != -1 or g.find("дальше") != -1 or g.find("сейчас") != -1:
                for i in range(0, 100):
                    try:
                        asyncio.run(dinamik())
                        break
                    except:
                        print("ошибка")
                        pass

            else:
                print('я вас не понимаю')
        except KeyboardInterrupt:
            pass
            print("пока, пока")

        self.update_lable()



MyLabelApp().run()