from progress.bar import Bar


lst = []
with Bar('Processing', max=1000) as bar:
    for i in range(1000):
        lst.append(i)
        bar.next()