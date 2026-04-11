# УРОК 5. ДОМАШНЄ ЗАВДАННЯ

Створи **свою повну міні-гру** з такими елементами:

1. **Герой** — Player, який керується клавіатурою (стрілочки або WASD)
2. **Ворог або бонус** — другий Actor, який рухається автоматично
3. **Лічильник очків** — рахуй їх на екрані
4. **Game Over** — коли герой зіткнеться з ворогом (або зібере бонусів достатньо)
5. **Фон** — залий екран кольором або намалюй декорацію

**Приклад сюжетів:**
- Вихованець у морі збирає рибу і утікає від акули
- Космічний корабель бомбардує астероїди
- Птаха ловить комах і утікає від лиса
- Танцюрист уникає перешкод

**Обов'язкові умови:**
- Програма має структуру з Кроку 1 (змінні + draw() + update())
- У коді мають бути: герой + ворог/бонус + score + game_over
- Керування працює (hero рухається)
- На екрані видно очки
- При зіткненні щось відбувається (Game Over або зміна очків)

**Підказки:**
```python
# Список спрайтів для вибору
# Герої: bird1, bird3, bird5, sship5, things15
# Вороги: sea3, sea5, sea8
# Бонуси: things17, things18

# Керування WASD замість стрілок
if keyboard.w:
    hero.y -= 5
if keyboard.a:
    hero.x -= 5
if keyboard.s:
    hero.y += 5
if keyboard.d:
    hero.x += 5

# Кілька врагів
enemy1.x -= 3
enemy2.x -= 2
if hero.colliderect(enemy1) or hero.colliderect(enemy2):
    game_over = True
```

---

## ДОВІДКА

| Що | Код |
|---|---|
| Створити Actor | `hero = Actor('bird1')` |
| Встановити позицію | `hero.pos = (400, 300)` |
| Намалювати Actor | `hero.draw()` |
| Рух з клавіатури | `if keyboard.up: hero.y -= 5` |
| Автоматичний рух | `hero.x += 3` або `hero.x -= 3` |
| Перевірка зіткнення | `if hero.colliderect(enemy): ...` |
| Текст на екрані | `screen.draw.text("Текст", (x, y))` |
| Залити фон | `screen.fill((R, G, B))` |
| Глобальна змінна | `global game_over` або `global score` |

**Доступні спрайти:**
- `bird1`, `bird2`, `bird3`, `bird4`, `bird5`, `bird6`, `bird7` — птахи
- `sea1`, `sea2`, `sea3`, `sea4`, `sea5`, `sea6`, `sea7`, `sea8`, `sea9`, `sea10`, `sea11`, `sea12`, `sea13`, `sea14`, `sea15`, `sea16` — морські істоти
- `sship5` — корабель
- `things15` — утка
- `things17`, `things18` — різні предмети

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

# Змінні гри
score = 0
game_over = False

hero = Actor('bird1')
hero.pos = (400, 300)

enemy = Actor('sea3')
enemy.pos = (700, 300)

def draw():
    screen.fill((173, 216, 230))
    
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
    
    # Керування героєм
    if keyboard.up:
        hero.y -= 5
    if keyboard.down:
        hero.y += 5
    if keyboard.left:
        hero.x -= 5
    if keyboard.right:
        hero.x += 5
    
    # Рух ворога
    enemy.x -= 3
    
    # Перевірка зіткнення
    if hero.colliderect(enemy):
        game_over = True

pgzrun.go()
```
