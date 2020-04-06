# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class TorPipeline(object):
    def process_item(self, item, spider):
        with open('./out.txt', 'a') as f:
            f.write(item['name'] + ' ' + str(item['status']) + '\n')
            # if item['name']=='Hello!':
            #     f.write(item['html'] + '\n')
            f.write(item['url'] + '\n')
        return item
        # print(item['name'])
        # print(item['url'])
        # print('test')
