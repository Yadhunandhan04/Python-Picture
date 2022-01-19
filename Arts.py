import requests
for i in range(1,600):
    img_data = requests.get(f'http://result.skasc.ac.in:810/assets/StudentImage/20BAF{i:03}.jpg').content
    print(f'Downloading {i:03}')
    with open(f'20BAF{i:03}.jpg','wb') as handler:
        handler.write(img_data)