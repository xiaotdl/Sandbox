# Inspired by:
# https://www.youtube.com/watch?v=u8g9scXeAcI&start=1260


# == Generators Use Cases ==
# - Useful for refactoring nested loops:
#     - separate iteration logic from loop body
#     - break out several loops using return
# - Performance improvements:
#     - only execute code when necessary
# - Infinite loop.


# ==> nested loop improvement e.g.
def pairs(group):
    if person1 in group:
        if person1.is_antisocial():
            continue
        if person2 in group:
            if person1 == person2:
                continue
            if bad_match(person1, person2):
                return
            yield person1, person2
for person1, person2 in pairs(group):
    person1.greet(person2)


# ==> lazy load performace improvement e.g.
import requests

def get_widgets():
    page = 1
    while True:
        url = "/widgets?page={}".format(page)
        resp = requests.get(url)
        for widgets in resp.json()["widgets"]:
            yield widget
        if resp.join()["hasNextPage"]:
            page += 1
        else:
            return


for widget in get_widgets():
    process(widget)

