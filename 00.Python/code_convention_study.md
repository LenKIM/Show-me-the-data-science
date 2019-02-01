# 파이썬 코드 컨벤션

***파이썬스럽다(Pythonic)*** 하다 라는 의미는 무엇인가?

- PEP 8
- PEP 20

: https://bitbucket.org/sk8erchoi/peps-korean/downloads/

다운로드 받아서 번역본 읽기.

**"멍청한 일관성의 고집은 소인배의 발상(a foolish consistency is the hobgoblin of little minds)"**



## 파이썬 스타일 철학

### ⚫️ 명시가 암시보다 좋다.

```python
# 나쁨
def make_dict(*args):
    x, y = args
    return dict(**locals())

# 좋은
def make_dict(x, y):
    return {'x':x, 'y':y}
```

### ⚫️ 여유로운 것이 밀집한 것보다 좋다.

```python
#나쁨
print('one'); print('two')

if x == 1: print('one')
    
if (<복잡한 표현 1> and
   	<복잡한 표현 2>):
    # 원하는 작업
    
#좋음
print('one')
print('two')

if x==1:
    print('one')
    
cond1 = <복잡한 표현 1>
cond1 = <복잡한 표현 2>
if cond1 and cond2:
    # 원하는 작업

```

cond1, cond2 로 여유롭게 코딩할 것.



### ⚫️ 오류 앞에서 절대 침묵하지 말지어다.

오류 앞에서 침묵해도 되는 상황이 언제인지 아래 코드가 보여준다.

```python
def format_output(code, args):
    if not args['color']:
        return code
    lexer = None
    
    # 스택오버플로 태그에서 렉서를 착거나
    # 쿼리 문자열로부터 렉서를 찾으려 시도
    for keyword in args['query'].split() + args['tags']:
        try:
            lexer = get_lexer_by_name(keyword)
            break
        except ClassNotFound:
            pass
        
    # 위에서 렉서를 찾지 못하면 렉서 추정 도구(guess_lexor)를 사용함
    if not lexer:
        lexer = guess_lexer(code)
        
    return highlist(code,
                   lexer,
                   TerminalFormatter(bg='dark'))
```

그럼 '침묵하지 말지어다' 의 의미는?

```python
while True:
    try:
        print('nyah', end=" ")
    except:
        pass
```

위 코드는 절대 멈추지 않을 것. 그러므로 실행시키면 안된다.

*오류는 꼭 예외처리하거나 재발생 처리하여 그대로 묻히는 일이 없도록 하자.*



### ⚫️ 함수 인자는 사용하기에 직관적이어야 한다.

```python
def func(positional, keyword=value, *args, **kwargs):
    pass
```

1. positional - 위치 인자
2. keyword - 키워드 인자
3. *arg - 가변 인자 리스트
   send(message, *args)   
   send("42", "Frankie", "Benjy", "Trillian") => ("Frankie", "Benjy", "Trillian") 만 튜플
4. **kwargs - 가변 키워드 인자 딕셔너리  
   키워드 인자를 개수의 제약 없이 자유롭게 정의하여 함수에 전달.  dict 으로 넘겨줘야 함.

참고 예시 사이트 :
https://ddanggle.gitbooks.io/interpy-kr/content/ch1-args-kwargs.html



### ⚫️ 구현 결과를 설명하기 어렵다면, 그 아이디어는 나쁘다.

 파이써니트나는 복잡한 방법으로 문제를 해결할 줄도 알아야 하지만 그 문제를 우회하는 방법도 알아야 한다.



### ⚫️ 우리는 모두 책임 있는 사용자다.

파이썬에서는 자바에서처럼 'private'가 같이 방어적인 성격의 코드와는 다른 철학을 가졌다.

파이썬 커뮤니티에서는 개발자가 서로의 코드 사이에 콘크리트 벽과 같은 보안을 세우는 방식보다 구성 요소에 직접 접근하는 것을 방지하는 컨벤션 모음을 따르길 서호한다. 프라이빗 속성에 관한 컨벤션은 변수명 앞에 sys._getframe 같이 밑줄로 표기

만약 이를 어기면 클라이언트는 책임 져야 한다.



### ⚫️ 함수의 결과 값은 한 곳에서만 반환하자.

함수 실행의 종료는 2가지.

하나는 오류가 발생하여 종료되는 경우 / 나머지는 함수가 정상적으로 실행되어 결과 값을 반환한 뒤 종료되는 경우

None,False를 반환하는 것 Ok.

가끔은 여러 개의 반환문을 사용하는 것도 필요.

