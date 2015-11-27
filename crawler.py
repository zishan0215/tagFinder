from bs4 import BeautifulSoup
import requests

def crawl(parent):
    if 'http' not in parent:
        parent += 'http://'
    toBeVisitedUrls = [parent]
    visitedUrls = []
    tagDict = {'a' : 0,'abbr' : 0,'address' : 0,'area' : 0,'article' : 0,'aside' : 0,'audio' : 0,'b' : 0,'base' : 0,'bdi' : 0,'bdo' : 0,'blockquote' : 0,'body' : 0,'br' : 0,'button' : 0,'canvas' : 0,'caption' : 0,'cite' : 0,'code' : 0,'col' : 0,'colgroup' : 0,'command' : 0,'datalist' : 0,'dd' : 0,'del' : 0,'details' : 0,'dfn' : 0,'div' : 0,'dl' : 0,'dt' : 0,'em' : 0,'embed' : 0,'fieldset' : 0,'figcaption' : 0,'figure' : 0,'footer' : 0,'form' : 0,'h1' : 0,'h2' : 0,'h3' : 0,'h4' : 0,'h5' : 0,'h6' : 0,'head' : 0,'header' : 0,'hgroup' : 0,'hr' : 0,'html' : 0,'i' : 0,'iframe' : 0,'img' : 0,'input' : 0,'ins' : 0,'kbd' : 0,'keygen' : 0,'label' : 0,'legend' : 0,'li' : 0,'link' : 0,'map' : 0,'mark' : 0,'menu' : 0,'meta' : 0,'meter' : 0,'nav' : 0,'noscript' : 0,'object' : 0,'ol' : 0,'optgroup' : 0,'option' : 0,'output' : 0,'p' : 0,'param' : 0,'pre' : 0,'progress' : 0,'q' : 0,'rp' : 0,'rt' : 0,'ruby' : 0,'s' : 0,'samp' : 0,'script' : 0,'section' : 0,'select' : 0,'small' : 0,'source' : 0,'span' : 0,'strong' : 0,'style' : 0,'sub' : 0,'summary' : 0,'sup' : 0,'table' : 0,'tbody' : 0,'td' : 0,'textarea' : 0,'tfoot' : 0,'th' : 0,'thead' : 0,'time' : 0,'title' : 0,'tr' : 0,'track' : 0,'u' : 0,'ul' : 0,'var' : 0,'video' : 0,'wbr' : 0}

    for url in toBeVisitedUrls:
        r = requests.get(url)
        content = r.text
        soup = BeautifulSoup(content)
        # print(soup.prettify())

        # find all tags in the current page
        for tag in tagDict:
            count = 0
            for i in soup.find_all(tag):
                count += 1
            tagDict[tag] += count

        # Get all urls in the current page
        for link in soup.find_all('a'):
            link = link.get('href')
            # Update toBeVisitedUrls list to include the newly found urls
            if 'https://' in parent:
                name = parent[8:]
            elif 'http://' in parent:
                name = parent[7:]
            if type(link) != type(None) and name in link:
                if 'mailto:' not in link:
                    if link[-4:] != '.pdf':
                        if link not in toBeVisitedUrls:
                            print(link)
                            toBeVisitedUrls.append(link)

        # remove the url from toBeVisitedUrls and add it to visitedUrls
        toBeVisitedUrls.remove(url)
        visitedUrls.append(url)

    fileName = name[:name.find('.')] + '.txt'
    f = open(fileName, 'w')
    f.write(parent + '\n')
    f.write('{0:10s} | {1:4s}\n'.format('Tag', 'Count'))

    for tag in tagDict:
    	if tagDict[tag] != 0:
	        print("{0:10s} : {1:3d}".format(tag, tagDict[tag]))
	        f.write("{0:10s} : {1:4d}\n".format(tag, tagDict[tag]))

    f.close()
    # print(visitedUrls)

if __name__ == '__main__':
    # Add websites here
    toBeCrawled = ['http://fiction.csijmi.com']
    for url in toBeCrawled:
        crawl(url)
