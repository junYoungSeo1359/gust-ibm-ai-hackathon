# 1. 파이썬 언어 번개처럼 배우기 
본 교육은 Cloud Native Python app을 개발하기 위한 이론과 실습을 위한 교재입니다.  

## 1.1. 사전준비 
파이썬 애플리케이션을 개발하면서 이전에는 Jupyter Notebook으로 개발하거나,  
단일 stand-alone 으로 실행되는 파이썬 애플리케이션을 개발하였을 것입니다.  

이번 lab에서는 파이썬 애플리케이션을 REST API를 제공하는 파이썬 애플리케이션을 개발하고  
애플리케이션을 컨테이너화해서 Cloud Native App으로 만드는 것을 실습해 보겠습니다.  

파이썬 기반  웹 프레임워크는 FastAPI를 사용하여 API Spec을 swaggerUI로 제공하며  
소스는 Git Repository로 저장합니다. 개발 Tool은 마이크로소스트 사의 VSCode를 사용합니다.  

  - python 3.10.11
  - FastAPI 
  - virtualenv
  - VSCode
  - git
  - docker desktop

파이썬 애플리케이션의 독립된 가상 개발환경으로 구성하기 위해 virtualenv를 사용하고, 
컨테이너화를 위해 docker를 사용합니다. 

**SW 설치**
python 3.10을 window store 앱을 사용하여 설치합니다.  

VSCode Tool을 설치합니다.  

VSCode에서 Python Extensions에서 Microsoft에서 제공하는 Python 및 Juypter notebook을 설치합니다.  


## 1.2. 변수 
**변수명 규칙**

> 변수 이름은 문자(letter)나 밑줄(_)로 시작  
> 변수 이름은 문자, 숫자, 밑줄을 포함  

**변수 정의**
파이썬에서 변수를 정의할 때는 특별한 선언이 필요 없습니다. 변수에 값을 할당함으로써 변수를 생성할 수 있습니다.  
변수 이름은 문자와 숫자, 밑줄(_)을 포함할 수 있지만, 숫자로 시작할 수는 없습니다.  
파이썬은 대소문자를 구분하므로 Name과 name은 서로 다른 변수입니다.  

## 1.3. 자료형 
**기본 자료형**
```python
name = "kildong"  # 문자열 변수
age = 20        # 정수 변수
height = 1.5    # 부동 소수점 변수
is_adult = True # 불리언 변수
```

**자료형 : 불리언(Boolean)**
불리언 타입은 True와 False의 두 가지 값만을 가지며, 조건문의 결과를 나타내는 데 주로 사용됩니다.  
```python
is_enabled = True
is_audit = False
```

**자료형: 리스트(List)**  
리스트는 가변적(mutable)으로, 그 내용(요소)을 변경할 수 있습니다.  
대괄호([])를  사용하여 리스트를 생성하며, 리스트 안에는 어떠한 데이터 타입도 저장할 수 있습니다.  
또한, 리스트는 중복된 값을 저장할 수 있습니다.  

```python
fruits = ["apple", "banana", "cherry", "kiwi"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "apple", True]

print(fruits)
print(numbers)
print(mixed)
```

__리스트 요소 접근__: 인덱스를 사용하여 리스트의 특정 요소에 접근할 수 있습니다. 인덱스는 0부터 시작합니다.
```python
print(fruits[0])  # apple
```
__리스트 수정__: 리스트의 요소를 변경하거나, append() 메소드를 사용하여 새 요소를 추가할 수 있습니다.
```python
fruits[1] = "blueberry"
fruits.append("orange") . 
```
__리스트에서 요소 제거__: remove() 메소드로 특정 값을 제거하거나, pop() 메소드로 특정 인덱스의 요소를 제거할 수 있습니다.  

```python
fruits.remove("banana")
fruits.pop(1)
```

**리스트(List) 좀더 알아보기**
리스트 슬라이싱: 리스트의 일부분을 선택하여 새로운 리스트를 생성합니다. [시작:끝:간격]의 형태로 사용합니다.
numbers = [0, 1, 2, 3, 4, 5]
print(numbers[1:4])  # [1, 2, 3]
print(numbers[::2])  # [0, 2, 4], 간격이 2인 요소들
**리스트 컴프리헨션**: 리스트를 생성하기 위한 간결한 방법으로, for 루프와 if 조건문을 포함할 수 있습니다.
squares = [x**2 for x in range(10)]
even_squares = [x**2 for x in range(10) if x % 2 == 0]

