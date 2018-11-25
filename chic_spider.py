# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 14:07:16 2018

@author: abinitha
"""

import scrapy
import csv



class ChicSpider(scrapy.Spider):
    #name identifies each unique spider
    name = "Chicdata"
    start_urls = ['http://www.chictopia.com/', 'http://www.chictopia.com/', 'http://www.chictopia.com/browse/people', 'http://www.chictopia.com/browse/people', 'http://www.chictopia.com/browse/new_photos/approve', 'http://www.chictopia.com/browse/people?g=2', 'http://www.chictopia.com/browse/people?ti=2', 'http://www.chictopia.com/browse/people?ti=3', 'http://www.chictopia.com/account/signup?src=sg', 'http://www.chictopia.com/community/chictopians', 'http://www.chictopia.com/photo/everybody', 'http://www.chictopia.com/reviews', 'http://www.chictopia.comhttps://www.creatordeck.com', 'http://www.chictopia.com#', 'http://www.chictopia.com#', 'http://www.chictopia.com#', 'http://www.chictopia.com#', 'http://www.chictopia.com#', 'http://www.chictopia.com#', 'http://www.chictopia.com#', 'http://www.chictopia.com#', 'http://www.chictopia.com/upload/style_photo', 'http://www.chictopia.com/upload/shop_photo', 'http://www.chictopia.com/upload/reward', 'http://www.chictopia.com/account/signup', 'http://www.chictopia.com/account', 'http://www.chictopia.com/upload', 'http://www.chictopia.com/shop', 'http://www.chictopia.com#myCarousel', 'http://www.chictopia.com#myCarousel', 'http://www.chictopia.comhttps://www.facebook.com/Chictopia', 'http://www.chictopia.comhttps://twitter.com/Chictopia', 'http://www.chictopia.comhttps://www.youtube.com/Chictopia', 'http://www.chictopia.comhttps://instagram.com/chictopia', 'http://www.chictopia.com/Natural/info', 'http://www.chictopia.com/Basic/info', 'http://www.chictopia.com/80s/info', 'http://www.chictopia.com/Classic/info', 'http://www.chictopia.com/Comfortable/info', 'http://www.chictopia.com/Leather/info', 'http://www.chictopia.com/Maternity/info', 'http://www.chictopia.com/Modest/info', 'http://www.chictopia.com/Sports/info', 'http://www.chictopia.com/photo/show/1154279-black+white+and+studded-black-forever-21-boots-eggshell-sheinside-sweater-neutral-balenciaga-bag', 'http://www.chictopia.com/KimTuttle', 'http://www.chictopia.com/photo/show/1154300-CANT+WE+START+THE+WEEKEND+AGAIN-black-saint-laurent-jacket-heather-gray-2-pc-rib-set-dress', 'http://www.chictopia.com/GIGIL4M', 'http://www.chictopia.com/photo/show/1154213-Kingdom+Collab+with+Coach-coach-sweater-pull-bear-shorts-coach-sneakers', 'http://www.chictopia.com/HenEvia', 'http://www.chictopia.com/photo/show/1154373-Day+1+NYFW-navy-structured-reiss-blazer-sky-blue-mirrored-dior-sunglasses', 'http://www.chictopia.com/PamHetlinger', 'http://www.chictopia.com/photo/show/1154474-Boylymia+Jeans-black-ripped-boylymia-jeans-black-monochrome-blackoutsg-sandals', 'http://www.chictopia.com/pupuren', 'http://www.chictopia.com/browse', 'http://www.chictopia.comhttp://www.chictopia.com/what-to-wear-dinner-date/clothing', 'http://www.chictopia.com/photo/show/1154540-L+Automne-chanel-bag', 'http://www.chictopia.com/PapillonLA', 'http://www.chictopia.com/photo/show/1153270-What+to+wear+on+Valentines+Day-black-tobi-top', 'http://www.chictopia.com/Kryz', 'http://www.chictopia.com/photo/show/1152840-Floral+skirt-skirt-evintagelife-skirt', 'http://www.chictopia.com/forever88', 'http://www.chictopia.com/photo/show/1153149-Torino+Getaway-ankle-boots-zara-boots-fur-ivanka-trump-coat-skinny-jeans-topshop-jeans', 'http://www.chictopia.com/AurelaLacaj', 'http://www.chictopia.com/photo/show/1154152-The+classic+outfit-guess-boots-stradivarius-boots-zaraq-vest', 'http://www.chictopia.com/marianelahd', 'http://www.chictopia.com/browse', 'http://www.chictopia.comhttp://www.chictopia.com/Forever-21-Top/info', 'http://www.chictopia.com/photo/show/1153358-SKIN+DEEP-forever-21-top', 'http://www.chictopia.com/hazelkrisferrando', 'http://www.chictopia.com/photo/show/1154510-Lets+bloom-brown-zara-skirt-white-lace-forever-21-top', 'http://www.chictopia.com/AnniBeniara', 'http://www.chictopia.com/photo/show/1153032-wine+and+galentines-pink-forever-21-top-army-green-personal-wine-watch', 'http://www.chictopia.com/KimTuttle', 'http://www.chictopia.com/photo/show/1153982-Styling+with+Forever+21-light-pink-forever-21-jacket-white-forever-21-top-navy-forever-21-pants', 'http://www.chictopia.com/queenhorsfall', 'http://www.chictopia.com/photo/show/1151654-VERTICAL+STRIPED+PANTS-crop-top-forever-21-top-topshop-pants', 'http://www.chictopia.com/elementsofellis', 'http://www.chictopia.com/browse', 'http://www.chictopia.comhttp://www.chictopia.com/what-to-wear-lunch-date/clothing', 'http://www.chictopia.com/photo/show/1153456-ivory+vest-cream-hot-miami-styles-vest', 'http://www.chictopia.com/LeFashionMonster', 'http://www.chictopia.com/photo/show/1154512-Utility+Pants-utility-pants-black-blazer', 'http://www.chictopia.com/luckyorchid', 'http://www.chictopia.com/photo/show/1153541-Blue+New+Year-gold-gold-dealsale-earrings-forest-green-floral-dressin-bag', 'http://www.chictopia.com/pupuren', 'http://www.chictopia.com/photo/show/1153179-Workwear+Wednesday+The+Cowl+Neck+Sweater+Dress-heather-gray-drape-saks-cardigan-gray-old-navy-dress', 'http://www.chictopia.com/sensiblestylista', 'http://www.chictopia.com/photo/show/1153095-Crop+Fringe-off-white-fringe-lamoda101-sweater-black-sock-boots-zara-boots', 'http://www.chictopia.com/thefashionmedley', 'http://www.chictopia.com/browse', 'http://www.chictopia.comhttp://www.chictopia.com/browse/style_icons', 'http://www.chictopia.com/photo/show/1154478-No+Non+sense+Black-black-zara-dress-black-chanel-bag-black-chinese-laundry-heels', 'http://www.chictopia.com/Dominiquetiu', 'http://www.chictopia.com/photo/show/1154509-The+Revenant-black-zara-boots-maroon-sweater', 'http://www.chictopia.com/RaniaKelesidou', 'http://www.chictopia.com/photo/show/1154431-The+Blues-blue-zerouv-sunglasses-black-zara-boots-black-target-jeans', 'http://www.chictopia.com/inspirafashion', 'http://www.chictopia.com/photo/show/1154381-WEEKEND+WITH+LACOSTE-cotton-lacoste-shirt', 'http://www.chictopia.com/michelletakeaim', 'http://www.chictopia.com/photo/show/1154502-Classic+look-navy-romwe-dress-black-fontana-20-coat-navy-h-m-hat', 'http://www.chictopia.com/Danielle_M', 'http://www.chictopia.com/browse', 'http://www.chictopia.com/about', 'http://www.chictopia.com/about/terms', 'http://www.chictopia.com/about/privacy', 'http://www.chictopia.com/faq', 'http://www.chictopia.com/about/jobs', 'http://www.chictopia.com/promote', 'http://www.chictopia.com/about/advertise', 'http://www.chictopia.com/user/feedback', 'http://www.chictopia.com/?webview=false']                
   
    def parse(self, response):
        #print ("ABINITHA")
        from bs4 import BeautifulSoup as BS
        html = response.body.decode("utf-8")
        #print (html)
        soup = BS(html)
       
        l = []
         
        for imgtag in soup.find_all('img'):
            print(imgtag['src'])
            l.append(imgtag['src'])
        #print (ChicSpider.start_urls)   
    
        with open('destination1.csv','a') as file:
            for line in l:
                file.write(str(line))
                file.write('\n')
                
                

        