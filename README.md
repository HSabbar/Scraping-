# Scraping-Scapy-Apache-Nutch-heritrix

Pour tester il faut tapez la commande à la racine de dossier `tutorial` : `scrapy crawl quotes`
###### La vidéo montre les résultats obtenus {a note des commentaires, sélectionner une langue, les avis textuel des utilisateur}
[Regardez la vidéo ici :](https://www.youtube.com/watch?v=ZCBSZE0jFPc&feature=youtu.be)
### Apache-Nutch : 

J'ai un ce probléme que je ne comprend pas 

```
MBP-de-sabbar:local sabbar$ bin/crawl local/conf/urls/seed.txt TestCrawl 4
No SOLRURL specified. Skipping indexing.
Injecting seed URLs
/Users/sabbar/Desktop/Master/Anna/apache-nutch-2.3.1/runtime/local/bin/nutch inject local/conf/urls/seed.txt -crawlId TestCrawl
InjectorJob: starting at 2019-01-10 04:23:51
InjectorJob: Injecting urlDir: local/conf/urls/seed.txt
InjectorJob: java.lang.ClassNotFoundException: org.apache.gora.mongodb.store.MongoStore 
	at java.net.URLClassLoader.findClass(URLClassLoader.java:381)
	at java.lang.ClassLoader.loadClass(ClassLoader.java:424)
	at sun.misc.Launcher$AppClassLoader.loadClass(Launcher.java:335)
	at java.lang.ClassLoader.loadClass(ClassLoader.java:357)
	at java.lang.Class.forName0(Native Method)
	at java.lang.Class.forName(Class.java:264)
	at org.apache.nutch.storage.StorageUtils.getDataStoreClass(StorageUtils.java:93)
	at org.apache.nutch.storage.StorageUtils.createWebStore(StorageUtils.java:77)
	at org.apache.nutch.crawl.InjectorJob.run(InjectorJob.java:218)
	at org.apache.nutch.crawl.InjectorJob.inject(InjectorJob.java:252)
	at org.apache.nutch.crawl.InjectorJob.run(InjectorJob.java:275)
	at org.apache.hadoop.util.ToolRunner.run(ToolRunner.java:70)
	at org.apache.nutch.crawl.InjectorJob.main(InjectorJob.java:284)

Error running:
  /Users/sabbar/Desktop/Master/Anna/apache-nutch-2.3.1/runtime/local/bin/nutch inject local/conf/urls/seed.txt -crawlId TestCrawl
Failed with exit value 255.
MBP-de-sabbar:local sabbar$ bin/nutch inject urls/
InjectorJob: starting at 2019-01-10 04:23:56
InjectorJob: Injecting urlDir: urls
InjectorJob: java.lang.ClassNotFoundException: org.apache.gora.mongodb.store.MongoStore 
	at java.net.URLClassLoader.findClass(URLClassLoader.java:381)
	at java.lang.ClassLoader.loadClass(ClassLoader.java:424)
	at sun.misc.Launcher$AppClassLoader.loadClass(Launcher.java:335)
	at java.lang.ClassLoader.loadClass(ClassLoader.java:357)
	at java.lang.Class.forName0(Native Method)
	at java.lang.Class.forName(Class.java:264)
	at org.apache.nutch.storage.StorageUtils.getDataStoreClass(StorageUtils.java:93)
	at org.apache.nutch.storage.StorageUtils.createWebStore(StorageUtils.java:77)
	at org.apache.nutch.crawl.InjectorJob.run(InjectorJob.java:218)
	at org.apache.nutch.crawl.InjectorJob.inject(InjectorJob.java:252)
	at org.apache.nutch.crawl.InjectorJob.run(InjectorJob.java:275)
	at org.apache.hadoop.util.ToolRunner.run(ToolRunner.java:70)
	at org.apache.nutch.crawl.InjectorJob.main(InjectorJob.java:284)

MBP-de-sabbar:local sabbar$ 
