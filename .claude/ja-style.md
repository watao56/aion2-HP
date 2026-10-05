# 日本語版の翻訳ルール(AION 2 Guides)

読者は AION 2 グローバル版を日本語クライアントで遊ぶ日本人プレイヤー。英語の攻略テキストを、日本の攻略 Wiki に載っていて違和感のない日本語にする。直訳ではなく、同じ内容を日本語で書き直すつもりで。

## 文体

- **常体**で簡潔に書く(「〜する」「〜できる」「〜が強い」)。です・ます調は使わない。
- 指示は「〜する」「〜しよう」「〜を使う」。「あなた」は書かず、主語は省く。
- 一文を短く。英語の長い一文は 2 文に分けてよい。レベリングの手順やチェックリストは体言止めや短い命令形でよい。
- 英語のダッシュ「—」は持ち込まない。文を分けるか、「：」や（）で書き直す。
- 内容の追加・削除・要約・訳注はしない。数値、レベル、回数、秒数、スキルの並び順は原文どおり。
- 原文が曖昧なところを勝手に断定しない。「〜と思われる」「未確認」などのニュアンスも残す。

## 表記

- 句読点と括弧は全角(、。「」（）)。数字と英字は半角。日本語と英数字の間に空白は入れない。
- 単位: `20 metres` → `20m`、`15 seconds` → `15秒`、`level 22` → `Lv22`、スキルレベルは `スキルLv8`、`%` はそのまま。
- `→` `·` `×` `+` などの記号はそのまま使う。
- キー名(Space、Shift、Tab、F1 など)は英語のまま。マウスは「右クリック」「左クリック」。
- `PvE` `PvP` `DPS` `HP` `MP` `AoE` `CC` `UI` はそのまま。

## ゲーム用語

1. **スキル、スティグマ、パッシブ、アイテム、ボード、ボス名**は、`data/skills/<class>.json`、`data/items.json`、`data/boards/`、`data/bosses.json` の `ja` を一字一句そのまま使う。英語名の併記はしない。データにない固有名詞は訳語を作らず英語のまま残す。
2. **一般的なゲーム用語**は下の「用語表」に従う。
3. 用語表にない MMO 用語は日本のプレイヤーが普通に使う言い方にする(バフ、デバフ、タンク、ヒーラー、バースト、火力、ヘイト、範囲攻撃、単体、詠唱、クールタイム、スタック、コンボ、カイト、ビルド、ローテーション)。
4. **ゲーム内の設定項目名・メニュー名**(設定ページの「Separate Defiance Hotkey」のような項目名)は英語のまま残す。日本語クライアントでの正式な表記を確認できていないため。
5. 配信者名、チャンネル名、動画タイトル、サイト名、URL は原文のまま。
6. `<strong>ON</strong>` と `<strong>OFF</strong>` はそのまま(ビルドがこの文字列で色を付ける)。

## マークアップ

- HTML タグ、属性、`{i:key}`、`[[slug]]`、`{{ … }}`、`{% … %}`、`{# … #}` は一切変えない。訳すのは人が読むテキストだけ。
- `<strong>` `<em>` は、原文で囲まれていた語に対応する日本語を囲む。数や順序を変えない。
- 文字列の中の `"` は JSON を壊さないように注意する(日本語の引用は「」を使う)。

## 用語表

日本語クライアントのデータ(questlog.gg)で確認できた表記。この表記をそのまま使う。

| 英語 | 日本語 |
|---|---|
| Gladiator / Templar / Ranger / Assassin | グラディエーター / テンプラー / レンジャー / アサシン |
| Sorcerer / Elementalist / Cleric / Chanter | ソーサラー / スピリットマスター / クレリック / チャンター |
| Greatsword / Bow / Sword / Dagger | グレートソード / ボウ / ソード / ダガー |
| Spellbook / Orb / Mace / Staff | マジックブック / オーブ / メイス / ワンド |
| Stigma / Daevanion / Arcana | スティグマ / ディーヴァニオン / アルカナ |
| Daevanion Points / Stigma Shard | ディーヴァニオン ポイント / スティグマ シャード |
| Daeva / Ascension / Odyle | ディーヴァ / 覚醒 / オード |
| Kinah (Kina) / Abyss / Abyss Points | ギーナ / アビス / アビス ポイント |
| Elyos / Asmodian | 天族 / 魔族 |
| Rift / Expedition / Transcendence / Sanctuary | 亀裂 / 遠征 / 超越 / 聖域 |
| Verteron / Altgard / Lower Reshanta | ベルテロン / アルトガルド / エレシュランタ下層 |
| Attack / Defense / Max HP / Max MP | 攻撃力 / 防御力 / 最大HP / 最大MP |
| Critical Hit / Accuracy / Evasion | クリティカル / 命中 / 回避 |
| Block / Parry | ガード / 武器ガード |
| Combat Speed / Movement Speed | 戦闘速度 / 移動速度 |
| Cooldown / Cooldown Reduction | 再使用時間 / 再使用時間減少 |
| Damage Boost / Damage Tolerance | ダメージ増幅 / ダメージ耐性 |
| Critical Damage Boost | クリティカル ダメージ増幅 |
| Multi-Hit / Multi-Hit Chance / Multi-Hit Resist | 多段ヒット / 多段ヒット的中 / 多段ヒット抵抗 |
| PvP Damage Boost / PvE Damage Boost | PvPダメージ増幅 / PvEダメージ増幅 |
| Nezekan / Zikel / Vaizel / Triniel / Azphel | ネザカン / ジケル / バイゼル / トリニエル / アスフェル |
| Lumiel / Kaisinel / Yustiel / Marchutan / Ariel | ルミエル / カイジネル / ユスティエル / マルクタン / アリエル |
| Stun / Knockdown / Airborne | 気絶 / 転倒 / 空中束縛 |
| Bleed / Poison / Root / Slow / Stagger | 出血 / 中毒 / 束縛 / 鈍化 / グロッキー |
| Shield (barrier effect) / Buff / Debuff | バリア / バフ / デバフ |
| (Bound) | (刻印) |

