from .. import udB

if not udB.get("BOTCHAT"):
    udB.set("BOTCHAT", "{}")
elif udB.get("BOTCHAT") == "":
    udB.set("BOTCHAT", "{}")


def add_stuff(msg_id, user_id):
    ok = eval(udB.get("BOTCHAT"))
    ok.update({msg_id: user_id})
    udB.set("BOTCHAT", str(ok))


def get_who(msg_id):
    ok = eval(udB.get("BOTCHAT"))
    try:
        user = ok.get(msg_id)
        return user
    except BaseException:
        return