**자료형 : 튜플(Tuple)**
튜플은 불변적(immutable)으로, 한 번 생성되면 그 내용을 변경할 수 없습니다.  
소괄호(())를 사용하여 튜플을 생성합니다. 튜플 역시 다양한 데이터 타입의 요소를 포함할 수 있고, 중복된 값을 저장할 수 있습니다.  
```python
colors = ("red", "green", "blue")
info = (1, "kildong", True)
```

__튜플 요소 접근__: 리스트와 마찬가지로 인덱스를 사용하여 튜플의 특정 요소에 접근할 수 있습니다.  
```python
print(colors[1])  # green
```

__불변성__: 튜플의 요소는 변경할 수 없으므로, 튜플을 수정하려고 시도하면 오류가 발생합니다.  
```python
# colors[1] = "yellow"  # 이 코드는 오류를 발생시킵니다.
```
> **리스트 vs 튜플**
> 
> __공통점__: 두 타입 모두 다양한 데이터 타입의 요소를 저장할 수 있으며, 중복된 값을 포함할 수 있습니다.  
**차이점**: 리스트는 가변적이어서 요소의 추가, 삭제, 변경이 가능하지만, 튜플은 생성 후 변경할 수 없습니다.  

**자료형 : 사전(Dictionary)**
사전은 키(key)와 값(value)의 쌍을 저장하는 가변 컨테이너입니다.  
사전은 중괄호를 사용하여 생성하며, 각 키-값 쌍은 콜론(:)으로 구분됩니다.  

```python
customer_list = {}
customer_array = []
customer = {"name": "kildong", "age": 20, "city": "Seoul"}
print(customer["name"])  # kildong
print(customer)  # kildong
print(customer_list) 
print(customer_array)   
```

**사전(Dictionary) 변경**

항목 추가 및 수정: 사전에 새로운 키-값 쌍을 추가하거나, 이미 존재하는 키의 값을 수정할 수 있습니다.
```python
customer["email"] = "kildong@gmail.com"  # 새 항목 추가
customer["age"] = 30                     # 기존 항목 수정
print(customer_list) 
print(customer_array)   
```

**사전(Dictionary) 삭제**
항목 제거: del 키워드나 .pop(key) 메서드를 사용하여 사전에서 항목을 제거할 수 있습니다.  
```python
del customer["city"]  # 키와 값을 제거
age = customer.pop("age")  # 값을 제거하고 그 값을 반환
print(customer_list) 
print(customer_array)   
```

**사전 메서드**

.keys(): 사전의 모든 키를 반환합니다.

.values(): 사전의 모든 값을 반환합니다.
.items(): 사전의 모든 키-값 쌍을 (키, 값) 형태의 튜플로 반환합니다.

```python
for key in customer.keys():
    print(key)

for value in customer.values():
    print(value)

for key, value in customer.items():
  print("key:{0}, value:{1}".format(key, value))
```

# 2. FastAPI를 이용한 backend 애플리케이션 개발
FastAPI란 파이썬 3.6이상에서 동작하는 최근에 주목받고 있는 현대적이고,  
빠르게 REST API기반 서비스를 제공하는 웹 프레임워크입니다.

FastAPI는 파이썬 프레임워크의 Flask와 비슷한 구조를 가지고 있으나 아래와 같은 특징을 가지고 있습니다  
  - 적은 코드로 훨씬 간편하고, 쉽고, 빠르게 Web 개발  
  - 비동기식 작성되어 있어 빠른 성능을 지원  
  - 개방형 표준 OpenAPI 인 Swagger 지원  

## 2.1. Setting Up FastAPI
fastapi는 적은 코드로 쉽게 API를 작성할 수 있도록 합니다. 
fastapi를 이용하여 hello world API를 작성할 수 있습니다.  

### 2.2.1. fastapi 설치-실습 
pip를 사용하여 FastAPI 및 해당 종속성을 설치합니다:  
```bash
mkdir sample
cd sample
python3 -m venv venv
source venv/bin/activate
```

 pip를 사용하여 FastAPI 및 해당 종속성을 설치합니다:
 ```
 pip install fastapi uvicorn
 ```

## 2.2. fast api API 개발
FastAPI 는 다음의 순서로 개발합니다.  
- Import FastAPI  
- app instance 생성   
- path operation decorator 작성 (예시 :  @app.get("/"))  
- path operation function 작성 (like def root(): ... above)   
- Run server (예시 uvicorn main:app --reload 또는 fastapi dev main.py)  

