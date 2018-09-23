clean: 
	find . -name *.pyc |xargs rm  
	find . -name *.log |xargs rm
	find . -name test.log* |xargs rm
	find . -name crawler.log* |xargs rm
	find . -name *.csv |xargs rm 
	find . -name *.tar.gz |xargs rm 
	find . -name *.tgz |xargs rm 
build:
	cd ../ && tar cvzf crawler-admin/crawler-admin.tar.gz crawler-admin/*
upload:
	proxychains4 /usr/local/bin/rsync -arz crawler-admin.tar.gz web_server@td-dz-vm35::files/
.pony:	
	clean