그러나 결론은 가능한 한 하나의 종료 시점만을 설정할 것. 종료 시점이 여러 개라면 함수의 최종 결과 값이 어디서 반환되었는지 파악하기 쉬워진다.

```python
def select_ad(third_party_ads, user_preferences):
    if not third_party_ads:
        return None #예외 발생이 나음
    if not user_preferences:
        return None #예외 발생
    
    # 주어진 ad와 개별 설정 중 best_ad를 선택하는 복잡한 코드 부분...
    # 여기서 best_ad가 결정되더라도 바로 반환 노노
    if not best_ad:
        # best_ad 의 플랜 B
    return best_ad
```



## 컨벤션

### ■ 같음을 확인하기 위한 대안

```python
# 나쁨
if attr == True:
    print('true')
    
if attr == None:
    print('attr is None!')

# 좋음
if attr:
    print 'attr is truthy!'
   
if attr is None:
    print 'attr is None!'
    
if attr is True:
    print 'attr is True!'
```



### ■ 딕셔너리 요소에 접근하기

dict.has_key 메서드 대신 x in d 구문 사용하거나 dict.get()에 기본 인자를 전달.



### ■ 리스트 다루기

https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions



### ■ 매우 긴 한 줄의 코드를 여러 줄로 나누기

한 줄의 코드가 정해진 길이보다 길면 여러 줄로 나누자.(80자)

코드 줄의 마지막에 백슬래시를 쓰면 파이썬 인터프리터가 그다음 줄 코드를 한 줄로 이어서 인식한다. 그러나 휴먼에러가 발생할 수 있으므로 괄호로 감싸는 방법을 사용하자.

```python
# 나쁨
french_insult = \
"Your mother was a hamster, and \
your father smelt of elderberries!"

form some.deep.module.in.a.module \
	import a_nice_function, \
    	another_nice_function, \
        yet_another_nice_function
        
# 좋음
french_insult =(
	"Your mother was a hamster, and "
	"your father smelt of elderberries")
form some.deep.module.in.a.module import 
(
    a_nice_function,
	another_nice_function,
	yet_another_nice_function
)
```



## 관용구



### 언패킹

```python
a, *rest = [1,2,3]
# a = 1, rest = [2,3]

a, *middle, c = [1,2,3,4]
# a = 1, middle = [2,3], c = 4
```

https://bitbucket.org/sk8erchoi/peps-korean/src/767c779c164856af198a9d08d906a55b24652728/pep-3132.txt?at=default&fileviewer=file-view-default

PEP 3132 참고.



### 값 무시하기

언패킹해야 할 값 중 무시하고 싶은, 즉 변수로 지정하고 싶지 않은 값이 있다면 이중 밑줄(_ _)을 사용하자.

```python
filename = 'foobar.txt'
basename, __, ext = filename.rpartition('.')
```



### 같은 값으로 채워진 길이가 N인 리스트 만들기.

리스트에 * 연산자를 사용하면 모든 성분이 동일한 불편 값으로 채워진 리스트를 만들 수 있다.

```python
four_nones = [None] * 4
print(four_nones)
[None] [None] [None] [None]
```

그러나 리스트는 변경 가능한 객체임을 유의하자.

*연산자를 사용하면 같은 리스트를 가리키는 N개의 참조가 생김.

```python
# 나쁨
four_lists = [[]] * 4
four_lists[0].append("Ni")
print(four_lists)
# [['Ni], ['Ni], ['Ni], ['Ni]]

# 좋음
four_lists = [[] for __ in range(4)]
four_lists[0].append("Ni")
print(four_lists)
[['Ni'], [], [], []]
```

문자열을 만들 때는 빈 문자열에 str.join()



### 예외로부터 안전한 문맥

파일이나 스레드 잠금과 같은 자원을 관리할 때, 예외 상황에 대처하기 위해 try/finally 구문을 사용하는 것이 일반적.

PEP343에 소개된 바와 같이 with문과 컨텍스트 매니저 프로토콜이 try/finally구분을 보다 읽기 쉬운 코드로 대체하는 고나용구다.

이 프로토콜은 \__enter()__ 와 \_\_exit()__ 라는 두 메서드로 구성

```python
import threading
some_lock = threading.Lock()

with some_lock:
    # blah blah blah
    print("blahblahbalbab")
```

이전에는 이렇게 작성했음

```python
import threading
some_lock = threading.Lock()

some_lock.acquire()
try:
    print("blahblahbalbab")
finally:
    some_lock.release()
    
```

표준 라이브러리 묘듈 중 contextlib은 함수를 컨텍스트 매니저로 변호나하는 부가 도구를 제공한다. 이 도구는 close()메서드의 호출을 강제하고, 예외를 억제하며, 표준 출력과 오류 스트림을 리디렉션

