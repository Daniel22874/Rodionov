# В программе хранится словарь вступительных экзаменов вида Предмет=Баллы.
# Узнать, проходит ли абитуриент на специальность, если нужно сдать
# все перечисленные экзамены с не меньшим количеством баллов.
try:
    need_exams = {
        "Информатика": 80,
        "Математика": 85,
        "Русский язык": 75
    }
    print("""Для определения возможности поступления, необходима информация о
    Вас.
    Для ввода экзамена и баллов введите их через |: Химия | 40.
    Для завершения ввода нажмите Enter.
    """)
    passed_exams = {}
    while True:
        vvod = input("").strip()
        if vvod == "":
            break
        exam, balls = [x.strip() for x in vvod.split("|")]
        passed_exams[exam] = int(balls)
    print("Ваши экзамены:")
    for i, (exam, ball) in enumerate(passed_exams.items(), start=1):
        print("{}) {} {}".format(i, exam, ball))
    ok = False
    for need_exam, balls in need_exams.items():
        if passed_exams[need_exam] < balls:
            break
    else:
        ok = True
    print("Вы можете к нам поступить!" if ok else "Увы...")
except KeyError as e:
    print("У вас сданы не все основные экзамены для вашей специальности")
