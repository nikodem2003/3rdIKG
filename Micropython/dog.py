def dog():
    #modules
    import machine
    button = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)
    #variables
    toggle = 1
    while True:
        if not button.value()
            toggle = toggle + 1
        if toggle = 1:
            #some random function
        if toggle = 2:
            #another function
        if toggle > 2:
            toggle = 1
        