**Step 1 : import FastAPI** 
fastAPI 프레임워크로 Hello world를 제공하는 API를 만듭니다.  
 ```bash
"""
main.py
"""
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello world"}
```

**Step 2 : 생성FastAPI "instance"**  
위에서 작성한 main.py에서 **app = FastAPI()** 문장에서 app라는 변수는 FastAPI의 인스턴스가 됩니다. 

**Operation**
여기서 'Operation'은 HTTP '메소드' 중 하나를 의미합니다.

One of:
- POST
- GET
- PUT
- DELETE

**Step 3 : path operation 생성** 
'path'는 일반적으로 '엔드포인트' 또는 '경로'라고도 합니다.  
'path'는 첫 번째 "/"로 시작하는 URL의 root부분을 의미합니다.  
API를 구축할 때 'path'는 비즈니스와 관련된 '리소스'를 묶어 구분하는 방법을 정의합니다.  

API를 구축할 때는 일반적으로 이러한 특정 HTTP 메서드를 사용하여 특정 작업을 수행합니다.  

일반적으로 다음과 같이 사용합니다: 

POST: 데이터 생성  
GET: 데이터 읽기  
PUT: 데이터 수정  
DELETE: 데이터 삭제  

그래서 OpenAPI에서는 각 HTTP 메서드를 "operation"이라고 합니다.

***path operation decorator***
```python
@app.get("/")
```
app.get("/")은 바로 아래의 함수가 다음 요청을 처리하는 역할을 담당한다고 FastAPI에 알려줍니다:
 - path는 /  
 - get operation 사용  

> **@decorator**
> 
> 파이썬에서 @something 구문을 "데코레이터"라고 합니다.  
> "데코레이터"는 아래 함수를 가져와서 무언가를 수행하는 것을 의미합니다.  
> 이 경우, 이 데코레이터는 아래 함수가 경로 / 연산 get에 해당한다고 FastAPI에 알려줍니다  
> 이것이 바로 "path operation 데코레이터"입니다.

다음은 그 이외 operation들 입니다.

- @app.post()  
- @app.put()  
- @app.delete()  

**Step 4: path operation function 정의**
다음은 path operation function 입니다.  
- path: is /.
- operation: is get.
- function: "decorator" 아래의 파이썬 function

이 함수는 GET operation을 사용하여 URL "/"에 대한 요청을 받을 때마다 FastAPI에 의해 호출되는 비동기 function 입니다.  

```python  
@app.get("/")
async def hello():
  return {"message": "Hello World"}
```

비동기 정의 대신 일반 함수로 정의할 수도 있습니다:
```python
@app.get("/")
def hello():
    return {"message": "Hello World"}
```

**Step 5: 실행** 
```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def hello():
    return {"message": "Hello World"}
```
딕셔너리, 리스트, 단수값을 문자열, int 등으로 반환할 수 있습니다.

또한 다음에 실습하는 Pydantic 모델을 반환할 수도 있습니다.


```bash
uvicorn main:app --reload

또는 

fastapi dev main.py
```
## 2.3. Path Parameters 
파이썬 형식 문자열에 사용되는 것과 동일한 구문을 사용하여 path 'parameter' 또는 'variable'를 선언할 수 있습니다:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}
```
path parameter item_id의 값은 함수에 item_id 인수로 전달됩니다.

따라서 이 예제를 브라우져의 Url 입력창에서 입력하면 **http://127.0.0.1:8000/items/foo** 다음과 같은 응답이 표시됩니다:  
```python
{"item_id":"foo"}
```

**Path parameters with types**
이 예제를 실행하고 http://127.0.0.1:8000/items/3 에서 브라우저를 열면 다음과 같은 응답이 표시됩니다:

표준 파이썬 타입 어노테이션을 사용하여 함수에서 경로 매개변수의 타입을 선언할 수 있습니다:

이 예제를 실행하고 http://127.0.0.1:8000/items/3 에서 브라우저를 열면 다음과 같은 응답이 표시됩니다:

```bash
{"item_id":3}
```

**async def read_item(item_id: int):**
이 경우 item_id는 int로 선언됩니다.  

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
```

{"item_id":3}

**Data conversion**
함수가 받은(그리고 반환한) 값은 문자열 "3"이 아니라 파이썬 정수로 3이라는 것을 알 수 있습니다. 

따라서 해당 유형 선언을 사용하면 FastAPI는 자동 요청 "파싱"을 제공합니다.  

