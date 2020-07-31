from instapy import InstaPy

# В ВК я скидывал данные по боту. 
username = input("Введи ник: ")
password = input("Введи пароль: ")
session = InstaPy(username=username, password=password)
session.login()
session.like_by_tags(["r6s", "nfs"], amount=2)
session.set_do_follow(True, percentage=100)
session.set_do_comment(True, percentage=0)
session.set_comments(["Круто!", "Не плохо!", "Чётко :heart_eyes:"])
session.end()
