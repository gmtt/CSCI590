import json

from stackapi import StackAPI


def fetch(SITE, PAGE_SIZE):
    my_questions = []
    for page in range(1, 10):
        questions = SITE.fetch('/questions',
                               filter='!LZg2O0N6oRxnBg-ybCLGaM',
                               page=page,
                               pagesize=PAGE_SIZE)

        for question in questions['items']:
            my_question = {
                'tags': question['tags'],
                'title': question['title'],
                'body': question['body_markdown'],
                'answers': [],
                'up_vote_count': question['up_vote_count'],
                'view_count': question['view_count']
            }
            if 'answers' in question:
                for answer in question['answers']:
                    my_question['answers'].append(answer['body_markdown'])
            my_questions.append(my_question)
    with open('raw_data.json', 'w') as out:
        json.dump(my_questions, out)


if __name__ == '__main__':
    SITE = StackAPI('stackoverflow')
    PAGE_SIZE = 10
    fetch(SITE, PAGE_SIZE)
