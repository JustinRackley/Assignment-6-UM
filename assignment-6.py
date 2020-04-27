text = "X-DSPAM-Confidence:    0.8475"
index_start = text.find('0')
index_finish = text.find('5',num)
final_index = text[index_start:index_finish+1]
print(final_index)