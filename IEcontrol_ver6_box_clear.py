#googleを開いてからいったん入力した文字を消す

# webdriver の情報
from selenium import webdriver
# html の タブの情報を取得
from selenium.webdriver.common.by import By
# キーボードを叩いた時に web ブラウザに情報を送信する
from selenium.webdriver.common.keys import Keys
# 次にクリックしたページがどんな状態になっているかチェックする
from selenium.webdriver.support import expected_conditions as EC
# 待機時間を設定
from selenium.webdriver.support.ui import WebDriverWait
# 確認ダイアログ制御
from selenium.webdriver.common.alert import Alert

# 1.IEドライバのセットアップ
driver = webdriver.Ie()

# 3.Web 情報を取得(Web ブラウザを開く)
driver.get('https://www.google.co.jp')

# 検索ワード入力
location = "東京"
search_box = driver.find_element_by_name("q")
search_box.send_keys(location)

# 検索ワードを消す
search_box.clear()