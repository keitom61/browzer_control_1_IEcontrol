#HPを開いてからリンクをクリック

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

#要素がみつかるまで、最大10秒間待機する
driver.implicitly_wait(10)

# 3.Web 情報を取得(Web ブラウザを開く)
driver.get('https://monoist.atmarkit.co.jp/mn/articles/1508/19/news018.html')

# メカ設計のリンクを選んでクリック
driver.find_element_by_link_text('メカ設計').click()
#driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/div/table/tbody/tr/td[1]/a').click()