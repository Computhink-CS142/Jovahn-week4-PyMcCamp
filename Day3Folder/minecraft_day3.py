# AT THE END OF LESSON, COPY YOUR CODE FROM MINECRAFT HERE.
# THIS IS SO THAT YOU HAVE A RECORD OF YOUR CODE FROM MINECRAFT CODE BUILDER
def addition(num1, num2):
    player.say(num1 * num2)

addition(12, 9)

def teleport():
    agent.teleport_to_player()



player.on_chat("come", teleport)

def tr():
    agent.turn (RIGHT)

player.on_chat("tr", tr)
 
def forward(count):
     agent.move(FORWARD, count)
player.on_chat("fw", forward)




def up(count):
     agent.move(UP, count)
player.on_chat("u", up)


def movesteps():
    agent.move(FORWARD, 4)
    agent.move(LEFT, 4)
    agent.move(FORWARD, 3)
    agent.move(UP, 4)
    agent.move(FORWARD, 7)
    agent.move(DOWN, 4)


player.on_chat("obby2", movesteps)

def choptree(height):
    for count in range(height):
        agent.destroy(FORWARD)
        agent. move(UP, 1)
    agent.move(DOWN, height)
    agent.collect_all()

player.on_chat("chop", choptree)


def mine(len1):
    for count in range(len1):
        agent.destroy(FORWARD)
        agent.destroy(LEFT)
        agent.destroy(RIGHT)
        agent.destroy(DOWN)
        agent.collect_all()
        agent.move(FORWARD, count)

player.on_chat("m", mine)



def place():
    for count in range(count):
        agent.place(DOWN)
        agent.move(FORWARD, count)

player.on_chat("p", place)