# AION 2 Guides(日本語版フォーク)

**AION 2 グローバル版シーズン1** のクラスガイドとトラッカー。英語・ロシア語・ウクライナ語・トルコ語・日本語で読める。スキル、アイテム、ディーヴァニオン ボードのデータはグローバル版クライアントのもの(questlog.gg 経由)、ビルドは配信者・クリエイターのガイドが元で、各ページに出典を明記している。

このリポジトリは [Couga54/aion2-guides](https://github.com/Couga54/aion2-guides) を個人用に改良したフォークで、日本語版を追加している。日本語のゲーム内名称は日本語クライアントの表記(questlog.gg の `ja` データ)を使う。

**公開サイト:** https://watao56.github.io/aion2-HP/

## サイトの内容

| クラス | PvE | PvP | レベリング | ディーヴァニオン ボード |
|---|---|---|---|---|
| グラディエーター | ✅ | ✅ | ✅ | PvE、PvP、レベリング |
| テンプラー | ✅ | ✅ | ✅ | PvE、PvP |
| レンジャー | ✅ | — | ✅ | PvE |
| アサシン | ✅ | — | ✅ | PvE |
| チャンター | ✅ | — | ✅ | PvE |
| クレリック | ✅ | ✅ | ✅ | PvE、PvP |
| ソーサラー | ✅ | — | ✅ | PvE |
| スピリットマスター | ✅ | ✅ | ✅ | PvE、PvP |

PvP モードは、ちゃんとした出典があるクラスだけ有効にしている。

クラスガイド以外のページ:

- **Lv45 以降**(進行)と **採集と製作**: レベル上限後にやること、装備強化の基本、生産。
- **ダンジョン**: ローンチ時ダンジョンのボスギミックをアリーナ図付きで。
- **ティアリスト**: 複数のクリエイターの評価をコンテンツ別に並べ、その平均も載せる。
- **ゲーム設定**: 操作、ターゲット、キー、画面表示、FPS、大規模 PvP で初日に変えておく設定。
- **最初の 1 週間**: ローンチ週の日ごとのプラン。
- **週間トラッカー** と **ワールドボス**: ブラウザに保存されるチェックリストとリポップタイマー(通知はオプション)。
- **出典**: ガイドの元になったクリエイターとサイト、クラスごとの「おすすめ配信者」。
- **更新履歴**: 変更履歴。更新のたびにポップアップでも一度表示される。

各クラスページには、ビルド概要パネル、特化付きのスキルカード、スキルとアイテムのホバーツールチップ、ホットバーのラインとゲーム内マクロ、ホットバー配置の例、レベリングのチェックリスト、ガイドのルートを示すディーヴァニオン ボード(レベリング順のスライダー付き)がある。検索は `Ctrl+K`。

## 仕組み

小さな Python 製の静的サイトジェネレーター(Jinja2)がすべてを `docs/` に書き出し、それを GitHub Pages が配信する。フレームワークはなく、CSS や JS のビルド工程もない。

```
data/
  site.json               クラス(モード、出典と日付、状態)、言語、イベント、公開設定
  i18n.json               UI 文字列(EN / RU / UK / TR / JA)
  skills/<class>.json     スキル名、説明、特化(自動生成)
  boards/<class>.json     ディーヴァニオン ボード: ノード、コスト、効果(自動生成)
  boards/presets.json     各ガイドモードが取るノード。ルートはビルド時に計算する
  items.json              アイテム名、アイコン、ツールチップ(自動生成)
  class_items.json        クラスガイド内で使うアイテムキー
  leveling/*.json         レベリングのチェックリスト: 共通ルート + クラス別の手順
  dungeons.json           ダンジョンページの本文(ギミック)。dungeons_db.json はダンジョン名とボス名(自動生成)
  tierlist.json           ティアリスト
  progression.json, crafting.json, settings.json, week1.json, weekly.json, bosses.json   その他のページ
  sources.json            クリエイターとサイト、「おすすめ配信者」
  changelog.json          更新履歴
src/
  templates/              ベース、ホーム、クラスページ、ガイドページ、トラッカー、マクロ、アリーナ図(diagrams/)
  content/<class>/        en.html、ru.html、uk.html、tr.html、ja.html: ガイド本文
  assets/                 css、js、アイコン、クラスアート、SNS プレビュー画像
tools/
  build.py                データ + テンプレート → docs/(ガイドの整合性チェック lint_guides.py も呼ぶ)
  fetch_skills.py         questlog.gg からスキルとアイコン(en / ru / ja)
  fetch_boards.py         questlog.gg からディーヴァニオン ボード
  fetch_items.py          questlog.gg からアイテムとアイコン
  fetch_dungeons.py       questlog.gg からダンジョン名、ボス名、ボスの肖像
  fetch_art.py            クラスアート
  make_og.py              SNS プレビュー画像
  make_icons.py           ラスターのサイトアイコン(favicon)
  lang_fill.py            手整形の JSON を崩さずに言語を追加する(extract / check / inject)
  i18n_check.py           英語の変更に対して他言語が追従しているかの確認
  jedit.py                data/*.json をパス指定で編集(再ダンプしない)
  find_guides.py          YouTube の新しいガイド動画を探す
  video_guide.py          ガイド動画の分析準備: fetch_video.py + fetch_transcript.py + storyboard.py
docs/                     ビルド出力(コミットして公開する)
frames/                   ガイド動画ごとのローカル作業ファイル(git 管理外、下記参照)
```

## セットアップ

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

Windows では `.venv/bin/python` を `.venv/Scripts/python` に読み替える。

## ビルドとプレビュー

```bash
PYTHONHASHSEED=0 .venv/bin/python tools/build.py
python3 -m http.server 8000 --directory docs
```

http://localhost:8000 を開く。`PYTHONHASHSEED=0` を付けるのは、同コストのディーヴァニオン ボード経路の選択を毎回同じにして、触っていないクラスの `docs/` に差分が出ないようにするため。

## 動画からガイドを更新する

```bash
.venv/bin/python tools/video_guide.py <youtube url or id>
```

動画(Full HD、音声なし)をダウンロードし、字幕を保存し、フレームとコンタクトシートに切り出して `frames/<youtube id>/` に置く。その先の手順(フレームを読む、現在のガイドと比べる、変更を提案する、更新後にやること)は `.claude/skills/guide-from-video/SKILL.md` に書いてある。

**素材はローカルにだけ置く。** クリエイターの動画、字幕、フレーム、スクリーンショットは git 管理外の `frames/` にのみ置き、コミットも公開もしない。リポジトリに入れるのは自分たちの文章、ゲームデータ、出典へのリンクだけ。

## クラスガイドの編集

- 本文は `src/content/<class>/en.html`、`ru.html`、`uk.html`、`tr.html`、`ja.html`。必ず 5 つすべてを変更する。ウクライナ語とトルコ語のページはスキル名やアイテム名などゲーム内名称を英語で表示する(該当言語のゲームデータがない)ので、`uk.html` と `tr.html` でも英語で書く。日本語ページは日本語クライアントの表記を使う(文体と用語は `.claude/ja-style.md`)。
- `{{ s('skill-slug') }}` はスキルをアイコンとページ言語の名前で表示する。`{{ it('{i:item_key}') }}` はアイテムで同じ。
- `{% call skill('slug', 'must', '16', [1, 3]) %}…{% endcall %}` は特化を選んだスキルカード。レベル 20 の 3 つ目は `then=[i]`。`hotline(...)` と `macroseq(...)` はホットバーのラインとマクロの手順、`hotbar(...)` はホットバー配置の例、`{{ dv_board('pve') }}` はそのモードのルート付きディーヴァニオン ボード。
- セクションには属するモードのタグを付ける(`'pve'`、`'pvp'`、`'pve pvp'`、`'lvl'`)。PvP ブロックは対応する PvE ブロックの直後に置き、両モードが同じ順で読めるようにする。
- 変更後は `data/site.json` でそのクラスの `updated` と再確認したモードの `src` の日付を更新し、`data/sources.json` のクリエイターを更新し、`data/changelog.json` に項目を足す。
- レベリングの手順では `[[skill-slug]]` がスキル名、`[[skill-slug#N]]` がその N 番目の特化になる。
- 他言語との整合性は `.venv/bin/python tools/i18n_check.py --all` で確認する(テンプレートタグの並びが `en.html` と一致しているか、`ja` などの欠けた文字列がないか)。

## クラスの追加

1. データを取得する: `tools/fetch_skills.py <class>` と `tools/fetch_boards.py <class>`。
2. `src/content/<class>/` に 5 言語の本文を書く(既存クラスをテンプレートにする)。
3. `data/leveling/<class>.json` にクラスの手順を、ボード用に `data/boards/presets.json` にクラスのプリセットを足す。
4. `data/site.json` でそのクラスを `"status": "ready"` にする(`accent`、`weapon`、`difficulty`、`pitch`、`src` も)。
5. `tools/make_og.py` を実行し、`tools/build.py` を実行する。

## 公開

`main` に push すると GitHub Pages が `docs/` を配信する(**Settings → Pages → Deploy from a branch**、ブランチ `main`、フォルダ `/docs`)。

このフォークの公開設定(`data/site.json`):

- `noindex: true`: 全ページに robots の noindex を付け、`robots.txt` でクロールを拒否する。元サイトの複製が検索に載らないようにするため。
- `ga` と `feedback_url` は空。Google Analytics は読み込まず、「フィードバックを送る」ボタンは GitHub の issue を開く(元サイトは Cloudflare Worker 経由で作者の Telegram に送る。そのコードは `tools/feedback-worker/worker.js`)。

`LAUNCH.md` は稼働中のサーバーで再確認すべき値の一覧、`CONTEXT.md` はプロジェクトの要件と確認済みのゲーム仕様。

## 上流の取り込み

```bash
git fetch upstream
git merge upstream/main
```

衝突はほぼ「こちらが `"ja"` を足した行を上流も編集した」型。上流の文を採り、`"tr"` の直後に `"ja"` を戻す。このフォーク独自の設定(`base_url`、`langs`、`ga`、`noindex`、`feedback_url`)は戻さない。マージ後は必ず再ビルドし、新しく入った英語には `tools/lang_fill.py extract ja` と `tools/i18n_check.py` で日本語を足す。

## クレジット

NCSOFT とは無関係の非公式ファンサイト。AION 2、そのアート、スキルアイコンの著作権は NCSOFT に帰属する。ゲームデータは [questlog.gg](https://questlog.gg/aion-2/) のもの。ビルドはクリエイターのガイドに基づいており、各ガイドページと出典ページからリンクしている。元のサイトとリポジトリは [Couga54/aion2-guides](https://github.com/Couga54/aion2-guides)。
