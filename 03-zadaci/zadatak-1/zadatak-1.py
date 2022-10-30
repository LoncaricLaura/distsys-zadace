import asyncio
import os

current_dir = os.getcwd()+"/zadatak-1"

async def afun1(list_names):
    await asyncio.sleep(0.2)
    return [{"naziv": name, "velicina": os.path.getsize(name)} for name in list_names]


def fun2(list_names):
    for x in list_names:
        f = open(x, 'w')
        for i in range(1, 10001):
            f.write(str(i)+'\t')


async def main():
    list_names =  []
    for i in range(3):
        open("datoteka{}".format(i+1), "w")
        list_names.append("datoteka{}".format(i+1))
    fun2(list_names)
    result = await afun1(list_names)
    print(result)

if __name__ == "__main__":
    asyncio.run(main())