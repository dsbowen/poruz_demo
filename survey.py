from articles import ARTICLES, ARTICLE_NAMES

import pandas as pd
from hemlock import Branch, Page, Label, RangeInput, Embedded, route
from hemlock.tools import Assigner, consent_page, completion_page
from hemlock_demographics import basic_demographics
from joblib import load

import random

N_ARTICLES = 2
# assigner = Assigner({'Ideal': (0, 1)})
assigner = Assigner({'Condition': ('random', 'ideal', 'actual')})
reg = load('model.p')
cols = [
    'Ideal',
    'RaceWhite',
    'RaceBlack',
    'RaceSouth Asian',
    'RaceEast Asian',
    'RaceArabic or Central Asian',
    'RaceOther',
    'Male',
    'Age',
    'ArticleName'
]

@route('/survey')
def start():
    assigner.next()
    return Branch(
        consent_page(
            '''
            By entering your MTurk ID, you consent to sell us your first-born son for no more than $102.23.
            '''
        ),
        basic_demographics(page=True, require=True),
        navigate=rate_articles,
        navigate_worker=True
    )

def rate_articles(start_branch):
    def select_articles(part):
        if part.meta['Condition'] == 'random':
            return random.sample(ARTICLES, k=N_ARTICLES)
        df = pd.DataFrame(part.get_data())
        df['Ideal'] = df['Condition'] == 'ideal'
        df = df.append((len(ARTICLES)-1)*[df], ignore_index=True)
        df['ArticleName'] = ARTICLE_NAMES
        X = df[cols]
        y_pred = reg.predict(X)
        article_ratings = list(zip(ARTICLES, y_pred))
        article_ratings.sort(key=lambda x: x[1], reverse=True)
        return [article for article, rating in article_ratings][:N_ARTICLES]

    # def gen_rate_articles_page(name, headline, url):
    #     page = Page(
    #         RangeInput(
    #             '''
    #             <p>From 0 (not at all) to 10 (very much), how much do you think you'd enjoy reading the following article?</p>

    #             <p><b>{}</b></p>
    #             '''.format(headline),
    #             min=0, max=10, required=True, var='Enjoy'
    #         )
    #     )
    #     if start_branch.part.meta['Ideal']:
    #         page.questions.insert(
    #             0,
    #             Label(
    #                 '''
    #                 First, think of the sort of news an ideal version of yourself would enjoy reading.
    #                 '''
    #             )
    #         )
    #     return page

    def gen_rate_articles_page(name, headline, url):
        return Page(
            RangeInput(
                '''
                <p>Take a few minutes to read <a href="{}" target="_blank">this article</a>.</p>

                {}

                <p>From 0 (not at all ) to 10 (very much), how much did you enjoy reading that article?</p>
                '''.format(url, headline),
                min=0, max=10, required=True, var='Enjoy'
            )
        )

    # articles = random.sample(ARTICLES, k=N_ARTICLES)
    articles = select_articles(start_branch.part)
    start_branch.embedded.append(
        Embedded('ArticleName', [name for name, headline, url in articles])
    )
    return Branch(
        *[gen_rate_articles_page(*article) for article in articles],
        navigate=end
    )

def end(rate_articles_branch):
    return Branch(
        completion_page()
    )