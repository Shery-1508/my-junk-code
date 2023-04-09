# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3


class GamesDataExtractorPipeline:
    
    
    conn = sqlite3.connect("Games_Datase.db")
    conn.execute("""create table if not exists pagee(
                    Games text,
                    DateUploaded text
                    )""")
    conn.commit()
    
    
    def data_to_database(self,Items):
        self.conn.execute('''insert into pagee values(?,?)''',
                    (
                        Items['title'],
                        Items['upload_date'],
                    ))
        self.conn.commit()
    
    
    def process_item(self, item, spider):
        self.data_to_database(item)
        return item
