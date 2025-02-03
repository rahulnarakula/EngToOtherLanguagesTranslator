import requests
import json

def google_translate(text, from_lang, to_lang):
    url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl={from_lang}&tl={to_lang}&dt=t&q={requests.utils.quote(text)}"
    response = requests.get(url)
    if response.status_code == 200:
        try:
            # The response is a nested list structure. We'll extract the translated text.
            translated_text = json.loads(response.text)[0][0][0]
            return translated_text
        except (IndexError, json.JSONDecodeError) as e:
            print("Error parsing response:", e)
            return None
    else:
        print("Error with the request, status code:", response.status_code)
        return None

 
##
def flatten_dict(d, parent_key='', sep='.'):
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

##
def unflatten_dict(d, sep='.'):
    result_dict = {}
    for flat_key, value in d.items():
        keys = flat_key.split(sep)
        d_ref = result_dict
        for key in keys[:-1]:
            if key not in d_ref:
                d_ref[key] = {}
            d_ref = d_ref[key]
        d_ref[keys[-1]] = value
    return result_dict

langs = ["es","fr-CA","zh-CN","zh-HK"]
foreign_data = {}
en_data = {
    "Date_Before_PreviousPeriod": "Before previous period"
}

for lang in langs:
  print(lang)
  for key in en_data.keys():
    foreign_data[key] = google_translate(en_data[key].replace("{","{0z"), "en", lang).replace("{0z", "{")
  json_output = json.dumps(foreign_data, ensure_ascii=False, indent=4)
  print(json_output)
