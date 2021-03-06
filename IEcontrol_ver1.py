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
ie = webdriver.Ie("./driver/IEDriverServer.exe")

# 検索対象の入力
id_number = input("ID:")
password_number = input("password:")

# 3.Web 情報を取得(Web ブラウザを開く)
ie.get("https://www.yutolife.com/user/pre_login.html")

# ログインIDとパスワードの入力
id_box = ie.find_element_by_name("login_id")
input_words = id_number
id_box.send_keys(input_words)

password_box = ie.find_element_by_name("password")
input_words = password_number
password_box.send_keys(input_words)

# 実行
password_box.send_keys(Keys.RETURN)
print(ie.title)

# 2.IEドライバ終了処理
#driver.close()