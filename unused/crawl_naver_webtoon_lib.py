def crawl_naver_webtoon(ep_url):
    html = requests.get(ep_url).text
    soup = BeautifulSoup(html, 'html.parser')

    comic_title = ' '.join(soup.select('.comicinfo h2')[0].text.split())
    ep_title = ' '.join(soup.select('.tit_area h3')[0].text.split())

    image_list = []
    full_width, full_height = 0, 0


    for tag in soup.select('.wt_viewer img'):
        img_url = tag['src']
        img_name = os.path.basename(img_url)
        headers = {'Referer': ep_url}
        cache_dir_path = os.path.join(os.path.dirname(__file__), 'cache')
        image_dir_path = os.path.join(os.path.dirname(__file__), comic_title)
        if not os.path.exists(cache_dir_path):
            os.makedirs(cache_dir_path)
        if not os.path.exists(image_dir_path):
            os.makedirs(image_dir_path)
        os.chdir(cache_dir_path)
        img_data = requests.get(img_url, headers=headers).content

        with open(img_name, 'wb') as f:
            f.write(img_data)
            im = PILImage.open(img_name)
            width, height = im.size
            image_list.append(im)
            full_width = max(full_width, width)
            full_height += height

    canvas = PILImage.new('RGB', (full_width, full_height), 'white')
    output_height = 0

    for im in image_list:
        width, height = im.size
        canvas.paste(im, (0, output_height))
        output_height += height
        toonname = str(n) + '화.jpg'
    canvas.save(toonname)
    os.chdir(currentPath)
    src = 'cache/' + toonname
    dst = ''' + currentPath + '''
    shutil.copy2('cache/' + toonname, image_dir_path)
    shutil.rmtree('cache/')
    print(str(n), '화 Completed !')
