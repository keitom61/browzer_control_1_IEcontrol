#googleを別windowで開く
#元のwindowは閉じてからgoogleに文字を入力する

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

# 別windowを開く
driver.execute_script("window.open()")

# 新しいwindowにうつる
driver.switch_to.window(driver.window_handles[1])
driver.get('https://www.google.co.jp')


# 元のwindowにうつる
driver.switch_to.window(driver.window_handles[0])

# 元のwindowを閉じる
driver.close()

# 新しいwindowにうつる
#元のwindowが閉じて[1]から[0]に繰り上がったことに注意
driver.switch_to.window(driver.window_handles[0])

# 検索ワード入力
location = "東京"
search_box = driver.find_element_by_name("q")
search_box.send_keys(location)

# 検索実行
search_box.send_keys(Keys.RETURN)