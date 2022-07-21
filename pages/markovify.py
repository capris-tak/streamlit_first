import streamlit as st

from janome.tokenizer import Tokenizer
import pandas as pd
#import collections
#from wordcloud import WordCloud

file = 'pages/Hermann_Hesse.txt' 
f = open(file, 'r', encoding="utf-8")
text = f.read()

def text_split(text):
    # textをmarkovifyで読み取れるように前処理を行う関数です。
    
    # 引数：text
    # 引数の型：str
    
    # 戻り値：splitted_text_str
    # 引数の型：str
    
    # 今回は複数の文字列を一回で置換できるようにします。
    # maketransで置換する文字列の置き換え表を作成して、
    # str_tableという変数に入れる
    
    str_table = str.maketrans({
        # markovifyで読み取れるよう該当する文字の置換。
        # https://github.com/jsvine/markovify/issues/84
        # アンケートデータ内に「。」がついているものとついていないものがあります。
        # 表記を統一するため一旦、「。」を削除し、
        # 「'\n'」を「。」で置換する。文末が「。」で終わるように統一します。
        
        # 例：句点「。」がついているものと、ついていないものがあります。
        # 喉 越しが良いから。\n　自分に合っている\n
        # 。を削除　↓
        # 喉越しが良いから\n　自分に合っている\n
        #　\nを。で置換
        # 喉越しが良いから。　自分に合っている。
        
        #文字列の置き換え表　
        #変換前 : 変換後
        '。': '',   
        '\n': '。',
        '\r': '',
        '(': '（',
        ')': '）',
        '[': '［',
        ']': '］',
        '"':'”',
        "'":"’",
    })
    # 文字列をstr_tableの情報を用いて置換します。
    text = text.translate(str_table)
    
    # textを単語分割（文章を形態素で分ける）
    # wakati=Trueで分かち書き（単語分割）モードにできるのでこれを利用して、
    # 戻り値、文字列 (str) のリストを返します。
    # 例：['分かち書き', 'モード', 'が', 'つき', 'まし', 'た', '！']
    
    t = Tokenizer()
    tokens = t.tokenize(text, wakati=True)
    
    # splitted_text_listを用意します。
    splitted_text_list = []
    # 分かち書きされているtokensを一つずつ処理していき
    # 「。」や感嘆符でなければ、文字の後にスペース、
    # 「。」や感嘆符であれば、「'\n'」に置換
    # splitted_text_listに連結。
    # リストの要素を連結し、一つの文字列にして返します。
    for i in tokens:
        if i != '。' and i != '！' and i != '？':
            i += ' '
        elif i == '。' or i == '！' or i == '？':
            i = '\n'
        splitted_text_list.append(i)
        splitted_text_str = "".join(splitted_text_list)
            
    return splitted_text_str

import markovify
splitted_text_str = text_split(text)
text_model = markovify.NewlineText(splitted_text_str, state_size=3)

for i in range(5):
    st.write(text_model.make_sentence(tries=1000))
    st.write("---------------------------------")


st.caption("---------------------------------")


txt = st.text_area('Text to analyze', '''
It was the best of times, it was the worst of times, it was
the age of wisdom, it was the age of foolishness, it was
the epoch of belief, it was the epoch of incredulity, it
was the season of Light, it was the season of Darkness, it
was the spring of hope, it was the winter of despair, (...)
''', height=200)
st.write('Sentiment:', text_split(txt))

if txt != None:
    splitted_txt_str = text_split(txt)
    txt_model = markovify.NewlineText(splitted_txt_str, state_size=3)
    for i in range(5):
        st.write(txt_model.make_sentence(tries=1000))
        st.write("---------------------------------")

        
st.write('''
今回は、マルコフ連鎖をPythonで実装して実際に文章自動生成をやってみたという動画になります。
文章自動生成というとなんだか難しそう…という方のために、わかりやすく解説しています！
そのため、初心者の方や学び始めた方にとって、最適な動画となっております。
＜初心者に嬉しい３つのポイント＞
・使うライブラリがわかる！
・図解入りの説明でコードの仕組みがわかる！（他の動画にはない最大のポイント！）
・すぐに使えるJupyter Notebookつき！（GitHubでダウンロード可）
また、文章自動生成に挑戦してみたかったけど、結局作り方がよくわからなかった…という方にもオススメな動画です。
ぜひこの動画で、作り方の流れを学びましょう！
https://www.youtube.com/watch?v=I_2WlQDPQOA
https://qiita.com/mapps/items/c0d3f1b73bc9ef398790
【下記、公式ドキュメントを日本語訳にしたもの】
「Markovify は、大きくて句読点の整ったテキストに最適に動作します。
テキストが文の区切りに .s を使用していない場合は、各文を改行して、 markovify.Text クラスの代わりに markovify.NewlineText クラスを使用してください。」
今回は各文を「\n」で改行しているので「markovify.NewlineText」を使用します。 
ewlineTextにtextを入れてモデルを作成します。
state_sizeでは「◯階」の「◯」を指定し、何単語ずつのブロックに分けるか指定します。
今回は2単語ずつのブロックに分けるため「state_size=2」と指定（※デフォルトも2）。
これで「2階マルコフ連鎖のモデルを作りますよ」という意味となる。
text_modelモデルでmake_sentenceメソッドを用いて文章を生成します。
make_sentenceメソッドでは、元の文章と重ならないように、1回の呼び出しで何回試行を行うか、
tries（トライズ）で試行回数を指定することができます。
ここでは一旦、triesに100と入れています。（10回でも20回でもOK）。
for i in range(10)で作成する文章の数を決めます。
今回はとりあえず10個生成してみましょう。
printで「"---------------------------------"」と記載しています。
これは生成された文章がまとまって出てきて、どこが1文かわかりづらい状態で出力されるため、
生成された文章を1文ずつ区切るために使用しています。
''')
