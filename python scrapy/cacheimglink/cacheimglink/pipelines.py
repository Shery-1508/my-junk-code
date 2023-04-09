# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3


class CacheimglinkPipeline:
    conn = sqlite3.connect("CAPTCHAS.db")
    crsr = conn.cursor()
    conn.execute("""create table if not exists table1(
                    Cap_links text
                    )""")
    conn.commit()
    print("this is pipeline file")
    def enterdata(self,item):
        self.crsr.execute('''insert into table1 values(?)''',
                    (
                    item['lnk'],
                    ))
        self.conn.commit()


    def process_item(self, item, spider):
        self.enterdata(item)
        return item