from simple_ddl_parser import DDLParser

ddl = """
DROP TABLE IF EXISTS contacts;

CREATE TABLE contacts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    fullname varchar(101) GENERATED ALWAYS AS (CONCAT(first_name,' ',last_name)),
    email VARCHAR(100) NOT NULL
);
"""
result = DDLParser(ddl).run(group_by_type=True)

print(result)
