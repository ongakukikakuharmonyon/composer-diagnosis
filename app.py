import streamlit as st
import random

# 診断データを定義
# ----------------------------------------------------------
# 作曲家タイプ一覧
composer_types = {
    'A': {'name': 'ベートーヴェン', 'type': '不屈の情熱家', 'text': 'あなたは、困難な状況であるほど燃え上がる不屈の精神の持ち主。一度決めた目標に向かって、情熱的に突き進む力強さがあります。あなたのその姿は、周りの人に勇気と希望を与えるでしょう。まさに、運命の喉首を締め上げるような力強い魂を持った革命家です。'},
    'B': {'name': 'モーツァルト', 'type': '天才肌の自由人', 'text': 'あなたは、生まれながらの才能と遊び心を兼ね備えた天才肌。好奇心旺盛で、人生を楽しむことが得意です。あなたの周りには自然と人が集まり、その自由で明るい雰囲気で場を和ませます。退屈なルールよりも、直感的なひらめきを大切にするタイプです。'},
    'C': {'name': 'バッハ', 'type': '偉大なる探求者', 'text': 'あなたは、物事を構造的に捉え、コツコツと努力を積み重ねることができる勤勉な探求者です。一見、控えめで内省的に見えますが、内には揺るぎない信念と論理的な思考を持っています。あなたの仕事は常に丁寧で、その積み重ねがやがて偉大な成果へと繋がるでしょう。'},
    'D': {'name': 'ショパン', 'type': '繊細なロマンチスト', 'text': 'あなたは、非常に感受性豊かで繊細な心を持ったロマンチスト。美しいものや詩的な世界に深く心を動かされます。一人で静かに物思いにふける時間を大切にし、その内面には豊かな感情の世界が広がっています。あなたの言葉や表現は、周りの人の心に優しく響きます。'},
    'E': {'name': 'ドビュッシー', 'type': '感覚のアーティスト', 'text': 'あなたは、常識や既存のルールに縛られない、個性的な感性の持ち主です。誰も思いつかないような新しい視点で物事を捉え、直感を信じて行動します。あなたのユニークな世界観は、時に周りを驚かせますが、それが新しい時代の扉を開く鍵となるでしょう。'},
    'F': {'name': 'シューマン', 'type': '二つの顔を持つ思索家', 'text': 'あなたは、知的な冷静さと豊かな感情という、二つの側面を併せ持っています。文学や物語を愛し、物事の裏にあるストーリーを読み解くのが得意です。理性と感情のバランスを取りながら、深く物事を考える思索家タイプです。'},
    'G': {'name': 'リスト', 'type': '華やかなカリスマ', 'text': 'あなたは、圧倒的な存在感とスター性を放つカリスマ。常に注目を集め、人々を惹きつける華やかさを持っています。情熱的でパフォーマンス精神も旺盛。自分の才能を最大限に発揮して、多くの人を魅了する力があります。'},
    'H': {'name': 'マーラー', 'type': '壮大な哲学者', 'text': 'あなたは、物事の本質や人生の意味について考える、壮大なスケールを持った哲学者です。日常の些細な出来事からも、宇宙的な真理を見出そうとします。その深い精神性は、あなたの世界観をどこまでも広げていくでしょう。'},
    'I': {'name': 'ストラヴィンスキー', 'type': '大胆な革命家', 'text': 'あなたは、古い常識を打ち破り、新しい時代を切り拓く大胆な革命家です。論理的な思考に基づき、革新的で時には過激なアイデアを生み出します。周りからどう思われるかよりも、自分が信じる「新しさ」を追求する強さを持っています。'},
    'J': {'name': 'プーランク', 'type': '洒脱な社交家', 'text': 'あなたは、ウィットに富んだ会話と洒脱なセンスで人を楽しませるのが得意な社交家です。軽快でユーモアがあり、どんな場でも明るい雰囲気を作り出します。人生の楽しい側面を見つけるのがうまく、あなたの周りはいつも笑顔で溢れています。'},
    'K': {'name': 'ラヴェル', 'type': '完璧を求める職人', 'text': 'あなたは、細部にまでこだわり、完璧なものを創り上げることに情熱を燃やす職人気質。精密な作業を得意とし、冷静な分析力で物事を進めます。あなたの手にかかれば、どんなものも洗練された芸術品のように仕上がるでしょう。'},
    'L': {'name': 'シベリウス', 'type': '孤高の思想家', 'text': 'あなたは、都会の喧騒から離れ、静かな自然の中で思索にふけることを好む孤高の思想家です。他人に流されることなく、自分の内なる声に耳を傾けます。その落ち着いた佇まいと独立した精神は、あなたにしかない独特の深みを与えています。'}
}

