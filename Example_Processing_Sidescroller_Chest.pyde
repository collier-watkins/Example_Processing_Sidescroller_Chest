
#Making a 2D mario style game

class Player:
    
    def __init__(self, X, Y):
        self.x = X
        self.y = Y
        self.feetX = self.x
        self.feetY = self.y + 35
        self.rightX = self.x + 14
        self.rightY = self.y
        self.leftX = self.x - 14
        self.leftY = self.y
        self.canMoveDown = True
        self.canMoveLeft = True
        self.canMoveRight = True
        self.jumpTime = 0
        self.items = ["Shield"]
        self.facingRight = True
        self.running = True
        self.runningFrameTime = 0
        
        
    def draw(self):
        line(self.x - 14, self.y, self.x + 14, self.y) #Arms
        line(self.x, self.y - 20, self.x, self.y + 20) #Body
        
        # Legs
        line(self.x, self.y + 20, self.x - 7, self.y + 35) #Left Leg
        line(self.x, self.y + 20, self.x + 7, self.y + 35) #Right Leg
        
        
        
        fill(255,255,255) #Head Color
        ellipse(self.x, self.y - 25, 20, 30)
        
        #Face Stuff
        if self.facingRight :
            triangle(self.x + 10, self.y - 30, self.x + 10, self.y - 25, self.x + 20, self.y - 25)
            line(self.x + 7, self.y - 15, self.x, self.y - 18)
            fill(0,0,255)
            ellipse(self.x + 5, self.y - 30, 5,5)
        else:
            triangle(self.x - 10, self.y - 30, self.x - 10, self.y - 25, self.x - 20, self.y - 25)
            line(self.x - 7, self.y - 15, self.x, self.y - 18)
            fill(0,0,255)
            ellipse(self.x - 5, self.y - 30, 5,5)
        
        #Contact Point Draw
        fill(0,255,0)
        #ellipse(self.x, self.y, 5, 5)
        #ellipse(self.feetX,self.feetY, 5,5)
        #ellipse(self.rightX, self.rightY, 5,5)
        #ellipse(self.leftX, self.leftY, 5,5)
        
        #Inventory Draw
        fill(255,255,0)
        textSize(18)
        text("Items:", 0,height-100)
        for i in range(0,len(self.items)):
            text(self.items[i],10,(height-82) + 18*i)
        
    def move(self):
        self.feetY = self.y + 35
        self.feetX = self.x
        self.rightX = self.x + 14
        self.rightY = self.y
        self.leftX = self.x - 14
        self.leftY = self.y
        
        self.running = False
        
        if self.canMoveDown :
            self.y = self.y + 5
        if keyPressed and key == "d" and self.canMoveRight:    #If key d is currently pressed
            self.x = self.x + 5
            self.facingRight = True
            self.running = True
        if keyPressed and key == "a" and self.canMoveLeft :    #If key a is currently pressed
            self.x = self.x - 5
            self.facingRight = False
            self.running = True
        if keyPressed and key == " " and not self.canMoveDown :
          self.jumpTime = millis()
          
        if millis() < self.jumpTime + 500 and keyPressed and key == " " :
            self.y = self.y - 10
            
                
class Box:
  
  def __init__(self, X, Y, W, H):
    self.x1 = X
    self.x2 = X + W
    self.y1 = Y
    self.y2 = Y + H
    
  def draw(self):
    rectMode(CORNERS)
    fill(255,0,0)
    rect(self.x1,self.y1,self.x2,self.y2)
    
  def isPointInside(self, x, y):
    if x >= self.x1 and x <= self.x2 and y >= self.y1 and y <= self.y2 :
      return True
    else:
      return False
  
class Chest:
  
  def __init__(self, X, Y, W, H, itemName):
    self.x1 = X
    self.x2 = X + W
    self.y1 = Y
    self.y2 = Y + H
    self.item = itemName
    self.itemOld = self.item
    self.grabTime = -10000000
    
  def draw(self):
    rectMode(CORNERS)
    fill(137,85,26) #Brown
    rect(self.x1,self.y1,self.x2,self.y2)
    
    if self.item == "" :
        fill(150,150,150)
    else:
        fill(255,215,0) #Gold
    rect(self.x1,self.y1+10,self.x2,self.y1+20)
    
    fill(255,255,255)
    if millis() < self.grabTime + 5000 :
        text("You found a " + self.itemOld,100,100)
    
  def isPointInside(self, x, y):
    if x >= self.x1 and x <= self.x2 and y >= self.y1 and y <= self.y2 :
      return True
    else:
      return False
  
  def grabbedItem(self):
       self.grabTime = millis()
       self.item = ""
      

class BowlingBall:
    
    def __init__(self, X, Y, W):
        self.x = X
        self.y = Y
        self.w = W
        self.canMoveDown = True
        self.movingRight = True
        self.launched = False
        
    
    def draw(self):
        fill(0,0,0)
        ellipse(self.x, self.y, self.w, self.w)
        
    def move(self, handX, handY):
        
        if keyPressed and key == "x" :
            self.launched = True
            
        if keyPressed and key == "r" :
            self.launched = False
        
        if self.launched :
            if self.canMoveDown :
                self.y = self.y + 5
            if self.movingRight:
                self.x = self.x + 10
            else :
                self.x = self.x - 10
        else:
            self.x = handX
            self.y = handY
                
##############################

man = Player(100,100)
boxes = []
chests = []

ball = BowlingBall(0,0, 10)
                

def setup():
  size(800,600)
  boxes.append( Box(50,200,400,50) )
  boxes.append( Box(50,400,400,50) )
  boxes.append( Box(200,300,400,50) )
  boxes.append( Box(550,200,200,100))
  boxes.append( Box(0,200,50,250) )
  
  chests.append( Chest(650,150,50,50,"Sword") )

  
def draw():
  background(150)
  
  
  
  for b in boxes:
    b.draw()
    
  for c in chests:
      c.draw()
      
      # Collision Detection Here
  man.canMoveDown = True
  man.canMoveRight = True
  man.canMoveLeft = True
  
  ball.canMoveDown = True
  
  for b in boxes:
      if b.isPointInside(man.feetX,man.feetY) :
        man.canMoveDown = False
      if b.isPointInside(man.rightX, man.rightY) :
        man.canMoveRight = False
      if b.isPointInside(man.leftX,man.leftY) :
        man.canMoveLeft = False
        
      if b.isPointInside(ball.x, ball.y):
          ball.canMoveDown = False
        
      #
  for c in chests:
      if c.isPointInside(man.x, man.y) :
          if c.item != "" :
              man.items.append(c.item)
              c.grabbedItem()
          

          
  man.move()
  man.draw()
  
  ball.move(man.x + 10, man.y + 10)
  ball.draw()
  
  print("millis: " + str(millis()) )
  print("JumpTime: " + str(man.jumpTime) )
  
  if man.y > height:
      fill(255,0,0)
      text("GAME OVER. You died.", width/2,100)