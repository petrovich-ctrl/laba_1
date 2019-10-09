import websockets
import asyncio
import main as m

SessionID = "petrovich"

hScale = 20
vScale = 20
level = 1.0
length = 20


async def work1():
    url = "wss://sprs.herokuapp.com/first/" + SessionID
    async with websockets.connect(url) as websocket:

        await websocket.send("Let's start")
        response = await websocket.recv()
        print(f"\n>Request: Let's start \n<Response: {response}")

        temp = response.split(" ")
        bWidth = int(temp[0])
        bHeight = int(temp[1])
        numAmount = int(temp[2])

        width = bWidth * hScale
        height = bHeight * vScale

        temp = str(hScale) + " " + str(vScale) + " " + str(level) + " " + str(length) + " on"

        await websocket.send(temp)
        response = await websocket.recv()
        print(f"\n>Request: {temp} \n<Response: collected")

        dictionary = m.list(m.parseEven(response,0, 0), numAmount, width * height)

        for step in range(0, length):
            await websocket.send("Ready")
            response = await websocket.recv()
            print(f"\n>Request: Ready \n<Response: Task-{step + 1} \n{response}\n")
            x = m.parseEven(response, step)

            probs = []
            if (level == 0):
                answer = m.find(x, dictionary)
            elif (level == 1):
                answer = m.find(m.invert(x), dictionary)
            else:
                for k in range(0, numAmount):
                    a = m.best(x, dictionary[k], level)
                    probs.append(a)
                answer = m.maxInd(probs)

            await websocket.send(f"{step + 1} {answer}")
            response = await websocket.recv()
            print(f"\n>Request: answer - {answer} \n<Response: correct - {response}")

        await websocket.send("Bye")
        response = await websocket.recv()
        print(f"\n>Request: Bye \n<Response: {response}")

        input("Press enter...")


asyncio.get_event_loop().run_until_complete(work1())
