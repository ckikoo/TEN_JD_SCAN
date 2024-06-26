import time, requests, uuid, random, json, re
from urllib.parse import unquote_plus, quote
from datetime import datetime

def printf(cookie, T):
    try:
        pt_pin = re.compile(r'pt_pin=(.*?);').findall(cookie)[0]
        pt_pin = unquote_plus(pt_pin)
    except IndexError:
        pt_pin = re.compile(r'pin=(.*?);').findall(cookie)[0]
        pt_pin = unquote_plus(pt_pin)
    print(f"{str(datetime.now())[0:22]}->{pt_pin}->{T}")

def base64Encode(string):
    oldBin = ""
    tempStr = []
    result = ""
    base64_list = 'KLMNOPQRSTABCDEFGHIJUVWXYZabcdopqrstuvwxefghijklmnyz0123456789+/'
    for ch in string:
        oldBin += "{:08}".format(int(str(bin(ord(ch))).replace("0b", "")))
    for i in range(0, len(oldBin), 6):
        tempStr.append("{:<06}".format(oldBin[i:i + 6]))
    for item in tempStr:
        result = result + base64_list[int(item, 2)]
    if len(result) % 4 == 2:
        result += "=="
    elif len(result) % 4 == 3:
        result += "="
    return result

def getTimestamp():
    return int(round(time.time() * 1000))
def TDEncrypt(m):
    m = json.dumps(m, separators=(',', ':'))
    m = quote(m)
    n = ""
    g = 0
    s64 = "23IL<N01c7KvwZO56RSTAfghiFyzWJqVabGH4PQdopUrsCuX*xeBjkltDEmn89.-"
    m_l = len(m)
    while g < m_l:
        f = ord(m[g])
        g += 1
        d = ord(m[g]) if g < m_l else 0
        g += 1
        a = ord(m[g]) if g < m_l else 0
        g += 1
        b = f >> 2
        f = (f & 3) << 4 | d >> 4
        e = (d & 15) << 2 | a >> 6
        c = a & 63
        if d == 0:
            e = c = 64
        elif a == 0:
            c = 64

        if b < 64: n += s64[b]
        if f < 64: n += s64[f]
        if e < 64: n += s64[e]
        if c < 64: n += s64[c]
    return n + "/"

