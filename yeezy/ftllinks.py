#!/usr/bin/python
# -*- coding: utf-8 -*-

baseurl = "http://www.footlocker.com/catalog/miniAddToCart.cfm?secure=0"
def constructlink(model, requestk, sku, size):
    lesting = "&inlineAddToCart=1"
    link =baseurl+"&model="+model+"&requestKey="+requestk+"&sku="+sku +"&the_model_nbr="+model+"&qty=1"+"&size="+size+lesting
    print "Link:  %s" % link
    return

lemodel = raw_input("MODEL NUMBER:")
lerequest = raw_input("REQUEST KEY:")
lesku = raw_input("SKU:")
lesize = raw_input("SIZE:")
constructlink(lemodel, lerequest, lesku, lesize)


