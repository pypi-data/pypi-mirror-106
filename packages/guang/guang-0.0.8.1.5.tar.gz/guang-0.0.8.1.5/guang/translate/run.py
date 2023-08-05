import translators as ts
import json
from pprint import pprint

wyw_text = '季姬寂，集鸡，鸡即棘鸡。棘鸡饥叽，季姬及箕稷济鸡。'
chs_text = '季姬感到寂寞，罗集了一些鸡来养，鸡是那种出自荆棘丛中的野鸡。野鸡饿了唧唧叫，季姬就拿竹箕中的谷物喂鸡。'

# input languages
print(ts.deepl(wyw_text))  # default: from_language='auto', to_language='en'

## output language_map
print(ts._deepl.language_map)


def tencent(text):
    target = ts.tencent(text, is_detail_result=True)
    try:
        print(ts.tencent(text))
    except:
        print("未查询到输入语句，请检查后再输入")
    try:
        ph_json = json.loads(target['suggest']['data'][0]['ph_json'])
        # pprint(ph_json)
        print(
            f'''[美]:{ph_json["AmE"]} [发音]{ph_json["AmE_url"]}\n[英]:{ph_json["BrE"]} [发音]{ph_json["BrE_url"]}'''
        )
    except:
        pass
