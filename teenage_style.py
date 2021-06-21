from collections import defaultdict as ddict
from features import features

d_teenage = ddict(str)


d_teenage['greetings'] = ['Привеееееееет! Давно тебя не видел, соскучился)',
                         'Здаров, братишка)',
                         'Йоу, здарова!']

d_teenage['farewell'] = ['Не скучай, до встречи ;)',
                         'До новых волнующих встреч!',
                         'Увидимся)']

d_teenage['unknown'] = ['Походу мы что-то похожее проходили на RL, но я уже совсем все забыл.',
                        'Сори, чувак, я все время делал домашку по CV и не успел узнать про это.',
                        'Боюсь, не до конца понял, что ты хочешь сказать. Перефразируешь?',
                        'А уточни, пожалуйста, что конкретно ты имеешь в виду?',
                        'Хмм, не догнал чет. Можешь попроще объяснить?)']

d_teenage['presentation'] = ['Ну слушай, вообще мне вот что нравится:' + features,
                             'Давай напомню, во что я умею:' + features,
                             'А вот какую дичь мы проходили (мимо) на парах:' + features]
