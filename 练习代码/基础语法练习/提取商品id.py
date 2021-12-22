import re
import os
import json
import sys
null = ""
json1 = {
    "status":0,
    "data":{
        "total":1,
        "list":[
            {
                "id":161594059,
                "masterName":"嘿猪猪-sweet莓莓保温圆杯",
                "slaveName":"Q萌造型 316不锈钢内胆  食品级硅胶 真空隔热",
                "categoryId":10004,
                "categoryName":"保温杯",
                "parentCategoryName":"餐厨/保温杯壶",
                "firstLevelCategoryId":10001,
                "afterSaleServiceAttr":"",
                "afterSaleServiceType":null,
                "afterSaleDeadline":"",
                "serviceRule":"",
                "deliveryArea":null,
                "supplierName":"苏打直供",
                "applicableCardType":"",
                "freightRules":null,
                "predictDeliveryPeriod":"",
                "detail":"",
                "buyNotes":"",
                "setPriceStatus":0,
                "productStatus":1,
                "productStatusDesc":"",
                "operatorId":0,
                "operatorName":"",
                "productType":4,
                "productTypeDesc":"实物",
                "mainImages":null,
                "video":{
                    "url":"",
                    "previewUrl":"",
                    "duration":0,
                    "size":0
                },
                "brand":"嘿猪猪",
                "skuList":[
                    {
                        "id":161618200,
                        "masterName":"圆杯280ML",
                        "image":"",
                        "inventory":0,
                        "availableInventory":496,
                        "costPrice":5300,
                        "salesPrice":7900,
                        "settlementPrice":5300,
                        "marketPrice":0,
                        "sdyxSalesPrice":7900,
                        "kaopSalesPrice":7900,
                        "skuCode":"P332-280ml ",
                        "barCode":"",
                        "settlementType":0,
                        "relateSkuInfos":null
                    },
                    {
                        "id":161618201,
                        "masterName":"圆杯350ML",
                        "image":"",
                        "inventory":0,
                        "availableInventory":494,
                        "costPrice":5300,
                        "salesPrice":7900,
                        "settlementPrice":5300,
                        "marketPrice":0,
                        "sdyxSalesPrice":7900,
                        "kaopSalesPrice":7900,
                        "skuCode":"P332-350ml  ",
                        "barCode":"",
                        "settlementType":0,
                        "relateSkuInfos":null
                    }
                ],
                "image":"https://mall.s.maizuo.com/aura/de8705b72635c6e73414d1d9089a8de3.png",
                "isSelfSupport":0
            }
        ],
        "priceTypeList":null
    },
    "msg":"ok"
    }
# json2={"name": "Nowcoder", "no": 1, "url": "http://www.nowcoder.com"}
# dict = json.dumps(json2)
# dict2 =json.loads(dict)
# print(dict2["name"])
dict = json.dumps(json1)
dict2 = json.loads(dict)
list1 = dict2["data"]["list"]
dict4 = list1[0]

print(dict4["id"])
# print(list1)
# dict3 = len(list1)
# print(dict3)
# print(list1)
