from random import randint, choice

questions = {
    'references_and_phrases': {
        'question_with_0':'Which phrase goes with the following reference: PLACEHOLDER',
        'question_with_1':'Which reference matches this phrase: "PLACEHOLDER"',
        'type':['new_pairs'],
        'course_code':'',
        'pairs':(
            ('Matthew 5:14-16', ['Let your light so shine before men', 'light shine', 'light', 'shine']),
            ('Matthew 11:28-30', ['Come unto me, all ye that labour and are heavy laden, and I will give you rest','rest','all ye that labour and are heavy laden', 'I will give you rest', ]),
            ('Matthew 16:15-19', ['I will give unto thee the keys of the kingdom', 'keys of the kingdom', "keys"]),
            ('Matthew 22:36-39', ["Thou shalt love the Lord thy God. … Thou shalt love thy neighbour", "Thou shalt love the Lord thy God","Thou shalt love thy neighbour","love thy neighbour","love the Lord thy God"]),
            ('Luke 2:10-12', [f"For unto you is born this day in the city of David a Saviour, which is Christ the Lord", 'For unto you is born this day','in the city of David','a Saviour, which is Christ the Lord']),
            ('Luke 22:19-20', [f"Jesus Christ commanded, partake of the sacrament 'in remembrance of me'.", 'in remembrance of me', 'sacrament']),
            ('Luke 24:36-39', [f"For a spirit hath not flesh and bones, as ye see me have.",'spirit hath not flesh and bones', 'flesh and bones']),
            ('John 3:5', [f"Except a man be born of water and of the Spirit, he cannot enter into the kingdom of God.","Except a man be born of water and of the Spirit","born of water and of the Spirit","cannot enter into the kingdom of God."]),
            ('John 3:16', [f"For God so loved the world, that he gave his only begotten Son.","For God so loved the world", "that he gave his only begotten Son", "only begotten Son"]),
            ('John 7:17', [f"If any man will do his will, he shall know of the doctrine.","If any man will do his will","he shall know of the doctrine","doctrine", "will"]),
            ('John 17:3', [f"And this is life eternal, that they might know thee the only true God, and Jesus Christ.","And this is life eternal","that they might know thee","the only true God, and Jesus Christ","life eternal", "the only true God"]),
            ('1 Corinthians 6:19–20', [f"Your body is the temple of the Holy Ghost.","Your body is the temple","temple of the Holy Ghost", "temple"]),
            ('1 Corinthians 11:11', [f"Neither is the man without the woman, neither the woman without the man, in the Lord.","Neither is the man without the woman","neither the woman without the man", "man", "woman"]),
            ('1 Corinthians 15:20–22', [f"As in Adam all die, even so in Christ shall all be made alive.","As in Adam all die","even so in Christ shall all be made alive", "Adam", "all be made alive"]),
            ('1 Corinthians 15:40–42', [f"In the Resurrection, there are three degrees of glory","three degrees of glory"]),
            ('Ephesians 1:10', [f"In the dispensation of the fulness of times he might gather together in one all things in Christ.","In the dispensation of the fulness of times","gather together in one all things in Christ", "fulness of times", "gather together"]),
            ('Ephesians 2:19–20', [f"The Church is “built upon the foundation of the apostles and prophets, Jesus Christ himself being the chief corner stone.”","foundation of the apostles and prophets","Jesus Christ himself being the chief corner stone", "chief corner stone", "foundation"]),
            ('2 Thessalonians 2:1–3', [f"The day of Christ … shall not come, except there come a falling away first","The day of Christ … shall not come","except there come a falling away first","The day of Christ","falling away"]),
            ('2 Timothy 3:15–17', [f"The holy scriptures … are able to make thee wise unto salvation.","The holy scriptures","wise unto salvation", "scriptures"]),
            ('Hebrews 12:9', [f"fathers of our flesh","Father of spirits", "Father"]),
            ('James 1:5–6', [f"If any of you lack wisdom, let him ask of God","If any of you lack wisdom","let him ask of God", "lack wisdom"]),
            ('James 2:17–18', [f"Faith, if it hath not works, is dead","Faith is dead","Faith, if it hath not works", "works", "without works"]),
            ('1 Peter 4:6', [f"The gospel [was] preached also to them that are dead", "preached also to them that are dead"]),
            ('Revelation 20:12', [f"And the dead were judged … according to their works", "And the dead were judged", "according to their works", "Judged", "book of life", "another book was opened"]),
        ),
        'fillers': ()
    },
    'references_and_descriptions': {
        'question_with_0':'Which description goes with the following reference: PLACEHOLDER',
        'question_with_1':'Which reference matches this description: PLACEHOLDER',
        'type':['new_pairs'],
        'course_code':'',
        'pairs':(
            ('Matthew 5:14-16', ['Share your talents', f"Analagy to do with {choice(['candles', 'light'])}"]),
            ('Matthew 11:28-30', ['The Saviour can help carry our burdens','Being yoked with the Saviour makes our load lighter']),
            ('Matthew 16:15-19', ['I will give unto thee the keys of the kingdom', 'keys of the kingdom']),
            ('Matthew 22:36-39', ["Love is the beginning and end of the law", "The first great commandment","Love your neighbour as yourself"]),
            ('Luke 2:10-12', [f"Birth of the saviour", 'A message from Angels to shepherds','Location of Jesus\' birth','Sheperds are told the Saviour\'s name']),
            ('Luke 22:19-20', [f"The sacrament", 'The disciples were taught how to remember the Saviour', 'Jesus institutes the sacrament', 'bread is symbolic of Jesus\' body', 'Wine is symbolic of Jesus\' blood', 'This happenned just before Jesus was crucified']),
            ('Luke 24:36-39', [f"Occurred following the resurrection",'The Saviour showed himself to his disciples after his death', 'The disciples saw the marks in the Saviour\'s hands and feet']),
            ('John 3:5', [f"A meeting between the Saviour and {choice(['Nicodemus','a pharisee', 'a man who came to see him at night'])}","We must be baptised and confirmed","We must be born again","How to enter the kingdom of heaven"]),
            ('John 3:16', [f"The reason that Jesus Christ was sacrified","About God's love", "How much God loves us"]),
            ('John 7:17', [f"How to know if doctrine is true","How to know if someone is speaking of themselves or of God"]),
            ('John 17:3', [f"The reason we must come to know God","How to get eternal life",f"The importance of coming to know {choice(['God', 'Jesus Christ', 'God and Jesus Christ'])}"]),
            ('1 Corinthians 6:19–20', [f"Teaching about the importance of the body","Why we should keep our bodies clean","Using a temple as a metaphor for the body"]),
            ('1 Corinthians 11:11', [f"About marriage","Marriage","Men and Women are meant to work together"]),
            ('1 Corinthians 15:20–22', [f"Adam fell that men might be","Christ made it possible to reverse the consequences of Adam's transgression","We can have eternal life through Christ"]),
            ('1 Corinthians 15:40–42', [f"The sun, moon and stars","Celestial, Terrestrial and Telestial kingdoms","Three kingdoms of glory","The three degrees of glory"]),
            ('Ephesians 1:10', [f"In the dispensation of the fulness of times he might gather together in one all things in Christ.","In the dispensation of the fulness of times","gather together in one all things in Christ"]),
            ('Ephesians 2:19–20', [f"The structure of the church","Prophets and apostles","Jesus Christ is the center of His church", "Uses the analagy of a building to describe the leadership of the church"]),
            ('2 Thessalonians 2:1–3', [f"Prophecy of the apostacy","About the apostacy","The end will not come before there has been a great apostacy"]),
            ('2 Timothy 3:15–17', [f"The scriptures can help us know the way to be saved","The importance of the scriptures"]),
            ('Hebrews 12:9', [f"Comparison between earthly and spiritual parents","God is our Heavenly Father", "God is the Father of our spirits", "We should listen to God because he is the father of our spirits"]),
            ('James 1:5–6', [f"If you lack wisdom, you can ask God","God will not hold back if we ask him something","If we ask in faith, God will give us wisdom", "If there is something we need to know, we can ask God"]),
            ('James 2:17–18', [f"Belief without action is pointless","Faith should lead to good works","Faith by itself isn't enough"]),
            ('1 Peter 4:6', [f"The Saviour preached to people in the spirit world", "The gospel was preached to spirits"]),
            ('Revelation 20:12', [f"The small and great will all be judged", "About the final judgement", "Everyone will be judged", "The dead are judged using what is written in the book of life"]),
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
