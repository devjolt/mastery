from random import randint, choice

questions = {
    'references_and_keywords': {
        'question_with_0':'Which phrase or word goes with the following reference: PLACEHOLDER',
        'question_with_1':'Which reference matches this phrase: "PLACEHOLDER"',
        'type':['new_pairs'],
        'course_code':'',
        'pairs':(
            ('Matthew 5:14-16', ['Let your light so shine before men', 'light shine']),
            ('Matthew 11:28-30', ['Come unto me, all ye that labour and are heavy laden, and I will give you rest','all ye that labour and are heavy laden', 'I will give you rest', ]),
            ('Matthew 16:15-19', ['I will give unto thee the keys of the kingdom', 'keys of the kingdom']),
            ('Matthew 22:36-39', ["Thou shalt love the Lord thy God. … Thou shalt love thy neighbour", "Thou shalt love the Lord thy God","Thou shalt love thy neighbour"]),
            ('Luke 2:10-12', [f"For unto you is born this day in the city of David a Saviour, which is Christ the Lord", 'For unto you is born this day','in the city of David','a Saviour, which is Christ the Lord']),
            ('Luke 22:19-20', [f"Jesus Christ commanded, partake of the sacrament 'in remembrance of me'.", 'in remembrance of me', 'sacrament']),
            ('Luke 24:36-39', [f"For a spirit hath not flesh and bones, as ye see me have.",'spirit hath not flesh and bones', 'flesh and bones']),
            ('John 3:5', [f"Except a man be born of water and of the Spirit, he cannot enter into the kingdom of God.","Except a man be born of water and of the Spirit","born of water and of the Spirit","cannot enter into the kingdom of God."]),
            ('John 3:16', [f"For God so loved the world, that he gave his only begotten Son.","For God so loved the world", "that he gave his only begotten Son"]),
            ('John 7:17', [f"If any man will do his will, he shall know of the doctrine.","If any man will do his will","he shall know of the doctrine"]),
            ('John 17:3', [f"And this is life eternal, that they might know thee the only true God, and Jesus Christ.","And this is life eternal","that they might know thee","the only true God, and Jesus Christ."]),
            ('1 Corinthians 6:19–20', [f"Your body is the temple of the Holy Ghost.","Your body is the temple","temple of the Holy Ghost"]),
            ('1 Corinthians 11:11', [f"Neither is the man without the woman, neither the woman without the man, in the Lord.","Neither is the man without the woman","neither the woman without the man"]),
            ('1 Corinthians 15:20–22', [f"As in Adam all die, even so in Christ shall all be made alive.","As in Adam all die","even so in Christ shall all be made alive"]),
            ('1 Corinthians 15:40–42', [f"In the Resurrection, there are three degrees of glory","three degrees of glory"]),
            ('Ephesians 1:10', [f"In the dispensation of the fulness of times he might gather together in one all things in Christ.","In the dispensation of the fulness of times","gather together in one all things in Christ"]),
            ('Ephesians 2:19–20', [f"The Church is “built upon the foundation of the apostles and prophets, Jesus Christ himself being the chief corner stone.”","foundation of the apostles and prophets","Jesus Christ himself being the chief corner stone", "chief corner stone"]),
            ('2 Thessalonians 2:1–3', [f"The day of Christ … shall not come, except there come a falling away first.","The day of Christ … shall not come","except there come a falling away first","The day of Christ","falling away"]),
            ('2 Timothy 3:15–17', [f"The holy scriptures … are able to make thee wise unto salvation.","The holy scriptures","wise unto salvation."]),
            ('Hebrews 12:9', [f"fathers of our flesh","Father of spirits"]),
            ('James 1:5–6', [f"If any of you lack wisdom, let him ask of God","If any of you lack wisdom","let him ask of God"]),
            ('James 2:17–18', [f"Faith, if it hath not works, is dead","Faith is dead","Faith, if it hath not works"]),
            ('1 Peter 4:6', [f"The gospel [was] preached also to them that are dead"]),
            ('Revelation 20:12', [f"And the dead were judged … according to their works", "And the dead were judged", "according to their works"]),
        ),
        'fillers': ()
    },
    
    
}
"""
    'references_and_keywords': {
        'question_with_0':'which of the following POSNEG PLACEHOLDER?',
        'positive_negative':('are','could not be described as'),
        'type':['posneg_pairs', 'multi_option_pairs'],
        'course_code':'1',
        'pairs':(
            ('elements of an attack', ['motive','goal','method','vulnerability']),
            ('something other than the elements of an attack', ['risk','threat','identification','disruption','backdoor']),
        ),
        'fillers': ([])  
    },

    'formula of attack': {
        'question':'Which of the following PLACEHOLDERcorrectly describes the formula of an attack?',
        'type':'correct_incorrect',
        'positive':'',
        'negative':'in',
        'course_code':'',
        'correct':(
            'attacks = motive + method + vulnerability',
            'attacks = goal + method + vulnerability',
            'attacks=goal+method+vulnerability',
        ),
        'incorrect': (
            f"attacks = goal + method + ",
            f"attacks = goal +  + vulnerability",
            f"attacks =  + method + vulnerability",
        ),
    },

"""
