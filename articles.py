from hemlock.tools import img

ARTICLES = [
    (
        'GA-Trump',
        img(
            'https://media.11alive.com/assets/WXIA/images/a2dea6c3-a110-46f4-9649-a0cf0e7907de/a2dea6c3-a110-46f4-9649-a0cf0e7907de_1920x1080.jpg',
            img_align='center',
            img_attrs={'style': {'max-height': '256px'}},
            caption="Georgia GOP lieutenant governor says Trump call with secretary of state 'inappropriate'",
            caption_align='center'
        ),
        'https://www.cnn.com/2021/01/04/politics/geoff-duncan-trump-raffensperger-call-cnntv/index.html'
    ),
    (
        'Iran-tanker',
        img(
            'https://media2.s-nbcnews.com/j/newscms/2021_01/3432881/201203-iran-nuclear-mc-14073_46addc1bda76c57f8df8456a14fcbc64.fit-2000w.JPG',
            img_align='center',
            img_attrs={'style': {'max-height': '256px'}},
            caption="Iran seizes tanker, ramps up uranium enrichment in fresh escalation with West",
            caption_align='center'
        ),
        'https://www.nbcnews.com/news/world/iran-resumes-20-percent-uranium-enrichment-nuclear-facility-state-news-n1252708'
    ),
    (
        'UK-extradite-wikileaks',
        img(
            "https://media.npr.org/assets/img/2021/01/04/gettyimages-1229998368-607ae685381bbfd50e7b1a216fe3d7c175d1e0f2-s1600-c85.jpg",
            img_align='center',
            img_attrs={'style': {'max-height': '256px'}},
            caption="British Court Rejects U.S. Request To Extradite WikiLeaks Founder Julian Assange",
            caption_align='center'
        ),
        'https://www.npr.org/2021/01/04/953142687/british-court-rejects-u-s-request-to-extradite-wikileaks-founder-julian-assange'
    )
]
ARTICLE_NAMES = [name for name, headline, url in ARTICLES]