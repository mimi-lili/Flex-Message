import make_flex_message


a_list = []
# a_list.append( ['課程名稱1', '授課老師1', '上課時間1', '上課地點1', '課程代碼1'])
# a_list.append( ['課程名稱2', '授課老師2', '上課時間2', '上課地點2', '課程代碼2'])
# a_list.append( ['課程名稱3', '授課老師3', '上課時間3', '上課地點3', '課程代碼3'])
# a_list.append( ['課程名稱4', '授課老師4', '上課時間4', '上課地點4', '課程代碼4'])
# a_list.append( ['課程名稱5', '授課老師5', '上課時間5', '上課地點5', '課程代碼5'])
a_list.append( ['課程名稱6', '授課老師6', '1-12', '上課地點6', '1-34', '上課地點62','課程代碼6'])
a_list.append( ['課程名稱7', '授課老師7', '2-56', '上課地點7', '5-34', '上課地點72','5-78', '上課地點73','課程代碼7'])
content = make_flex_message.make_course_search_flex(a_list)

print( content )
