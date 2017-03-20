-------------------------------------------
-- sdk_dangle_android<sdkName>
-------------------------------------------

module(..., package.seeall)

local tools = require("sdkaccountSys.tools")

local rmb, gold, goldAdd = sdkFunc.sdkConfClass.getRechargeAmount(index)
local productName = gold.."元宝"
local payProductIndex = sdkFunc.sdkConfClass.getProductList('apple')[index]
local roleBasicInfo = sdkFunc.sdkConfClass.getRoleBasicInfo()
local roleId = roleBasicInfo.roleId
local roleName = roleBasicInfo.roleName
local serverIdentification = sdkFunc.sdkConfClass.getServerIdentification()
local serverUrl = sdkFunc.sdkConfClass.getServerUrl()
serverIdentification = string.sub(serverIdentification, 7)
local str = serverIdentification .. "|" .. roleId .. "|"..payProductIndex
local serverName = sdkFunc.sdkConfClass.getServerName()
local roleLv = roleBasicInfo.roleLv
local roleCreateTime = roleBasicInfo.roleCreateTime

--初始化回调
function deleInit( params )
	print('========================deleInit=========================')
end

--初始化
function init()
	print('========================init=============================')
	liblua.init(deleInit)
end

--登录回调
function deleLogin( params )
	print('========================deleLogin=========================')
end

--登录
function login()
	print('========================login=============================')
	liblua.login(deleLogin)
end

--挂起
function appSuspend()
	print('========================appSuspend=============================')
	--liblua.pause()
end

--暂停
function apResume()
	print('========================apResume=============================')
	--liblua.resume
end

--显示浮标
function showBuoy()
	print('========================showBuoy=============================')
	--liblua.showBuoy
end

--隐藏浮标
function hideBuoy()
	print('========================hideBuoy=============================')
	--liblua.hidBuoy
end

--支付回调
function delePay(params)
	print('========================hideBuoy=============================')
	print('statusCode:', params.statusCode)
	print('orderIdCall:', params.orderIdCall)
	print('pIdCall:', params.pIdCall)
	print('rmbCall:', params.rmbCall)
	local statusCode = params.statusCode
	if statusCode == 0 then
		if sdkFunc.payOnComplete then sdkFunc.payOnComplete(params) end
	end
end

--支付
function pay(index)
	print('========================hideBuoy=============================')
	liblua.pay(serverIdentification, serverName, roleId, roleName , roleCreateTime, roleLv, payProductIndex, productName, str, delePay)
end



--退出应用回调
function deleEixt(params)
	print('========================deleEixt=============================')
	if params.statusCode == 0 then
		native.requestExit()
	end
end

--退出应用
function appExit()
	if liblua.exit() then
	print('========================exit=============================')
		liblua.exit(deleEixt)
	else
		local function onComplete( event )
		if "clicked" == event.action then
			if 1 == event.index then
				native.requestExit()
			end
		end
	end
	local alert = native.showAlert("提示", "要退出游戏吗?",  {"确定", "取消"}, onComplete)
	end
end

