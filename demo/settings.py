# Scrapy settings for demo project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'demo'

SPIDER_MODULES = ['demo.spiders']

NEWSPIDER_MODULE = 'demo.spiders'

ROBOTSTXT_OBEY = False

CHROME_DRIVER_PATH="E:/Scrapy/chromedriver.exe"

SPLASH_ENABLED = True

if SPLASH_ENABLED:
    SPLASH_URL = 'http://localhost:8050/'

    DOWNLOADER_MIDDLEWARES = {
        'scrapy_splash.SplashCookiesMiddleware': 723,
        'scrapy_splash.SplashMiddleware': 725,
        'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
    }
    
    SPIDER_MIDDLEWARES = {
        'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
    }
    
    DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
    
    HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'
