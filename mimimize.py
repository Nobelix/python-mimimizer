import re


def mimimize(text : str):
    """Mimimize text."""

    #SZ pattern
    ss = r"([aeiou])ss([aeiou])"
    s = r"([^aeiou]|)s([aeiou])"
    ends = r"(.*?)s"
    z = r"([aeiou])s([aeiou])"
    c = r"c([eiy])"
    tion = r"t(ion|ia|ie)"

    text = re.sub(ss,r"\1ch\2",text)    #ss
    text = re.sub(s,r"\1ch\2",text)     #s
    text = text.replace("sc", "ch")     #sc
    text = re.sub(z,r"\1z\2",text)      #z
    text = re.sub(tion,r"ch\1",text)    #tion
    text = text.replace("oi", "oa")     #oi

    text = re.sub(c,r"ch\1",text)       #c
    text = text.replace("ç", "ch")      #ç

    text = text.replace("j", "z")       #j

    text = text.replace("tr", "cr")     #tr

    text = text.replace("petit", "poti")#petit

    text = text.replace("dix", "dich")  #dix
    text = text.replace("chix", "chich")#six
    text = text.replace("oui", "ui")#six


    return text
