urls = [
    "https://docs.google.com/presentation/d/10b-OWkX3fIVsZG680uDT3jAnfiYL5QaDcHUzoQluHjw/edit?usp=drive_link",
    "https://docs.google.com/presentation/d/1FeknZ_lR2koAGx-FgF68st8z9UJeKbuRgQL8zYMZuNQ/edit?usp=drive_link",
    "https://docs.google.com/presentation/d/16mDp3wNUiEpHwqsUnbO4Wdq9EDf2YTZEXx_ZsY2ovJk/edit?usp=drive_link",
    "https://docs.google.com/presentation/d/1clcNJg78aEduyT3iD9lRFcDf68yImAfXSqVHs_lfYPE/edit?usp=drive_link",
    "https://docs.google.com/presentation/d/1I_K1Z4IitdsmmM-YUOkxCr2n5Zu82ZZRle1lPwwKnbE/edit?usp=drive_link",
]

pres_template = """<div class="presentation" onclick="openPresentation('{name}')">
    <img
    src="{image}"
    alt="Presentation {num}">
</div>"""
container = """<div class="container">
{pres}
</div>"""


def get_name(link):
    return link.split("?")[0].split("/")[-2]


def get_image(link):
    return link.split("/edit")[0] + "/export/png?id=" + get_name(link)


html = container.format(
    pres="\n".join(
        pres_template.format(name=get_name(link), image=get_image(link), num=num)
        for num, link in enumerate(urls, start=1)
    )
)

with open("builed.html", "w") as f:
    f.write(html)
