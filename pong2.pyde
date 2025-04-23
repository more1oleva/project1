def collideRectCircle(rx, ry, rw, rh, cx, cy, diameter):
  #2d
  # временные переменные для установки краёв для тестирования
  # rectmode — CORNER, ellipseMode — CENTER, то есть оба по-умолчанию
  testX = cx
  testY = cy

  # which edge is closest?
  if cx < rx:
    testX = rx       # Левый край
  elif cx > rx+rw:
    testX = rx+rw     # правый край

  if cy < ry:
    testY = ry       # верхний край
  elif cy > ry+rh:
    testY = ry+rh   # нижний край

  # получить расстояние от ближайших краев с помощью processing функции dist()
  distance = dist(cx,cy,testX,testY) 

  # если расстояние меньше радиуса, столкновение!
  if distance <= diameter/2:
    return True
  else:
    return False


shar_x = 400
shar_y = 300
shar_dx = 3
shar_dy = -3
shar_razmer = 40
ladder_x = 250
ladder_y = 590
ladder_width = 70
ladder_height = 30
pause = False
mode = "начало"
score = 0
def setup():
    size(600,600)
    rectMode(CENTER)
    
def draw():
    global shar, score, pause, mode,ladder, game, vkl, shar_x, shar_y, ladder_x, ladder_x, shar_dx, shar_dy, ochki
    background(100)
    if mode == "начало":
        fill(255)
        rect(225, 150, 150, 100)
        
        fill(0)
        textAlign(CENTER, CENTER)
        textSize(20)
        text(u"Старт", 225, 150)
    elif mode == "игра":
        textSize(20)
        text(u"очки:", 25, 25)
        text(score, 80, 25)
        ellipse(shar_x, shar_y, shar_razmer, shar_razmer)
        rect(ladder_x, ladder_y, ladder_width, ladder_height)
        if pause == True:
            textAlign(CENTER, CENTER)
            textSize(50)
            text(u"Пауза", 300, 200)
        else:
            shar_x = shar_x + shar_dx
            shar_y = shar_y + shar_dy
            
            if shar_x > 580:
                shar_dx = -shar_dx
            if shar_x < 20:
                shar_dx = -shar_dx
                
            if shar_y < 20:
                shar_dy = random(0, 3)
            #касание шаром ракетки
            if collideRectCircle(ladder_x, ladder_y, ladder_width, ladder_height,   shar_x, shar_y, shar_razmer):
                shar_dy = -random(4,6)
                shar_dx = random(-5, 5)
                score = score + 1
            
            #Проигрыш
            if shar_y > 650:
                textSize(50)
                textAlign(CENTER, CENTER)
                text(u'Проигрыш',300,300)
                text(u'Результат:',300,350)
                text(score,450,350)
            
                
            if keyPressed and key == CODED:
                if keyCode == LEFT:
                    ladder_x = ladder_x - 4
                if keyCode == RIGHT:
                    ladder_x = ladder_x + 4
        
def keyPressed():
    global pause
    if key == "P" or key == "p" or key == "з" or key == "З":
        if pause == True:
            pause = False
        else:
            pause = True

        
def mouseClicked():
    global  mode
    if mode == "начало":
    
            mode = "игра"
    elif mode == "игра":
    
            mode = "начало"     
           