**Data Validation**
http://127.0.0.1:8000/items/test 브라우저로 이동하면 다음과 같은 HTTP 오류가 표시됩니다:  

```python
{
  "detail": [
    {
      "type": "int_parsing",
      "loc": [
        "path",
        "item_id"
      ],
      "msg": "Input should be a valid integer, unable to parse string as an integer",
      "input": "test",
      "url": "https://errors.pydantic.dev/2.1/v/int_parsing"
    }
  ]
}
```

다음과 같이 int 대신 float를 제공한 경우에도 동일한 오류가 나타납니다: 
**http://127.0.0.1:8000/items/4.2**

**Documentation**
http://127.0.0.1:8000/docs 에서 브라우저를 열면 다음과 같은 자동 대화형 API 문서가 표시됩니다:

![](img/01-swagger-ui.png)

## 2.4. Query Parameters(실습)
path parameter에 포함되지 않은 다른 함수 매개변수를 선언하면 해당 매개변수는 자동으로 'Query' parameter로 해석됩니다.  
```python
from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]
```

쿼리는 URL의 ? 뒤에 오는 키-값 쌍의 집합으로, & 문자로 구분됩니다.  

예를 들어, URL:  
```python
http://127.0.0.1:8000/items/?skip=0&limit=10
```
query parameters 는:  

- skip: 값을 0으로 설정  
- limit: 값을 10으로 설정  

쿼리는 URL의 ? 뒤에 오는 키-값 쌍의 집합으로, & 문자로 구분됩니다.

**Defaults**
Query parameter는 path의 고정된 부분이 아니므로 선택 사항일 수 있으며 기본값을 가질 수 있습니다.  
위의 예에서 기본값은 skip=0 및 limit=10입니다.  
아래의 Url을 입력하면 
```python
http://127.0.0.1:8000/items/
```

다음과 동일
```python
http://127.0.0.1:8000/items/?skip=0&limit=10
```

## 2.5. FastAPI 라우터(실습)
**FastAPI 라우터(router)**  
FastAPI의 라우터(router)는 
- 서로 다른 기능을 그룹화하여 코드를 분리하고  
- 애플리케이션을 구조화하고  
- 독립적으로 모듈화  
하는데 도움을 제공하는 FastAPI 패키지입니다.  


예제에서는 APIRouter를 사용하여 Hello world에 router로 구조화합니다.  
> **include_router**
> include_router(router1, router2, router3, ...) 함수는 APIRouter로 정의한 라우트를 main 애플리케이션에 import하고, main 애플리케이션의 인스턴스(app)의  

**hello router를 작성** 
fastapi 패키지의 APIRouter 클래스를 임포트(import)하고, APIRouter() 를 사용하여 인스턴스를 생성합니다.  

routers 폴더를 생성햐고, 아래의 hello.py 파이썬을 작성합니다.  
```bash
# 폴더 생성
mkdir routers
```

hello.py 파이썬 프로그램을 작성합니다.   
```python
# hello.py
from fastapi import APIRouter, HTTPException

router = APIRouter(prefix='/api/v1')

@router.get("/")
def hello(message: str):
    return {"message": "Hello {0} !!!".format(message)}

```
### 라우터(router) 추가 
**include_router** 함수를 사용하여 임포트할 hello 라우터를 추가합니다. 

```bash
# main.py

from fastapi import FastAPI
from routers import hello

app = FastAPI()

# Add router
app.include_router(hello.router)

```

### 2.5.1. todo API 개발 
**todo router 개발**
todo 리스트를 조회하고 post하는 것을 router를 이용하여 API를 작성하는 것을 실습니다.

todo를 생성하고 조회하는 라우터를 routers 폴더내에 정의합니다.  
이 코드는 todo를 처리를 위해 2개의 get/post 라우트를 다음과 같이 작성합니다.  
```python
# todo.py
from fastapi import APIRouter

todo_router = APIRouter()

todo_list = []

@todo_router.post("/todo")
async def add_todo(todo: dict) -> dict: 
  todo_list.append(todo)
  
  return {"message" : "todo가 등록되었습니다."}

@todo_router.get("/todo")
async def retrieve_todo_all() -> dict:  
  return {"todos" : todo_list}

@todo_router.get("/todo/{todo_id}")
async def retrieve_todo(item_id: int):
  for todo in todo_list:
    if todo.id == todo_id:
      return todo
  
  return {"message" : "id가 {0}인 todo가 존재하지 않습니다.".format(todo_id)}

@todo_router.delete("/todo/{item_id}")
async def delete_todo(item_id: int):
  for todo in todo_list:
    if todo.id == todo_id:
      return todo
  
  return {"message" : "id가 {0}인 todo가 존재하지 않습니다.".format(todo_id)}

```