> contextlib.closing()

```python
from contextlib import closing
with closing(open("outfile.txt", "w")) as output:
    output.write("Well, he's ... he's, asdasd")
```

그러나 \__enter()__ 와 \_\_exit()__ 라는 두 메서드는 파일 I/O 처리하는 객체를 위해 정의되었기 때문에 직접 사용

```python
with open("outfile.txt","w") as output:
    output.write(
    "sadasdasd")
```



## 일반적인 갓차 - 실수 유발 프로그래밍?

### 변경 가능한 기본 인자

```python
def append_to(element, to=[]):
    to.append(element)
    return to
```

```python
my_list = append_to(12)
print(my_list)
# 12
my_other_list = append_to(42)
print(my_other_list)
# 12 42
```

즉, 함수가 정의될 때 새 리스트 하나가 생성되고, 호출될 때마다 같은 리스트가 사용도니다.

파이썬의 기본 인자는 (루비 언어와 같이) 함수가 호출될 때마다 만들어지지 않고, 함수가 정의될 때만 한 번 만들어진다.

##### 대신 이렇게 하자.

```python
def append_to(element, to=None):
    if to is None:
        to = []
    to.append(element)
    return to
```

그러나 위의 함수가 정의될 때 리스트를 생성하는 것에 대해서 악용?(의도한 대로 쓸수 있다.)

바로 인메모리에 결과를 저장하는 캐싱 함수를 작성할 때 종종 사용.



### 게으른 바인딩 클로저

파이썬이 클로저(closure, 혹은 주변 전역 스코프) 안에서 변수를 바인딩하는 방식

```python
def create_multiplier(i=2):
	return [lambda x: i * x for i in range(5)]
```

```python
for multi in create_multiplier():
    print(multi(2), end=" ... ")
# 8... 8... 8...
```

// 조금더 학습이 필요함.



// \__import__ 문과 패키징 어떻게 작동하는지

https://docs.python.org/ko/3/reference/import.html



## 데코레이터

decorator

다른 함수나 메서드를 감싸는 (혹은 장식하는) 함수 혹은 클래스 메서드이다. 장식에 사용된 함수나 메서드는 원래의 함수나 메서드를 바꾼다.

함수는 파이썬에서 일급 객체이기 때문에 일일이 바꿔주는 것도 가능하지만, @decorator 구문을 사용하는 게 보다 명확하고 선호하는 방식

![](https://ws4.sinaimg.cn/large/006tNc79gy1fzqpvqrwrfj30vi0en0uz.jpg)

이런 메커니즘은 함수나 메서드의 핵심 논리을 유지하는데 유용하다. 데코레이터를 사용했을 때 좋은 경우에 대한 예는 메모이제이션(memoization) 혹은 캐싱.

즉, 계산 비용이 큰 함수 결과를 테이블에 저장하여 매번 계산하는 대신, 미리 계산한 결과를 반복적으로 가져다 사용하고 싶을 때 좋다. 이는 분명 함수로직에 해당하지 않는다.



## 동적 타이핑

```python
# 무관한 두 대상을 같은 변수에 지정하는 위험을 줄이기 위해 짧은 함수나 메서드를 사용하자.
# 나쁨
a = 1
a = 'answer is {}'.format(a)

# 좋음
def get_answer(a):
    return 'answer is {}'.format(a)

a = get_answer(1)

# 서로 다른 타입의 연관된 대상에 다른 이름을 사용하자.
# 나쁨
# 문자열
items = 'a b c d'
# 문자열을 리스트로
items = items.split(' ')
# 리스트를 집합으로
items = set(items)

# 좋음
items_string = 'a b c d'
items_lsit = items.split(' ')
items = set(items_list)
```

변수 재할당을 권장하지 말 것!



## 변경 가능한 / 불가능한 자료형

```python
# 리스트는 변경 가능
my_list = [1,2,3]
my_list[0] = 4
print( my_list ) # [4, 2, 3]

# 정수는 변경 불가능
x = 6 
x = x + 1 # 메모리의 다른 위치에 새 x가 만들어짐
```

\# **문자열은 아예 에러 출력**

![](https://ws3.sinaimg.cn/large/006tNc79gy1fzqq796bbsj30mn05y0te.jpg)

```python
adj = "Red"
noun = "Leicester"

cheese = "{} {}".format(adj, noun)
cheese = "{0} {1}".format(adj, noun) # 숫자 재사용 가능
cheese = "{adj} {noun}".format(adj=adj, noun=noun) # 가장 나은 스타일
```