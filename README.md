# portfolio-scrapy-salary

scrapyのportfolioです。

emolument.comという大学の卒業後の給与について掲載しているサイトを利用し、大学の専攻と卒業後の給与についてjsonファイルで出力するプログラムです。

```scrapy crawl univ_bot```を実行することで

https://www.emolument.com/salary-reports/universities

からすべての大学のリンクを取得しlinks.jsonファイルに出力します。

そして、```scrapy crawl salary_bot```を実行することでlink.jsonに出力されているリンクのBy JobとBy degreeの表の情報を取得し、output.jsonに出力しています。

大学の量が多いため、output.jsonに関しては途中で取得を終了しています。

複数のスパイダーを使用したため、可読性を考えてpipelines.pyとitems.pyを使用しませんでした。
