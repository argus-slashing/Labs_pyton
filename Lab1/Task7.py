def AdressGenerator():
    items = ["vk.com", "www.youtube", "spotify"]
    result = []
    for s in items:
        if len(s) >= 4:
            string = s[0:3]
            if string == "www":
                link = "http:/" + link
                string = link[-1:-5]
                if string != ".com":
                    link += ".com"
                result.append(link)
    print(result)

AdressGenerator()