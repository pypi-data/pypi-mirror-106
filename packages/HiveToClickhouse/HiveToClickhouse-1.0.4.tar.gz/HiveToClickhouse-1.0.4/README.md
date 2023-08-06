## hive sql 转 clickhouse sql<br>

## 使用方法： <br>

```ruby 
import HiveToClickhouse

if __name__ == '__main__':
    hive_sql = ''
    news_sql = HiveToClickhouse.execute(hive_sql)
