###### 20170520 - [SQL basic]

# SQL study #1. Tutorials

수업자료 - w3schools [바로가기][1]
[1]: https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all



#### # 관계형 데이터베이스 

-  키(key)와 값(value)들의 간단한 관계를 테이블화 시킨 매우 간단한 원칙의 전산정보 데이터베이스
-  종류 : MS SQL Server, IBM DB2, Oracle, MySQL, Microsoft Access


- 웹서비스를 하기 위해서는 웹서버가 필요
- 당연한 이치로 데이터베이스를 위해서는 데이터베이스 서버가 필요하다.

<br>

## 1. HOME

~~~html
SELECT * FROM Customers;
~~~

: 테이블명(Customers)에서 모든 테이블을 가져오라는 명령.
- 옆의 테이블 목록에서 보고 싶은 테이블 제목을 클릭하면 데이터베이스를 볼 수 있다. 

<br>

#### WebSQL

- HTML5와 연관되어 있어 웹에서도 실습을 할 수 있다. 
- 크롬, 사파리, 오페라에서 구동가능하다.

<br>


## 2. Introduction

#### SQL의 정의

- SQL은 구조화된 질의 언어이다.(Structured Query Language)
- 데이터베이스의 데이터를 저장, 조작 및 검색하기 위한 표준언어.
- 데이터베이스에 접근하고 조작할 수 있는 툴이다.
- ANSI(American National Standards Institute)의 표준을 따른다.

<br>

#### SQL의 기능

- SQL은 데이터베이스의 쿼리를 탐색할 수 있다.
- DB 데이터의 기록, 수정, 삭제, 추가, 열람 등이 가능.
- 새 디비 생성, 특정인에게 사용권한 부여 등의 일을 할 수 있다. 

<br>

#### SQL의 표준범위

- SQL이 표준언어로 지정되었지만 다른 버전의 SQL 언어도 존재한다.
- 아래의 명령어는 어떤 버전에서든 같은 양식으로 사용한다.
	- SELECT
	- UPDATE
	- DELETE
	- INSERT
	- WHERE

<br>

#### SQL을 웹사이트에서 사용하려면...

- RDBMS (관계형 데이터베이스 시스템, Relational Database Management System)가 필요하다.
	- ex_ MS access, SQL server, MySQL
- 서버쪽의 스크립트 언어인 PHP, ASP
- SQL 사용환경 구축
- 페이지를 구조화하기 위한 HTML, CSS 

<br>

#### RDBMS, 관계형 데이터베이스 시스템

- Relational DB Managemet System
- SQL의 기본이 되며, 최근 데이터베이스 시스템(MS SQL Server, IBM DB2, Oracle, MySQL, and Microsoft Access)의 기본이기도 하다.
- 모든 데이터는 RDBMS의 **테이블이라는 데이터베이스 객체로 존재**한다.
- 테이블은 관련된 데이터들의 목록을 모아놓은 것이며, 행과 열을 가지고 있다. 

<br>

## 3. SQL syntax

<br>

#### Database Tables

