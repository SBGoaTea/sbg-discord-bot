from random import choice, randint

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return 'Inrovert... Makes sense'
    elif 'hello' in lowered:
        return 'Waddup doe!'
    elif 'how are you' in lowered:
        return 'Well with everything going on, could be better'
    elif 'bye' in lowered:
        return 'Ope, see you later then.'
    elif 'roll dice' in lowered:
        return f'You rolled: {randint(1,6)}'
    else:
        return choice([
        "This is a good place to start. Lets relax for a moment into this 'don't know' place."
        ,"Remember that just because you answer, doesn't mean you need to do anything about it."
        ,"You may want to use a softener before this question: 'What are you pretending not to know?'"
        ,"I feel that too sometimes. Take a moment and let me know when you've thought of something"
        ,"What if you secretly knew the answer?"
        ,"So, what's underneath the 'I don't know?' What are you avoiding?"
        ,"What is it like for you to not know?"
        ,"How do you feel right now as you think about answering this question?"
        ,"Hmmmm. Take a deep breath and just allow yourself feel into the question for a second."
        ])