# text = input()
#
# unique_symbols = set()
#
# for ch in text:
#     unique_symbols.add(ch)
#
# for ch in sorted(unique_symbols):
#     print(f"{ch}: {text.count(ch)} time/s")


text = input()

unique_symbols = sorted(set(text))

for ch in sorted(unique_symbols):
     print(f"{ch}: {text.count(ch)} time/s")
