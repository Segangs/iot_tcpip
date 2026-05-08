# ex7_python_asyncio.py asyncio를 이용한 비동기 통신

import asyncio, time

async def brew_coffee(name, duration):
    print(f"{name} 주문 접수, {duration}초 소요 예정")
    await asyncio.sleep(duration)
    print(f"{name}완성")
    return (f"{name}")

async def main():
    print("카페 시작...")
    start_time = time.time()
    
    task1 = brew_coffee("아이스 아메리카노", 3)
    task2 = brew_coffee("라떼", 2)
    task3 = brew_coffee("스무디", 1)
    task4 = brew_coffee("자허블", 4)
    
    results = await asyncio.gather(task1, task2, task3, task4) # await asyncio 를 gather로
    end_time = time.time()
    print(f"총 소요 시간 : {end_time-start_time}초")
    print(f"받은 음료 : {results}")

#동시 작업하여 총 4초 걸리고, 가장 적게 걸리는것부터 완료시킴

#동기 / 비동기와 스레드의 차이점과 장단점 알아두기

if __name__ == "__main__":
    asyncio.run(main())