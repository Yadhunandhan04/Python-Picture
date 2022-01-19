import requests
for i in range(1,100):
    img_data = requests.get(f'http://results.skcet.ac.in:615/assets/StudentImage/20eucb{i:03}.jpg').content
    print(f'Downloading {i:03}')
    with open(f'20eucb{i:03}.jpg','wb') as handler:
        handler.write(img_data)