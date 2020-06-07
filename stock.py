import webbrowser, requests, datetime, bs4, os

todayDate = str(datetime.date.today()).replace('-','.')
print(todayDate)

issuers = {'Gazprom':'https://www.finam.ru/profile/moex-akcii/gazprom',
           'Sberbank':'https://www.finam.ru/profile/moex-akcii/sberbank',
           'VTB':'https://www.finam.ru/profile/moex-akcii/vtb'}

for key in issuers:

    res = requests.get(issuers[key])
    res.raise_for_status()

    playFile = open('{0} page {1}.html'.format(todayDate, key), 'wb')
    for chunk in res.iter_content():
        playFile.write(chunk)
    playFile.close()

    exampleFile = open('{0} page {1}.html'.format(todayDate, key))
    exampleBS = bs4.BeautifulSoup(exampleFile, features="html.parser")

    elems = exampleBS.select('td.value')

    price = elems[6].getText()
    print('Цена акции', key, ':', price)

    exampleFile.close()

    os.remove('{0} page {1}.html'.format(todayDate, key))

input()

    
