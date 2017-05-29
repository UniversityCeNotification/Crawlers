# Crawlers

This repo will not continue, you look this [repo](https://github.com/UniversityCeNotification/Crawling-Rss-Xpath-Bot)

All university crawlers, crawling university page then insert mongodb


<h4>MongoDB Document is like json on the bottom;</h4>

```json
{
  "site": "ytuce.maliayas.com",
  "authorName": "Ali Mehmet",
  "authorLink": "ce.yildiz.edu.tr/alimehmet",
  "titleName": "Exam Questions",
  "titleLink": "ce.yildiz.edu.tr/alimehmet/news/123AB45",
  "content": "Exam is hard",
  "id": "ASD12123SDSF9IASKDASD",
  "date": "27.01.2017",
  "clock": "20:00",
  "status": "new"
}
```
<h6>Content should hash with md5, then assign id</h6>

<h4>University Computer Science or Engineer List</h4>

|       University                                          |       Crawling Site                       |  Status  |
| --------------------------------------------------------- |:-----------------------------------------:|:--------:|
| [Yildiz Technical](https://www.ce.yildiz.edu.tr/)         |  https://ytuce.maliayas.com/              |   Ok     |
| [Istanbul](http://ce.istanbul.edu.tr/)                    |  http://ce.istanbul.edu.tr/               |   Nope   |
| [Pamukkale](http://www.pamukkale.edu.tr/bilgisayar)       |  http://www.pamukkale.edu.tr/bilgisayar   |   Nope   |
| [Istanbul Technical](http://www.bb.itu.edu.tr/)           |  http://www.bb.itu.edu.tr/                |   Nope   |
