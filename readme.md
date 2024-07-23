# 36小時內的天氣預報

## 專案概述
此專案使用Python提供36小時的天氣預報。資料每天分別於上午6:00和下午6:00更新，並利用市政府的公開資訊和各種網絡資源。

## 動機
了解每日的天氣情況是一個常見的做法，因為天氣對日常活動有著重要影響。這種動機促使我創建了這個專案。

## 執行過程
專案從中央氣象局讀取天氣資料，並使用Unsplash API取得與天氣條件相符的背景圖片。該專案通過GitHub Actions實現自動化，並將完成的預報圖片發送到Line群組中。

## 資料來源
- 天氣資料: [中央氣象局的公開網站](https://opendata.cwa.gov.tw/dataset/forecast/F-C0032-001)
- 圖片: [Unsplash API](https://unsplash.com/developers)

排程執行時間來源: [it-tools Crontab generator](https://it-tools.tech/crontab-generator)