urls = [
    "https://docs.google.com/presentation/d/10b-OWkX3fIVsZG680uDT3jAnfiYL5QaDcHUzoQluHjw/edit?usp=drive_link",
    "https://docs.google.com/presentation/d/1FeknZ_lR2koAGx-FgF68st8z9UJeKbuRgQL8zYMZuNQ/edit?usp=drive_link",
    "https://docs.google.com/presentation/d/16mDp3wNUiEpHwqsUnbO4Wdq9EDf2YTZEXx_ZsY2ovJk/edit?usp=drive_link",
    "https://docs.google.com/presentation/d/1clcNJg78aEduyT3iD9lRFcDf68yImAfXSqVHs_lfYPE/edit?usp=drive_link",
    "https://docs.google.com/presentation/d/1I_K1Z4IitdsmmM-YUOkxCr2n5Zu82ZZRle1lPwwKnbE/edit?usp=drive_link",
    "https://docs.google.com/presentation/d/1f2-OtyHUHjuIaMEIrrcUbZIwb8aK1MPYuyxv4pzR9Io/edit?usp=drive_link",
    "https://docs.google.com/presentation/d/1YpZLDW3v_mARILdOf1ZvkfqmKZMRVlLDQs9SfJM1LMA/edit?usp=drive_link",
]

names = [
    "Литературный проект ПЭКАЛЭ И ТЫНДАЛЭ",
    "Литературный проект КОШЕЛЁК С ДВУМЯ ДЕНЕЖКАМИ",
    "Литературный проект ИСТОРИЯ МУРАВЬЯ. ",
    "Литературный проект ГАДКИЙ УТЁНОК.",
    "Литературный проект ВОРИШКА",
    "Литературный проект Спиридона Вангели «Шапка Гугуцэ»",
    "Литературный проект Иона Крянгэ «Дочь старика и дочь старухи»",
]
assert len(names) == len(urls)

pres_template = """<div class="presentation" onclick="openPresentation('{link}')">
    <img
    src="{image}"
    alt="{name}">
</div>"""
container = """<div class="container">
{pres}
</div>"""


def get_link(full_link):
    return full_link.split("?")[0].split("/")[-2]


def get_image_link(full_link):
    return full_link.split("/edit")[0] + "/export/png?id=" + get_link(full_link)


def get_image(name):
    return f"Images/{name}.png"


import urllib.request

def download_image(full_link, name):
    with urllib.request.urlopen(get_image_link(full_link)) as response, open(
        f"Images/{name}.png", "wb"
    ) as out_file:
        data = response.read()
        out_file.write(data)

for name, full_link in zip(names, urls):
    download_image(full_link, name)

html = container.format(
    pres="\n".join(
        pres_template.format(link=get_link(full_link), image=get_image(name), name=name)
        for name, full_link in zip(names, urls)
    )
)

with open("builed.html", "w", encoding="utf-8") as f:
    f.write(html)
