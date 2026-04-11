# Правила для цього проєкту

## Контекст
Матеріали для уроків інформатики, 9 клас. Тема: Python + Pygame Zero (pgzrun).
Середовище: https://ed-info.github.io/pgz/

---

## Правила написання PGZ коду

### Обов'язкова структура кожної програми
```python
import pgzrun

WIDTH = 800
HEIGHT = 600

def draw():
    pass

def update():
    pass

pgzrun.go()
```

- `import pgzrun` — ЗАВЖДИ перший рядок
- `pgzrun.go()` — ЗАВЖДИ останній рядок

### Кольори
- ЛИШЕ RGB кортежі: `(255, 0, 0)`
- Рядки типу `"red"`, `"blue"` — НЕ ПРАЦЮЮТЬ у цьому середовищі

Довідка кольорів:
| Колір | RGB |
|-------|-----|
| Чорний | `(0, 0, 0)` |
| Білий | `(255, 255, 255)` |
| Червоний | `(255, 0, 0)` |
| Зелений | `(0, 200, 0)` |
| Синій | `(0, 0, 255)` |
| Жовтий | `(255, 255, 0)` |
| Помаранчевий | `(255, 165, 0)` |
| Коричневий | `(139, 69, 19)` |
| Сірий | `(150, 150, 150)` |
| Блакитний | `(173, 216, 230)` |
| Темно-зелений | `(34, 139, 34)` |

### API — функції малювання
```python
screen.fill((r, g, b))
screen.clear()
screen.draw.filled_rect(Rect((x, y), (w, h)), (r, g, b))
screen.draw.filled_circle((x, y), radius, (r, g, b))
screen.draw.line((x1, y1), (x2, y2), (r, g, b))
screen.draw.text("текст", (x, y))
```

### API — Actor (спрайти)
```python
hero = Actor('sea3')   # назва спрайту без розширення
hero.pos = (400, 300)
hero.x = 400
hero.y = 300
hero.angle = 0         # кут повороту в градусах
hero.scale = 1.0       # масштаб
hero.image = 'sea5'    # змінити зображення
hero.draw()            # намалювати у функції draw()
```

Доступні спрайти: `sship5`, `things15`, `things17`, `things18`, `bird1`–`bird7`, `sea1`–`sea16`

### API — клавіатура (у функції update)
```python
if keyboard.right:  player.x += 5
if keyboard.left:   player.x -= 5
if keyboard.up:     player.y -= 5
if keyboard.down:   player.y += 5
if keyboard.space:  # дія
```

### API — події
```python
def on_key_down(key):
    pass

def on_mouse_down(pos, button):
    if button == mouse.LEFT:
        pass

def on_mouse_move(pos):
    pass
```

### API — таймер
```python
clock.schedule_interval(func, seconds)  # повторювати кожні N секунд
clock.schedule(func, seconds)           # один раз через N секунд
```

### API — звук і музика
```python
sounds.name.play()
music.play('name')
music.set_volume(0.5)
```

---

## Правила оформлення роздаткових матеріалів

- Мова: **виключно українська**
- Формат: Markdown, готовий для друку на A4
- Структура кожної роздатки:
  1. Коротка теорія (поняття, концепції)
  2. Практичне завдання: готовий код → набрати → запустити → розібрати → змінити
  3. Домашнє завдання
- Інструкції для учнів: "набери код", "запусти", НЕ "скопіюй"
- Рівень: низький технічний рівень учнів, пояснення прості
