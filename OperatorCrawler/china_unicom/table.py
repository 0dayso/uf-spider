#coding=utf-8

# 表名
TABEL_NAME_1 = 't_operator_user'
TABLE_NAME_2 = 't_operator_call'
TABLE_NAME_3 = 't_operator_note'

# 用户信息内容字段转换
KEY_CONVERT_USER = {
    'custname': 'name',
    'custsex': 'sex',
    'certaddr': 'address',
    'certtype': 'cert_type',
    'certnum': 'cert_num',
    'productname': 'product_name',
    'custlvl': 'level',
    'opendate': 'open_date',
}

# （原）通话记录内容字段转换
# KEY_CONVERT_CALL = {
#     'homeareaName': 'call_area',
#     'calldate': 'call_date',
#     'calltime': 'call_time',
#     'totalfee':  'call_cost',
#     'calllonghour': 'call_long',
#     'othernum': 'other_phone',
#     'calltypeName': 'call_type',
#     'landtype': 'land_type'
# }

# （更新0220）通话记录内容字段转换

KEY_CONVERT_CALL = {
    'call_area': [u'通话地点', u'本机通话地'],
    # 'call_date': [u'通话日期', u''],##
    # 'call_time': [u'通话时分秒', u''],##
    'call_cost': [u'通话费用', u'通话费'],
    'call_long': [u'通话时长'],
    'other_phone': [u'对方号码'],
    'call_type': [u'呼叫类型'],
    'land_type': [u'通话类型']
}


# 短信记录内容字段转换
KEY_CONVERT_NOTE = {
    'smsdate': 'note_date',
    'smstime': 'note_time',
    'amount': 'note_cost',
    'businesstype': 'business_type',
    'othernum': 'other_phone'
}

# 用户表-需要插入数据的字段
COLUMN_USER = (
    'name','sex', 'address', 'cert_type', 'cert_num',
    'phone', 'company', 'province', 'city', 'product_name',
    'level', 'open_date', 'balance', 'user_valid'
)

# 通话记录表-需要插入数据的字段
COLUMN_CALL = (
    'cert_num', 'phone', 'call_area', 'call_date',
    'call_time','call_cost', 'call_long', 'other_phone',
    'call_type', 'land_type'
)

# 短信记录表-需要插入数据的字段
COLUMN_NOTE = (
    'cert_num', 'phone', 'note_date', 'note_time',
    'note_cost', 'business_type', 'other_phone'
)