クライアントで確認できず、このサイトで決めた訳語(これで統一する):

| 英語 | 日本語 |
|---|---|
| Specialization (skill specialization, spec) | 特化(特化スロット、特化オプション) |
| Shield (Templar's off-hand) | 盾 |
| Silence / Immobilize | 沈黙 / 移動不可 |
| Leveling / Build / Rotation / Opener | レベリング / ビルド / ローテーション / 開幕 |
| Skill points / Skill level | スキルポイント / スキルLv |
| Hotbar / Macro | ホットバー / マクロ |
| World boss / Field boss | ワールドボス / フィールドボス |
| Weekly reset / Daily | 週間リセット / デイリー |
| Gathering / Crafting | 採集 / 製作 |
| Founder's early access | ファウンダー先行アクセス |
| Global (the global server/client) | グローバル版 |

「cooldown」はステータス名やスキル説明の引用では「再使用時間」、会話的な説明文では「クールタイム」でもよい。
| Nightmare / Ascension Trial / Arena of Solitude | 悪夢 / 覚醒戦 / 孤独の闘技場 |
| Draupnir / Vakron Sky Island / Urugugu Canyon | ドラウプニル / バクロンの空中島 / ウルググ峡谷 |
| Ferocious Horn Den / Krao Cave / Fire Temple | 獰猛な角岩窟 / クラオ洞窟 / 炎の神殿 |
| Shugo Festa / Monolith / Kromede / Ludra | シューゴ フェスタ / モノリス / クロメデ / ルドラ |
| True Dragon Lord / White Dragon Lord / Holy Spirit (gear) | 真龍王 / 白龍王 / 聖霊 |
| Handicrafting / Alchemy / Cooking / Essence Extraction | 細工 / 錬金 / 料理 / 精気抽出 |
| Double Chance / Perfect Chance / Endurance | 強打 / 完璧 / 鉄壁 |
| Tenacity / Stamina / Weapon Damage Boost / Incoming Heal | 強靭さ / 行動力 / 武器ダメージ増幅 / 受ける治癒量 |
| Manastone / Theostone / Soul bind / Philosopher's Stone | 魔石 / 神石 / 魂刻印 / 賢者の石 |
| Arcana cards: Chalice (Grail) / Parchment / Compass / Bell / Mirror | 聖杯 / 羊皮紙 / コンパス / 鐘 / 鏡 |

上のどちらの表にもないゲーム内の固有名詞(ダンジョン名、地名、NPC 名、通貨、称号など)は、questlog.gg の日本語データ(`language: "ja"`)で確認できればその表記、できなければ英語のまま。
クライアントの表記を確認できず英語のまま残しているもの: ステータス名の Might / Precision / Constitution / Dexterity、アルカナとステータスボードの種類
(Justice / Wisdom / Death / Space / Illusion / Destruction / Life / Destiny / Time / Freedom)、ゲーム内の設定項目名とメニュー名。

## ガイド共通の定訳

セクション見出し: Overview → 概要 / Skills → スキル / Passives → パッシブ / Stigmas → スティグマ / Arcana → アルカナ / Recap → まとめ /
Daevanion boards → ディーヴァニオン ボード / Leveling macro → レベリング用マクロ / Macro & rotation → マクロとローテーション /
Gear & stats → 装備とステータス / Global Season 1: what changes → グローバル版シーズン1：変更点 / Stigmas while leveling → レベリング中のスティグマ

スキルカードのバッジ(短いラベル): `Lv 5` → `Lv5` / `Lv 5 → 10` → `Lv5 → 10` / `16 → 20` と `12–16` はそのまま / alt. → 代替 / skip → 不要 /
if spare → 余裕があれば(例: `16 if spare` → `余裕があれば16`) / early → 序盤 / later → 後回し / late game → 終盤 / leveling → レベリング /
group → パーティー / solo → ソロ / sanctuary → 聖域 / bosses → ボス / farming → 周回 / Utility → 補助 / Arena → アリーナ / Abyss → アビス

soul bind(装備の魂刻印)→ 魂刻印 / pet → ペット / party → パーティー / expedition (5 人) → 遠征 / dungeon → ダンジョン
