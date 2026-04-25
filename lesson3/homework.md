---
lesson: 3
type: homework
title: "УРОК 3. ДОМАШНЄ ЗАВДАННЯ"
---

# УРОК 3. ДОМАШНЄ ЗАВДАННЯ

Створи програму з **підводним мешканцем, яким ти керуєш**.

**Завдання:**

1. Обери спрайт із категорії **sea** (морська істота)
2. Намалюй **фон** — воду і дно
3. Керуй спрайтом **стрілками клавіатури** (праворуч, ліворуч, вгору, вниз)
4. Використай змінну **`speed`** для швидкості
5. Додай **межі** — спрайт не повинен виходити за краї і заходити в дно
6. Додай **дію на клавішу Space** — наприклад, змінити вигляд істоти або колір води

**Приклад поведінки:**
```
Гравець натискає → → ↑
Істота пливе праворуч і вгору...
Досягає правого краю — і зупиняється
Гравець натискає Space
Істота змінює вигляд...
```

**Підказка — дія на Space:**

```python
    if keyboard.space:
        fish.image = 'sea5'   # змінюємо спрайт
```

---

## Для тих, хто впорався

**Додай небо і птаха.**

1. Намалюй смужку неба **над** водою — додай у `draw()` після `screen.fill(...)`:

```python
    screen.draw.filled_rect(Rect((0, 0), (640, 80)), "lightblue")
```

2. Створи другого актора **перед** `def draw()`:

```python
bird = Actor('bird1')
bird.pos = (200, 40)
```

3. Намалюй птаха у `draw()`:

```python
    bird.draw()
```

4. Керуй птахом клавішами **W, A, S, D** — додай у `update()`:

```python
    if keyboard.w:  bird.y -= speed
    if keyboard.s:  bird.y += speed
    if keyboard.a:  bird.x -= speed
    if keyboard.d:  bird.x += speed
```

5. Обмеж птаха зоною неба:

```python
    if bird.y < 0:   bird.y = 0
    if bird.y > 70:  bird.y = 70
    if bird.x < 0:   bird.x = 0
    if bird.x > 640: bird.x = 640
```

---

## ДОВІДКА

| Що | Код |
|----|-----|
| Створити Actor | `fish = Actor('sea3')` |
| Встановити позицію | `fish.pos = (320, 200)` |
| Рух праворуч | `fish.x += speed` |
| Рух ліворуч | `fish.x -= speed` |
| Рух вгору | `fish.y -= speed` |
| Рух вниз | `fish.y += speed` |
| Намалювати Actor | `fish.draw()` |
| Розворот | `fish.flip_x = True` |
| Перевірити клавішу | `if keyboard.right:` |
| Space клавіша | `if keyboard.space:` |
| Змінити спрайт | `fish.image = 'sea5'` |
| Залити екран | `screen.fill("steelblue")` |
| Прямокутник | `screen.draw.filled_rect(Rect((x,y),(w,h)), "brown")` |

**Кольори:**

| Колір | Назва || Колір | Назва |
|-------|-------|-|-------|-------|
| Синій | `"blue"` | | Коричневий | `"brown"` |
| Темно-синій | `"darkblue"` | | Жовтий | `"yellow"` |
| Блакитний | `"lightblue"` | | Сірий | `"gray"` |
| Зелений | `"green"` | | Білий | `"white"` |

**Доступні спрайти:**
- `sea1` … `sea16` — морські істоти
- `bird1` … `bird7` — птахи
- `sship5` — корабель

**Структура програми:**

```python
import pgzrun

WIDTH = 640
HEIGHT = 480

speed = 5
fish = Actor('sea3')
fish.pos = (320, 200)

def draw():
    screen.fill("steelblue")
    screen.draw.filled_rect(Rect((0, 400), (640, 80)), "tan")
    fish.draw()

def update():
    if keyboard.right:
        fish.x += speed
        fish.flip_x = False
    if keyboard.left:
        fish.x -= speed
        fish.flip_x = True
    if keyboard.up:
        fish.y -= speed
    if keyboard.down:
        fish.y += speed

    if keyboard.space:
        pass   # твоя дія тут

    if fish.x < 0:    fish.x = 0
    if fish.x > 640:  fish.x = 640
    if fish.y < 0:    fish.y = 0
    if fish.y > 380:  fish.y = 380

pgzrun.go()
```