def getUUID(x="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", t=0):
    if isinstance(x, int):
        x = "x" * x
    uuid = re.sub("[xy]", lambda x: str(int((16 * random.random()) // 1) if x.group() == "x" else ((3 & int(x.group(), 16)) | 8)), x)
    return uuid

def x_api_eid_token(ua, cookie):
    t = getTimestamp()
    g = {
        'pin': '',
        'oid': '',
        'bizId': 'jd-babelh5',
        'fc': '',
        'mode': 'strict',
        'p': 's',
        'fp': '26402d879256c911a19f750ac9e6137b',
        'ctype': 1,
        'v': '3.1.1.1',
        'f': '3',
        'o': 'pro.m.jd.com/jdlite/active/23CeE8ZXA4uFS9M9mTjtta9T4S5x/index.html',
        # 'qs': 'babelChannel=ttt6&lng=104.624159&lat=28.765053&sid=aa6042f7bd594f9ef8c2bc549246161w&un_area=22_2005_36315_57211',
        # 'jsTk': '',
        'qi': ''
    }
    a = TDEncrypt(g)
    d = '{"ts":{"deviceTime":1684749932883,"deviceEndTime":1684749932968},"ca":{"tdHash":"ae7bb88f7eac3baa052a6d2fd3c4eab8","contextName":"webgl,experimental-webgl","webglversion":"WebGL 1.0 (OpenGL ES 2.0 Chromium)","shadingLV":"WebGL GLSL ES 1.0 (OpenGL ES GLSL ES 1.0 Chromium)","vendor":"WebKit","renderer":"WebKit WebGL","extensions":["ANGLE_instanced_arrays","EXT_blend_minmax","EXT_color_buffer_half_float","EXT_float_blend","EXT_texture_filter_anisotropic","WEBKIT_EXT_texture_filter_anisotropic","EXT_sRGB","OES_element_index_uint","OES_fbo_render_mipmap","OES_standard_derivatives","OES_texture_float","OES_texture_float_linear","OES_texture_half_float","OES_texture_half_float_linear","OES_vertex_array_object","WEBGL_color_buffer_float","WEBGL_compressed_texture_astc","WEBGL_compressed_texture_etc","WEBGL_compressed_texture_etc1","WEBGL_debug_renderer_info","WEBGL_debug_shaders","WEBGL_depth_texture","WEBKIT_WEBGL_depth_texture","WEBGL_lose_context","WEBKIT_WEBGL_lose_context","WEBGL_multi_draw"],"wuv":"Qualcomm","wur":"Adreno (TM) 730"},"m":{"compatMode":"CSS1Compat"},"fo":["Bauhaus 93","Casual"],"n":{"vendorSub":"","productSub":"20030107","vendor":"Google Inc.","maxTouchPoints":5,"hardwareConcurrency":8,"cookieEnabled":true,"appCodeName":"Mozilla","appName":"Netscape","appVersion":"","platform":"Linux aarch64","product":"Gecko","userAgent":"","language":"zh-CN","onLine":true,"webdriver":false,"javaEnabled":false,"deviceMemory":8,"enumerationOrder":["vendorSub","productSub","vendor","maxTouchPoints","userActivation","doNotTrack","geolocation","connection","plugins","mimeTypes","webkitTemporaryStorage","webkitPersistentStorage","hardwareConcurrency","cookieEnabled","appCodeName","appName","appVersion","platform","product","userAgent","language","languages","onLine","webdriver","getBattery","getGamepads","javaEnabled","sendBeacon","vibrate","scheduling","mediaCapabilities","locks","wakeLock","usb","clipboard","credentials","keyboard","mediaDevices","storage","serviceWorker","deviceMemory","bluetooth","getUserMedia","requestMIDIAccess","requestMediaKeySystemAccess","webkitGetUserMedia","clearAppBadge","setAppBadge"]},"p":[],"w":{"devicePixelRatio":3,"screenTop":0,"screenLeft":0},"s":{"availHeight":904,"availWidth":407,"colorDepth":24,"height":904,"width":407,"pixelDepth":24},"sc":{"ActiveBorder":"rgb(255, 255, 255)","ActiveCaption":"rgb(204, 204, 204)","AppWorkspace":"rgb(255, 255, 255)","Background":"rgb(99, 99, 206)","ButtonFace":"rgb(221, 221, 221)","ButtonHighlight":"rgb(221, 221, 221)","ButtonShadow":"rgb(136, 136, 136)","ButtonText":"rgb(0, 0, 0)","CaptionText":"rgb(0, 0, 0)","GrayText":"rgb(128, 128, 128)","Highlight":"rgb(181, 213, 255)","HighlightText":"rgb(0, 0, 0)","InactiveBorder":"rgb(255, 255, 255)","InactiveCaption":"rgb(255, 255, 255)","InactiveCaptionText":"rgb(127, 127, 127)","InfoBackground":"rgb(251, 252, 197)","InfoText":"rgb(0, 0, 0)","Menu":"rgb(247, 247, 247)","MenuText":"rgb(0, 0, 0)","Scrollbar":"rgb(255, 255, 255)","ThreeDDarkShadow":"rgb(102, 102, 102)","ThreeDFace":"rgb(192, 192, 192)","ThreeDHighlight":"rgb(221, 221, 221)","ThreeDLightShadow":"rgb(192, 192, 192)","ThreeDShadow":"rgb(136, 136, 136)","Window":"rgb(255, 255, 255)","WindowFrame":"rgb(204, 204, 204)","WindowText":"rgb(0, 0, 0)"},"ss":{"cookie":true,"localStorage":true,"sessionStorage":true,"globalStorage":false,"indexedDB":true},"tz":-480,"lil":"","wil":""}'
    d = json.loads(d)
    d["ts"]["deviceTime"] = t
    d["ts"]["deviceEndTime"] = t + 77
    d["n"]["appVersion"] = ua[ua.find("appBuild/") + 9:]
    d["n"]["userAgent"] = ua
    d = TDEncrypt(d)
    data = {"d": d}
    url = f'https://gia.jd.com/jsTk.do?a={a}'
    headers = {
        "Host": "gia.jd.com",
        "User-Agent": ua,
        "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Accept": "*/*",
        "Origin": "https://pro.m.jd.com",
        "X-Requested-With": "com.jd.jdlite",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://pro.m.jd.com/jdlite/active/23CeE8ZXA4uFS9M9mTjtta9T4S5x/index.html?babelChannel=ttt6",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cookie": cookie + ";cid=8"
    }
    x_api_eid_token = ""
    try:
        res = requests.post(url=url, data=data, headers=headers, timeout=2).text
        try:
            res = json.loads(res)
            if res['code'] == 0:  # res.data
                x_api_eid_token = res['data']['token']
            else:
                print(f"{res}")
        except Exception as e:
            x_api_eid_token = 'jdd03H7YPMPX4UMJGV4I7JIRD723Y56MTYLBTKHO3GSQEEXPUGIBTTHYVOXTVVDBX6QFQ3HOR23DLATIH35CP6V267L5PZ4AAAAMI3XMOL3YAAAAACW4NZ56GANBBEUX'
    except Exception as e:
        x_api_eid_token = 'jdd03H7YPMPX4UMJGV4I7JIRD723Y56MTYLBTKHO3GSQEEXPUGIBTTHYVOXTVVDBX6QFQ3HOR23DLATIH35CP6V267L5PZ4AAAAMI3XMOL3YAAAAACW4NZ56GANBBEUX'
    return x_api_eid_token


def cache_eid_token():
    x_api_eid_token =[
            'jdd03XKQIU7JHWU3FTRPNHLXLGLMHRJD7OMVOISOPHL7C455LVYVP7WHVONHZQY27CVJH7N5ZFIRZHLU5YMPD2XYEYAI4V4AAAAMJO66VUUYAAAAADBSJHFBBXFNGN4X',
            'jdd03AFZAXQMGABTJ343PVG25KROTKXYAWNYIPKPLE3E2WW2WP6DPYYYSSAL4YUXQ3EJMPZJLDOXGEGTUPY2JJOUWNK2LSYAAAAMJO66VWHIAAAAACHT6O6PRMVQJSQX',
            'jdd03AVQGWCCOCTLX6RI4APW5FTDQA5DGHQPHF3UE6FRNAIBMIFO7SGBUZZWYN6BCNXX3SMO4JHOYYVL2IVG3QU5335GA44AAAAMJO66VX3AAAAAADQL4YVFGKIM6HIX',
            'jdd03QZWP3FHPQVJPLNWLIZMPPTUMQBYGBKSYJZFB3XHFZ4T65CLGDXO5562I7ZHOWRF4ECMC6Y3JZCF36N6K5LLFGL4AIYAAAAMJO66VZHYAAAAACV3DLQTH56CCDYX',
            'jdd03L52TCDU3WIZGZBXCBT6DRPEFBF2LVF5AEZAOUKCMGOUAERBFJCDSYFEORLQSH4YDTMQRETKLB754YQTNVPBW5TS4PIAAAAMJO66V2VIAAAAADX54AHX2ALAZ2IX',
            'jdd03WOBY4EEM6YTGJSCTG3EUDM2BEEAZJZNBXZMQVHTFZTBUFFVYKUUYCXGCFTWFW6T622KIJX57USNXPLUU6TRKOKLVPAAAAAMJO66V4BIAAAAADPIDD2RSBWV7WIX',
            'jdd03GP3ZLDDCCDJ2KRZNWMWNQ5546Q2BV7G3ZBKRQJAS6LILMSEA462XHAFH2LIFDIFICQUFYYYHEDLB45V7GRHY6OTAIIAAAAMJO66V5QYAAAAAD2L2DF3QSYOFDMX',
            'jdd03CEGEO2NES34BBUMIO3UMMWGZSXRMCKRXPLLPNECTK6KIYWMZACJGYFHAEVHFX22PBRWKFEVFMGNLMRAABVSQS7OWGUAAAAMJO66V67IAAAAADMJBDGJZXUYDJQX',
            'jdd03SBQH2WS3L3N3RR3VCVXPTGVFHHRHRBW67FYEQBIZDADNN2LEDKFX626WLPM7ZBPBET2RYNWSTGLQPCOQSIJ5LEAWMQAAAAMJO66WAJYAAAAADVLVMZFFCJYHIMX',
            'jdd03AFZAXQMGABTJ343PVG25KROTKXYAWNYIPKPLE3E2WW2WP6DPYYYSSAL4YUXQ3EJMPZJLDOXGEGTUPY2JJOUWNK2LSYAAAAMJO66WBXYAAAAACDM535LRY7EKLAX',
            'jdd03WOBY4EEM6YTGJSCTG3EUDM2BEEAZJZNBXZMQVHTFZTBUFFVYKUUYCXGCFTWFW6T622KIJX57USNXPLUU6TRKOKLVPAAAAAMJO66WDFYAAAAADM3IKKXMPHCDGAX',
            'jdd03P5ZZOAUGQIX4QVU7H2DACD7HAMETQGBWTEMGQBR3SNZJCIWQEFFBRRCAVUWKQ2QXLYMBQYYK4N2U7VEGC3MLI3WHPUAAAAMJO66WEUQAAAAACM5EBZXRWWAAU4X',
            'jdd03XYEXEFFJPTXJOKKBGADUQEEZEET4SITJRMMZQHY247Q2I2UKYEW4KBI3KG327O77N3QWQE3UYMUBLWRSAGKV4BVW3MAAAAMJO66WGEQAAAAADUDGSB3KFYIZXAX',
            'jdd03L52TCDU3WIZGZBXCBT6DRPEFBF2LVF5AEZAOUKCMGOUAERBFJCDSYFEORLQSH4YDTMQRETKLB754YQTNVPBW5TS4PIAAAAMJO66WHTIAAAAAD5ZJGZVO3NCA6UX',
            'jdd034OSEHYIMLLVRCARD6AREEJYHRD5MQMNVGU3SMBL3UMSWCZZ6XFVWI47O2SQFXN6UZ6GF2UK73PXRB4OC4FOUZD4OLIAAAAMJO66WJCAAAAAAC6XVFLZT5W2LNQX',
            'jdd03CMV72XMO7MTENZKV2DVKWWTOAL62FIFHCCZYISD7ZND66FHFDNYJZNNLQ6U3KE57VCIOKT4YCPPHYOELUKHQVF4NSAAAAAMJO66WKMQAAAAACZQDI52SP6J2EAX',
            'jdd034OSEHYIMLLVRCARD6AREEJYHRD5MQMNVGU3SMBL3UMSWCZZ6XFVWI47O2SQFXN6UZ6GF2UK73PXRB4OC4FOUZD4OLIAAAAMJO66WL2IAAAAADWOGMIVHI375KEX',
            'jdd03P5ZZOAUGQIX4QVU7H2DACD7HAMETQGBWTEMGQBR3SNZJCIWQEFFBRRCAVUWKQ2QXLYMBQYYK4N2U7VEGC3MLI3WHPUAAAAMJO66WNJAAAAAADVFG5UHWNUAZHEX',
            'jdd03WOBY4EEM6YTGJSCTG3EUDM2BEEAZJZNBXZMQVHTFZTBUFFVYKUUYCXGCFTWFW6T622KIJX57USNXPLUU6TRKOKLVPAAAAAMJO66WOWIAAAAADSNPCF4TP745DUX',
            'jdd033GJ6QCLAE3EPZWGSZTOBMQNE2F5CBDD3VBQD7VZC2OKMDUBNVEG5XL3T4LKGU2N5DGTXKJ7GPM7UHVXMM4W4LW663YAAAAMJO66WQEIAAAAACEOHLBZDCTC3AEX',
            'jdd03WOBY4EEM6YTGJSCTG3EUDM2BEEAZJZNBXZMQVHTFZTBUFFVYKUUYCXGCFTWFW6T622KIJX57USNXPLUU6TRKOKLVPAAAAAMJO66WRTYAAAAACQRPDPYKA5KMFYX',
            'jdd03XKQIU7JHWU3FTRPNHLXLGLMHRJD7OMVOISOPHL7C455LVYVP7WHVONHZQY27CVJH7N5ZFIRZHLU5YMPD2XYEYAI4V4AAAAMJO66WTEIAAAAADXFZM5WUQ4N5OEX',
            'jdd036FUK2T5SB3ZN3PTPGXTKBN7PUFJZ6BBJXG2QH2YWCJCHAMUGUB5YDEMGOFJ6U4UYHZU6OKFQIGW44LCLXDTC4HZFLEAAAAMJO66WUXQAAAAAC7A7MRUG4QPWEUX',
            'jdd03AFZAXQMGABTJ343PVG25KROTKXYAWNYIPKPLE3E2WW2WP6DPYYYSSAL4YUXQ3EJMPZJLDOXGEGTUPY2JJOUWNK2LSYAAAAMJO66WWGQAAAAADR3UUMCMMTEYZMX',
            'jdd03AVQGWCCOCTLX6RI4APW5FTDQA5DGHQPHF3UE6FRNAIBMIFO7SGBUZZWYN6BCNXX3SMO4JHOYYVL2IVG3QU5335GA44AAAAMJO66WXTAAAAAACLSSFU73VSDH64X',
            'jdd03UAZ5IYW3BBGOQK5YPENREZH5MCHIGJIKQ53PJPRIFORA2GCM324N3EU4CJLITELA2XZ3L327B4PYGNOFAHC22FS6CYAAAAMJO66WZGIAAAAAD5BTH2LBJYLRYUX',
            'jdd036XDNRU4J57IQ7EZJIWHRD7HRCCA362TYBSQ5S2IQTJ54LRX4TPNNWFQHJFM63BCH3Y7UGKPO7GDEAL5EPM3X6HKE4EAAAAMJO66W2XYAAAAAD6DIS4IUQ4LBFYX',
            'jdd03YEDPTAEWWFAO5VGK5BLOASK7KT57OZZBPGKYKLLM5AH3ZF3BKTTHYYLD5CTZXODAF7KTK3RF6ALAPUS4B6JZKQ57MEAAAAMJO66W4DIAAAAACJSVR55JUTPHXAX',
            'jdd03D6TZSITOQRTA64ZKVRRPBODGSEYORDML3W6HBJXHCXV7MFIS6ZOU7D5RZUB7HONYV2UXS2FZI6YOTQLQC6HHGMVVKMAAAAMJO66W5TIAAAAACLJTL2OAQA6TZMX',
            'jdd03V6HHLB5YOCTNKUI2OTEE7YSBKJDO3MRCOS2YO5P2JCZL2MVEET2F22Y6GQ2JTFRYFWYZT7NQ7RKT7NJSD3IT7T7D5YAAAAMJO66W7BAAAAAADOK6DSJDIBY3NAX',
            'jdd03RAVZKBDOYLSCPSG4X5BVVZWTN3QQ5NXXTXWUBOKE6IP2S7CSYHW34ZUJFAGQXBXHUNAE53HNTDVGKGBXSB4FYDXTWQAAAAMJO66XATIAAAAADZFYSQELBGNRSYX',
            'jdd03RPDO53GTVWX3VDIVSCXPWR3ZIBNQTWHJK4ZCC63P3HG56TMQ4YGXPUEXCPB5QSPEO7CBTOE7HYA6XC6FTNM4AAZG3UAAAAMJO66XB4AAAAAADYMYAJKMWOVLBUX',
            'jdd034OSEHYIMLLVRCARD6AREEJYHRD5MQMNVGU3SMBL3UMSWCZZ6XFVWI47O2SQFXN6UZ6GF2UK73PXRB4OC4FOUZD4OLIAAAAMJO66XDGAAAAAACQLHXZW2A34E5MX',
            'jdd03H6ZKFSWLZQ4Z36MJLAO7UNAG4MK5BVNA562CAHVWOJQDKHGJD5UIIVZODYE5IQLD2R6WYIX3O6SENHXZ47Q5NDB2WEAAAAMJO66XEUYAAAAACAZZ6JPG3QRXEUX',
            'jdd03KX3XOWK5VOSASX6V2KIMTHL5GYLXURRNMXH5DADVEE5KDING4TVCROXNRIJCG5APXDSMB2IZMNP5YFZX6EZUYNAYFIAAAAMJO66XGEAAAAAADJTSYARSHU7TEAX',
            'jdd03RMX5XAFVFJ36RNXRVM2QVX6HHX37KCJGVPYMYWJ4DPZZJQGVLDDY64EJNJ7ECLUEOTMK63HVECQZYR4VVW7PQBW5QQAAAAMJO66XHWYAAAAACJ6DI3KK5XOHCEX',
            'jdd03DWMOFIEXMSUY4NMKJPSDV4J4SFRLL75VBRAAGUQIKENDMUPLI2Y7FFACZJ4B5RBKTLZMOHGLAL37KRAZDWL4GBSQRUAAAAMJO66XJEYAAAAADXRVZETNGBKF7UX',
            'jdd03AFZAXQMGABTJ343PVG25KROTKXYAWNYIPKPLE3E2WW2WP6DPYYYSSAL4YUXQ3EJMPZJLDOXGEGTUPY2JJOUWNK2LSYAAAAMJO66XKSIAAAAADQZUS6R376KPCEX',
            'jdd03AVQGWCCOCTLX6RI4APW5FTDQA5DGHQPHF3UE6FRNAIBMIFO7SGBUZZWYN6BCNXX3SMO4JHOYYVL2IVG3QU5335GA44AAAAMJO66XL6QAAAAACY6VHFMQ7QGRWEX',
            'jdd03SBQH2WS3L3N3RR3VCVXPTGVFHHRHRBW67FYEQBIZDADNN2LEDKFX626WLPM7ZBPBET2RYNWSTGLQPCOQSIJ5LEAWMQAAAAMJO66XNKYAAAAADL7GOZJRKQLL7EX',
            'jdd036FUK2T5SB3ZN3PTPGXTKBN7PUFJZ6BBJXG2QH2YWCJCHAMUGUB5YDEMGOFJ6U4UYHZU6OKFQIGW44LCLXDTC4HZFLEAAAAMJO66XOYQAAAAAD5V7AKVHBSX6IMX',
            'jdd0343NXY34KFUBI7NPXVIRPPFDNTMABDGFURAL2QQ3UFFW2MKCXTJTUDYLITCJVRYPT5DTQDE53XULR57FQGLXCO66GTAAAAAMJO66XQFIAAAAACHF225N6C5TZCEX',
            'jdd03WOBY4EEM6YTGJSCTG3EUDM2BEEAZJZNBXZMQVHTFZTBUFFVYKUUYCXGCFTWFW6T622KIJX57USNXPLUU6TRKOKLVPAAAAAMJO66XRQQAAAAACWH6VHVJ56JWPEX',
            'jdd03JINZA7UBQTRR2CULCESA2PL3CY4VO7US6YLK235FMWE4JNVHKMQAIJX6G6FEZRNRVFAXM6LR5EOK3LNR62VIWWOQFQAAAAMJO66XS2QAAAAACEEIG2CYYOCQRIX',
            'jdd03YEDPTAEWWFAO5VGK5BLOASK7KT57OZZBPGKYKLLM5AH3ZF3BKTTHYYLD5CTZXODAF7KTK3RF6ALAPUS4B6JZKQ57MEAAAAMJO66XUIIAAAAAC6A5QY4CN3OZD4X',
            'jdd03SBQH2WS3L3N3RR3VCVXPTGVFHHRHRBW67FYEQBIZDADNN2LEDKFX626WLPM7ZBPBET2RYNWSTGLQPCOQSIJ5LEAWMQAAAAMJO66XVUQAAAAADD6YYY4D3UTBBUX',
            'jdd034OSEHYIMLLVRCARD6AREEJYHRD5MQMNVGU3SMBL3UMSWCZZ6XFVWI47O2SQFXN6UZ6GF2UK73PXRB4OC4FOUZD4OLIAAAAMJO66XXBAAAAAADI7R7SHTZ5BGRYX',
            'jdd03SBQH2WS3L3N3RR3VCVXPTGVFHHRHRBW67FYEQBIZDADNN2LEDKFX626WLPM7ZBPBET2RYNWSTGLQPCOQSIJ5LEAWMQAAAAMJO66XYSIAAAAAD4DOPLLBCQV5UEX',
            'jdd03WOBY4EEM6YTGJSCTG3EUDM2BEEAZJZNBXZMQVHTFZTBUFFVYKUUYCXGCFTWFW6T622KIJX57USNXPLUU6TRKOKLVPAAAAAMJO66XZ6YAAAAADUFSVAM2VD36F4X',
            'jdd03AFZAXQMGABTJ343PVG25KROTKXYAWNYIPKPLE3E2WW2WP6DPYYYSSAL4YUXQ3EJMPZJLDOXGEGTUPY2JJOUWNK2LSYAAAAMJO66X3PAAAAAACDJYNCFJKQTIAIX',
            'jdd03CEGEO2NES34BBUMIO3UMMWGZSXRMCKRXPLLPNECTK6KIYWMZACJGYFHAEVHFX22PBRWKFEVFMGNLMRAABVSQS7OWGUAAAAMJO66X45AAAAAADLUCGYYQDRXNDUX',
            'jdd0364LGMOEE7MP5C7CT733VEJKVZ3LGD7VR5AY7ZUHCWXRG6CUZFKA3T4ADR66CNZIFRRM76TID4L7YRXZP5OMH2DWOAAAAAAMJO66X6JIAAAAAC447E5DLGAMHUEX',
            'jdd03TKB4U2UBJJYBXZJLUMHRAHLKPQZ5XAAF3PKFMYTYNBJQL2PBL2JUJXMQRMSBBPZQE3ZSQ5QGNPVPC7VE5JIHHML6UEAAAAMJO66X7YYAAAAACTH53AG6SBY6ZQX',
            'jdd03WOBY4EEM6YTGJSCTG3EUDM2BEEAZJZNBXZMQVHTFZTBUFFVYKUUYCXGCFTWFW6T622KIJX57USNXPLUU6TRKOKLVPAAAAAMJO66YBCYAAAAADPSMSV577JA2WYX',
            'jdd033GJ6QCLAE3EPZWGSZTOBMQNE2F5CBDD3VBQD7VZC2OKMDUBNVEG5XL3T4LKGU2N5DGTXKJ7GPM7UHVXMM4W4LW663YAAAAMJO66YCOQAAAAACA6GSJFVBU6H2IX',
            'jdd036FUK2T5SB3ZN3PTPGXTKBN7PUFJZ6BBJXG2QH2YWCJCHAMUGUB5YDEMGOFJ6U4UYHZU6OKFQIGW44LCLXDTC4HZFLEAAAAMJO66YD4IAAAAACKLE7TX4NXTSF4X',
            'jdd03AVQGWCCOCTLX6RI4APW5FTDQA5DGHQPHF3UE6FRNAIBMIFO7SGBUZZWYN6BCNXX3SMO4JHOYYVL2IVG3QU5335GA44AAAAMJO66YFGIAAAAACKT7HL7V2W6IMQX',
            'jdd03GCJLKXQ67KKBULPZS4OXYATA3TJ4C5X472KEXGINROB6742KDJY46KFKEOSJ7IJDTJCXEHMHOIQKS6QGOA43EIZDAUAAAAMJO66YGQAAAAAADUTXRL3323F6E4X',
            'jdd03CEGEO2NES34BBUMIO3UMMWGZSXRMCKRXPLLPNECTK6KIYWMZACJGYFHAEVHFX22PBRWKFEVFMGNLMRAABVSQS7OWGUAAAAMJO66YIAIAAAAADJNJY2IEFAU3IYX',
            'jdd03CEGEO2NES34BBUMIO3UMMWGZSXRMCKRXPLLPNECTK6KIYWMZACJGYFHAEVHFX22PBRWKFEVFMGNLMRAABVSQS7OWGUAAAAMJO66YJRYAAAAAC3AK2D2CYXXVXAX',
            'jdd03WOBY4EEM6YTGJSCTG3EUDM2BEEAZJZNBXZMQVHTFZTBUFFVYKUUYCXGCFTWFW6T622KIJX57USNXPLUU6TRKOKLVPAAAAAMJO66YK7QAAAAADT5PHLDTKHSA3YX',
            'jdd033HJRD6Z2CUXMIM7NKIVKQS55EAHCUSAQ3MBSOHZCYVFFDEPPO3I3V5UQQOFRU5I7QU2ZS53LGPU4VQYEYFWDKKWIVQAAAAMJO66YMMAAAAAADR5ADX4IXDPJBUX',
            'jdd03TKD2ABIFXO2TJZFKBOP7HROSRFYCSW3DBBW4NZ5GDDFCQ7YEXW6Q4IMGJO2RPG6XNU5WPPTEAHB5ALP4FVDB2AMQ2QAAAAMJO66YN2YAAAAAC5NCJFO2AKRYOQX',
            'jdd03XKQIU7JHWU3FTRPNHLXLGLMHRJD7OMVOISOPHL7C455LVYVP7WHVONHZQY27CVJH7N5ZFIRZHLU5YMPD2XYEYAI4V4AAAAMJO66YPIIAAAAACO3XFV5A33OSQEX',
            'jdd03AIEDI4NFNSDUDHNEFTRSPUYVLHENOGLL5HKRHSG5FJCS72KOR7WP7Q65D6JXH6IRGKGZKLV7XOQMSQ3FCNONLVZYP4AAAAMJO66YQ2AAAAAACE2M6UESBRGYLIX',
            'jdd03AVQGWCCOCTLX6RI4APW5FTDQA5DGHQPHF3UE6FRNAIBMIFO7SGBUZZWYN6BCNXX3SMO4JHOYYVL2IVG3QU5335GA44AAAAMJO66YSGAAAAAADZUP2WW6NSEDXEX',
            'jdd03WOBY4EEM6YTGJSCTG3EUDM2BEEAZJZNBXZMQVHTFZTBUFFVYKUUYCXGCFTWFW6T622KIJX57USNXPLUU6TRKOKLVPAAAAAMJO66YTTQAAAAACLBE3L2QGKX4IMX',
            'jdd035JZQJ7TPQK3J5ZFWXO5AZ2GPV7CMTDJ6TWKW2OSG52AUETSJ7XDHP35N2SPE72PRUTNHJGWBGE3OXZFPMYXY2SV6OYAAAAMJO66YU7QAAAAADWE2PBJ5O76CVIX',
            'jdd03D6TZSITOQRTA64ZKVRRPBODGSEYORDML3W6HBJXHCXV7MFIS6ZOU7D5RZUB7HONYV2UXS2FZI6YOTQLQC6HHGMVVKMAAAAMJO66YWOYAAAAADWOMTTDWFRX4AIX',
            'jdd03TKB4U2UBJJYBXZJLUMHRAHLKPQZ5XAAF3PKFMYTYNBJQL2PBL2JUJXMQRMSBBPZQE3ZSQ5QGNPVPC7VE5JIHHML6UEAAAAMJO66YX6IAAAAADF2ANDJJ42C3VUX',
            'jdd035JZQJ7TPQK3J5ZFWXO5AZ2GPV7CMTDJ6TWKW2OSG52AUETSJ7XDHP35N2SPE72PRUTNHJGWBGE3OXZFPMYXY2SV6OYAAAAMJO66YZRQAAAAADG2WSOTXPY532IX',
            'jdd03AIEDI4NFNSDUDHNEFTRSPUYVLHENOGLL5HKRHSG5FJCS72KOR7WP7Q65D6JXH6IRGKGZKLV7XOQMSQ3FCNONLVZYP4AAAAMJO66Y3BQAAAAAC7O3CMYBTOJE4QX',
            'jdd03AFZAXQMGABTJ343PVG25KROTKXYAWNYIPKPLE3E2WW2WP6DPYYYSSAL4YUXQ3EJMPZJLDOXGEGTUPY2JJOUWNK2LSYAAAAMJO66Y4PIAAAAADHCFZJFORLMNNQX',
            'jdd03MEN7ZOOHVHNMWGEAK3STYF4CKDHGOIZNFPXUWLKOEJ3FI4E7IZLVEJYTF7AR2VKK5XNUJ6NHRMB6Y5YOWF6KYBNIGEAAAAMJO66Y56QAAAAAC2O4CU4IIR2N44X',
            'jdd03LJ3JUWQHIQOP5TVMXKV2UBG6H3WGO3HYFXNDN3BXMXZ5PBZC77SMON5LQG66CWM5Y6QAIK3PTOO2UJ4MUCCHTDKWDEAAAAMJO66Y7KQAAAAADEKHRD7VVQXTMYX',
            'jdd035JZQJ7TPQK3J5ZFWXO5AZ2GPV7CMTDJ6TWKW2OSG52AUETSJ7XDHP35N2SPE72PRUTNHJGWBGE3OXZFPMYXY2SV6OYAAAAMJO66ZAWAAAAAADSOZ7ZKJ2EIICEX',
            'jdd036FUK2T5SB3ZN3PTPGXTKBN7PUFJZ6BBJXG2QH2YWCJCHAMUGUB5YDEMGOFJ6U4UYHZU6OKFQIGW44LCLXDTC4HZFLEAAAAMJO66ZCCQAAAAADH7KRFCZ6AFHKMX',
            'jdd03Q53ZTHXKGA775A5CH4V6XQV4F2LKROIULGIIXU2EY4D4S2AGFERE67FCGXT4MKS3D2WYTBG7NU7QEJ43RUOBBQSDPMAAAAMJO66ZDNQAAAAAC37VLBBGTXK46QX',
            'jdd03AFZAXQMGABTJ343PVG25KROTKXYAWNYIPKPLE3E2WW2WP6DPYYYSSAL4YUXQ3EJMPZJLDOXGEGTUPY2JJOUWNK2LSYAAAAMJO66ZE3AAAAAADFZE5CBICLM5NMX',
            'jdd034OSEHYIMLLVRCARD6AREEJYHRD5MQMNVGU3SMBL3UMSWCZZ6XFVWI47O2SQFXN6UZ6GF2UK73PXRB4OC4FOUZD4OLIAAAAMJO66ZGIIAAAAADWSJ72S55U6QFUX',
            'jdd03RPDO53GTVWX3VDIVSCXPWR3ZIBNQTWHJK4ZCC63P3HG56TMQ4YGXPUEXCPB5QSPEO7CBTOE7HYA6XC6FTNM4AAZG3UAAAAMJO66ZHUIAAAAAD3YMUEDSXZK4UUX',
            'jdd03RPDO53GTVWX3VDIVSCXPWR3ZIBNQTWHJK4ZCC63P3HG56TMQ4YGXPUEXCPB5QSPEO7CBTOE7HYA6XC6FTNM4AAZG3UAAAAMJO66ZJCQAAAAAD3W6MJ3VWUESCQX',
            'jdd03EHSX3QL5THY7WSG5ERNAMBOFZNEZOOQCIGBVC4NQO4YSYKMOW7GVZPBFN6WHVBZELDS6QZ7DYN3WGURLVSCR6KOG6UAAAAMJO66ZKSQAAAAAC6DYGDTP4GKLFAX',
            'jdd03CMV72XMO7MTENZKV2DVKWWTOAL62FIFHCCZYISD7ZND66FHFDNYJZNNLQ6U3KE57VCIOKT4YCPPHYOELUKHQVF4NSAAAAAMJO66ZMEYAAAAACA2WJ4QZH6H5LAX',
            'jdd03XKQIU7JHWU3FTRPNHLXLGLMHRJD7OMVOISOPHL7C455LVYVP7WHVONHZQY27CVJH7N5ZFIRZHLU5YMPD2XYEYAI4V4AAAAMJO66ZNTYAAAAADX36XFX7NQH3XEX',
            'jdd03XCGBBJLWTS6UE5HTF5DWUND7QLAZTY4YEOGZI3XELFIJBFX57LKFZJ4JUAUWFYMW5ILQAVRAN334UQB57RH52XDRBEAAAAMJO66ZPDIAAAAACM3JOQUYCHFA4YX',
            'jdd03AFZAXQMGABTJ343PVG25KROTKXYAWNYIPKPLE3E2WW2WP6DPYYYSSAL4YUXQ3EJMPZJLDOXGEGTUPY2JJOUWNK2LSYAAAAMJO66ZQQQAAAAACEP2WAWNRYYJVYX',
            'jdd03AIEDI4NFNSDUDHNEFTRSPUYVLHENOGLL5HKRHSG5FJCS72KOR7WP7Q65D6JXH6IRGKGZKLV7XOQMSQ3FCNONLVZYP4AAAAMJO66ZSAQAAAAADLNUSKRNIRQMQYX',
            'jdd03MEN7ZOOHVHNMWGEAK3STYF4CKDHGOIZNFPXUWLKOEJ3FI4E7IZLVEJYTF7AR2VKK5XNUJ6NHRMB6Y5YOWF6KYBNIGEAAAAMJO66ZTNAAAAAAC4Z2TGUQ67AYL4X',
            'jdd03GP3ZLDDCCDJ2KRZNWMWNQ5546Q2BV7G3ZBKRQJAS6LILMSEA462XHAFH2LIFDIFICQUFYYYHEDLB45V7GRHY6OTAIIAAAAMJO66ZU6QAAAAACUCLRFTNI2FXEMX',
            'jdd03SBQH2WS3L3N3RR3VCVXPTGVFHHRHRBW67FYEQBIZDADNN2LEDKFX626WLPM7ZBPBET2RYNWSTGLQPCOQSIJ5LEAWMQAAAAMJO66ZWOAAAAAADHMEL4MGEGX3LAX',
            'jdd03AIEDI4NFNSDUDHNEFTRSPUYVLHENOGLL5HKRHSG5FJCS72KOR7WP7Q65D6JXH6IRGKGZKLV7XOQMSQ3FCNONLVZYP4AAAAMJO66ZX5QAAAAACQMCGACKJ7VUHAX',
            'jdd03TKB4U2UBJJYBXZJLUMHRAHLKPQZ5XAAF3PKFMYTYNBJQL2PBL2JUJXMQRMSBBPZQE3ZSQ5QGNPVPC7VE5JIHHML6UEAAAAMJO66ZZKYAAAAACOBFB2RD2CGNVYX',
            'jdd03AIEDI4NFNSDUDHNEFTRSPUYVLHENOGLL5HKRHSG5FJCS72KOR7WP7Q65D6JXH6IRGKGZKLV7XOQMSQ3FCNONLVZYP4AAAAMJO66Z2YIAAAAACULE6HXBZMMQFIX',
            'jdd03NFDMBGXIWBEQVBBOEPSSCM5QR6MD5JXRH4JID73BFWE2YBSOEY24BDT5IRQCKG64FNIEORYBS3AKCTZF7XKY3RSBREAAAAMJO66Z4LIAAAAACUYLPZFVHCJ3XYX',
            'jdd03WOBY4EEM6YTGJSCTG3EUDM2BEEAZJZNBXZMQVHTFZTBUFFVYKUUYCXGCFTWFW6T622KIJX57USNXPLUU6TRKOKLVPAAAAAMJO66Z5XYAAAAACRW6B6D2MUHJUEX',
            'jdd03AVQGWCCOCTLX6RI4APW5FTDQA5DGHQPHF3UE6FRNAIBMIFO7SGBUZZWYN6BCNXX3SMO4JHOYYVL2IVG3QU5335GA44AAAAMJO66Z7GYAAAAACYSYZIJXAYFK24X',
            'jdd03GP3ZLDDCCDJ2KRZNWMWNQ5546Q2BV7G3ZBKRQJAS6LILMSEA462XHAFH2LIFDIFICQUFYYYHEDLB45V7GRHY6OTAIIAAAAMJO662AVQAAAAADI2NPRQD6ZSMSMX',
            'jdd034OSEHYIMLLVRCARD6AREEJYHRD5MQMNVGU3SMBL3UMSWCZZ6XFVWI47O2SQFXN6UZ6GF2UK73PXRB4OC4FOUZD4OLIAAAAMJO662CFQAAAAADARDE4SEHHOTYAX',
            'jdd03RPDO53GTVWX3VDIVSCXPWR3ZIBNQTWHJK4ZCC63P3HG56TMQ4YGXPUEXCPB5QSPEO7CBTOE7HYA6XC6FTNM4AAZG3UAAAAMJO662DQIAAAAACWG5PM73EKDYHUX',
            'jdd03CMV72XMO7MTENZKV2DVKWWTOAL62FIFHCCZYISD7ZND66FHFDNYJZNNLQ6U3KE57VCIOKT4YCPPHYOELUKHQVF4NSAAAAAMJO662FCIAAAAAC3FPH6S4ZNZSDIX',
            'jdd03AIEDI4NFNSDUDHNEFTRSPUYVLHENOGLL5HKRHSG5FJCS72KOR7WP7Q65D6JXH6IRGKGZKLV7XOQMSQ3FCNONLVZYP4AAAAMJO662GOIAAAAADS2P4GFICVFZMUX',
            'jdd035JZQJ7TPQK3J5ZFWXO5AZ2GPV7CMTDJ6TWKW2OSG52AUETSJ7XDHP35N2SPE72PRUTNHJGWBGE3OXZFPMYXY2SV6OYAAAAMJO662H6IAAAAACITXAJGEASW724X',
            'jdd03XKQIU7JHWU3FTRPNHLXLGLMHRJD7OMVOISOPHL7C455LVYVP7WHVONHZQY27CVJH7N5ZFIRZHLU5YMPD2XYEYAI4V4AAAAMJO662JKQAAAAADKFFLSUB246XXIX',
            'jdd03GP3ZLDDCCDJ2KRZNWMWNQ5546Q2BV7G3ZBKRQJAS6LILMSEA462XHAFH2LIFDIFICQUFYYYHEDLB45V7GRHY6OTAIIAAAAMJO662K5IAAAAADQSCMLVXVK2NGMX',
            'jdd03YEDPTAEWWFAO5VGK5BLOASK7KT57OZZBPGKYKLLM5AH3ZF3BKTTHYYLD5CTZXODAF7KTK3RF6ALAPUS4B6JZKQ57MEAAAAMJO662MLAAAAAADGYEMES7QG46JYX',
            'jdd03CMV72XMO7MTENZKV2DVKWWTOAL62FIFHCCZYISD7ZND66FHFDNYJZNNLQ6U3KE57VCIOKT4YCPPHYOELUKHQVF4NSAAAAAMJO662NWQAAAAAD2CRWWXQHNRLLAX',
            'jdd03WOBY4EEM6YTGJSCTG3EUDM2BEEAZJZNBXZMQVHTFZTBUFFVYKUUYCXGCFTWFW6T622KIJX57USNXPLUU6TRKOKLVPAAAAAMJO662PCQAAAAACOPJD3HBDPR3OAX',
            'jdd03SBQH2WS3L3N3RR3VCVXPTGVFHHRHRBW67FYEQBIZDADNN2LEDKFX626WLPM7ZBPBET2RYNWSTGLQPCOQSIJ5LEAWMQAAAAMJO662QQIAAAAADDWYQX6JLH6LPEX',
            'jdd03XKQIU7JHWU3FTRPNHLXLGLMHRJD7OMVOISOPHL7C455LVYVP7WHVONHZQY27CVJH7N5ZFIRZHLU5YMPD2XYEYAI4V4AAAAMJO662R7AAAAAADJTRLEM35PS3NEX',
            'jdd03RJNWPL3QU6UB6WNAJ4OLCOHAA3BQXJ5GLF7IDB7IGFU6WLD224KNVWDB5J4JCXIOJ3UCKWZ5LD6UITIOG7QLNSNLKEAAAAMJO662TMAAAAAADGF26NZ7ONCCVEX',
            'jdd03CMV72XMO7MTENZKV2DVKWWTOAL62FIFHCCZYISD7ZND66FHFDNYJZNNLQ6U3KE57VCIOKT4YCPPHYOELUKHQVF4NSAAAAAMJO662U5YAAAAADOOCQ7AQQYXMJEX',
            'jdd03P5ZZOAUGQIX4QVU7H2DACD7HAMETQGBWTEMGQBR3SNZJCIWQEFFBRRCAVUWKQ2QXLYMBQYYK4N2U7VEGC3MLI3WHPUAAAAMJO662WPAAAAAADHWITXJ342EZK4X',
            'jdd03AVQGWCCOCTLX6RI4APW5FTDQA5DGHQPHF3UE6FRNAIBMIFO7SGBUZZWYN6BCNXX3SMO4JHOYYVL2IVG3QU5335GA44AAAAMJO662XYIAAAAADCBEVHJYYZXKZMX',
            'jdd03TKD2ABIFXO2TJZFKBOP7HROSRFYCSW3DBBW4NZ5GDDFCQ7YEXW6Q4IMGJO2RPG6XNU5WPPTEAHB5ALP4FVDB2AMQ2QAAAAMJO662ZHQAAAAAD4MJWUKVRBIRYQX',
            'jdd034OSEHYIMLLVRCARD6AREEJYHRD5MQMNVGU3SMBL3UMSWCZZ6XFVWI47O2SQFXN6UZ6GF2UK73PXRB4OC4FOUZD4OLIAAAAMJO6622TIAAAAACSCVNYBXXKNQ7MX',
            'jdd03CMV72XMO7MTENZKV2DVKWWTOAL62FIFHCCZYISD7ZND66FHFDNYJZNNLQ6U3KE57VCIOKT4YCPPHYOELUKHQVF4NSAAAAAMJO6624CIAAAAACOPXUNINXI2QFMX',
            'jdd03WOBY4EEM6YTGJSCTG3EUDM2BEEAZJZNBXZMQVHTFZTBUFFVYKUUYCXGCFTWFW6T622KIJX57USNXPLUU6TRKOKLVPAAAAAMJO6625QIAAAAACZOQQ4DVJLNOLIX',
            'jdd03AFZAXQMGABTJ343PVG25KROTKXYAWNYIPKPLE3E2WW2WP6DPYYYSSAL4YUXQ3EJMPZJLDOXGEGTUPY2JJOUWNK2LSYAAAAMJO66265QAAAAADSX7W225OZ3VKYX',
            'jdd03WOBY4EEM6YTGJSCTG3EUDM2BEEAZJZNBXZMQVHTFZTBUFFVYKUUYCXGCFTWFW6T622KIJX57USNXPLUU6TRKOKLVPAAAAAMJO663AQYAAAAADSPJLFLEX7QAOAX',
            'jdd034OSEHYIMLLVRCARD6AREEJYHRD5MQMNVGU3SMBL3UMSWCZZ6XFVWI47O2SQFXN6UZ6GF2UK73PXRB4OC4FOUZD4OLIAAAAMJO663CBAAAAAACJDWEUU7AWLTGQX',
            'jdd03WOBY4EEM6YTGJSCTG3EUDM2BEEAZJZNBXZMQVHTFZTBUFFVYKUUYCXGCFTWFW6T622KIJX57USNXPLUU6TRKOKLVPAAAAAMJO663DSAAAAAADYYV7662Z4EUGMX',
            'jdd03AFZAXQMGABTJ343PVG25KROTKXYAWNYIPKPLE3E2WW2WP6DPYYYSSAL4YUXQ3EJMPZJLDOXGEGTUPY2JJOUWNK2LSYAAAAMJO663FAQAAAAADV7VUJLTNG75UIX',
            'jdd03AFZAXQMGABTJ343PVG25KROTKXYAWNYIPKPLE3E2WW2WP6DPYYYSSAL4YUXQ3EJMPZJLDOXGEGTUPY2JJOUWNK2LSYAAAAMJO663GNQAAAAACHY3VMIM4TVIJQX',
            'jdd03DBNYODXHAC7MOYNXFCUYQ3SSMMKJWFHMPXC5KF3J3L4VSW2BBME3GR7AFYHNFB4UT6XHFX64KYYDPHMC7UG5Y256PUAAAAMJO663H4QAAAAADZRWE6ZG77Y7KUX',
            'jdd03XKQIU7JHWU3FTRPNHLXLGLMHRJD7OMVOISOPHL7C455LVYVP7WHVONHZQY27CVJH7N5ZFIRZHLU5YMPD2XYEYAI4V4AAAAMJO663JNQAAAAADZ6GHRP74WZ7GEX',
            'jdd03XKQIU7JHWU3FTRPNHLXLGLMHRJD7OMVOISOPHL7C455LVYVP7WHVONHZQY27CVJH7N5ZFIRZHLU5YMPD2XYEYAI4V4AAAAMJO663KZIAAAAACY6LHYFZ2BSD74X',
            'jdd03AIEDI4NFNSDUDHNEFTRSPUYVLHENOGLL5HKRHSG5FJCS72KOR7WP7Q65D6JXH6IRGKGZKLV7XOQMSQ3FCNONLVZYP4AAAAMJO663MIAAAAAAD3WSPZLQ3ZJV2MX',
            'jdd03GP3ZLDDCCDJ2KRZNWMWNQ5546Q2BV7G3ZBKRQJAS6LILMSEA462XHAFH2LIFDIFICQUFYYYHEDLB45V7GRHY6OTAIIAAAAMJO663NVYAAAAACCILCN27Q3W4I4X',
            'jdd03AIEDI4NFNSDUDHNEFTRSPUYVLHENOGLL5HKRHSG5FJCS72KOR7WP7Q65D6JXH6IRGKGZKLV7XOQMSQ3FCNONLVZYP4AAAAMJO663PFQAAAAACW4FMZFP5CRRKUX',
            'jdd03AVQGWCCOCTLX6RI4APW5FTDQA5DGHQPHF3UE6FRNAIBMIFO7SGBUZZWYN6BCNXX3SMO4JHOYYVL2IVG3QU5335GA44AAAAMJO663QUAAAAAADSOWIFKQLTHIDIX',
            'jdd03TKB4U2UBJJYBXZJLUMHRAHLKPQZ5XAAF3PKFMYTYNBJQL2PBL2JUJXMQRMSBBPZQE3ZSQ5QGNPVPC7VE5JIHHML6UEAAAAMJO663SBIAAAAADOTZYYXCQ4AIJYX',
            'jdd03AIEDI4NFNSDUDHNEFTRSPUYVLHENOGLL5HKRHSG5FJCS72KOR7WP7Q65D6JXH6IRGKGZKLV7XOQMSQ3FCNONLVZYP4AAAAMJO663TUAAAAAACQUINBVX7JWCEMX',
            'jdd03YEDPTAEWWFAO5VGK5BLOASK7KT57OZZBPGKYKLLM5AH3ZF3BKTTHYYLD5CTZXODAF7KTK3RF6ALAPUS4B6JZKQ57MEAAAAMJO663VCAAAAAACAR34K5N5TGBXUX',
            'jdd03AIEDI4NFNSDUDHNEFTRSPUYVLHENOGLL5HKRHSG5FJCS72KOR7WP7Q65D6JXH6IRGKGZKLV7XOQMSQ3FCNONLVZYP4AAAAMJO663WSYAAAAACSJ6ZZSHMTNFBUX',
            'jdd03TKB4U2UBJJYBXZJLUMHRAHLKPQZ5XAAF3PKFMYTYNBJQL2PBL2JUJXMQRMSBBPZQE3ZSQ5QGNPVPC7VE5JIHHML6UEAAAAMJO663X7AAAAAACSAC2T6FQPMCHIX',
            'jdd03AVQGWCCOCTLX6RI4APW5FTDQA5DGHQPHF3UE6FRNAIBMIFO7SGBUZZWYN6BCNXX3SMO4JHOYYVL2IVG3QU5335GA44AAAAMJO663ZKQAAAAADXSP6JO5VH2PAMX',
            'jdd03AVQGWCCOCTLX6RI4APW5FTDQA5DGHQPHF3UE6FRNAIBMIFO7SGBUZZWYN6BCNXX3SMO4JHOYYVL2IVG3QU5335GA44AAAAMJO6632WQAAAAACDQOQNOBLS3CVAX',
            'jdd03RPDO53GTVWX3VDIVSCXPWR3ZIBNQTWHJK4ZCC63P3HG56TMQ4YGXPUEXCPB5QSPEO7CBTOE7HYA6XC6FTNM4AAZG3UAAAAMJO6634FIAAAAADSEM5FMLMATK64X',
            'jdd03RJNWPL3QU6UB6WNAJ4OLCOHAA3BQXJ5GLF7IDB7IGFU6WLD224KNVWDB5J4JCXIOJ3UCKWZ5LD6UITIOG7QLNSNLKEAAAAMJO6635UAAAAAACWHN2YNBD3IKZYX',
            'jdd03L52TCDU3WIZGZBXCBT6DRPEFBF2LVF5AEZAOUKCMGOUAERBFJCDSYFEORLQSH4YDTMQRETKLB754YQTNVPBW5TS4PIAAAAMJO6637DAAAAAAD3S3W3EQUFNYNYX',
            'jdd034US2BBVLCOCSJWMDM6EDAUB245HDKC2CVE4R42QA5YH6OVDRQZIKJ7OEDAPJF262IPI6NJPQVIAW4CBIYZYNS6GDV4AAAAMJO664AQAAAAAADUZHMSCYNOFYZIX',
            'jdd03AVQGWCCOCTLX6RI4APW5FTDQA5DGHQPHF3UE6FRNAIBMIFO7SGBUZZWYN6BCNXX3SMO4JHOYYVL2IVG3QU5335GA44AAAAMJO664B2YAAAAACEMTGKO4576IQ4X',
            'jdd034OSEHYIMLLVRCARD6AREEJYHRD5MQMNVGU3SMBL3UMSWCZZ6XFVWI47O2SQFXN6UZ6GF2UK73PXRB4OC4FOUZD4OLIAAAAMJO664DHQAAAAACSIII2UAYH6D5YX',
            'jdd03AIEDI4NFNSDUDHNEFTRSPUYVLHENOGLL5HKRHSG5FJCS72KOR7WP7Q65D6JXH6IRGKGZKLV7XOQMSQ3FCNONLVZYP4AAAAMJO664EWIAAAAACGBX7SCFWXWPDYX',
            'jdd03AFZAXQMGABTJ343PVG25KROTKXYAWNYIPKPLE3E2WW2WP6DPYYYSSAL4YUXQ3EJMPZJLDOXGEGTUPY2JJOUWNK2LSYAAAAMJO664GFIAAAAAD52SNX4GC7RX7QX',
            'jdd03D7R5BMRK7RQQLBJ74XPCET2SNHDNITNX4FSKBPGGA7MMS56ZBDYM5DHZEQHL5UKT4JIHGSTGTIFEEX2RXJE376C5ZQAAAAMJO664HTQAAAAACCBJ33E4FL6E6YX',
            'jdd03D6TZSITOQRTA64ZKVRRPBODGSEYORDML3W6HBJXHCXV7MFIS6ZOU7D5RZUB7HONYV2UXS2FZI6YOTQLQC6HHGMVVKMAAAAMJO664I7IAAAAACFO6XFJZYCD6GAX',
            'jdd03UAZ5IYW3BBGOQK5YPENREZH5MCHIGJIKQ53PJPRIFORA2GCM324N3EU4CJLITELA2XZ3L327B4PYGNOFAHC22FS6CYAAAAMJO664KNYAAAAACTQO5QBACGALR4X',
            'jdd03K2OXOQQ2RDOMBALJIH2OVZHD7GTOIUUGJI6Q4WXGVQTVPFTDZP3E72QFNBBQA7R2XPYIUK3PVX33YZ6BYNJDD5HLV4AAAAMJO664MAQAAAAAC4HVASSSLVNILIX',
            'jdd0364LGMOEE7MP5C7CT733VEJKVZ3LGD7VR5AY7ZUHCWXRG6CUZFKA3T4ADR66CNZIFRRM76TID4L7YRXZP5OMH2DWOAAAAAAMJO664NSAAAAAACQI6NC7K43GCD4X',
            'jdd03GP3ZLDDCCDJ2KRZNWMWNQ5546Q2BV7G3ZBKRQJAS6LILMSEA462XHAFH2LIFDIFICQUFYYYHEDLB45V7GRHY6OTAIIAAAAMJO664O7IAAAAAC4WCCZI7W3SCREX',
            'jdd03AYYGAVNH5QC76QQVCEGXM6LVU6OLZ3QHD7QE5JXMIAUF6OSIFOXH67VVT2XDA7SS7G64BRULUJUVIXUV4ZIIBH3F7YAAAAMJO664QJAAAAAADNR4747XJMMPZYX',
            'jdd034OSEHYIMLLVRCARD6AREEJYHRD5MQMNVGU3SMBL3UMSWCZZ6XFVWI47O2SQFXN6UZ6GF2UK73PXRB4OC4FOUZD4OLIAAAAMJO664RVIAAAAACTL2ZDQ5NMQ3AUX',
            'jdd03Z4ECWWMDPF22BWHWUAVJFYKJPJTIGZ6JK52GQKUDD6SPIVG4SNEM2GUCNWDHXKAAU22O3VNI46JBHFXLAUNX3XGKSEAAAAMJO664TDAAAAAADM6WKHZGEKVM7AX',
            'jdd03AVQGWCCOCTLX6RI4APW5FTDQA5DGHQPHF3UE6FRNAIBMIFO7SGBUZZWYN6BCNXX3SMO4JHOYYVL2IVG3QU5335GA44AAAAMJO664UPQAAAAAC6HFR5YW65O4GYX',
            'jdd03AIEDI4NFNSDUDHNEFTRSPUYVLHENOGLL5HKRHSG5FJCS72KOR7WP7Q65D6JXH6IRGKGZKLV7XOQMSQ3FCNONLVZYP4AAAAMJO664V7YAAAAACI36YKCD2U7WSAX',
            'jdd03YWPBXVP3N473QOKSJBXEA5ZKPAUIQPFA2OSUHMTPIVLN2MO3ZYYCBS7EF44MLG7VBP6VW2DV5UMNGVXCAWIRVUNDSMAAAAMJO664XOAAAAAADKMLGICZX623UUX',
            'jdd03X3MVIZSTMSO5KZSVERGFALOT3JQ77OVBNK65XKF5TWAS6JGQZOUNQLOHAAMNZIQEZDVPAOUZDKHZVHGYSWMJDN5SEMAAAAMJO664YYAAAAAADNIUYFNV2ZZK4UX',
            'jdd032OHTF4ZRCN5JCHNGZ6HRGCTPJW77BXF65X5BGQJL6C5YA2H7SALU4G6FSXCC7MNIB32OTN3ZG6CAT2UTNSU4C3QTOMAAAAMJO6642EYAAAAACXCHACUKAOP53UX',
            'jdd03WOBY4EEM6YTGJSCTG3EUDM2BEEAZJZNBXZMQVHTFZTBUFFVYKUUYCXGCFTWFW6T622KIJX57USNXPLUU6TRKOKLVPAAAAAMJO6643XAAAAAACHURRHNM2PCWWMX',
            'jdd03RPDO53GTVWX3VDIVSCXPWR3ZIBNQTWHJK4ZCC63P3HG56TMQ4YGXPUEXCPB5QSPEO7CBTOE7HYA6XC6FTNM4AAZG3UAAAAMJO6645CYAAAAADRJM7QJYBMC3G4X',
            'jdd03YEDPTAEWWFAO5VGK5BLOASK7KT57OZZBPGKYKLLM5AH3ZF3BKTTHYYLD5CTZXODAF7KTK3RF6ALAPUS4B6JZKQ57MEAAAAMJO6646QIAAAAACAJSOSTCLTRZW4X',
            'jdd03SBQH2WS3L3N3RR3VCVXPTGVFHHRHRBW67FYEQBIZDADNN2LEDKFX626WLPM7ZBPBET2RYNWSTGLQPCOQSIJ5LEAWMQAAAAMJO66473AAAAAAC56B2WIVPX3P7MX',
            'jdd03AIEDI4NFNSDUDHNEFTRSPUYVLHENOGLL5HKRHSG5FJCS72KOR7WP7Q65D6JXH6IRGKGZKLV7XOQMSQ3FCNONLVZYP4AAAAMJO665BNAAAAAADTK4OS5ZE45CPEX',
            'jdd0364BDOR6OGPHQYOJIIOXY4JUCX7KQ3KMWJT2CC4WWPBPYE3ZJ4FUOKULUL76MUOHDZRNISVULYJEA3VJ7M5PYEZVITUAAAAMJO665CZAAAAAADCERDM72SRVZKQX',
            'jdd03WOBY4EEM6YTGJSCTG3EUDM2BEEAZJZNBXZMQVHTFZTBUFFVYKUUYCXGCFTWFW6T622KIJX57USNXPLUU6TRKOKLVPAAAAAMJO665ECIAAAAACGU6EGONUKO2KAX',
            'jdd034OSEHYIMLLVRCARD6AREEJYHRD5MQMNVGU3SMBL3UMSWCZZ6XFVWI47O2SQFXN6UZ6GF2UK73PXRB4OC4FOUZD4OLIAAAAMJO665FMQAAAAADLYLQQZIOD4COQX',
            'jdd03WOBY4EEM6YTGJSCTG3EUDM2BEEAZJZNBXZMQVHTFZTBUFFVYKUUYCXGCFTWFW6T622KIJX57USNXPLUU6TRKOKLVPAAAAAMJO665GYAAAAAADGGN6DPXS7TEJAX',
            'jdd03CMV72XMO7MTENZKV2DVKWWTOAL62FIFHCCZYISD7ZND66FHFDNYJZNNLQ6U3KE57VCIOKT4YCPPHYOELUKHQVF4NSAAAAAMJO665IGIAAAAACK7BEDYDMMXOOQX',
            'jdd03V3G6TDMB2DDLU37PW4EEXFKAQXVWLDGNUC2JJ63SX6Y4YIJQ4QEBZPGW7RBVRE43MATG4N5WKE6S2HE553FR32IIVEAAAAMJO665JXIAAAAACBLY53PFXSD33QX',
            'jdd0336C7GAWKPQFE5TORHSKYN26IF2OGZKPI2OMNHYAB72M6WYHK2KTWWEM2ILPN6ZV7XCXRZTRNJAEKFMXV27UFJWSZSIAAAAMJO665LFAAAAAADIJFMEOV5ISVZYX',
            'jdd03WOBY4EEM6YTGJSCTG3EUDM2BEEAZJZNBXZMQVHTFZTBUFFVYKUUYCXGCFTWFW6T622KIJX57USNXPLUU6TRKOKLVPAAAAAMJO665MRAAAAAACQ7543BG4XMJG4X',
            'jdd033HJRD6Z2CUXMIM7NKIVKQS55EAHCUSAQ3MBSOHZCYVFFDEPPO3I3V5UQQOFRU5I7QU2ZS53LGPU4VQYEYFWDKKWIVQAAAAMJO665OAQAAAAACJBUPQBP5HUH3UX',
            'jdd03AXMHAALL7SLYXIOMNV7HYJWT5MDZK7I6TM57MRMBGFQ3N3LAYPGDMUAJ3VAKZBRV6RO6WGRXCW7PESTZIVGPS7W3GQAAAAMJO665PMQAAAAACCNOKEXR5AN7LUX',
            'jdd03AFZAXQMGABTJ343PVG25KROTKXYAWNYIPKPLE3E2WW2WP6DPYYYSSAL4YUXQ3EJMPZJLDOXGEGTUPY2JJOUWNK2LSYAAAAMJO665Q3YAAAAACDIETSZ4MTFG4MX',
            'jdd03D7GXV5UUOGVIDLFOQDTVVXFQBRBFJ4OVKJ5XCDJD65OUQPBNZXKD7KE6DYM56HAX46JJ6OWY5JI65DIBDB33GRZLOIAAAAMJO665SGAAAAAAC6VM2Z5M5OR6L4X',
            'jdd03WOBY4EEM6YTGJSCTG3EUDM2BEEAZJZNBXZMQVHTFZTBUFFVYKUUYCXGCFTWFW6T622KIJX57USNXPLUU6TRKOKLVPAAAAAMJO665TPQAAAAACF2ZXBULYKQUXEX',
            'jdd03F77NNFYB7OZH6RHVCZK4YUTM5KGOKIIVX3WSG6QOSYB7LMCDVV4NTB24KEPX56MBLYWVIMBFDI43X36HDUWW3KFKJIAAAAMJO665UYYAAAAADFTXMA5JZU3H6MX',
            'jdd03L52TCDU3WIZGZBXCBT6DRPEFBF2LVF5AEZAOUKCMGOUAERBFJCDSYFEORLQSH4YDTMQRETKLB754YQTNVPBW5TS4PIAAAAMJO665WGAAAAAADXEOBKFS2YRO5MX',
            'jdd03YEDPTAEWWFAO5VGK5BLOASK7KT57OZZBPGKYKLLM5AH3ZF3BKTTHYYLD5CTZXODAF7KTK3RF6ALAPUS4B6JZKQ57MEAAAAMJO665XYQAAAAADEYMUXHMNQHQREX',
            'jdd03GP3ZLDDCCDJ2KRZNWMWNQ5546Q2BV7G3ZBKRQJAS6LILMSEA462XHAFH2LIFDIFICQUFYYYHEDLB45V7GRHY6OTAIIAAAAMJO665ZKQAAAAACBQ3RUTKYATA3YX',
            'jdd034OSEHYIMLLVRCARD6AREEJYHRD5MQMNVGU3SMBL3UMSWCZZ6XFVWI47O2SQFXN6UZ6GF2UK73PXRB4OC4FOUZD4OLIAAAAMJO6652YIAAAAADAUW3WBJOEVIVEX',
            'jdd03YWPBXVP3N473QOKSJBXEA5ZKPAUIQPFA2OSUHMTPIVLN2MO3ZYYCBS7EF44MLG7VBP6VW2DV5UMNGVXCAWIRVUNDSMAAAAMJO6654FAAAAAADUQOXRLG3Z7FAUX',
            'jdd03WOBY4EEM6YTGJSCTG3EUDM2BEEAZJZNBXZMQVHTFZTBUFFVYKUUYCXGCFTWFW6T622KIJX57USNXPLUU6TRKOKLVPAAAAAMJO6655OQAAAAACUNJRMW7XSAAZUX',
            'jdd03CMV72XMO7MTENZKV2DVKWWTOAL62FIFHCCZYISD7ZND66FHFDNYJZNNLQ6U3KE57VCIOKT4YCPPHYOELUKHQVF4NSAAAAAMJO66565QAAAAAD45DRUIBT53AVYX',
            'jdd03D6TZSITOQRTA64ZKVRRPBODGSEYORDML3W6HBJXHCXV7MFIS6ZOU7D5RZUB7HONYV2UXS2FZI6YOTQLQC6HHGMVVKMAAAAMJO666AKYAAAAADZL3MEMYQEBICMX',
            'jdd03SBQH2WS3L3N3RR3VCVXPTGVFHHRHRBW67FYEQBIZDADNN2LEDKFX626WLPM7ZBPBET2RYNWSTGLQPCOQSIJ5LEAWMQAAAAMJO666BVYAAAAACBMYL4ESTNPZXAX',
            'jdd03AFZAXQMGABTJ343PVG25KROTKXYAWNYIPKPLE3E2WW2WP6DPYYYSSAL4YUXQ3EJMPZJLDOXGEGTUPY2JJOUWNK2LSYAAAAMJO666DEYAAAAADXCAPWGJGK3XM4X',
            'jdd03AIEDI4NFNSDUDHNEFTRSPUYVLHENOGLL5HKRHSG5FJCS72KOR7WP7Q65D6JXH6IRGKGZKLV7XOQMSQ3FCNONLVZYP4AAAAMJO666ERAAAAAACIGNKPAAWRLHQUX',
            'jdd03RAVZKBDOYLSCPSG4X5BVVZWTN3QQ5NXXTXWUBOKE6IP2S7CSYHW34ZUJFAGQXBXHUNAE53HNTDVGKGBXSB4FYDXTWQAAAAMJO666F5IAAAAAC6OU4ROBDS4YNMX',
            'jdd03AIEDI4NFNSDUDHNEFTRSPUYVLHENOGLL5HKRHSG5FJCS72KOR7WP7Q65D6JXH6IRGKGZKLV7XOQMSQ3FCNONLVZYP4AAAAMJO666HGQAAAAACX7CSPVD2XAFRMX',
            'jdd03YEDPTAEWWFAO5VGK5BLOASK7KT57OZZBPGKYKLLM5AH3ZF3BKTTHYYLD5CTZXODAF7KTK3RF6ALAPUS4B6JZKQ57MEAAAAMJO666ITAAAAAADSXZEGCIM6BWCAX',
            'jdd03GP3ZLDDCCDJ2KRZNWMWNQ5546Q2BV7G3ZBKRQJAS6LILMSEA462XHAFH2LIFDIFICQUFYYYHEDLB45V7GRHY6OTAIIAAAAMJO666J6IAAAAADOWVIY7I52YSGIX',
            'jdd03TKD2ABIFXO2TJZFKBOP7HROSRFYCSW3DBBW4NZ5GDDFCQ7YEXW6Q4IMGJO2RPG6XNU5WPPTEAHB5ALP4FVDB2AMQ2QAAAAMJO666LKQAAAAAC2PCLKIRL5O3B4X',
            'jdd03L52TCDU3WIZGZBXCBT6DRPEFBF2LVF5AEZAOUKCMGOUAERBFJCDSYFEORLQSH4YDTMQRETKLB754YQTNVPBW5TS4PIAAAAMJO666M4QAAAAAD4TWDBBZ5TOMHUX',
            'jdd03IICH4IJRCVPCNXEWP6PK3LV5G53WZJ6RVSV4CIZO7EHEIS4V3BCEVKXMQQR75AMRIYC4TCAPEMWULHJYVAUFFLZCVQAAAAMJO666OPAAAAAAD3XHP3WZTKZHYYX',
            'jdd03SBQH2WS3L3N3RR3VCVXPTGVFHHRHRBW67FYEQBIZDADNN2LEDKFX626WLPM7ZBPBET2RYNWSTGLQPCOQSIJ5LEAWMQAAAAMJO666P5IAAAAADXJJCB5SFISY5YX',
            'jdd034OSEHYIMLLVRCARD6AREEJYHRD5MQMNVGU3SMBL3UMSWCZZ6XFVWI47O2SQFXN6UZ6GF2UK73PXRB4OC4FOUZD4OLIAAAAMJO666RKQAAAAACISQXAEPZ357PUX']

    token = random.choice(x_api_eid_token)
    return token