**todo main**
todo main.py 파이썬 프로그램을 작성합니다.  
```python
# main.py
from fastapi import FastAPI
from routers import todo 
app = FastAPI()

app.include_router(todo.todo_router)
```

**todo test** 
fastapi 기반 todo api를 다음과 같이 item을 todo_list에 추가하는 post api를 테스트 합니다.  
```bash
curl -X 'POST' \
'http://localhost:8000/todo' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{
  "id": 1,
  "item" : "My Item"
}'
```

item을 todo_list에 추가하는 post api를  재수행 테스트 합니다.  
```bash
curl -X 'POST' \
'http://localhost:8000/todo' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{
  "id": 2,
  "item" : "My Item 2"
}'
```

## 2.6. pydantic 모델
Pydantic은 데이터의 타입과 데이터 검증을 해주는 라이브러리로, 타입 힌트를 활용하여 런타임에 입력 데이터 유효성을 검사하는데 활용됩니다. 그리고 BaseModel을 상속하여 클래스를 정의하고 Property 데이터를 정의할 수 있습니다. 

```python
from pydantic import BaseModel

class Item(BaseModel):
  id: int
  item : str
```

### 2.6.1. todo app 개발 
Pydantic을 이용하고, todo app을 main과 routers로 분리해서 todo app을 개발합니다.  

model 파일을 다음과 같이 작성합니다.  기존에 dictionry 대신 Pydantic 을 사용하여 모델을 정의하고  
Request Body의 Input으로 사용합니다.  

**models**
```python
# models.py
from pydantic import BaseModel
from typing import Optional 

class Item(BaseModel):
  id: int
  item : str
```
**router**
routers 폴더를 작성하고 routers 폴더에 todo router를 작성합니다.
위에서 작성한 models.py 파일을 import 합니다.  
라우터에 Pydantic Model을 적용합니다.  

```python
#todo.py
from models import Item 
```

router의 전체 코드는 다음과 같습니다.  
```python
from fastapi import APIRouter 
from models import Item 

todo_router = APIRouter()
todo_list = [] 

@todo_router.get("/items/{item_id}")
async def read_item(item_id: int):
  for item in todo_list:
    print(item)
    if item.id == item_id:
      return item

  return {"message" :  "todo가 존재하지 않습니다."}

@todo_router.get("/items")
async def read_item_all():
  return todo_list

@todo_router.post("/items")
async def add_item(item: Item):
  todo_list.append(item)
  return {"message" : "성공적으로 추가되었습니다."}

@todo_router.put("/items/{item_id}") 
async def update_todo(item: Item, item_id: int):
  for todo in todo_list:
    print(item)
    if todo.id == item_id:
      todo.item = item.item
      return {"message" : "성공적으로 업데이트 되었습니다."}

  return {"message" : "{0} todo 가 없습니다.".format(item_id)}

@todo_router.delete("/items/{item_id}")
async def delete_todo(item_id: int):
  for index in range(len(todo_list)):
    todo = todo_list[index]
    if todo.id == item_id:
      todo_list.pop(index)
  
  return {"message" : "id 가 {0}인 todo 가 없습니다.".format(item_id)} 

@todo_router.delete("/items")
async def delete_todo_all():
  todo_list.clear()
  
  return { "message" : "Todos가 삭제되었습니다."}
```

**main**
파이썬 메인 애플리케이션을 작성합니다.  
todo router를 import하여 app에 router를 추가합니다.  

```python
# main.py 
from fastapi import FastAPI
from routers import todo 

app = FastAPI() 

app.include_router(todo.todo_router)
```

## 2.7. 응답 모델
응답 모델은 API 라우터의 path가 반환하는 데이터의 템플릿 역할을 하며,  
API 요청에 대한 적절한 응답을 렌더링하기 위해 pydantic을 사용합니다.  

### 2.7.1. FastAPI 응답
응답은 HTTP 메소드를 API를 통해 요청을 응답하는 결과를 의미하며,  
API 응답은 JSON 또는 XML 형식으로 전달합니다.  
응답의 결과로는  
- 응답 헤더(+상태코드)
- 응답 Body로

구성됩니다. 

**응답 헤더**
응답 헤더는 요청에 대한 응답 상태와 Body에 대한 Content-Type의 유형이 무엇인지 알려주는 역할을 합니다.  

