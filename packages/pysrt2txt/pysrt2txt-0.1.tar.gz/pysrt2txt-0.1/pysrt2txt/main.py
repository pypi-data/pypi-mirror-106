import re


def srt2txt(srt_file):
    file = open(srt_file)
    lines= file.readlines()
    file.close()

    for line in lines:
        if re.search('^[0-9]+$', line) is None and \
                re.search('^[0-9]{2}:[0-9]{2}:[0-9]{2}', line) is None and \
                re.search('^$', line) is None:
            text += '\n' + line.rstrip('\n')
        text = text.lstrip()
    return text

