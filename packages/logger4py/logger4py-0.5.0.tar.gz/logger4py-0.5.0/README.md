**Logger4py**  

**_Custom logging module_**  

**Usage**  

> install package 

`pip install logger4py `  

> How to use logger4py  

`from logger4py import Logger  
log = Logger.get_logger('my_module')  

log.debug('this is a debug message')  
log.info('this is an info message')  
log.error('this is an error message')  
log.warning('this is a warning message')  `

**Demo**    

> 2021-05-20T00:06:20.736	DEBUG	35692	44080	test_log	this is a debug message      
2021-05-20T00:06:20.736	INFO	35692	44080	test_log	this is an info message    
2021-05-20T00:06:20.736	ERROR	35692	44080	test_log	this is an error message    
2021-05-20T00:06:20.736	WARNING	35692	44080	test_log	this is a warning message    
2021-05-20T10:13:09.552	DEBUG	42864	43524	test_log	this is a debug message    
2021-05-20T10:13:09.552	INFO	42864	43524	test_log	this is an info message    
2021-05-20T10:13:09.552	ERROR	42864	43524	test_log	this is an error message    
2021-05-20T10:13:09.553	WARNING	42864	43524	test_log	this is a warning message  

**logger4py Configuration file**  



