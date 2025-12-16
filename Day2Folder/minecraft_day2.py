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


player.on_chat("obby 2", movesteps)

def chop():
    for count in range(12):
        agent.destroy(FORWARD)
        agent.collect_all()
        agent. move(UP, 1)
    agent.teleport_to_player()

player.on_chat("chop", chop)




