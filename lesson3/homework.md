---
lesson: 3
type: homework
title: "УРОК 3. ДОМАШНЄ ЗАВДАННЯ"
---

# УРОК 3. ДОМАШНЄ ЗАВДАННЯ

Створи програму з **кораблем або птахом, яким ти керуєш зі швидкістю й спеціальною дією**.

**Завдання:**

1. Створи спрайт (корабель `sship5`, птаха `bird1`–`bird7` або морську істоту `sea1`–`sea16`)
2. Керуй спрайтом за допомогою **стрілок клавіатури** (праворуч, ліворуч, вгору, вниз)
3. Додай змінну `speed` для **швидкості** — змінюй її для рівня складності
4. Додай **границі екрану** — спрайт не повинен вилітати за край
5. Додай **дію на клавішу Space** (наприклад: змініть колір, або спрайт мигне, або щось іще творче)
6. Додай **фон** (небо, море, або обидва)

**Приклад поведінки:**
```
Гравець нажимає → → ↑
Корабель рухається праворуч і вгору...
Гравець натискає Space
Корабель мигає або змінює вигляд...
```

**Підказка — змінна speed:**

```python
speed = 5    # швидкість в пікселях на кадр

def update():
    if keyboard.right:
        player.x += speed
    if keyboard.left:
        player.x -= speed
    if keyboard.up:
        player.y -= speed
    if keyboard.down:
        player.y += speed
```

**Підказка — клавіша Space:**

```python
def update():
    # ... рух ...
    
    if keyboard.space:
        # твоя дія: змініть спрайт, колір фону, звук тощо
        player.image = 'sea4'  # приклад
```

---

## ДОВІДКА

| Що | Код |
|----|-----|
| Створити Actor | `player = Actor('sea3')` |
| Встановити позицію | `player.pos = (400, 300)` |
| Змінити X координату | `player.x += 5` |
| Змінити Y координату | `player.y += 5` |
| Намалювати Actor | `player.draw()` |
| Перевірити клавішу | `if keyboard.right:` |
| Space клавіша | `if keyboard.space:` |
| Залити екран кольором | `screen.fill((R,G,B))` |
| Прямокутник | `screen.draw.filled_rect(Rect((x,y),(w,h)), (R,G,B))` |
| Коло | `screen.draw.filled_circle((x,y), radius, (R,G,B))` |
| Змінити спрайт | `player.image = 'sea5'` |

**Доступні спрайти:**
- `bird1`, `bird2`, … `bird7` — птахи
- `sea1`, `sea2`, … `sea16` — морські істоти
- `sship5` — корабель
- `things15`, `things17`, `things18` — різні предмети

**Кольори (RGB):**

| Колір | RGB || Колір | RGB |
|-------|-----|-|-------|-----|
| Чорний | `(0, 0, 0)` | | Блакитний | `(173, 216, 230)` |
| Білий | `(255, 255, 255)` | | Темно-синій | `(34, 100, 200)` |
| Червоний | `(255, 0, 0)` | | Коричневий | `(139, 69, 19)` |
| Зелений | `(0, 200, 0)` | | Жовтий | `(255, 255, 0)` |
| Синій | `(0, 0, 255)` | | Темно-зелений | `(34, 139, 34)` |

**Структура програми:**

```python
import pgzrun

WIDTH = 800
HEIGHT = 600

speed = 5
player = Actor('bird1')
player.pos = (400, 300)

def draw():
    screen.fill((173, 216, 230))
    player.draw()

def update():
    global speed
    
    if keyboard.right:
        player.x += speed
    if keyboard.left:
        player.x -= speed
    if keyboard.up:
        player.y -= speed
    if keyboard.down:
        player.y += speed
    
    if keyboard.space:
        # дія
        pass
    
    # межи
    if player.x < 0:
        player.x = 0
    if player.x > 800:
        player.x = 800
    if player.y < 0:
        player.y = 0
    if player.y > 600:
        player.y = 600

pgzrun.go()
```
