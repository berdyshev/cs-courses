---
lesson: 5
type: homework
title: "УРОК 5. ДОМАШНЄ ЗАВДАННЯ"
---

# УРОК 5. ДОМАШНЄ ЗАВДАННЯ

Створи **свою міні-гру** з усіма елементами, які ми вивчили.

---

## Завдання

Програма має містити:

1. **Герой** — Actor, яким керуєш стрілками або WASD
2. **Ворог або бонус** — другий Actor, що рухається автоматично
3. **Лічильник очків** — видно на екрані
4. **Game Over** — при зіткненні з ворогом (або після збору достатньої кількості бонусів)
5. **Фон** — залитий кольором або з декорацією

**Приклади сюжетів:**
- Підводна істота збирає рибу і тікає від акули
- Птаха ловить комах і уникає лиса
- Космічний корабель збирає зірки і уникає метеоритів

---

## ДОВІДКА

| Що | Код |
|----|-----|
| Створити Actor | `hero = Actor('bird1')` |
| Встановити позицію | `hero.pos = (320, 240)` |
| Намалювати Actor | `hero.draw()` |
| Рух з клавіатури | `if keyboard.up: hero.y -= 5` |
| Клавіші WASD | `if keyboard.w:` / `keyboard.a:` / `keyboard.s:` / `keyboard.d:` |
| Автоматичний рух | `enemy.x -= 3` |
| Wraparound | `if enemy.x < -50: enemy.x = 690` |
| Перевірка зіткнення | `if hero.colliderect(enemy):` |
| Текст на екрані | `screen.draw.text("Текст", (x, y), fontsize=30)` |
| Залити фон | `screen.fill("steelblue")` |
| Глобальні змінні | `global score, game_over` |
| Зупинити логіку | `if game_over: return` |

**Доступні спрайти:**

| Категорія | Спрайти |
|-----------|---------|
| Птахи | `bird1` – `bird7` |
| Море | `sea1` – `sea16` |
| Корабель | `sship5` |
| Предмети | `things15`, `things17`, `things18` |

**Структура програми:**

```python
import pgzrun
import random

WIDTH = 640
HEIGHT = 480

score = 0
game_over = False

hero = Actor('bird1')
hero.pos = (100, 240)

enemy = Actor('sea3')
enemy.pos = (600, 240)

def draw():
    screen.fill("lightblue")

    if game_over:
        screen.draw.text("GAME OVER", (150, 180), fontsize=60, color="red")
        screen.draw.text("Очки: " + str(score), (230, 260), fontsize=40)
        return

    hero.draw()
    enemy.draw()
    screen.draw.text("Очки: " + str(score), (10, 10), fontsize=30)

def update():
    global score, game_over

    if game_over:
        return

    if keyboard.up:    hero.y -= 5
    if keyboard.down:  hero.y += 5
    if keyboard.left:  hero.x -= 5
    if keyboard.right: hero.x += 5

    enemy.x -= 3
    if enemy.x < -50:
        enemy.x = 690

    if hero.colliderect(enemy):
        game_over = True

pgzrun.go()
```
