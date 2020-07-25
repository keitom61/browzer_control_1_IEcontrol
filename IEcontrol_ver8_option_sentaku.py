#セレクトボックスから要素を選択、選択をクリック

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
driver.implicitly_wait(10)

# 3.Web 情報を取得(Web ブラウザを開く)
driver.get('http://www.htmq.com/html/select.shtml')

# 普通にエレメントを取得する
horo_element = driver.find_element_by_name('horoscope')

# 取得したエレメントをSelectタグに対応したエレメントに変化させる
horo_select_element = Select(horo_element)

# 選択したいvalueを指定する
horo_select_element.select_by_value('Aquarius')

# formを送付する
horo_element.submit()

# 送信のリンクを選んでクリック
#botton_elem = driver.find_element_by_xpath("//input[@value='リセット']").click()
#y_pos = botton_elem.location["y"]
#driver.execute_script("window.scroll(0 , " + str(y_pos) + ");")
#time.sleep(3)
#botton_elem.click()