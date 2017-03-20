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

if __name__ == '__main__':
    test_list = [{'f_name': 'init', 'type': '1'},{'f_name':'login'}];
    print test_list[0]['f_name']
    all_list = [
                {'f_name': 'init', 'type': '1', 'params':['serverId', 'serverName'], 'callBack':'login'},
                {'f_name': 'login', 'type': '1', 'params':['serverId', 'serverName'], 'callBack':'login'},
                {'f_name': 'logout', 'type': '1', 'params':['serverId', 'serverName'], 'callBack':'login'},
                {'f_name': 'appSuspend', 'type': '2'},
                {'f_name': 'appResume', 'type': '2'},
                {'f_name': 'showBuoy', 'type': '2'},
                {'f_name': 'hidBuoy', 'type': '1', 'params':['serverId', 'serverName'], 'callBack':'login'},
                {'f_name': 'pay', 'type': '1', 'params':['serverId', 'serverName'], 'callBack':'login'},
                {'f_name': 'exit', 'type': '1', 'params':['serverId', 'serverName'], 'callBack':'login'}
                ]
    body_str = ''
    for x in range(len(all_list)):
        print 'x--->'+str(x)
        if all_list[x]['type'] == '1':
            modelBody2Change = ['dele'+all_list[x]['f_name'].capitalize(), all_list[x]['f_name']]
            body_str += replace_var(modelLua.modelLuaListBody2, modelBody2Change, modelLua.modelLua_body2)
        elif all_list[x]['type']== '2':
            modelBody3Change = [all_list[x]['f_name']]
            body_str += replace_var(modelLua.modelLuaListBody3, modelBody3Change, modelLua.modelLua_body3)
    print body_str



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
