from collections import OrderedDict 
def lmf_help():
    data=[
    ("百度云ip","106.13.239.200"),
    ("nn身份证号码","42118219901115302x/421182199303050356"),
    ("lmf银行卡号","6214857551021522"),
    ("lmf电话","13828744705"),
    ("报警电话(50年后启动)","110")
    ]
    content=OrderedDict(data)

    for k,v in content.items():
        print("%s:%s"%(k,v))
    return  content