상태 코드는 클라이언트가 요청한 서버의 응답에 포함되는 상태코드로서 다음과 같은 의미합니다.  
- 2XX : 요청을 성공적으로 처리했다  
- 3XX : 요청을 리다이렉트했다  
- 4XX : 클라이언트측의 요청에 오류가 있다  
- 5XX : 서버측에 오류가 있다  

### 2.7.2. 응답 모델 작성 
응답 모델을 pydantic 을 사용하여 응답 모델을 정의합니다.  
List로 출력하기 위해 models.py 파일에 typing 모듈에서 List를 Import 합니다.  
**from typing import List**  

Items라는 응답 모델을 다음과 같이 정의합니다.  

```python
from pydantic import BaseModel
from typing import List

class Item(BaseModel):
  id: int
  item : str

  
class Items(BaseModel):
  todos : List[Item]
```
Swagger-UI 에서 전체 todo 목록을 조회하는 API의 응답 부분을 확인하면 아래와 같습니다.  

![](img/02-before-response-model.png)
todo 목록을 반환하는 todo.py에 있는 router에 응닫 모델을 추가합니다.   

```python
from models import Item, Items
:



@todo_router.get("/items", response_model=Items)
async def read_item_all():
  return {"todos": todo_list}
```

다음은 router에 응답 모델을 추가한 경우 Swagger UI에서 API의 응답정보가 
어떻게 변경되었는지 확인합니다.  

![](img/03-after-response-model.png)

Swagger-UI 에서 todo item을 추가하는 API를 호출하고, todo Item 전체 목록을 조회하는 API를 호출합니다.  

### 2.7.3. 응답 오류 처리 
이전에 상태 코드를 클라이언트에 알리는 방법을 알아봤습니다.  
오류 응답 메시지를 그대로 클라이언트에게 노츨하면 오류의 원인을 파악하기 어려울 뿐만 아니라 시스템에 중요정보가 보안 위험에 그대로 노출될 수 있습니다. 
FastAPI에서는 이러한 문제를 해결하기 위해 오류 처리를 위한 **HTTPException** 클래스를 사용하여 오류처리를 합니다.  

> HTTPException 은 다음의 인수를 갖고 있습니다.
>
> status_code : 예외처리시 응답 상태코드  
> detail : 클라이언트에게 전달할 메시지  
> headers : 헤더를 요구하는 응답을 위한 인수 

이전에 작성했던 id값을 입력하면 todo 를 조회하는 router를 확인합니다.  
```python
@todo_router.get("/items/{item_id}")
async def read_item(item_id: int):
  for item in todo_list:
    print(item)
    if item.id == item_id:
      return item

  return {"message" :  "todo가 존재하지 않습니다."}
```

위의 todo가 존재하지 않는 경우를 HTTPException으로 처리하는 것으로 수정합니다.
```python
@todo_router.get("/items/{item_id}")
async def read_item(item_id: int):
  for item in todo_list:
    print(item)
    if item.id == item_id:
      return item

  raise HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="id가 {0} todo가 존재하지 않습니다.".format(item_id)
  )  
```


## 2.8. database 연결
이번 랩은 FastAPI를 사용하여 데이터베이스와 연결하는 것을 실습니다. 
지금까지는 애플리케이션을 구조화하거나, 라우트를 추가하고, 모델을 구현하였습니다.  
이제는 데이터를 영구적으로 저장하기 위해 데이터베이스를 사용할 것입니다.  
데이터베이스와 파이썬 API를 연돌할려면 SQLModel 라이브러리를 설치해야 해야하며, 
pydantic과 SQLAlchemy를 기반으로 합니다.  

> **SQLAlchemy**
> 
> 파이썬 ORM 모듈에서 가장 많이 사용되는 패키지  
> SQLAlchemy는 파이썬 코드에서 DB와 연결하기 위해 사용  
> SQLAlchemy는 DB 테이블을 프로그래밍 언어의 클래스로 표현해주고 테이블의 CRUD를 처리   


### 2.8.1. 모듈 설치  
데이터베이스 연결을 위한 파이썬 모듈을 설치합니다.  
```python
pip install SQLAlchemy
pip install mysql
```

### 2.8.2. 데이터베이스 연결 모듈 작성
database를 sqlalchemy를 이용해 연결해주는 파일을 작성합니다.  

