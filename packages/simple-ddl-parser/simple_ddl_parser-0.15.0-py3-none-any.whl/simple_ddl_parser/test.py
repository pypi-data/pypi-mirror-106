from simple_ddl_parser import DDLParser

ddl = """
CREATE TABLE IF NOT EXISTS test_table
 (col1 int PRIMARY KEY COMMENT 'Integer Column',
 col2 string UNIQUE COMMENT 'String Column'
 )
 COMMENT 'This is test table'
 ROW FORMAT DELIMITED
 FIELDS TERMINATED BY ','
 STORED AS TEXTFILE;
"""
result = DDLParser(ddl).run(group_by_type=True)
print(result)
