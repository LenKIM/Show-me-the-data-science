파이썬 코드를 잘 짠다는 것은 무엇인가?

## HowDoI 



Common Feature

1. 함수의 길이가 평균적으로 매우 짫음(20줄 미만, 주석 제외)



## Intro

1. 직관적인 이름의 함수를 사용.  
   - command_line_runner()
   - _get_instructions()
   - _get_links()
   - _get_answer()
   - _get_result()

- 하나의 함수는 하나의 일만 하도록 하자.
- 시스템에서 사용할 수 있는 데이터 활용

----

#### 1. 밑줄이 앞에 붙은 함수 이름(우리는 모두 책임 있는 사용자다.)

> ```python
> def _get_instructions(args)
> def _clear_cache()
> def _get_answer(args, links)
> ```

오직 해당 패키지 내에서만 쓴다라는 명시적인 약속

#### 2. 호환성은 한 곳에서만 처리(가독성은 중요하다.)

```python
# Handle imports for Python 2 and 3
if sys.version < '3':
    import codecs
    from urllib import quote as url_quote
    from urllib import getproxies

    # Handling Unicode: http://stackoverflow.com/a/6633040/305414
    def u(x):
        return codecs.unicode_escape_decode(x)[0]
else:
    from urllib.request import getproxies
    from urllib.parse import quote as url_quote

    def u(x):
        return x
```

호환성은 한 곳에서만 처리하도록 설정함(가독성이 중요)

#### 3.파이썬 스러운 선택(아름다움이 추함보다 좋다.)

```python
def _is_question(link):  =1
    return re.search('question/\d+/', link)

#[... 기타 함수 생략...]
def get_link_at_pos(links,position):
    links = [link for link in links if _is_question(link)] =2
    if not links:
        return False =3
    
    if len(links) >= position:
        link = links[position-1] =4
    else:
        link = links[-1] =5
    return link =6
```