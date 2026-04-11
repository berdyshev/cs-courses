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
- Іменовані рядки: `"red"`, `"blue"`, `"green"` тощо — **ПРАЦЮЮТЬ**
- RGB кортежі також підтримуються: `(255, 0, 0)` — для точних кольорів

Довідка кольорів:
| Колір | Назва | RGB |
|-------|-------|-----|
| Чорний | `"black"` | `(0, 0, 0)` |
| Білий | `"white"` | `(255, 255, 255)` |
| Червоний | `"red"` | `(255, 0, 0)` |
| Зелений | `"green"` | `(0, 128, 0)` |
| Синій | `"blue"` | `(0, 0, 255)` |
| Жовтий | `"yellow"` | `(255, 255, 0)` |
| Помаранчевий | `"orange"` | `(255, 165, 0)` |
| Коричневий | `"brown"` | `(165, 42, 42)` |
| Сірий | `"gray"` | `(128, 128, 128)` |
| Блакитний | `"lightblue"` | `(173, 216, 230)` |
| Темно-зелений | `"darkgreen"` | `(0, 100, 0)` |
| Рожевий | `"pink"` | `(255, 192, 203)` |
| Темно-синій | `"darkblue"` | `(0, 0, 139)` |

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