```python
# database.py 
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os    

load_dotenv()

DB_SERVER = os.getenv("DB_SERVER")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD") 
DB_NAME = os.getenv("DB_NAME")
DB_PORT = os.getenv("DB_PORT")

DATABASE_URL = "mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_SERVER}:{DB_PORT}/{DB_NAME}".format(DB_USERNAME=DB_USERNAME, DB_PASSWORD=DB_PASSWORD, DB_SERVER=DB_SERVER, DB_PORT=DB_PORT, DB_NAME=DB_NAME)
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# db 세션 객체를 생성하고 함수 종료 직전에 다시 db.close()를 호출한다.  
def get_db():
  db = SessionLocal() 
  
  try:
    yield db
  finally:
    db.close()
```  

앞으로 우리가 만들 대부분의 API는 데이터베이스를 사용해야 하기 때문에 이러한 패턴이 반복될 것이다. 이 부분을 자동화할 수는 없을까? FastAPI의 "Dependency Injection"을 사용하면 이 부분을 깔끔하게 처리할 수 있다  

database.py에서 연결한 db를 테이블과 매핑시키는 역할을 하는 model 파일을 작성합니다.  

### 2.8.3. 모델 파일 작성 
데이터베이스에 데이터를 crud하기 위한 pydantic 을 이용하여 model 파일을 작성합니다.  
Base 모델을 상속받아서 테이블 오브젝트를 정의하고 테이블 이름과 컬럼을 정의하고, Primary 컬럼을 설정합니다.  
테이블의 Row에 해당하는 Model을 정의합니다.  

```python
from sqlalchemy import Column, Integer, String
from database import Base 
from pydantic import BaseModel

class User(Base):
  __tablename__ = "user_01"
  
  id = Column(Integer, primary_key=True, index=True)
  username = Column(String(50), index=True)
  nickname = Column(String(100))
  
class UserModel(BaseModel):
  username: str
  nickname: str
```

### 2.8.4. crud 처리 작성 
데이터베이스 crud처리하는 모듈을 별도로 작성합니다.
```python
# crud.py
from sqlalchemy.orm import Session
from models import User, UserModel

def get_user_all(db: Session):
    return db.query(User).all()

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def create_user(db: Session, user: UserModel):
    db_user= User(username=user.username, nickname=user.nickname)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return db_user
```

### 2.8.5. router 작성

데이터베이스 테이블의 Row에 해당하는 UserModel과 데이터베이스를 연결하기 위한 Base를 import 합니다.  
```python
from models import UserModel, Base
```

이전에 작성했던 데이터베이스 처리를 위한 curd.py 모듈을 import 합니다.  
```python
from routers import crud
```

```python
rom fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import Annotated

from models import UserModel, Base
from routers import crud
from database import SessionLocal, engine, get_db

router = APIRouter()

Base.metadata.create_all(bind=engine)

db_conn = Annotated[Session, Depends(get_db)]    

@router.get("/users")
def read_user_all(db : db_conn):
    tasks = crud.get_user_all(db)
    
    return tasks

@router.get("/users/{user_id}")
def read_task(user_id: int, db: db_conn):
    user = crud.get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/users/")
def create_user(user: UserModel, db: db_conn):
    return crud.create_user(db, user)
```

### 2.8.6. 데이터베이스 연결정보 설정

**.env** 파일을 다음과 같이 작성합니다.  
```bash
DB_SERVER=DB SERVER IP
DB_USERNAME=DB 연결 사용자 
DB_PASSWORD=DB 사용자 비밀번호
DB_NAME=데이터베이스명 
DB_PORT=데이터베이스 포트  
```

### 2.8.7. 테이터베이스 연결 테스트 
애플리케이션을 시작합니다.  
```bash
uvicorn main:app --reload
```

## 3. 배포
이번 랩에서는 docker를 이용하여 local에 container로 배포하는 것을 실습합니다.

### 3.1. 배포 준비
배포는 애플리케이션 단계에서 마지막 단계로 애플리케이션을 배포하기 전에 배포를 위한 설정이 모두 제대로 준비됐는지 확인해야 합니다.  
이 설정에는 의존 라이브러리가 포함된 requirements.txt 파일이 준비되어야 하고, 항상 최신상태로 유지되어야 합니다.  

파이썬에서는 requirements.txt 파일을 **pip freeze** 명령어로 추출할 수 있습니다.  
이 명령어를 사용하면 현재 환경에서 설치된 모든 패키지의 목록과 
의존성 패키지 목록을 다음과 같이 추출하고, 의존성 패키지를 관리 할 수 있습니다.  

