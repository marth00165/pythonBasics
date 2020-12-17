def printbuildorder(required, dependencyDictionary):
    installed = {}
    order = []

    for dependency in dependencyDictionary[required]:
        installed[dependency] = False

    x = 0
    while all(value == False for value in installed.values()):
        if x >= len(dependency[required]):
            x = 0
        dependency = dependencyDictionary[required][x]

        if installed[dependency]:
            x += 1
        else:
            if len(installed[dependency]):
                order.append(dependency)
                x += 1
    for i in order:
        print(i)


dependencyDictionary = {
    "a": ["b", "c", "d"],
    "b": ["d"],
    "c": ["b"],
    "d": []
}

printbuildorder("a", dependencyDictionary)
