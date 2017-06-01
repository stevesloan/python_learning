def take(count, iterable):
    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item


def run_take():
    items = range(50)
    for item in take(40, items):
        print(item)

if __name__ == '__main__':
    run_take()

