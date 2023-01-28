# noborderz49@gmail.com,No@12345
# nodushambali@gmail.com,No@12345
# chamberszara536@gmail.com,No@12345
# m49711196@gmail.com,No@12345
# l4594793@gmail.com,No@12345
# mohammadrichard12@gmail.com,Richard@123
# humphriesamber039@gmail.com,No@12345
# evejenkins070@gmail.com,No@12345
# aaliyahhenry959@gmail.com,No@12345
# bettygerstner22@gmail.com,No@12345
# st4826577@gmail.com,No@12345
# jerriandersen123@gmail.com,No@12345
# janetbrewton34@gmail.com,No@12345
# judithfarkas09@gmail.com,No@12345
# beck71514@gmail.com,No@12345
# lewismay064@gmail.com,No@12345
# barbaraclouser504@gmail.com,No@12345
# charles.gomez6001@gmail.com,No@12345
# james667661@gmail.com,No@12345
# tony648973@gmail.com,No@12345

# video_json = {}
# from pprint import pprint
# with open("video.txt", "r") as f_in:
#     lines = f_in.readlines()
#     for line in lines:
#         line = line.strip().split(' = ')
#         video_json[line[0]] = line[-1]
        
# pprint(video_json)

# a = '5.2K views'

# if 'K views' in a:
    
#     a = float(a.replace('K views',''))
#     a = a*1000
#     print(a)
#     if a < 5500:
#         print('yess')

# a = a.replace('K views','')
# a = float(a.replace(' views',''))
# print(a)

# a = 'https://www.youtube.com/watch?v=RhpTougdSz0&ab_channel=XANA'
# a = a.replace('https://www.youtube.com/watch?v=','')
# a = a.replace('&ab_channel=XANA','')
# print(a)


# channel_link = https://www.youtube.com/@XANAMetaverse 
# channel_name = XANAMetaverse 
# channel_username = XANAMetaverse 
# video_link = https://www.youtube.com/watch?v=RhpTougdSz0&ab_channel=XANA 
# VideoTItle = 誰も知らないXANAジェネシスの秘密を初公開！


# a = 'kanoooo123567'
a = 'kanoooo'

if  not ('123' or '567' ) in a:
    print(a)

abc = []
jss = {
    'channel_link' : 'https://www.youtube.com/@XANAMetaverse ',
    'channel_name' : 'XANAMetaverse ',
    'channel_username' : 'XANAMetaverse ',
    'video_link' : 'https://www.youtube.com/watch?v=RhpTougdSz0&ab_channel=XANA ',
    'VideoTItle' : '誰も知らないXANAジェネシスの秘密を初公開！'
    
}


print(jss)
# for key in jss:
#     print(key,':',jss[key])

with open("video.txt", "r") as f_in:
    lines = f_in.readlines()
    for line in lines:
        print(line.strip())
        
        
        # line = line.strip()
        # if not 'video_link'   in line:
        #     if not 'VideoTItle' in line:
        #         print(line)
        #         abc.append(line)
                
# for i in 

# with open("video.txt", "w") as f_out:
#     for i in jss:
#         line = f'{i} = {jss[i]}\n'
#         f_out.write(line)