```bash
pip freeze > requirements.txt
```

### 3.2. Dockerfile 작성 
Dockerfile은 docker 이미지를 빌드하기 위한 template 입니다.  
Dockerfile에는 아래와 같이 몇개의 docker 명령어로 구성됩니다.  

**FROM**  
Dockerfile 첫번째 라인은 FROM 키워드로 기본 이미지를 지정합니다.  
여기에 python 버전을 명시할 수 있습니다. 현재 랩에서 사용하는 버전은 3.11.x 버전을 사용합니다.  

**ENV**  
Docker가 실행했을 때 사용하는 환경변수를 정의합니다.  
여기에서는 fastapi를 실행할 때 사용하는 포트번호를 환경변수로 정의합니다.  

**WORKDIR**  
위 키워드는 작업 디렉토리 또는 폴더를 지정합니다.  여기에서는 /app 디렉토리를 지정합니다.  

**RUN**  
위 키워드는 패키지를 설치하거나 명령어를 실행할 때 사용합니다. 여기에서는 가상환경을 만드는 것을 실행합니다.  

**ADD**  
ADD 명령어는 COPY와 유사하게 작동하지만 몇 가지 추가 기능을 제공합니다.  
이 명령어는 지정한 URL을 통해 파일을 다운로드할 수 있으며, 압축된 파일을 자동으로 추출할 수 있는 기능을 갖고 있습니다. 여기에서는 의존성 파일정보가 들어있는 requirements.txt 파일을 docker에 복사합니다.  

**COPY**  
COPY 명령어는 Docker 소스 파일이나 디렉토리를 Docker 이미지로 복사하는 데 사용됩니다.  

**EXPOSE**  
docker가 실행될 때 외부로 오픈하는 포트 번호를 지정합니다.  


CMD 명령어는 docker 이미지를 컨테이너로 실행할 때나 default로 실행할 커맨드, ENTRYPOINT 명령어로 지정된 커맨드에 default로 넘길 파라미터를 지정할 때 사용됩니다.  


> **CMD vs ENTRYPOINT**
컨테이너 실행시 CMD 명령문은 파라미터 입력이 없을 경우 정의된 파라미터가 실행이 되며, 상황에  따라 파라미터를 추가 입력시 입력 파라미터가 우선순위를 갖게 됩니다.  
> ENTRYPOINT의 경우 컨테이너가 실행시 항상 실행이 되기 때문에 디폴트 실행 명령어를 사용할때 유용합니다.  


```python
FROM python:3.10.11-slim
ENV PORT 8000
WORKDIR /app
# Create virtual environment
RUN python3 -m venv /ve

# Enable ve
ENV PATH="/ve/bin:$PATH"

# Copy requirements file
ADD requirements.txt .

# Copy source to target in docker
COPY . . 

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt 

EXPOSE $PORT

CMD uvicorn --host=0.0.0.0 --port $PORT  main:app
```

### 3.3. docker build 
Dockerfile을 정의하고 이미지를 빌드할려면 다음과 같이 실행합니다.  

```bash
# docker hub에 등록한 자신의 계정명/이미지명:테그 
docker build -t owner/이미지명:tag명 . 

# 예시
docker build -t nexweb1/todo:latest .
```

![](img/04-docker-build.png)


### 3.4. 배포 
docker 이미지를 만들고 이것을 container로 실행하는 명령어가 **docker run** 명령어 입니다.  
docker run 명령어를 실행하면 docker가 실행되고 local 환경에 docker 이미지가 없는 경우 docker hub에서 docker 이미지를 pull하고 container 로 실행합니다.  

이전에 만든 docker 이미지를 docker hub에 push하고, docker를 local에 배포하는 명령어를 다음과 같이 실행합니다.  

**docker hub**
```bash
docker push 자신의dockerhub계정/todo:latest 
# 예시
docker push nexweb1/todo:latest
```

![](img/05-docker-push.png)

**docker run**
docker 이미지를 pull하고 container로 실행합니다.  
container로 실행할때 파이썬 애플리케이션이 DB 접속정보를 환경정보에서 읽어오기 때문에 파라메터로 DB 접속정보를 제공합니다.  

```bash
docker run --name todo -d
docker run --name todo -p 8000:8000 -d -e DB_USERNAME=username -e DB_PASSWORD=password -e DB_SERVER=DB_SERVER_IP -e DB_PORT=3306 -e DB_NAME=demo
demo nexweb1/todo  

```

![](img/06-docker-run.png)




