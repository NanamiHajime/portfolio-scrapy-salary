# portfolio-scrapy-salary

scrapyのportfolioです。

emolument.comという大学の卒業後の給与について掲載しているサイトを利用し、大学の学位と卒業後の給与についてjsonファイルで出力するツールです。

https://www.emolument.com/salary-reports/universities

このリンクはこのようなサイトになっています。

![image](https://user-images.githubusercontent.com/117371263/226238819-24ff283b-ed70-4f5b-8cd1-221ffc594abb.png)

この中の大学のリストをクリックすることで、就職後の職種(by job)、学位(by degree)とその給与がリストとなって表示されます。

![image](https://user-images.githubusercontent.com/117371263/226238951-7b503ba6-92bc-491a-8b28-5be4f9fd99a6.png)


このツールは```scrapy crawl univ_bot -o links.json```を実行することで

リストからすべての大学のリンクを取得し```links.json```ファイルに出力します。

そして、```scrapy crawl salary_bot -o output.json```を実行することで```links.json```に出力されているリンクのBy JobとBy degreeの表のActivityとSample Salaryを取得し、output.jsonに出力しています。

大学の量が多いため、```output.json```に関しては途中で取得を終了しています。

複数のスパイダーを使用したため、可読性を考えて```pipelines.py```と```items.py```を使用しませんでした。
