def addDeadzone(x, y):
    newX = 1.05 * (x - 0.05)
    newY = 1.05 * (y - 0.05)
    if newX < 0:
        newX = 0
    if newY < 0:
        newY = 0
    return {
        "x": newX,
        "y": newY
    }
