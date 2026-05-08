---
lesson: 5
type: handout
title: "УРОК 5. ПОВНА ГРА: АРХІТЕКТУРА ТА GAME OVER"
---

# УРОК 5. ПОВНА ГРА: АРХІТЕКТУРА ТА GAME OVER

## ТЕОРЕТИЧНИЙ МАТЕРІАЛ

### Що таке Game Over?

**Game Over** — це стан, коли гра закінчилась. Гру вже не можна грати, тільки бачити результат.

У Pygame Zero це контролюється **глобальною змінною**:

```python
game_over = False   # гра йде
# ... після якої-небудь умови:
game_over = True    # гра закінчилась
```

---

### Як зупинити гру?

Коли `game_over = True`, потрібно:
1. **Не оновлювати** логіку гри (не рухати персонажів, не лічити очки)
2. **Намалювати** екран Game Over замість звичайної сцени

```python
def update():
    global game_over
    if game_over:
        return              # вихід: нічого не робимо
    
    # Решта логіки гри
    hero.x += 5

def draw():
    screen.fill((0, 0, 50))
    
    if game_over:
        # Екран Game Over замість звичайного малювання
        screen.draw.text("GAME OVER", (250, 250), fontsize=60)
        screen.draw.text("Очки: " + str(score), (320, 330), fontsize=40)
        return              # вихід: не малюємо персонажів
    
    # Звичайне малювання гри
    hero.draw()
    enemy.draw()
    screen.draw.text("Очки: " + str(score), (10, 10))
```

---

### Коли запускати Game Over?

Найчастіше — при **зіткненні** персонажів:

```python
def update():
    global game_over, score
    if game_over:
        return
    
    hero.x += 5
    enemy.x -= 3
    
    # Перевірка зіткнення
    if hero.colliderect(enemy):
        game_over = True
```

`.colliderect()` повертає `True`, якщо два Actor'и дотикаються.

---

### Архітектура простої гри

Типова програма має такі частини:

```python
import pgzrun

WIDTH = 800
HEIGHT = 600

# ЗМІННІ ГРИ (глобальні)
score = 0
game_over = False
hero = Actor('bird1')
hero.pos = (100, 300)
enemy = Actor('sea3')
enemy.pos = (700, 300)

# ФУНКЦІЇ
def draw():
    screen.fill((0, 0, 50))
    if game_over:
        screen.draw.text("GAME OVER", (250, 250), fontsize=60)
        screen.draw.text("Очки: " + str(score), (320, 330), fontsize=40)
        return
    hero.draw()
    enemy.draw()
    screen.draw.text("Очки: " + str(score), (10, 10))

def update():
    global game_over, score
    if game_over:
        return
    
    hero.x += 5
    enemy.x -= 3
    
    if hero.colliderect(enemy):
        game_over = True

pgzrun.go()
```

---

## ПРАКТИЧНЕ ЗАВДАННЯ

Будуємо **повну гру** з керуванням, ворогом, лічильником очків та Game Over.  
На кожному кроці: набери зміну → натисни **▶️**.

---

### Крок 1. Базова програма

Набери у редакторі та натисни **▶️**:

```python
import pgzrun

WIDTH = 800
HEIGHT = 600

score = 0
game_over = False

hero = Actor('bird1')
hero.pos = (100, 300)

enemy = Actor('sea3')
enemy.pos = (700, 300)

def draw():
    screen.fill((0, 0, 50))
    hero.draw()
    enemy.draw()

def update():
    global game_over, score
    if game_over:
        return
    
    hero.y += 0

pgzrun.go()
```

На екрані: птаха ліворуч, морська істота праворуч, чорний фон.

---

### Крок 2. Керування птахою

Натисни **⏹️**, замість `hero.y += 0` напиши:

```python
    if keyboard.up:
        hero.y -= 5
    if keyboard.down:
        hero.y += 5
```

Натисни **▶️**. Тепер птаху можна рухати стрілочками вгору/вниз.

---

### Крок 3. Ворог рухається

Натисни **⏹️**, додай після керування птахою:

```python
    enemy.x -= 3
```

Натисни **▶️**. Морська істота летить ліворуч.

---

### Крок 4. Лічильник очків на екрані

Натисні **⏹️**, додай у `draw()` після малювання врагів:

```python
    screen.draw.text("Очки: " + str(score), (10, 10))
```

Натисни **▶️**. Вгорі ліворуч видно "Очки: 0".

---

### Крок 5. Зіткнення = Game Over

Натисни **⏹️**, додай у `update()` після руху ворога:

```python
    if hero.colliderect(enemy):
        game_over = True
```

Натисни **▶️**. Коли птаха торкнеться морської істоти — гра зупиняється (але екрану Game Over ще не видно).

---

### Крок 6. Екран Game Over

Натисни **⏹️**, замість звичайного малювання напиши у `draw()`:

```python
def draw():
    screen.fill((0, 0, 50))
    
    if game_over:
        screen.draw.text("GAME OVER", (250, 250), fontsize=60)
        screen.draw.text("Очки: " + str(score), (320, 330), fontsize=40)
        return
    
    hero.draw()
    enemy.draw()
    screen.draw.text("Очки: " + str(score), (10, 10))
```

Натисни **▶️**. Торкнись птахою врага — з'явиться экран Game Over із текстом.

---

### Крок 7. Добавляємо життя

Натисни **⏹️**, додай після `score = 0`:

```python
lives = 3
```

Натисни **⏹️**, замість `game_over = True` напиши:

```python
    if hero.colliderect(enemy):
        lives -= 1
        if lives == 0:
            game_over = True
```

Натисни **▶️**. Тепер гра закінчується тільки після третього зіткнення.

---

### Крок 8. Показуємо життя

Натисни **⏹️**, додай у `draw()` перед `screen.draw.text("Очки: "...)`:

```python
    screen.draw.text("Життя: " + str(lives), (700, 10))
```

Натисни **▶️**. Вгорі праворуч видно лічильник життів.

---

### Крок 9. Зміни програму

1. **Спрайти**: замість `bird1` і `sea3` спробуй інші: `bird5`, `sea10`, `sship5`
2. **Кольори**: змени `(0, 0, 50)` на `(34, 139, 34)` — буде зелене поле
3. **Швидкість**: змени `enemy.x -= 3` на `enemy.x -= 5` — враг швидше
4. **Додати бонус**: створи третій Actor `bonus = Actor('things17')`, намалюй його, рухай у `update()` та збільшуй `score` замість `game_over`, коли герой його торкнеться