![2_syntax_tablerow](https://github.com/juliahwang/wps-til/blob/master/0519-Day10-python3/HW-SQL%20study/sql-img/2_syntax-tablerow.png)

- 데이터베이스는 하나 이상의 테이블을 가지고 있다.
- 테이블은 이름을 가지고 이름으로 호출한다.
- **데이터는 테이블의 행(row)이라 한다.**
- **데이터 내용을 정의하는 구분자는 테이블의 열(column)이라고 한다.**

<br>

#### 기본 SQL문

- 예시 

~~~
SELECT * FROM <tablename>

SELECT * FROM Customers;
~~~

(1) SQL의 명령어는 대소문자 구분이 없다. 
	
	- select = SELECT

	
(2) SQL문의 세미콜론(;)

- 세미콜론(;)은 한번에 여러 개의 SQL문을 사용하고자 할 떄, 각각의 SQL문을 구분하기 위한 표준방법이다.

(3) 중요한 SQL명령어들

- `SELECT` : 데이터의 테이블을 호출.
- `UPDATE` : 데이터베이스에 데이터를 업데이트.
- `DELETE` : 데이터베이스에서 데이터(하나 이상)를 삭제.
- `INSERT INTO` : 새로운 데이터를 데이터베이스에 추가.

<br>

- `CREATE DATABASE` : 새로운 데이터베이스 생성.
	- 서버운영자가 주로 사용하는 명령어.
- `ALTER DATABASE` : 데이터베이스 구조를 수정.

<br>

- `CREATE TABLE` : 데이터베이스 안에 새 테이블 생성.
- `ALTER TABLE` : 테이블 수정.
	- `update`는 기본구조말고 데이터를 수정할 때
	- `alter`는 기본구조, 필드 등을 수정할 때
- `DROP TABLE` : 이미 있는 테이블 삭제.
	- `delete`는 테이블 안의 정보를 삭제.

<br>

- `CREATE INDEX` : 인덱스(서치키, 색인) 생성.
- `DROP INDEX` : 인덱스 삭제.	

- index는 필드를 검색 가능한 상태로 만든 것이다.

<br>

## 4. SQL SELECT 문

#### 구문

: 데이터베이스에서 데이터를 불러올 때 사용.

- **result-set** : 호출한 데이터는 **결과셋**이라고 부르는 결과 테이블에 저장한다.

##### (1) 테이블에서 선택한 필드만 가져오기.

~~~
SELECT column1, column2, ...
FROM table_name;

SELECT CustomerName, ContactName, PostalCode
FROM Customers;
~~~

- 결과 실행화면

![4_selectfields](https://github.com/juliahwang/wps-til/blob/master/0519-Day10-python3/HW-SQL%20study/sql-img/4_selectfields.png)

<br>

##### (2) 테이블에서 모든 필드 가져오기

- 모든 테이블을 가져오고 싶을 때는 ` * `를 사용한다. 

~~~
SELECT * FROM Customers;
~~~

- 결과 실행화면 

![4_selectall](https://github.com/juliahwang/wps-til/blob/master/0519-Day10-python3/HW-SQL%20study/sql-img/4_selectall.png)


<br>

#### 결과셋(Result-Set)의 네비게이션

- 대부분의 데이터베이스 소프트웨어 시스템은 결과셋을 바로 찾을 수 있도록 함수를 제공한다.
	- `Move-To-First-Record` 
	- `Get-Record`
	- `Get-Record-Content`
	- `Move-To-Next-Record`
- 이러한 명령어는 ASP나 PHP같은 서버쪽 언어를 함께 사용하여 결과값을 가공하고 웹사이트에 반영할 수 있다.

<br>

## 5. SQL SELECT DISTINCT 문

#### 구문

: 겹치는 데이터를 제외하고 유일한 데이터만 호출.<br>
: 중복된 데이터를 제외하고 불러온다. 

~~~
SELECT DISTINCT column1, column2, ...
FROM table_name;
~~~

- 아래 테이블에서 Country는 중복된 데이터들이 존재한다.

![5_selectdistincttable](https://github.com/juliahwang/wps-til/blob/master/0519-Day10-python3/HW-SQL%20study/sql-img/5_selectdistincttable.png)

##### (1) 위의 구문을 사용하면...

![5_selectdistinctresult](https://github.com/juliahwang/wps-til/blob/master/0519-Day10-python3/HW-SQL%20study/sql-img/5_selectdistinctresult.png)

<br>

##### (2) 중복되지 않는 값만 세고싶다면...
	
~~~
SELECT COUNT(DISTINCT Country) FROM Customers;
~~~

- 총 91개의 전체 데이터 중 중복되지 않은 데이터는 총 21개이다.
	
![5_selectdistinctcount](https://github.com/juliahwang/wps-til/blob/master/0519-Day10-python3/HW-SQL%20study/sql-img/5_selectdistinctcount.png)

<br>

##### (3) 중복되지 않는 결과셋에 이름을 주고 싶다면... 

~~~
SELECT COUNT(*) AS DistinctCountries
FROM (SELECT DISTINCT Countries FROM Customers);
~~~

![5_selectdistinctcountname](https://github.com/juliahwang/wps-til/blob/master/0519-Day10-python3/HW-SQL%20study/sql-img/5_selectdistinctcountname.png)

<br>

## 6. SQL WHERE 절(clause)

#### 구문

: WHERE 절은 레코드를 필터링하기 위해 사용. <br>
: 원하는 값만 추출하기 위해 사용.

- SELECT, UPDATE, DELETE 등의 여러 명령어에서 사용할 수 있다.

~~~
SELECT column1, column2, ...
FROM table_name
WHERE condition;

SELECT * FROM Customers
WHERE City = '
SELECT * FROM Customers
WHERE CustomerID = 45;
~~~

##### (1) 결과 실행화면 - 문자형
	- 문자가 일치하는 조건을 가질 때는 `''` 또는 `""`로 비교값을 둘러준다. 
	
![6_wherestr](https://github.com/juliahwang/wps-til/blob/master/0519-Day10-python3/HW-SQL%20study/sql-img/6_wherestr.png)



##### (2) 결과 실행화면 - 숫자형
	- 숫자가 일치하는 조건을 가질 때는 따옴표를 쓰지 않는다.

![6_wherenum](https://github.com/juliahwang/wps-til/blob/master/0519-Day10-python3/HW-SQL%20study/sql-img/6_wherenum.png)
	
<br>

##### (3) WHERE절의 연산자들

- `=` : 같다
- `<>` or `!=` : 다르다
- `>` or `>=` : 크다 or 크거나 같은
- `<` or `<=` : 작다 or 작거나 같은
- `BETWEEN` : 지정한 범위 안에 있는 데이터를 리턴.

![6_wherebetween](https://github.com/juliahwang/wps-til/blob/master/0519-Day10-python3/HW-SQL%20study/sql-img/6_wherebetween.png)

- `LIKE` : 패턴이 비슷한 데이터들을 리턴.

![6_wherelike](https://github.com/juliahwang/wps-til/blob/master/0519-Day10-python3/HW-SQL%20study/sql-img/6_wherelike.png)

- `IN` : 다양한 조건을 만족하는 여러 결과셋을 불러올 때

![6_wherein](https://github.com/juliahwang/wps-til/blob/master/0519-Day10-python3/HW-SQL%20study/sql-img/6_wherein.png)


<br>

## 7. SQL AND, OR, NOT 연산자

- WHERE절은 `AND`, `OR`, `NOT` 연산자와 함께 쓴다.

#### 구문

`AND` : 모든 조건을 만족하는 결과셋을 불러올 때
`OR` : 조건 중 하나라도 만족하는 결과셋을 불러올 때
`NOT` : 조건을 만족하지 않는 결과셋을 불러올 때

<br>

##### (1) AND 구문

~~~
SELECT column1, column2, ...
FROM table_name
WHERE condition1 AND condition....;

SELECT * 
FROM Customers
WHERE CustomerName Like 'A%' 
AND Country = 'Mexico';
~~~

- 결과실행화면

![7_and](https://github.com/juliahwang/wps-til/blob/master/0519-Day10-python3/HW-SQL%20study/sql-img/7_and.png)


<br>

##### (2) OR 구문

~~~
SELECT column1, column2, ...
FROM table_name
WHERE condition1 OR condition2 ...;

SELECT * 
FROM Customers
WHERE CustomerName Like 'A%' 
OR Country = 'Mexico';
~~~

- 결과실행화면

![7_or](https://github.com/juliahwang/wps-til/blob/master/0519-Day10-python3/HW-SQL%20study/sql-img/7_or.png)


<br>

##### (3) NOT 구문

~~~
SELECT column1, column2,...
FROM table_name
WHERE NOT condition;

SELECT * 
FROM Customers
WHERE NOT Country = 'Mexico';
~~~

- 결과실행화면

![7_not](https://github.com/juliahwang/wps-til/blob/master/0519-Day10-python3/HW-SQL%20study/sql-img/7_not.png)


<br>

##### (4) 연산자 섞어쓰기 구문

~~~
SELECT column1, column2,...
FROM table_name
WHERE condition1 AND NOT condition2;

SELECT * 
FROM Customers
WHERE CustomerName LIKE 'A%' 
AND NOT Country = 'Mexico';
~~~

- 결과실행화면

![7_mix](https://github.com/juliahwang/wps-til/blob/master/0519-Day10-python3/HW-SQL%20study/sql-img/7_mix.png)

<br>

~~~
SELECT column1, column2,...
FROM table_name
WHERE condition1 AND (condition2 OR condition3);

SELECT * 
FROM Customers
WHERE Country = 'Germany' 
AND (City = 'Berlin' OR City = 'München');
~~~

- 결과실행화면

![7_mix2](https://github.com/juliahwang/wps-til/blob/master/0519-Day10-python3/HW-SQL%20study/sql-img/7_mix2.png)


<br>

## 8. ORDER BY 

- 정렬기능
- 데이터를 갖고 올 때 순서를 정하여 가져오는 기능
- 여러 개의 column 이름을 기준으로 순서대로 정렬할 수 있다. 
- 기본정렬은 ASC(오름차순)
- DESC는 내림차순으로 정렬할 때 쓴다. 


#### 구문

~~~
SELECT column1, column2,...
FROM table_name
ORDER BY column1, column2, ... ASC|DESC

SELECT * FROM Categories
ORDER BY CategoryName DESC;
~~~


##### (1) 오름차순으로 2개의 칼럼을 기준으로 정렬

~~~
SELECT * FROM Categories;
ORDER BY CategoryName, City;
~~~

![8_orderbydesc](https://github.com/juliahwang/wps-til/blob/master/0519-Day10-python3/HW-SQL%20study/sql-img/8_orderbydesc.png)

##### (2) 여러 개의 칼럼에 각각의 정렬기준 적용

~~~
SELECT * FROM Customers
ORDER BY Country ASC, CustomerName DESC;
~~~


<br>

## 9. INSERT INTO

- 테이블에 새로운 기록을 추가할 때 사용
- 2개의 형태가 있다. 

#### 구문 1

- 컬럼 이름을 쓰지 않고 값을 칼럼 순서에 맞게 작성하는 방법

~~~
INSERT INTO table_name
VALUES (value1, value2,..., valueN)

INSERT INTO Customers
VALUES ('a', 'b', 'c', ..., 'g');
~~~

- 컬럼 갯수에 맞는 값을 추가해야 정확히 추가된다.

<br>

#### 구문 2

- 각각에 칼럼에 값을 넣을 수 없을 때 칼럼을 지정하여 값을 넣을 칼럼을 명시해주고 그 순서에 맞는 값을 넣는 방법
 
~~~
INSERT INTO table_name (column1, column4,..)
VALUES (value1, value4,....)

INSERT INTO Customers (CustomerName, ContactName, PostalCode, Country)
VALUES ('Ariana','Grande','4006','Norway');
~~~

-결과 실행화면
	- 넣은 데이터를 모두 채우지 않았으므로 없는 값은 Null로 들어간다.

![9_insertintofew](https://github.com/juliahwang/wps-til/blob/master/0519-Day10-python3/HW-SQL%20study/sql-img/9_insertintofew.png)

<br>

## 10. Null 값

- 값이 있는지 없는지 판단할 때 `Null`을 사용.
- Null 값은 연산자( =, <>, <)를 사용할 수 없다.
- 따라서 `IS NULL` 과 `IS NOT NULL`을 사용.

#### 구문 1. `IS NULL`

- 
~~~
SELECT column_names
FROM table_name
WHERE column_name IS NULL;
~~~

![10_isnull](https://github.com/juliahwang/wps-til/blob/master/0519-Day10-python3/HW-SQL%20study/sql-img/10_isnull.png)

<br>

#### 구문 2. `IS NOT NULL`

~~~
SELECT column_names
FROM table_name
WHERE column_name IS NOT NULL;
~~~

![10_isnotnull](https://github.com/juliahwang/wps-til/blob/master/0519-Day10-python3/HW-SQL%20study/sql-img/10_isnotnull.png)

<br>

## 11. UPDATE  

- 있는 데이터의 정보를 **수정**하는 기능
- **반드시!!! WHERE절을 적어서 수정하고자 하는 행을 명시해주어야 한다.**
- WHERE절을 적어주지 않으면 전체 데이터가 변경된다. 

#### 구문

~~~
UPDATE table_name
SET column = value1, column2 = value2, ...
WHERE condition;

UPDATE Customers;
SET CustomerName='ariana'
WHERE CustomerID = 1;
~~~

- Customers 테이블에서 CustomerID가 1인 행의 CustomerName을 'ariana'로 변경

<br>

- 많이 실수하는 부분 
	- WHERE절을 쓰지 않았을 때는 모든 행의 데이터에 수정이 적용되어 돌이킬 수 없다.

![11_updatemistake](https://github.com/juliahwang/wps-til/blob/master/0519-Day10-python3/HW-SQL%20study/sql-img/11_updatemistake.png)


<br>

## 12. DELETE

- 데이터베이스 테이블에 기록된 레코드를 **삭제**할 때 사용.

#### 구문

- UPDATE와 달리 SET은 없다.(추가할 값이 없으므로)
- UPDATE와 마찬가지로 WHERE절을 반드시 써야한다.

~~~
DELETE FROM table_name
WHERE condition;

DELETE FROM Customers
WHERE CustomerID > 40;
~~~

- 많이 실수하는 부분
	- WHERE절을 쓰지 않으면 모든 데이터가 삭제된다.

![12_deletemistake](https://github.com/juliahwang/wps-til/blob/master/0519-Day10-python3/HW-SQL%20study/sql-img/12_deleteall.png)

<br>

#### (1) TRUNCATE 

~~~
TRUNCATE TABLE table_name;
~~~

- mySQL에서 테이블을 리셋시킬 때 사용하는 구문
- WHERE절을 포함하여 부분 삭제가 불가능하다.
- 아예 테이블 전체를 삭제하는 기능이다. 


<br>

## 13. SELECT TOP 절

- 테이블 내에 저장된 내용이 많을 때 불러올 데이터의 갯수를 정하여 출력해주는 기능.
- 데이터 전체를 모두 가져오는 것은 성능에 문제를 일으킬 수 있으므로 부분적으로 가져올 수 있게 한다. 

#### 구문1 - SQL Server / MS Access Syntax

~~~
가져올 숫자 
SELECT TOP number|percent column_name(s)
FROM table_name
WHERE conditon;

SELECT TOP 3 * FROM Customers;
~~~


##### (1) 퍼센트 이용

~~~
SELECT TOP 50 PERCENT * FROM Customers;
~~~

##### (2) WHERE절 추가

~~~
SELECT TOP 3 * FROM Customers
WHERE Country = 'Germany';
~~~

<br>

#### 구문2 - MySQL

- `LIMIT` : ~까지 가져온다.

~~~
SELECT column_name(s)
FROM table_name
WHERE condition
LIMIT number;       # LIMIT가 TOP과 같은 역할.

SELECT * FROM Customers
LIMIT 3;
~~~

##### (1) WHERE절 추가

~~~
SELECT * FROM Customers
WHERE Country = 'Germany'
LIMIT 3;
~~~

<br>

#### 구문3 - Oracle

- `ROWNUM` : ~이하를 가져온다.

~~~
SELECT column_name(s)
FROM table_name
WHERE ROWNUM <= number;

SELECT * FROM Customers
WHERE ROWNUM <= 3;
~~~

##### (1) WHERE절 추가

~~~
SELECT * FROM Customers
WHERE Country = 'Germany' AND ROWNUM <= 3;
~~~

<br>

## 14. MIN() & MAX() 함수

- MIN() : 최소값의 '숫자'만 비교가능
- MAX() : 최대값의 '숫자'만 비교가능

#### 구문 - MAX()

~~~
SELECT MAX(column_name)
FROM table_name
WHERE condtion;

SELECT MAX(Price) AS LargiestPrice
FROM Products
~~~

![14_max](https://github.com/juliahwang/wps-til/blob/master/0519-Day10-python3/HW-SQL%20study/sql-img/14_max.png)

- 이름을 부여하지 않으면 그냥 함수이름으로 추출된다.

<br>

#### 구문 - MIN()

~~~
SELECT MIN(column_name)
FROM table_name
WHERE condtion;

SELECT MIN(Price)
FROM table_name
~~~

<br>

## 15. COUNT(), AVG(), SUM() 함수 

- COUNT() : 기준을 만족하는 행의 갯수를 출력하는 기능
- AVG() : 숫자로 구성된 열의 평균값을 출력
- SUM() : 숫자로 구성된 열의 총합을 출력

#### 구문 - COUNT()

~~~
SELECT COUNT(column_name)
FROM table_name
WHERE condition;

SELECT COUNT(OrderID)
FROM OrderDetails;
~~~

![15_count](https://github.com/juliahwang/wps-til/blob/master/0519-Day10-python3/HW-SQL%20study/sql-img/15_count.png)
<br>

#### 구문 - AVG()

~~~
SELECT COUNT(column_name)
FROM table_name
WHERE condition;

SELECT AVG(Price)
FROM Products;
~~~

![15_avg](https://github.com/juliahwang/wps-til/blob/master/0519-Day10-python3/HW-SQL%20study/sql-img/15_avg.png)

<br>

#### 구문 - SUM()

~~~
SELECT COUNT(column_name)
FROM table_name
WHERE condition;

SELECT SUM(Quantity)
FROM Orderdetails;
~~~

![15_sum](https://github.com/juliahwang/wps-til/blob/master/0519-Day10-python3/HW-SQL%20study/sql-img/15_sum.png)

<br>

## 16. LIKE 연산자 

- WHERE절 안에 사용된다.
- 컬럼의 패턴을 지정하여 탐색, 출력하는데 사용된다.

#### 구문

~~~
SELECT column1, column2,...
FROM table_name
WHERE columnN LIKE pattern;

SELECT * FROM Customers
WHERE City LIKE 'ber%';
~~~

LIKE 연산자 | 설명
:---------:|:-------:
`a%` | a로 시작하는 값
`%a` | a로 끝나는 값
`%or%` | or이 들어있는 값(위치상관없음).
`_r%`| 2번째 글자가 r 인 값
`a_%_%`| a로 시작하면서 3글자 이상인 값
`a%o`| a로 시작하고 o로 끝나는 값

<br>

##### (1) NOT Keyword

~~~
SELECT * FROM Customers
WHERE City NOT LIKE 'ber%';
~~~

<br>

## 17. Wildcard 문자들

- `%` : 0, 1, 또는 다수의 글자를 의미한다.
- `_` : 1개의 글자를 의미한다.

MS Access and SQL server only

- `[charlist]` : 문자의 셋과 범위가 일치하는 값 출력
- `[^charlist]` : 문자의 셋과 범위가 일치하지 않는 값 출력
- `[!charlist]` : 문자의 셋과 범위가 일치하지 않는 값 출력
- `^`와 `!` 는 일반적으로 프로그래밍에서 부정을 뜻한다.

#### 구문

~~~
SELECT * FROM Customers
WHERE City LIKE 'ber%';

# 'ber'로 시작하는 City 칼럼의 행만 출력
~~~

~~~
SELECT * FROM Customers
WHERE City LIKE '%es%';

# 문자열 중 'es'가 포함된 City 칼럼의 행만 출력
~~~

~~~
SELECT * FROM Customers
WHERE City LIKE '_erlin';

# 첫글자는 어떤 글자가 와도 상관없고, 'erlin'으로 끝나는 City칼럼의 행만 출력
~~~

~~~
SELECT * FROM Customers
WHERE City LIKE 'L_n_on';

# 'L'로 시작하고 2, 4번째는 어떤 글자가 와도 상관없으며 글자가 적힌 부분은 일치하는 City칼럼의 행만 출력
~~~

~~~
SELECT * FROM Customers
WHERE City LIKE '[bsp]%';

# b 또는 s 또는 p로 시작하는 값의 City칼럼의 행을 출력
~~~

~~~
SELECT * FROM Customers
WHERE City LIKE '[a-c]%';

# a, b, c로 시작하는 값의 City칼럼의 행을 출력
~~~

~~~
SELECT * FROM Customers
WHERE City LIKE '[!bsp]%';

SELECT * FROM Customers
WHERE City NOT LIKE '[bsp]%';

# b 또는 s 또는 p로 시작하지 않는 값의 City칼럼의 행을 출력
~~~


<br>

## 18. IN 연산자 

- WHERE절에서 다양한 값을 선택하고 싶을 때 사용
- OR 연산자를 사용하는 것보다 경제적이다.

#### 구문 1

~~~
SELECT column_name(s)
FROM table_name
WHERE column_name IN (value1, value2 ,,)

# column_name의 값이 value1, value2, ... valueN인 것들은 모두 가져오라는 의미
~~~

~~~
SELECT * FROM Customers
WHERE Country IN ('Germany', 'France', 'UK');

# 독일, 프랑스, 영국 국적의 행만 출력
~~~

#### 구문 2

~~~
SELECT column_name(s)
FROM table_name
WHERE column_name IN (SELECT STATMENT);

- column_name의 값에서 또 다른 조건을 충족하는 값만 출력
~~~

~~~
SELECT * FROM Customers
WHERE Country IN (SELECT Country FROM Suppliers;

# Suppliers 테이블에서 Country와 일치하는 국가명을 가진 Customers 테이블 행만 출력  
~~~

<br>

## 19. BETWEEN

- 주어진 값의 범위에 있는 값만 출력
- 값은 숫자, 문자, 날짜 등이 될 수 있다. 

#### 구문

~~~
SELECT column_name
FROM table_name
WHERE column_name BETWEEN value1 AND value2;

SELECT * FROM Products
WHERE Price BETWEEN 10 AND 15;

# Price의 데이터가 10에서 15 사이인 행을 출력
~~~

##### (1) NOT BETWEEN

- 주어진 범위에 속하지 않는 값을 출력 

~~~
SELECT * FROM Products
WHERE Price NOT BETWEEN 10 AND 15;
~~~

##### (2) IN 과 섞어쓰기 

~~~
SELECT * FROM Customers
WHERE (Price BETWEEN 10 and 15)
AND NOT CategoryID IN (1, 2, 3);

# Price의 데이터가 10에서 15 사이인 행 중에서 CategoryID가 1, 2, 3이 아닌 것. 
~~~

- 결과 실행화면 

![19_betweenin](https://github.com/juliahwang/wps-til/blob/master/0519-Day10-python3/HW-SQL%20study/sql-img/19_betweenin.png)
   
<br>

##### (3) 문자열 범위 정하기

- 알파벳 순으로 범위를 지정하여 출력 가능. 
- 아래에서, A로 시작하는 문자열은 출력하지만 'C'로 출력하는 문자열은 출력되지 않는다. 

~~~
SELECT * FROM Products
WHERE ProductName BETWEEN 'A' AND 'C'
ORDER BY ProductName;
~~~

- 결과 실행화면 

![19_betweenletter](https://github.com/juliahwang/wps-til/blob/master/0519-Day10-python3/HW-SQL%20study/sql-img/19_betweenletter.png)

<br>

##### (4) 문자열 범위 NOT

~~~
SELECT * FROM Products
WHERE ProductName NOT BETWEEN 'A' AND 'C'
ORDER BY ProductName DESC;

# 'A'와 'B'로 시작하지 않는 제품이름을 내림차순으로 정렬하여 출력
~~~

<br>

##### (5) 날짜 범위

- 문자열 범위와 달리 날짜 범위는 마지막 범위까지 포함한다.
- 아래에서, 7월 8일 데이터도 불러오는 것을 확인할 수 있다.

~~~
SELECT * FROM Orders
WHERE OrderDate BETWEEN #07/04/1996# AND #07/08/1996#

# 'A'와 'B'로 시작하지 않는 제품이름을 내림차순으로 정렬하여 출력
~~~

![19_betweendate](https://github.com/juliahwang/wps-til/blob/master/0519-Day10-python3/HW-SQL%20study/sql-img/19_betweendate.png)

<br>

## 20. ALIASES

- 테이블, 열에 별도의 이름을 할당하여 사용하고 싶을 때 사용
- 긴 칼럼 및 테이블 이름을 줄여서 쓸 수 있다.
- 2개 이상의 테이블을 함께 가져올 때 별칭을 줘서 간편하게 불러올 수 있다. 
- 조회기간에만 사용한다.

#### 구문 1 - column 이름바꾸기

~~~
SELECT column_name AS alias_name
FROM table_name;

SELECT CustomerName AS Customer, ContactName AS [Contact Person]
FROM Customers;

# CustomerName을 Customer로, ContactName을 Contact Person으로 바꾼다. 
# 이 때 바꿀 이름에 띄어쓰기가 있으면 []처리를 해준다.
~~~

##### (1) 컬럼묶음에 별칭 주기

~~~
SELECT CustomerName, Address + ', ' + PostalCode + ' ' + City + ', ' + Country AS Address
FROM Customers;
~~~

-결과 실행화면 

![20_aliascolumsumup](https://github.com/juliahwang/wps-til/blob/master/0519-Day10-python3/HW-SQL%20study/sql-img/20_aliascolumsumup.png)



##### (2) 컬럼묶음에 별칭 주기 - MySQL

- `CONCAT() 함수` 사용

~~~
SELECT CustomerName, CONCAT(Address,', ',PostalCode,', ',City,', ',Country) AS Address
FROM Customers;
~~~

<br>

#### 구문 2 - table 이름바꾸기

~~~
SELECT column_name 
FROM table_name AS alias_name;

SELECT o.OrderID, o.OrderDate, c.CustomerName
FROM Customers AS c, Orders AS o
WHERE c.CustomerName = "Around the Horn" AND c.CustomerID = o.CustomerID;

# Customers 테이블을 c로 정하고 Orders 테이블을 o로 정했을 때 아래의 조건을 만족하는 행 중에서 o테이블의 OrderID와 OrderDate, 그리고 c테이블의 CustomerName을 가져온다.
# 2개 이상의 테이블을 join할 때 길어지는 것을 방지하기 위하여 alias를 사용.
~~~

![20_aliastablejoin](https://github.com/juliahwang/wps-til/blob/master/0519-Day10-python3/HW-SQL%20study/sql-img/20_aliastablejoin.png)

<br>

## 21. JOIN

- 2개 이상의 테이블에서 레코드를 가져와 조합할 때 사용
- 일반적인 join은 inner 형식으로, 공통의 컬럼을 기준으로 값을 가져온다.

#### 구문 (INNER JOIN)

- ON은 WHERE절과 같은 기능으로 JOIN에서 쓰는 조건문이다.

~~~
SELECT o.OrderID, c.CustomerName, o.OrderDate
FROM Orders AS o
INNER JOIN Customers AS c ON o.CustomerID = c.CustomerID;
~~~

<br>

## 21-1. (INNER) JOIN 

- 두 개의 테이블에서 공통된 컬럼을 정하여 그 값이 일치하는행을 출력
- 교집합이라고 해서 `일치하는 수`로 생각하면 안된다.
- 칼럼에서 일치하는 값이 있다면 출력이 되므로 수치와는 아무 관련이 없다.

![innerjoin](https://www.w3schools.com/sql/img_innerjoin.gif)

#### 구문

~~~
SELECT column_name(s)
FROM table1
INNER JOIN table2 
ON table1.column_name = table2.column_name;

SELECT o.OrderID, c.CustomerName, o.OrderDate
FROM Orders AS o
INNER JOIN Customers AS c 
ON o.CustomerID = c.CustomerID;
~~~

##### (1) 3개 테이블 JOIN

~~~
SELECT Orders.OrderID, Customers.CustomerName, Shippers.ShipperName
FROM ((Orders
INNER JOIN Customers IN Orders.CustomerName = Customers.CustomerName)
INNER JOIN Shippers IN Orders.ShipperID = Shippers.ShipperID);

# Orders 테이블과 Customers 테이블 중 고객이름이 일치하는 열을 반환한 후 Orders테이블과 Shippers 테이블의 아이디가 일치하는 열만 출력
~~~

![21_1_innerjoin](https://github.com/juliahwang/wps-til/blob/master/0519-Day10-python3/HW-SQL%20study/sql-img/21_1_innerjoin.png)

<br>

## 21-2. LEFT (OUTER) JOIN

- 왼쪽 테이블 전체값과 그 중 일치하는 오른쪽 테이블의 값을 합해 출력

![leftjoin](https://www.w3schools.com/sql/img_leftjoin.gif)

#### 구문

~~~
SELECT column_name(s)
FROM table1
LEFT (OUTER) JOIN table2 
ON table1.column_name = table2.column_name;

# OUTER 는 써도 되고 안써도 된다.
# table1의 전체값
# table2에서 조건만족하는 값

SELECT Customers.CustomerName, Orders.OrderID
FROM Customers # 왼쪽테이블
LEFT JOIN Orders # 오른쪽 테이블
ON Customers.CustomerID = Orders.CustomerID
ORDER BY Customers.CustomerName;

# 고객 테이블에서는 모든 데이터를 가져오고, 실제로 주문테이블과 일치하는 데이터만 주문테이블에서 가져온다.
~~~

<br>

## 21-3. RIGHT (OUTER) JOIN

- 오른쪽 테이블 전체값과 그 중 일치하는 왼쪽 테이블의 값을 합해 출력

![rightjoin](https://www.w3schools.com/sql/img_rightjoin.gif)

#### 구문

~~~
SELECT column_name(s)
FROM table1
RIGHT (OUTER) JOIN table2 
ON table1.column_name = table2.column_name;

# OUTER 는 써도 되고 안써도 된다.
# table1에서 조건만족하는 값
# table2의 전체값

SELECT Orders.OrderID, Employees.LastName, Employees.FirstName
FROM Orders # 왼쪽테이블
RIGHT JOIN Employees # 오른쪽 테이블
ON Orders.EmployeeID = Employees.EmployeeID
ORDER BY Orders.OrderID;

# 주문에 상관없이 직원 테이블은 모두 가져오고, 그 중 직원아이디가 주문테이블의 아이디와 일치하는 값만 주문테이블에서 가져온다. 
~~~


<br>

## 21-4. FULL (OUTER) JOIN

- 왼쪽 테이블과 오른쪽 테이블 둘 중 하나에서 만족하는 값을 모두 출력 

![fullouterjoin](https://www.w3schools.com/sql/img_fulljoin.gif)

#### 구문

~~~
SELECT column_name(s)
FROM table1
FULL OUTER JOIN table2 ON table1.column_name = table2.column_name;

SELECT Customers.CustomerName, Orders.OrderID
FROM Customers
FULL OUTER JOIN Orders ON Customers.CustomerID=Orders.CustomerID
ORDER BY Customers.CustomerName;

# 다 갖고 오므로 데이터셋이 매우 크다.
~~~

![21_4_fulljoin](https://github.com/juliahwang/wps-til/blob/master/0519-Day10-python3/HW-SQL%20study/sql-img/21_4_fulljoin.png)

##### (1) MySQL에서의 FULL JOIN

- 지원하지 않으므로 UNION을 사용한다.
- mysql홈페이지 #1604 참고.


<br>

## 21-5. SELF JOIN

- 테이블 하나에서 조건을 통해 일치하는 값을 찾을 때 사용

#### 구문

~~~
SELECT column_name(s)
FROM table1 T1, table2 T2
WHERE condition;

SELECT A.CustomerName AS CustomerName1, B.CustomerName AS CustomerName2, A.City
FROM Customers A, Customers B
WHERE A.CustomerID <> B.CustomerID
AND A.City = B.City 
ORDER BY A.City;
~~~

<br>

## 22. UNION 연산자

- 2개 이상의 SELECT 구문을 조합하여 결과값을 합쳐준다.
- UNION에 사용된 각각의 SELECT문은 같은 수의 컬럼을 가지고 있어야 한다.
- 컬럼은 비슷한 데이터 타입을 가지고 있어야 한다.
- 각각의 SELECT문 내에 컬럼은 매칭될 수 있도록 같은 순서로 작성해야 한다.

#### 구문 1. UNION

- `UNION`은 서로 다른 데이터값만 출력한다. 
- 중복되는 것 중에 하나만 출력하는 것이다.

~~~
SELECT column_name(s) FROM table1
UNION
SELECT column_name(s) FROM table2;

SELECT City FROM Customers
UNION
SELECT City FROM Suppliers
ORDER BY City;
~~~

##### (1) UNION + WHERE

~~~
SELECT City, Country FROM Customers
WHERE Country='Germany'
UNION
SELECT City, Country FROM Suppliers
WHERE Country='Germany'
ORDER BY City;
~~~

##### (2) UNION Alias

~~~
# UNION에서 결과셋의 칼럼이름들은 대부분 첫번째 SELECT문을 따른다.

SELECT 'Customer' As Type, ContactName, City, Country
FROM Customers
UNION
SELECT 'Supplier', ContactName, City, Country
FROM Suppliers
~~~


<br> 

#### 구문 2. UNION ALL

- `UNION ALL`은 중복데이터값까지 모두 반환한다. 

~~~
SELECT column_name(s) FROM table1
UNION ALL 
SELECT column_name(s) FROM table2;

SELECT City FROM Customers
UNION ALL
SELECT City FROM Suppliers
ORDER BY City;
~~~

##### (1) UNION ALL + WHERE

~~~
SELECT City, Country FROM Customers
WHERE Country='Germany'
UNION ALL
SELECT City, Country FROM Suppliers
WHERE Country='Germany'
ORDER BY City;
~~~

<br>


## 23. GROUP BY 

- 하나 이상의 컬럼으로 결과셋을 묶을 때 사용 
- 보통 집계함수와 함께 사용된다.
	- COUNT(), MAX(), MIN(), SUM(), AVG()
- 주문테이블에서 상품별 판매액 등을 구할 때 사용

#### 구문

~~~
SELECT column_name, aggregate_func(column_name)
FROM table_name
WHERE column_name operator value
GROUP BY column_name(s);

# 어떤 칼럼을 호출하여 집계함수를 출력할 것인가?


SELECT COUNT(CustomerID), Country
FROM Customers
GROUP BY Country;
# 나라별로 회원 수를 세 준다.

ORDER BY COUNT(CustomerID) DESC;
# 회원이 많은 순서대로 정렬해준다.
~~~


##### (1) GROUP BY + JOIN 

~~~
SELECT Shippers.ShipperName, COUNT(Orders.OrderID) AS NumberOfOrders
FROM Orders
LEFT JOIN Shippers
ON Orders.ShipperID = Shippers.ShipperID
GROUP BY ShipperName;

# 주문테이블 모두에서 shippingID가 일치하는 데이터만 가져오고, 각 선적사 별 이름과 주문량을 이름을 기준으로 그룹핑하여 보여준다. 
~~~

<br>

## 24. HAVING 절

- 집계함수와 사용된다. 
- GROUP BY와 반드시 함께 사용된다. 
- WHERE절이 집계함수와 함께 연결될 수 없어서 HAVING절로 대체한다. 

#### 구문

~~~
SELECT column_name, aggregate_func(column_name)
FROM table_name
WHERE column_name operator value
GROUP BY column_name
HAVING aggregate_func(column_name) operator value;

SELECT COUNT(CustomerID), Country
FROM Customers
GROUP BY Country
HAVING COUNT(CustomerID) > 5;
# 나라별로 회원수를 출력하는데 회원수가 5명 이상인 레코드만 출력한다.
~~~

##### (1) GROUP BY + HAVING + JOIN

~~~
SELECT Employees.LastName, COUNT(Orders.OrderID) AS NumberOfOrders
FROM (Orders
INNER JOIN Employees ON Orders.EmployeeID = Employees.EmployeeID)
GROUP BY LastName
HAVING COUNT(Orders.OrderID) > 10;
# 직원의 성을 기준으로 그룹핑하는데 주문번호의 수가 10개 이상인 데이터만 반환한다.
~~~


<br>

## 25. EXISTS 연산자

- 내부 쿼리(셀렉트문)에 레코드가 존재하는지 알아보고자 할 때 사용
- 하위쿼리가 하나 이상의 레코드를 반환하면 `EXISTS`연산자는 참값을 반환한다.

#### 구문

~~~
SELECT column_name(s)
FROM table_name
WHERE EXISTS
(SELECT column_name FROM table_name WHERE condition);

SELECT SupplierName
FROM Suppliers
WHERE EXISTS (SELECT ProductName FROM Products WHERE SupplierID = Suppliers.supplierID AND Price <= 20);
# 제품테이블에서 공급아이디가 공급자테이블의 공급아이디와 일치하고 가격이 20미만인 제품이름을 반환한 결과셋 중 존재하는  SupplierName을 반환. 
~~~

<br>

## 26. ANY, ALL 연산자

- ANY, ALL : `WHERE`절과 `HAVING`절에 사용된다.
- ANY : 하위 쿼리값 중 하나가 조건을 충족하면 true 반환
- ALL : 모든 하위쿼리값이 조건을 충족하면 true 반환

#### 구문 - ANY

~~~
SELECT ProductName 
FROM Products
WHERE ProductID = ANY (SELECT ProductID FROM OrderDetails WHERE Quantity = 10);

# 주문수량이 10개인 OrderDetails테이블의 모든 레코드를 찾고 그 제품이름을 반환 
~~~

<br>

#### 구문 - ALL

~~~
SELECT ProductName 
FROM Products
WHERE ProductID = ALL (SELECT ProductID FROM OrderDetails WHERE Quantity = 10);

# OrderDetails테이블의 모든 레코드가 주문수량이 10개일 경우 제품이름을 반환 
~~~

<br>

## 27. SELECT INTO

- 데이터를 테이블에서 새 테이블로 복사할 때 사용

#### 구문 - 데이터 모두 옮기기 

~~~
SELECT * 
INTO newtable [IN externalDB]
FROM oldtable
WHERE condition;

SELECT * INTO CustomersBackup2017
FROM Customers;


SELECT * INTO CustomersBackup2017
IN 'Backup.mdb'
FROM Customers;
# 다른 데이터베이스에 새로운 테이블로 복사하는 경우.


SELECT * INTO CustomersGermany
FROM Customers
WHERE Country = 'Germany';
# WHERE절을 사용하여 조건에 맞는 결과셋만 복사.


SELECT * INTO newtable
FROM oldtable
WHERE 1 = 0;
# 기존테이블의 구조만 복사하고 레코드는 가져오고 싶지 않을 때. 
~~~

<br>

#### 구문 - 컬럼 일부만 옮기기 

~~~
SELECT column1 AS newcolumn_name, column2, ...
INTO newtable [IN externalDB]
FROM oldtable
WHERE condition;

SELECT CustomerName, ContactName INTO CustomersBackup2017
FROM Customers;


SELECT Customers.CustomerName, Orders.OrderID
INTO CustomersOrderBackup2017
FROM Customers
LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID;
# 2개 이상의 테이블에서 추출한 데이터를 새 테이블로 복사.
~~~

<br>

## 28. INSERT INTO ~ SELECT

- 이미 존재하는 테이블에 추출한 데이터를 추가로 붙여넣을 때 사용.
- 기존의 데이터에는 영향을 주지 않는다. 


#### 구문 1. 모두 가져와 붙여넣기

~~~
INSERT INTO table2
SELECT * FROM table1
WHERE condition;
~~~


#### 구문 2. 컬럼 일부만 가져와 붙여넣기

~~~
INSERT INTO table2 (column1, column2,...)
SELECT column1, column2,...
FROM table1
WHERE condition;

INSERT INTO Customers (CustomerName, City, Country)
SELECT SupplierName, City, Country FROM Suppliers;
# Customers 테이블의 행 아랫부분에 Supplier의 선택된 행의 레코드를 삽입
# 기존의 데이터에는 전혀 영향을 주지 않는다.
~~~

- 결과 실행화면 

![28_insertintoselect](https://github.com/juliahwang/wps-til/blob/master/0519-Day10-python3/HW-SQL%20study/sql-img/28_insertintoselect.png)

<br>

## 29. COMMENTS

- `--singleline comments`
- `/*multipleline comments*/`

#### 구문

~~~
--SELECT * FROM Customers;
SELECT * FROM Products;
~~~

~~~
/*SELECT * FROM Customers;
SELECT * FROM Products;
SELECT * FROM Orders;
SELECT * FROM Categories;*/
SELECT * FROM Suppliers;
~~~