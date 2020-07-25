#HPを開いてからリンクをクリックしてできた、新しいウィンドウに移動

import time
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
# Selectタグが扱えるエレメントに変化させる為の関数を呼び出す
from selenium.webdriver.support.ui import Select

# 1.IEドライバのセットアップ
driver = webdriver.Ie()

#要素がみつかるまで、最大10秒間待機する
driver.implicitly_wait(60)

# 3.Web 情報を取得(Web ブラウザを開く)
driver.get('https://nlab.itmedia.co.jp/nl/articles/2005/03/news010_2.html')

# 新しいウィンドウを開くリンクを選んでクリック
driver.find_element_by_partial_link_text('脳内法廷は大騒ぎ').click()

# 元のwindowにうつる
driver.switch_to.window(driver.window_handles[0])

# 元のwindowを閉じる
driver.close()