# 質問と選択肢、ポイント加算ロジック
# valueは加点されるタイプのキー(文字列)またはキーのリスト
questions = [
    {
        'question': 'Q1. 新しい一週間が始まります。あなたの心境は？',
        'answers': {
            'A: よし、今週もやるぞ！目標に向かって突き進む！': 'A',
            'B: 新しい出会いや発見があるかな？ワクワクする。': 'B',
            'C: 静かに自分のペースで、計画通りに進めたい。': 'C',
            'D: 少し憂鬱...。自分の世界に浸る時間がほしい。': 'D'
        }
    },
    {
        'question': 'Q2. 友人へのプレゼント、何を選ぶ？',
        'answers': {
            'A: 相手をあっと驚かせる、派手で豪華なもの。': 'G',
            'B: 誰も知らないような、個性的でアーティスティックな雑貨。': 'E',
            'C: 相手の趣味を徹底的にリサーチし、実用的なものを贈る。': 'K',
            'D: その場のノリとひらめきで、面白グッズを選ぶ。': 'J'
        }
    },
    {
        'question': 'Q3. あなたが物語を書くなら、どんなテーマ？',
        'answers': {
            'A: 一人の天才が常識を覆し、世界を変える物語。': 'I',
            'B: 壮大な宇宙と生命の謎に迫る、哲学的な物語。': 'H',
            'C: 知性と感情の間で揺れ動く、内面的な葛藤の物語。': 'F',
            'D: 都会の喧騒を離れ、自然と共に生きる人の物語。': 'L'
        }
    },
    {
        'question': 'Q4. 仕事や勉強で、あなたが最も評価されたいポイントは？',
        'answers': {
            'A: どんな困難も乗り越える、その精神力と情熱。': 'A',
            'B: 完璧に仕上げられた、その精密さとクオリティの高さ。': 'K',
            'C: 誰も思いつかない、そのユニークな発想力。': 'E',
            'D: チームを明るくする、その社交性とユーモア。': 'J'
        }
    },
    {
        'question': 'Q5. 旅に出るなら、どんな場所に行きたい？',
        'answers': {
            'A: 歴史的な建造物が並ぶ、秩序だった美しい街並み。': 'C',
            'B: 人々が集まる華やかなリゾート地や都会。': 'G',
            'C: 静寂に包まれた、手つかずの雄大な自然。': 'L',
            'D: 芸術家たちが集う、自由な雰囲気の街。': 'B'
        }
    },
    {
        'question': 'Q6. あなたが「美しい」と感じる瞬間は？',
        'answers': {
            'A: 緻密に計算された、完璧なシンメトリーを見たとき。': 'K',
            'B: 自分の内なる感情が、詩や音楽と重なったとき。': 'D',
            'C: 古い価値観が壊され、新しいものが生まれる瞬間。': 'I',
            'D: 人生の喜びや悲しみ、そのものすべて。': 'H'
        }
    },
    {
        'question': 'Q7. 議論になった時、あなたのスタンスは？',
        'answers': {
            'A: 論理的に矛盾点を突き、冷静に相手を説得する。': 'C',
            'B: 自分の信念を、熱意を持って情熱的に語る。': 'A',
            'C: 対立は好まない。ウィットを交えて平和的に収めたい。': 'J',
            'D: そもそも議論は苦手。自分の意見は心にしまっておく。': 'D'
        }
    },
    {
        'question': 'Q8. あなたの部屋はどんな状態？',
        'answers': {
            'A: 物は少ない。静かで思索にふけることができる空間。': 'L',
            'B: 好きな本やアートが飾られ、二つの世界観が同居している。': 'F',
            'C: いつでも人を呼べるように、楽しくて社交的な雰囲気。': 'B',
            'D: 型にはまらない、自分の感性だけで作られた空間。': 'E'
        }
    },
    {
        'question': 'Q9. 自分の性格を一言で表すなら？',
        'answers': {
            'A: 華やかで目立つ「スター」。': 'G',
            'B: 二面性を持つ「思索家」。': 'F',
            'C: 常識を壊す「革命家」。': 'I',
            'D: 壮大なビジョンを持つ「哲学者」。': 'H'
        }
    },
    {
        'question': 'Q10. 人生のゴールとは何だと思いますか？',
        'answers': {
            'A: 完璧な作品や仕事を、後世に残すこと。': 'K',
            'B: 多くの人に影響を与え、世界をより良く変えること。': ['A', 'I'],
            'C: 自分の内なる世界を、深く深く探求し続けること。': ['D', 'H'],
            'D: とにかく楽しく、自由に、人生を謳歌すること。': ['B', 'G']
        }
    }
]
# ----------------------------------------------------------

