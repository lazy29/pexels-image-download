import requests
import json
import urllib

# enter the api key
api_key = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'



url = "https://api.pexels.com/v1/search"


# enter the query
my_obj = {"query": "dark nature", "orientation": "landscape", "per_page": "80"}

def image_query_json():
    response = requests.get(url=url, headers={"Authorization": api_key}, data=my_obj)
    if response.ok:
        with open(f"{my_obj['query']}.json", "w") as f:
            f.write(json.dumps(response.json()))
            

image_query_json()

def dict_of_urls():

    with open(f"{my_obj['query']}.json", 'r') as f:
        content = f.read()
        content = json.loads(content)
        # return content
    
    url_list = [content["photos"][i]["src"]["original"] for i in range(80)]
    alt_list = [content["photos"][i]["alt"] for i in range(80)]

    alt_url = dict(zip(alt_list, url_list))

    return alt_url #returns dict of alt tag & urls


# print(dict_of_urls())

def downloading_images(my_dict):

    for key, value in my_dict.items():
        req = requests.get(value)
        with open(f"/home/itachi/codes/python/practice/images/{key}.{value.split('.')[3]}", "wb") as f:
            f.write(req.content)
        
        print(f"{key} downloaded")




    # ye code mujhe iss website se mila tha but 403 forbidden error fek rha h - https://blog.finxter.com/5-easy-ways-to-download-an-image-from-a-url-in-python/

    # urllib.request.urlretrieve(my_dict["Photo of Starry Night"], f"/home/itachi/codes/python/practice/images/Photo of Starry Night.{my_dict['Photo of Starry Night'].split('.')[3]}")
    # for key, value in my_dict.items():
    #     urllib.request.urlretrieve(value, f"/home/itachi/codes/python/practice/images/{key}.{value.split('.')[3]}")
    #     print(f"{key} downloaded")
    
    print("all downloaded")

downloading_images(dict_of_urls())
