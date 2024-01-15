import requests
from bs4 import BeautifulSoup

# URLからHTMLを取得し、BeautifulSoupで解析
url = 'https://www.asahi.com/news/daily/0101.html'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

import requests
from bs4 import BeautifulSoup

# 1ページ目から7ページ目までスクレイピング
for page in range(101, 108):
    url = f'https://www.asahi.com/news/daily/0{page}.html'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # スクレイピングのロジックをここに追加
    
    import requests
from bs4 import BeautifulSoup

# ベースURL
base_url = 'https://www.asahi.com/news/daily/'

# 文字コードをUTF-8に設定
encoding = 'utf-8'

# 1ページ目から7ページ目までスクレイピング
for page in range(101, 108):  # 0101から0107まで
    url = f'{base_url}0{page}.html'
    
    response = requests.get(url)
    response.raise_for_status()
    response.encoding = encoding

    soup = BeautifulSoup(response.text, 'html.parser')
    news_list = soup.find('ul', class_='List')

    # 最初のニュース項目を取得
    first_news_item = news_list.find('li', recursive=False)
    title = first_news_item.get_text().strip()
    link = first_news_item.find('a')['href']

    # 相対リンクを絶対リンクに変換
    if link.startswith('/'):
        link = 'https://www.asahi.com' + link

    print(f'1月{page - 100}日, {title},  {link}\n')
    
    import sqlite3
import requests
from bs4 import BeautifulSoup

# データベースに接続（存在しない場合は新規作成）
conn = sqlite3.connect('news.db')
c = conn.cursor()

# ニュースデータを格納するためのテーブルを作成
c.execute('''
    CREATE TABLE IF NOT EXISTS news (
        date TEXT,
        title TEXT,
        link TEXT
    )
''')

# ベースURL
base_url = 'https://www.asahi.com/news/daily/'

# 文字コードをUTF-8に設定
encoding = 'utf-8'

# 1ページ目から7ページ目までスクレイピング
for page in range(101, 108):  # 0101から0107まで
    url = f'{base_url}0{page}.html'
    
    response = requests.get(url)
    response.raise_for_status()
    response.encoding = encoding

    soup = BeautifulSoup(response.text, 'html.parser')
    news_list = soup.find('ul', class_='List')

    # 最初のニュース項目を取得
    first_news_item = news_list.find('li', recursive=False)
    title = first_news_item.get_text().strip()
    link = first_news_item.find('a')['href']

    # 相対リンクを絶対リンクに変換
    if link.startswith('/'):
        link = 'https://www.asahi.com' + link

    # データベースにデータを挿入
    c.execute('INSERT INTO news (date, title, link) VALUES (?, ?, ?)', 
              (f'1月{page - 100}日', title, link))

    # 挿入したデータをコミット
    conn.commit()

# データベースのクローズ
conn.close()

import pandas as pd

# CSVファイルを読み込むが、データは読み込まない
df = pd.read_csv('/Users/shuma/Lecture/programing/dsprogsaisyuu/dsprogramming-muro/2024news.csv', nrows=0)

# ヘッダー行を表示
print(df.columns.tolist())

# CSVファイルを開く
with open('/Users/shuma/Lecture/programing/dsprogramming-muro/2024news.csv', mode='r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)

    # ヘッダー行をスキップする場合
    next(csv_reader)

    # 行ごとに読み込む
    for row in csv_reader:
        print(row)
        
import pandas as pd
import sqlite3

# CSVファイルのパス
csv_file = '/Users/shuma/Lecture/programing/dsprogsaisyuu/dsprogramming-muro/2024news.csv'

# SQLiteデータベースファイルのパス（存在しない場合は新規作成されます）
db_file = 'example.db'

# CSVファイルをデータフレームとして読み込む
df = pd.read_csv(csv_file)

# SQLiteデータベースに接続
conn = sqlite3.connect(db_file)

# データフレームをデータベースのテーブルに保存（テーブル名は 'news_table' とします）
# 既にテーブルが存在する場合は置き換える
df.to_sql('news_table', conn, if_exists='replace', index=False)

# 接続を閉じる
conn.close()