# Streamlitアプリのセッション管理
def initialize_session_state():
    if 'screen' not in st.session_state:
        st.session_state.screen = 'start'
    if 'scores' not in st.session_state:
        st.session_state.scores = {key: 0 for key in composer_types.keys()}
    if 'current_question' not in st.session_state:
        st.session_state.current_question = 0
    if 'result_type' not in st.session_state:
        st.session_state.result_type = None

# 画面描画の関数
def show_start_screen():
    st.title('🎼 作曲家タイプ診断')
    st.write('いくつかの質問に答えて、あなたの性格に合った作曲家タイプを見つけましょう！')
    if st.button('診断をはじめる'):
        st.session_state.screen = 'question'
        st.experimental_rerun()

def show_question_screen():
    q_index = st.session_state.current_question
    st.title(f"質問 {q_index + 1}/{len(questions)}")
    
    # プログレスバーを追加
    progress_value = (q_index) / len(questions)
    st.progress(progress_value)

    st.write(f"**{questions[q_index]['question']}**")

    # 選択肢をボタンとして表示
    for answer_text, type_keys in questions[q_index]['answers'].items():
        if st.button(answer_text):
            # 複数のキーに加点する場合に対応
            if isinstance(type_keys, list):
                for key in type_keys:
                    st.session_state.scores[key] += 1
            else:
                st.session_state.scores[type_keys] += 1
            
            # 次の質問へ進むか、結果表示へ
            if st.session_state.current_question < len(questions) - 1:
                st.session_state.current_question += 1
            else:
                st.session_state.screen = 'result'
                calculate_result()
            st.experimental_rerun()

def show_result_screen():
    result_type_key = st.session_state.result_type
    result = composer_types[result_type_key]

    st.title('診断結果')
    st.header(f'あなたは **{result["name"]}タイプ** - {result["type"]} です！')
    
    # 結果表示を少しリッチに
    st.image(f"https://via.placeholder.com/600x300.png/E8DAEF/7F00FF?text={result['name'].replace(' ', '+')}", use_column_width=True) # 仮の画像
    st.markdown(f"--- \n ### {result['type']} の特徴")
    st.write(result['text'])
    
    # (オプション) 各スコアを表示して、透明性を出す
    with st.expander("あなたのスコア詳細を見る"):
        st.write(st.session_state.scores)

    if st.button('もう一度診断する'):
        # 状態をリセットしてスタート画面へ
        for key in st.session_state.keys():
            del st.session_state[key]
        initialize_session_state()
        st.experimental_rerun()

# 結果計算ロジック
def calculate_result():
    scores = st.session_state.scores
    max_score = -1
    max_types = []

    for type_key, score in scores.items():
        if score > max_score:
            max_score = score
            max_types = [type_key]
        elif score == max_score:
            max_types.append(type_key)

    # 同点の場合はランダムで1つ選ぶ
    st.session_state.result_type = random.choice(max_types)

# ---- メインロジック ----
initialize_session_state()

if st.session_state.screen == 'start':
    show_start_screen()
elif st.session_state.screen == 'question':
    show_question_screen()
elif st.session_state.screen == 'result':
    show_result_screen()
