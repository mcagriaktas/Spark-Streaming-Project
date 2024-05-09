## 1. Start the container:
docker-compose up --build -d

## 2. Connect the Postgres
psql -U cagri -d mydb

## 3. Create new DB and user
CREATE DATABASE mydb;

CREATE USER myuser WITH PASSWORD 'mypassword' CREATEDB;

GRANT ALL PRIVILEGES ON DATABASE mydb TO myuser;

GRANT CREATE ON SCHEMA public TO myuser;

ALTER USER myuser WITH SUPERUSER;

## 4. Check your db and user permission

\l

root@f629a9cf27a1:/# psql -U cagri -d mydb
psql (16.2 (Debian 16.2-1.pgdg120+2))
Type "help" for help.

mydb=# \l
                                                   List of databases
   Name    | Owner | Encoding | Locale Provider |  Collate   |   Ctype    | ICU Locale | ICU Rules | Access privileges
-----------+-------+----------+-----------------+------------+------------+------------+-----------+-------------------
 mydb      | cagri | UTF8     | libc            | en_US.utf8 | en_US.utf8 |            |           |
 postgres  | cagri | UTF8     | libc            | en_US.utf8 | en_US.utf8 |            |           |
 template0 | cagri | UTF8     | libc            | en_US.utf8 | en_US.utf8 |            |           | =c/cagri         +
           |       |          |                 |            |            |            |           | cagri=CTc/cagri
 template1 | cagri | UTF8     | libc            | en_US.utf8 | en_US.utf8 |            |           | =c/cagri         +
           |       |          |                 |            |            |            |           | cagri=CTc/cagri
(4 rows)

mydb=# CREATE DATABASE mydb;
ERROR:  database "mydb" already exists
mydb=# CREATE USER myuser WITH PASSWORD 'mypassword' CREATEDB;
CREATE ROLE
mydb=# GRANT ALL PRIVILEGES ON DATABASE mydb TO myuser;
GRANT
mydb=# GRANT CREATE ON SCHEMA public TO myuser;
GRANT
mydb=# ALTER USER myuser WITH SUPERUSER;
ALTER ROLE
mydb=# \l
                                                   List of databases
   Name    | Owner | Encoding | Locale Provider |  Collate   |   Ctype    | ICU Locale | ICU Rules | Access privileges
-----------+-------+----------+-----------------+------------+------------+------------+-----------+-------------------
 mydb      | cagri | UTF8     | libc            | en_US.utf8 | en_US.utf8 |            |           | =Tc/cagri        +
           |       |          |                 |            |            |            |           | cagri=CTc/cagri  +
           |       |          |                 |            |            |            |           | myuser=CTc/cagri
 postgres  | cagri | UTF8     | libc            | en_US.utf8 | en_US.utf8 |            |           |
 template0 | cagri | UTF8     | libc            | en_US.utf8 | en_US.utf8 |            |           | =c/cagri         +
           |       |          |                 |            |            |            |           | cagri=CTc/cagri
 template1 | cagri | UTF8     | libc            | en_US.utf8 | en_US.utf8 |            |           | =c/cagri         +
           |       |          |                 |            |            |            |           | cagri=CTc/cagri
(4 rows)

mydb=#
