# coding:utf8

import os, sys, re
import modelLua


def replace_var(a, b, c):
    # strinfo = re.compile(a[1])
    # h = strinfo.sub(b[1], c)
    print '-------------------------'
    for x in range(len(a)):
        print 'a' + a[x]
        print 'b' + b[x]
        c = replace(a[x], b[x], c)
    print '========================'
    return c


def replace(a, b, c):
    str_info = re.compile(a)
    return str_info.sub(b, c)

def appendKey(list):
    strKey = ''
    for x in list:
        strKey += (x + ',')
        print 'x-->',x
        print 'strKey-->',strKey
    return strKey

def appendStr(list):
    # list = [modelLua.lua_rmb, modelLua.lua_roleLv, modelLua.lua_roleName]
    list_str = ''
    for x in list:
        list_str += (x+".."+"'|'"+"..")
    list_str[0:-7]
    return list_str[0:-7]

if __name__ == '__main__':
    # body
    # , 'callBack':'login'
    all_list = [
                    {'f_name': 'init', 'type': '2', 'params':[modelLua.lua_serverIdentification, modelLua.lua_gold, modelLua.lua_rmb]},
                    {'f_name': 'login', 'type': '2', 'params':[modelLua.lua_serverIdentification, modelLua.lua_payProductIndex]},
                    {'f_name': 'logout', 'type': '2', 'params':[modelLua.lua_productName, modelLua.lua_roleId]},
                    {'f_name': 'showBuoy', 'type': '3'},
                    {'f_name': 'hidBuoy', 'type': '2', 'params': [modelLua.lua_roleName, modelLua.lua_rmb]},
                    {'f_name': 'pay', 'type': '2', 'params':[modelLua.lua_roleCreateTime, modelLua.lua_productName]},
                    {'f_name': 'exit', 'type': '2', 'params':[modelLua.lua_goldAdd, modelLua.lua_roleLv]}
                ]
    body_str = ''
    for x in range(len(all_list)):
        print 'x--->'+str(x)
        if all_list[x]['type'] == '2':
            modelBody2Change = ['dele'+all_list[x]['f_name'].capitalize(), all_list[x]['f_name']]
            if len(all_list[x]['params']) == 0:
                modelBody2Change.append('')
            else:
                strKey = appendKey(all_list[x]['params'])
                modelBody2Change.append(strKey)
            body_str += replace_var(modelLua.modelLuaListBody2, modelBody2Change, modelLua.modelLua_body2)
        elif all_list[x]['type']== '3':
            modelBody3Change = [all_list[x]['f_name']]
            body_str += replace_var(modelLua.modelLuaListBody3, modelBody3Change, modelLua.modelLua_body3)
    # print body_str

    # head
    head_list = ['liulua', [modelLua.lua_roleName, modelLua.lua_roleLv , modelLua.lua_gold]]
    head_list_2 = appendStr(head_list[1])
    head_str = replace_var(modelLua.modelLuaListHead, [head_list[0],head_list_2], modelLua.modelLua_head)
    print head_str + body_str




        # if all_list[x] == '1':
        #     print 'pay'
        # elif all_list[x] == 'exit':
        #     print 'exit'
        # elif all_list[x] == 'appSuspend':
        #     modelBody3Change = ['appSuspend']
        #     body_str += replace_var(modelLua.modelLuaListBody3, modelBody3Change, modelLua.modelLua_body3)
        # elif all_list[x] == 'appResume':
        #     modelBody3Change = ['appResume']
        #     body_str += replace_var(modelLua.modelLuaListBody3, modelBody3Change, modelLua.modelLua_body3)
        # else:
        #     modelBody2Change = ['dele'+all_list[x].capitalize(), all_list[x]]
        #     body_str += replace_var(modelLua.modelLuaListBody2, modelBody2Change, modelLua.modelLua_body2)
        #     print 'other'
        # print body_str

    # modelLuaListHeadChange = ['sdk_dangle_android', '\"haha\"']
    # print replace_var(modelLua.modelLuaListHead, modelLuaListHeadChange, modelLua.modelLua_head)
    # modelBody2Change = ['deleInit','init']
    # print replace_var(modelLua.modleLuaListBody2, modelBody2Change, modelLua.modelLua_body2)
