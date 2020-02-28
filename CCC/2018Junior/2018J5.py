class Page:
    def __init__(self, index, data):
        self.children = data[:]
        self.index = index
        self.reached = False

numPages = int(input())
pages = []
for i in range(numPages):
    data = list(map(int, input().split()))
    data.remove(data[0])
    for i in range(len(data)):
        data[i] -= 1
    pages.append(Page(i, data))


shortestPath = False
numCalls = 0


def searchPages(startingPage):
    global pages
    global shortestPath
    queue = [[1, startingPage]]
    while(len(queue) > 0):
        queue[0][1].reached = True
        if(not shortestPath and len(queue[0][1].children) == 0):
            shortestPath = queue[0][0]
        for child in queue[0][1].children:
            if(not pages[child].reached):
                queue.append([queue[0][0] + 1, pages[child]])
        queue.remove(queue[0])

def canBeReached(p):
    for page in p:
        if(not page.reached):
            return False
    return True

searchPages(pages[0])

if(canBeReached(pages)):
    print("Y")
    print(shortestPath)
else:
    print("N")
    print(shortestPath)
