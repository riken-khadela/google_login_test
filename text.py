textt = '''mega日本最大級のビル看板広告にNFTDuel x CryptoNinjaが登場！

新宿をジャック！
日本最大級のビル看板広告に NFTDuel × CryptoNinja のトレーラーが登場しました。

新宿駅前のユニカビジョンで放映中！
1月28日のNFTドロップ＆ゲームローンチまで見ることができます！
CM毎時28分45秒に放送されますので、お近くの人は是非訪れてくださいね。

blue_bookNFTDuel x CryptoNinja について
https://xana.net/ja/xana-metaverse-to-release-cryptoninja-nft-game/

arrow_forwardリツイート
https://twitter.com/XANAMetaversejp/status/1605159828619497472

2023年カウントダウン冬祭り（4日目／15日間）
@everyone​'''

file_obj = open('text.txt', 'r+')
tt = ''
for i in file_obj.readlines():
    tt += i
print(tt)   
file_obj.close()
# Program to show various ways to read and
# write data in a file.
file1 = open("text.txt","w")
L = "This is Delhi \nThis is Paris \nThis is London \n"

# # \n is placed to indicate EOL (End of Line)
# file1.write("Hello \n")
file1.writelines(L)
file1.close() #to change file access modes

# file1 = open("text.txt","r+")

# print("Output of Read function is ")
# print(file1.read())
# print()

# # seek(n) takes the file handle to the nth
# # bite from the beginning.
# file1.seek(0)

# print( "Output of Readline function is ")
# print(file1.readline())
# print()

# file1.seek(0)

# # To show difference between read and readline
# print("Output of Read(9) function is ")
# print(file1.read(9))
# print()

# file1.seek(0)

# print("Output of Readline(9) function is ")
# print(file1.readline(9))

# file1.seek(0)
# # readlines function
# print("Output of Readlines function is ")
# print(file1.readlines())
# print()
# file1.close()
