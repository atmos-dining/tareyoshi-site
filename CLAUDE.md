# たれよしサイト 作業メモ

## プロジェクト概要
- 店舗: 焼肉 たれよし
- URL: https://yakiniku-tareyoshi.com（公式サイトと同ドメインは別途確認）
- ホスティング: GitHub Pages
- リポジトリ: atmos-dining/tareyoshi-site（要作成）
- ブランチ: main

## デザイン
- テーマカラー: 深アンバー #a84400（たれをイメージした温かみのある色）
- フォント: Noto Sans JP
- だるまサイトと同じ構成・レイアウト

## 店舗情報
- 住所: 〒812-0045 福岡県福岡市博多区東公園2-24
- TEL: 092-645-1881
- 営業時間: 17:00〜0:00（L.O. 23:30）年中無休
- 席数: 71席（2フロア）
- 個室: 1〜4名・最大35名
- Instagram: @yakiniku_tareyoshi
- LINE: https://lin.ee/LlGfmMo
- 予約: 電話またはLINE

## 特徴・コンセプト
- 5種類の自家製もみダレ（醤油・塩・みそ・辛みそ・ガーリック）
- 厳選和牛をリーズナブルに
- 看板メニュー: たれ漬けメガカルビ（醤油）¥1,595

## ブログの仕組み
- ブログデータ: blog/posts.json（{ "posts": [...] }形式）
- 記事一覧: blog/index.html
- 記事詳細: blog/posts/post.html?slug=xxx
- 画像: images/ フォルダ

## CMS（Sveltia CMS）
- /admin でログイン
- GitHubリポジトリ atmos-dining/tareyoshi-site が必要
- Cloudflare Worker（共用）: https://sveltia-cms-auth.atmos-nextgen-team.workers.dev

## TODO（初期セットアップ）
- [ ] GitHubリポジトリ atmos-dining/tareyoshi-site 作成
- [ ] GitHub Pages 有効化（Settings → Pages → main / root）
- [ ] 独自ドメイン設定（要確認）
- [ ] 店舗写真をJPGで images/ に追加
  - hero-tareyoshi.jpg, hero-tareyoshi1.jpg, hero-tareyoshi2.jpg（ヒーロー）
  - concept-tareyoshi.jpg（コンセプト）
  - space-tareyoshi.jpg（店内）
  - topic-megakarubi.jpg, topic-tare.jpg, topic-inside.jpg（名物）
  - menu-megakarubi.jpg, menu-wagyu.jpg, menu-horumon.jpg（メニュー）
  - drink-beer.jpg, drink-sour.jpg, drink-shochu.jpg（ドリンク）
  - tareyoshi_logo.png, tareyoshi_icon.png（ロゴ）
- [ ] Google Analytics タグ追加
- [ ] CNAME ファイル追加
- [ ] Google Mapsの埋め込みURLを正しいものに更新（bottom.html）
- [ ] 予約URLの確認（HotPepperがある場合は追加）
- [ ] スタッフをGitHubリポジトリに招待（Write権限）

## 写真について
- 現在 images/ フォルダは空（写真なし）
- 写真が揃い次第 images/ フォルダに追加する
- 画像がない場合はブラウザで背景色（#f0e8e0）が表示される
